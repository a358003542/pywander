#!/usr/bin/env python
# -*-coding:utf-8-*-


from setuptools import setup, find_packages
import codecs
import mymodule

REQUIREMENTS = []


def long_description():
    with codecs.open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='mymodule',
    version=mymodule.__version__,
    description='a general purpose python module.',
    url='https://github.com/a358003542/mymodule',
    long_description=long_description(),
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer='wanze',
    maintainer_email='a358003542@gmail.com',
    license='MIT',
    platforms='Linux, windows',
    keywords=['python'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Operating System :: Microsoft',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
)
