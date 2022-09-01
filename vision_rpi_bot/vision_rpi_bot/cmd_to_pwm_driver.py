import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16

class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Int16,'pub_topic',self.cmd_to_pwm_callback,
            10)
        self.subscription  

    def cmd_to_pwm_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()