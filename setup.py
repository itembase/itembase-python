from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = ""
# Get the long description from the README file
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
    name='itembase-python',
    version='0.9b2',
    description='Itembase Python bindings',
    long_description=long_description,
    url='https://github.com/itembase/itembase-python',
    author='Itembase',
    author_email='dev@itembase.biz',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='itembase api bindings',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests>=2.9.1'],
)
