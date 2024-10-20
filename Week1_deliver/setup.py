from setuptools import find_packages, setup

package_name = 'Week1_deliver'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='yymelendez@ucsd.edu',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub.py = Week1_deliver.pub.py:main'
            'sub.py = Week1_deliver.sub.py:main'
            'random_turtle.py = Week1_deliver.random_turtle.py:main'
            'turtle_cleaner.py = Week1_deliver.turtle_cleaner.py:main' 
        ],
    },
)
