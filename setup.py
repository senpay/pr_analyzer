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
    name='pr_analyzer',
    version=version.VERSION,
    author='Alexander Pushkarev',
    author_email='alexspush@gmail.com',
    description='Small CLI to analyze PRs on the GitHub',
    license='MIT',
    url='http://packages.python.org/pr_analyzer',
    packages=['pr_analyzer', 'pr_analyzer.adapters', 'pr_analyzer.application'],
    scripts=['list_prs', 'print_stats'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=[
        'PyGithub==1.44'
    ],
)
