from importlib.metadata import entry_points
from setuptools import setup
setup(
    name="app",
    description="Mars Rover App",
    version="0.0.01",
    packages=["app"],
    entry_points={
        'console_scripts': [
            'app = app.__main__:main'
        ]
    }
)
