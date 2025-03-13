import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(Float32, 'sensor_data', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)
        self.get_logger().info("Sensor Publisher Node started.")

    def publish_sensor_data(self):
        sensor_value = random.uniform(0.0, 10.0)  # Szimulált távolságérték
        msg = Float32()
        msg.data = sensor_value
        self.publisher_.publish(msg)
        self.get_logger().info(f"Érzékelt távolság: {sensor_value:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
