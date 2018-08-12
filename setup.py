from setuptools import setup

setup(
    name='ipvanish-server-capacity',
    version='1.0',
    packages=['ipvanish'],
    url='',
    license='GPL',
    author='Daniel Mouritsen',
    author_email='daniel.mouritsen@gmail.com',
    description='Console script to query for IPVanish server statuses',
    entry_points={
        'console_scripts': ['ipvcap=ipvanish.main:main'],
    }, install_requires=['requests']
)
