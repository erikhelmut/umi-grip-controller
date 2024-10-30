from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="umigrip",
    version="1.0.0",
    description="Python controller for the actuated UMI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erikhelmut/umi-grip-controller",
    author="Erik Helmut",
    author_email="erik.helmut1@gmail.com",
    license="MIT",
    packages=["umigrip"],
    install_requires=[
        "dynamixel_sdk @ git+https://github.com/ROBOTIS-GIT/DynamixelSDK@e1252983b43d87ed56cb25e38a12c835e53cd933#egg=dynamixel_sdk&subdirectory=python"
    ],

    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
    ],
)
