# -*- coding: utf-8 -*-

from setuptools import setup

from dwml import __version__


setup(
	name='dwml',
	version=__version__,
	license='http://www.apache.org/licenses/LICENSE-2.0',
	description='reading DrawingML of Ms-office (2007 and above,omml,picture),And Convert them to latex',
	author='xilei',
	author_email='xilei125@163.com',
	packages=['dwml'],
	keywords=['word','excel','omml','latex'],
	classifiers=[
		'Development Status :: 3 - Alpha Development Status',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
	]

)