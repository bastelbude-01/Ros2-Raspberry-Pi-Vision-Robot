from setuptools import setup

package_name = 'vision_rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2',
    maintainer_email='ros2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'publisher_rpi_node= vision_rpi_bot.publisher:main',
                'subsciber_rpi_node = vision_rpi_bot.subsciber:main',
                'cmdVel_to_pwm_node = vision_rpi_bot.cmd_to_pwm_driver:main',

                            ],
                },
)
