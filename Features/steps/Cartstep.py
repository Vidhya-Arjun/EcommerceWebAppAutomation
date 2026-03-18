
from behave import when, then
from Features.pages import CartPage
import math

@when(u'the user selects products and adds them to the cart')
def step_impl(context):
    """
    Accepts an optional behave table with columns: name, price, quantity
    If provided, stores expected items in context.expected_cart_items.
    If table is not provided, assumes previous steps already added products.
    """
    expected = []
    if hasattr(context, "table") and context.table:
        for row in context.table:
            # table keys should be 'name', 'price', 'quantity' (case-insensitive)
            name = row.get("name") or row.get("Name") or ""
            price = row.get("price") or row.get("Price") or "0"
            qty = row.get("quantity") or row.get("Quantity") or "1"
            try:
                price_val = float(str(price).replace("$", "").replace(",", "").strip())
            except Exception:
                price_val = 0.0
            try:
                qty_val = int(''.join(ch for ch in str(qty) if ch.isdigit()) or 1)
            except Exception:
                qty_val = 1
            expected.append({"name": name.strip(), "price": price_val, "quantity": qty_val})
        context.expected_cart_items = expected
    # If no table, do not modify expected_cart_items (assume other steps set it)

@then(u'the cart icon count should be updated')
def step_impl(context):
    """
    Verifies the cart icon count matches the expected total quantity when possible,
    otherwise asserts it is greater than zero.
    """
    driver = context.driver
    cart = CartPage(driver)
    count = cart.get_cart_count()

    if hasattr(context, "expected_cart_items"):
        expected_total = sum(item["quantity"] for item in context.expected_cart_items)
        assert count == expected_total, f"Cart icon count {count} != expected {expected_total}"
    else:
        assert count > 0, f"Cart icon count is not updated (found {count})"

@then(u'the selected products should be added to the cart')
def step_impl(context):
    """
    Opens the cart and compares listed items to expected items (if provided).
    Comparison tolerates small float rounding differences for price.
    """
    driver = context.driver
    cart = CartPage(driver)
    cart.open_cart()
    listed = cart.get_cart_items()

    if not hasattr(context, "expected_cart_items"):
        # If no expected list was provided, ensure there is at least one item
        assert len(listed) > 0, "Cart is empty but expected items to be present."
        context.cart_items = listed
        return

    expected = context.expected_cart_items

    # Build lookup by normalized name
    def norm(s): return (s or "").strip().lower()

    listed_map = { norm(i["name"]): i for i in listed }
    for exp in expected:
        key = norm(exp["name"])
        assert key in listed_map, f"Expected product '{exp['name']}' not found in cart."
        actual = listed_map[key]

        # Compare quantity
        assert actual.get("quantity", 1) == exp.get("quantity", 1), (
            f"Quantity mismatch for '{exp['name']}': expected {exp.get('quantity')}, got {actual.get('quantity')}"
        )

        # Compare price within small tolerance
        exp_price = float(exp.get("price") or 0.0)
        act_price = float(actual.get("price") or 0.0)
        if math.isfinite(exp_price) and math.isfinite(act_price):
            assert abs(exp_price - act_price) < 0.01, (
                f"Price mismatch for '{exp['name']}': expected {exp_price}, got {act_price}"
            )

    # Save fetched items for later steps if needed
    context.cart_items = listed