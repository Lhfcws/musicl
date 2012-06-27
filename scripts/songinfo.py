#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from string import maketrans

def getName(st):
	left = st.index('[')
	right = st.index(']')
	thisName = st[left+1:right]
	print thisName
	return thisName.strip()

def translateChinese(chinst):
	pass	

'''
temp:
def getSinger(st):
	index = st.index(']')
	table = maketrans('','')[97:123] + maketrans('','')[65:91]
	singer = '';
	print len(st)
	while index < len(st):
		index += 1
		if st[index] in table:
			singer += st[index]
		else:
			if len(singer)>0:
				break
			else:
				continue
	print singer
	settrace()
	return singer.strip()
'''
