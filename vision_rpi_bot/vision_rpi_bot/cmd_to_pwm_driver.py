import rclpy
from rclpy.node import Node

from std_msgs.msg import Twist

class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist,'pub_topic',self.cmd_to_pwm_callback,
            10)
        self.subscription 

        self.right_motor_en = 5
        self.right_motor_a = 13
        self.right_motor_b = 6

        self.left_motor_a = 19
        self.left_motor_b = 16
        self.left_motor_en = 26
        self.second = 2
        

        GPIO.setup(right_motor_en , GPIO.OUT)
        GPIO.setup(right_motor_a  , GPIO.OUT)
        GPIO.setup(right_motor_b , GPIO.OUT)    

        GPIO.setup(left_motor_a , GPIO.OUT)
        GPIO.setup(left_motor_b , GPIO.OUT)
        GPIO.setup(left_motor_en , GPIO.OUT)


        self.pwm_r = GPIO.PWM(right_motor_en, 1000)
        self.pwm_l = GPIO.PWM(left_motor_en, 1000)

        self.self.pwm_r.start(75)
        self.self.pwm_l.start(75) 

    def cmd_to_pwm_callback(self, msg):

        right_wheel_vel = (msg.linear.x + msg.angular.y) /2
        left_wheel_vel = (msg.linear.x - msg.angular.y) /2
        
        print("right_wheel_vel ," / "left_wheel_vel")


def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()

    rclpy.spin(velocity_subscriber)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()