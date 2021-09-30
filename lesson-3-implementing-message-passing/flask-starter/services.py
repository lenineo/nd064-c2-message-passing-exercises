from .enums import Status

orders: list = []


def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    # Do something to create the resource
    orders.append(order_data)
    # print(orders)
    return order_data


def retrieve_orders():
    """
    This is a stubbed method of retrieving multiple resources. It doesn't actually do anything.
    """
    return orders if len(orders) > 0 else [
        {
            "id": "1",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:31:10.969696",
            "created_by": "USER14",
            "equipment": [
                "KEYBOARD", "MOUSE"
            ]
        },
        {
            "id": "2",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:29:10.969696",
            "created_by": "USER15",
            "equipment": [
                "KEYBOARD", "WEBCAM"
            ]
        }
    ]
