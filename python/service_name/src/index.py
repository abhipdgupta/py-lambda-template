from typing import List, TypedDict

from src.math.add import add_custom

class HandlerResponse(TypedDict):
    statusCode: int
    body: str
    event: dict
    sum: int | float


def handler(event, context) -> HandlerResponse:
    toSum: List[int | float] = event.get("toSum")
    if not toSum:
        raise ValueError("toSum is required")

    if not isinstance(toSum, list):
        raise ValueError("toSum must be a list")

    final_sum = add_custom(*toSum)

    return {"statusCode": 200, "body": "Hello World!", "event": event, "sum": final_sum}


print(handler({"toSum": [1, 2, 66]}, None))