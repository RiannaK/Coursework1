from setuptools import setup, find_packages

setup(
    name="greengraph",
    version="0.1",
    packages=find_packages(exclude=["*test"]),
    scripts=["scripts/graph"],
    install_requires=["argparse", "matplotlib", "geopy", "requests", "numpy"]
)