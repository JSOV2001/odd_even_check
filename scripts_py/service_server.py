#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from odd_even.srv import OddEvenChock

class OddEvenCheckServer(Node):
    def __init__(self):
        super().__init__("odd_even_service_server")
        self.server = self.create_service(OddEvenChock, "/odd_even_check", self.odd_even_callback)
    
    def odd_even_callback(self, request, response):
        if request.number % 2 == 0:
            response.decision = "Even"
        elif request.number % 2 == 1:
            response.decision = "Odd"
        else:
            response.decision = "Error"
        
        print(f"Request: {request.number}")
        print(f"Response: {response.decision}")

        return response

def main():
    rclpy.init()
    print("Initializing service server!")
    my_node = OddEvenCheckServer()
    try:
        rclpy.spin(my_node)
    except KeyboardInterrupt:
        my_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()