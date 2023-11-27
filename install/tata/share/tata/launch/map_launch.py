import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    turtlebot3_cartographer = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('turtlebot3_cartographer'), 'launch', 'cartographer.launch.py')],
        ),  launch_arguments={'use_sim_time': 'True'}.items(),
    )
    turtlebot3_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'turtlebot3_world.launch.py')],
        )
    )
    turtlebot3_teleop = Node(
        package='turtlebot3_teleop',
        executable='teleop_keyboard',
        name='teleop_keyboard',
        prefix = 'gnome-terminal --',
        output='screen'
    )
    
    return LaunchDescription([
        turtlebot3_cartographer,
        turtlebot3_gazebo,
        turtlebot3_teleop,
    ])