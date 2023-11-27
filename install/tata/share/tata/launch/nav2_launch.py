import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    turtlebot3_navigation2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'launch', 'navigation2.launch.py')]
        ), launch_arguments={ 'use_sim_time': 'True', 'map': 'tata-map.yaml'}.items(),
    )
    turtlebot3_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'turtlebot3_world.launch.py')],
        )
    )
    tata_tata = Node(
        package='tata',
        executable='tata',
        name='tata',
        output='screen'
    )

    return LaunchDescription([
        turtlebot3_navigation2,
        turtlebot3_gazebo,        
        tata_tata,
    ])