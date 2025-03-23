import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(Float32, 'sensor_data', self.sensor_callback, 10)
        self.get_logger().info("Sensor Subscriber Node started.")

    def sensor_callback(self, msg):
        self.get_logger().info(f"Kapott érték: {msg.data:.2f}")
        if msg.data < 2.0:
            self.get_logger().warn("⚠️ FIGYELEM: A kapott érték túl lözeli!")
        else:
            self.get_logger().warn("A távolság megfelelő!")

def main(args=None):
    rclpy.init(args=args)
    node = SensorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()