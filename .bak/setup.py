#!/usr/bin/env
# -*- coding: utf-8 -*-

from distutils.core import setup
import musicl

setup(
		name='musicl'
		version='1.0.0'
		description='A program for downloading music in terminal environment'
		author='Lhfcws'
		author_email='lhfcws@gmail.com'
		license='GPL'
		url=''
		packages=['musicl', 'musicl/sources']
		scripts=['scripts/musicl']
	 )
