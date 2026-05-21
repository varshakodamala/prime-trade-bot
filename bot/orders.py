from bot.client import client
import logging

logger = logging.getLogger()

def place_order(
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        payload = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            payload["price"] = price
            payload["timeInForce"] = "GTC"

        logger.info(f"REQUEST => {payload}")

        response = client.futures_create_order(
            **payload
        )

        logger.info(f"RESPONSE => {response}")

        return response

    except Exception as e:

        logger.error(
            f"ORDER FAILED => {str(e)}"
        )

        raise
