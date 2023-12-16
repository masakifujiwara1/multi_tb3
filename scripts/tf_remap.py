import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage
from rclpy.qos import QoSProfile

class TFRebroadcaster(Node):

    def __init__(self):
        super().__init__('tf_rebroadcaster')
        qos_profile = QoSProfile(depth=10)
        
        self.tf_subscription = self.create_subscription(
            TFMessage,
            '/tf',
            self.tf_callback,
            qos_profile
        )
        # self.tf_static_subscription = self.create_subscription(
        #     TFMessage,
        #     '/tf_static',
        #     self.tf_static_callback,
        #     qos_profile
        # )
        self.tf_publisher2 = self.create_publisher(
            TFMessage,
            '/robot2/tf',
            qos_profile
        )
        # self.tf_static_publisher = self.create_publisher(
        #     TFMessage,
        #     '/robot2/tf_static',
        #     qos_profile
        # )
        self.tf_publisher3 = self.create_publisher(
            TFMessage,
            '/robot3/tf',
            qos_profile
        )
        self.tf_publisher4 = self.create_publisher(
            TFMessage,
            '/robot4/tf',
            qos_profile
        )


    def tf_callback(self, msg):
        for transform in msg.transforms:
            self.tf_publisher2.publish(msg)
            self.tf_publisher3.publish(msg)
            self.tf_publisher4.publish(msg)

    # def tf_static_callback(self, msg):
    #     for transform in msg.transforms:
    #         self.tf_static_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    tf_rebroadcaster = TFRebroadcaster()
    rclpy.spin(tf_rebroadcaster)
    tf_rebroadcaster.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
