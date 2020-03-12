import os
from setuptools import setup

README = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')).read()

setup(
    name='django-monaco-old',
    version='0.1',
    packages=['monaco'],
    description='Monaco editor widgets in the Django Admin',
    package_data={
        "": ["LICENSE", "*.md"],
        "hello": ["static"],
    },
    include_package_data=True,
    long_description=README,
    long_description_content_type="text/markdown",
    author='Ayush Shanker',
    keywords=['django<1.11', 'monaco',],
    platforms=['OS Independent'],
    license='MIT',
    install_requires=[
        'Django<1.11',
    ]
)
