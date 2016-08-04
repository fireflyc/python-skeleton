# coding=utf-8
from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="python-skeleton",
    version="0.0.1",
    description="python skeleton demo",
    long_description=open("README.md").read(),
    author="fireflyc",
    author_email="fireflyc@126.com",
    url="",
    license="",
    packages=find_packages(exclude=("tests", "docs", "etc")),
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    test_suite="tests",
    entry_points="""
        [console_scripts]
        python-skeleton=python_skeleton.cli:main
    """
)
