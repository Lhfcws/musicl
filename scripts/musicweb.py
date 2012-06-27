#!/usr/bin/env python
# -*- coding: utf-8 -*-

def linkMusic(keyword):
	pass
	fil = open('.conf','r')
	lines = fil.readlines()
	fil.close()
	dlink = []
	for line in lines:
		if line[-1] == '\n':
			line = line[:-1]
		exec('from sources.' + line + ' import getMusic')
		dlink = getMusic(keyword)
		if dlink == 'n-exist':
			continue
		else:
			break
	return dlink
