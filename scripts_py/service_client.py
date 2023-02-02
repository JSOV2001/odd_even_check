#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from odd_even.srv import OddEvenChock

class OddEvenCheckClient(Node):
    def __init__(self):
        super().__init__("odd_even_service_client")
        self.client = self.create_client(OddEvenChock, "/odd_even_check")
        self.request = OddEvenChock.Request()
    
    def send_request(self, my_number):
        self.request.number = int(my_number)
        self.client.wait_for_service()
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        self.response = self.future.result()
        return self.response

def main():
    rclpy.init()
    my_node = OddEvenCheckClient()
    try:
        user_input = input("Enter an integer: ")
        response = my_node.send_request(user_input)
        print(f"Response: {response.decision}")
    except KeyboardInterrupt:
        my_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()