from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyspecs',
    version='0.1.0',
    description='Markdown Specifications',
    long_description=readme,
    author='Reese Walton',
    author_email='jrwalt4@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
