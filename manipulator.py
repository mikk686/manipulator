import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import TransformStamped

class Manipulator(Node):

    def __init__(self):
        super().__init__('minimal_publisher')

        self.publisher_angles = self.create_publisher(Float32MultiArray, 'angles_and_gripper', 10)

        self.subscription_obj = self.create_subscription(TransformStamped,'object_position', self.object_callback, 10)
        self.subscription_obj  # prevent unused variable warning
        self.subscription_endeff = self.create_subscription(TransformStamped,'effector_position', self.effector_callback, 10)
        self.subscription_endeff  # prevent unused variable warning

    def object_callback(self, msg):
        self.get_logger().info('Object Pose: "%s"' % msg.transform)

    def effector_callback(self, msg):
        self.get_logger().info('End Effector Pose: "%s"' % msg.transform)

    def publish_angles(self):
        msg = Float32MultiArray()
        msg.data = [0.,0.,0.,0.,0.,0.,0.,100.] #7DOF + Gripper 0 or 100
        self.publisher_angles.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)

    manipulator_node = Manipulator()

    rclpy.spin(manipulator_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    manipulator_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()





