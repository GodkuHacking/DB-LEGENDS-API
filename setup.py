from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='db-legends-api',
    version='1.83.4',
    description='Python module to retrieve DB Legends character information',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='ohioman02',
    author_email='ohioman02',
    packages=['db_legends'],
    install_requires=[],
)
