"""Python setup.py for fast_api_template package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("fast_api_template", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="fast_api_template",
    version=read("fast_api_template", "VERSION"),
    description="Awesome fast_api_template created by jammun",
    url="https://github.com/jammun/fast-api-template/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jammun",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["fast_api_template = fast_api_template.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
