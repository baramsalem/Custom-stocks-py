"""Python setup.py for custom_stocks_py package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("custom_stocks_py", "VERSION")
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
    name="custom_stocks_py",
    version=read("custom_stocks_py", "VERSION"),
    description="Awesome custom_stocks_py created by baramsalem",
    url="https://github.com/baramsalem/Custom-stocks-py/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="baramsalem",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["custom_stocks_py = custom_stocks_py.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
