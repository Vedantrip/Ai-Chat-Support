import json
from pathlib import Path

ORDERS_FILE = Path(__file__).resolve().parent.parent / "data" / "demo_orders.json"

ORDER_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "lookup_order",
            "description": (
                "Read the status and listed items for a demo clothing order. "
                "Only use after the customer has provided both their order number and "
                "the email address on the order. This action does not change an order."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "order_number": {
                        "type": "string",
                        "description": "The customer's order number, e.g. TL-DEMO-1001",
                    },
                    "customer_email": {
                        "type": "string",
                        "description": "The email address associated with the order",
                    },
                },
                "required": ["order_number", "customer_email"],
            },
        },
    }
]


def lookup_order(order_number: str, customer_email: str) -> dict:
    """Return minimal demo order details only after order number and email match."""
    number = order_number.strip().casefold()
    email = customer_email.strip().casefold()
    try:
        orders = json.loads(ORDERS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"found": False, "demo_mode": True, "error": "Demo order data is unavailable."}

    for order in orders:
        if order["order_number"].casefold() == number and order["customer_email"].casefold() == email:
            return {
                "found": True,
                "demo_mode": True,
                "order_number": order["order_number"],
                "status": order["status"],
                "items": order["items"],
                "tracking_note": order["tracking_note"],
            }
    return {"found": False, "demo_mode": True}