import os
import sys

from setuptools import setup, find_packages

setup(
    name="pick-n-place",
    version="0.0.1",
    packages=find_packages(),
    description="Course code for VIP-GEAI",
    url="https://github.com/purdue-mars/VIP-GEAI",
    author="Raghava Uppuluri",
    install_requires=[
        "robohive @ git+ssh://git@github.com/raghavauppuluri13/robohive.git",
        "vtils @ git+ssh://git@github.com/raghavauppuluri13/vtils.git",
    ],
)
