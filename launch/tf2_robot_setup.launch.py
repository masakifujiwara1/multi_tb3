from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher',
            output='screen',
	        remappings=[('tf_static', '/robot2/tf_static')],
            arguments=['0', '0', '1.7', '0', '3.14', '0', 'map', 'link']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher5',
            output='screen',
	        remappings=[('tf_static', '/robot3/tf_static')],
            arguments=['0', '0', '1.7', '0', '3.14', '0', 'map', 'link']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher6',
            output='screen',
	        remappings=[('tf_static', '/robot4/tf_static')],
            arguments=['0', '0', '1.7', '0', '3.14', '0', 'map', 'link']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher2',
            output='screen',
	        remappings=[('tf_static', '/robot2/tf_static')],
            arguments=['0', '0', '0.3', '0', '0', '0', 'robot2', 'robot2/base_scan']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher3',
            output='screen',
	        remappings=[('tf_static', '/robot3/tf_static')],
            arguments=['0', '0', '0.3', '0', '0', '0', 'robot3', 'robot3/base_scan']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher4',
            output='screen',
	        remappings=[('tf_static', '/robot4/tf_static')],
            arguments=['0', '0', '0.3', '0', '0', '0', 'robot4', 'robot4/base_scan']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher7',
            output='screen',
	        # remappings=[('tf_static', '/tf_static')],
            arguments=['0', '0', '0.3', '0', '0', '0', 'robot1', 'robot1/base_scan']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_publisher8',
            output='screen',
	        # remappings=[('tf_static', '/robot1/tf_static')],
            arguments=['0', '0', '1.7', '0', '3.14', '0', 'map', 'link']
        ),


    ])

