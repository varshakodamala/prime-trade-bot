def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side. Use BUY or SELL.")
    return side

def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type. Use MARKET or LIMIT.")
    return order_type

def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    return quantity
