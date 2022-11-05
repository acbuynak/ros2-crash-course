from setuptools import setup

package_name = 'sim_oven'

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
    maintainer='A.C. Buynak (The Ohio State University)',
    maintainer_email='44533530+acbuynak@users.noreply.github.com',
    description='Temperature publisher',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_oven_sim = sim_oven.sim_oven:main',
        ],
    },
)
