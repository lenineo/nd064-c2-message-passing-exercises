import grpc
import order_pb2
import order_pb2_grpc


print("Sending order payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    id="1111",
    created_by="USER123",
    status=order_pb2.OrderMessage.Status.QUEUED,
    created_at='2021-10-02',
    equipment=[order_pb2.OrderMessage.Equipment.KEYBOARD]
)


response = stub.Create(order)
print("response: ")
print(str(response))