#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import songinfo

def inFile(filename):
	fil = open(filename,'r')
	lines = fil.readlines()
	fil.close()
	newlines = []
	for line in lines:
		line = ''.join(line)
		line = line.strip('\n').strip('\r')
		if line.find('[') > -1:
			name = songinfo.getName(line)
			name += line[(line.find(']') + 1):]
			newlines.append(name)
		else:
			newlines.append('n-exist')
	return newlines
