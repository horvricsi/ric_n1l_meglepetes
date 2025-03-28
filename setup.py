from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ric_n1l_meglepetes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='horvricsi',
    maintainer_email='horvathricsi1210@gmail.com',
    description='Horváth Richárd: Távolságmérő szenzor',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'publisher_node = ric_n1l_meglepetes.publisher_node:main',
        'subscriber_node = ric_n1l_meglepetes.subscriber_node:main',
        ],
    },
)
