from setuptools import setup

PACKAGE_NAME = 'advancedeast'
PACKAGE_DIR = '.'

setup(
    name=PACKAGE_NAME, 
    version='0.0.1',
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: PACKAGE_DIR},
)
