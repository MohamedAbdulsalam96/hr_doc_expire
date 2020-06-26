# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in hr_doc_expire/__init__.py
from hr_doc_expire import __version__ as version

setup(
	name='hr_doc_expire',
	version=version,
	description='Manage employee documents within the company',
	author='Mostafa Mohamed',
	author_email='m.dev.odoo@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
