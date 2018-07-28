#!/usr/bin/env python
# -*-coding:utf-8-*-

import codecs

from setuptools import setup, find_packages, Extension


def long_description():
    try:
        with codecs.open('README.md', encoding='utf-8') as f:
            return f.read()
    except Exception as e: # 免得因为这个出现安装错误
        return "the bihu libary."


REQUIREMENTS = []



setup(
    name='bihu',
    version='0.1.3',
    description='the bihu libary',
    long_description=long_description(),
    author='cdwanze',
    author_email='a358003542@gmail.com',
    platforms='Linux, windows',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    zip_safe=False,
    include_package_data=True,
    setup_requires=REQUIREMENTS ,
    install_requires=REQUIREMENTS ,
    # entry_points = {
    #     'console_scripts': [
    #         'convert_image=expython.image.convert_image:main',
    #         'resize_image=expython.image.resize_image:main'
    #     ]
    # }
)
