from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name='healthy_sanjid',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)
