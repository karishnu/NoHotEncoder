from setuptools import setup

setup(
    name='NoHotEncoder',
    author='Karishnu Poddar',
    author_email='karishnu@gmail.com',
    packages=['nohotencoder'],
    install_requires=['pandas'],
    version='0.1',
    license='MIT',
    description='Converts One Hot Encoding to Integer encoding'
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)