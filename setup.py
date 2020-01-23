import os
from setuptools import setup

from pr_analyzer import version


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="an_example_pypi_project",
    version=version.VERSION,
    author="Alexander Pushkare",
    author_email="alexspush@gmail.com",
    description="Small CLI to analyze PRs on the GitHub",
    license="MIT",
    keywords="example documentation tutorial",
    url="http://packages.python.org/pr_analyzer",
    packages=['pr_analyzer', 'tests'],
    long_description=read('README')
)
