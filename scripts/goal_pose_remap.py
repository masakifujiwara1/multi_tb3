import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class GoalPosePublisher(Node):

    def __init__(self):
        super().__init__('goal_pose_publisher')
        self.sub = self.create_subscription(PoseStamped, '/goal_pose', self.goal_pose_callback, 10)
        self.pub2 = self.create_publisher(PoseStamped, '/robot2/goal_pose', 10)
        self.pub3 = self.create_publisher(PoseStamped, '/robot3/goal_pose', 10)
        self.pub4 = self.create_publisher(PoseStamped, '/robot4/goal_pose', 10)

    def goal_pose_callback(self, msg):
        # 受け取ったメッセージをそのまま別のトピックに発行する
        self.pub2.publish(msg)
        self.pub3.publish(msg)
        self.pub4.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoalPosePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

