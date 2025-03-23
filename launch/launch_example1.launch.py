from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ric_n1l_meglepetes',
            executable='publisher_node',
            name='publisher',
            output='screen'
        ),
        Node(
            package='ric_n1l_meglepetes',
            executable='subscriber_node',
            name='subscriber',
            output='screen'
        ),
    ])
