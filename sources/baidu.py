#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import urllib

def getLink(downlines):
	searchkey = ['id="downlink"', 'class="f12 gray9"', 'encurl = urlM(', 'subulrs = [urlM(']
	for downline in downlines:
		downline = ''.join(downline)
		item = -1
		for key in searchkey:
			index = downline.find(key)
			if index > -1:
				item = searchkey.index(key)
				break
		if item == -1: 
			continue
		
		if item == 1:
			return 'n-exist'

		if item == 0:
			index = downline.find('href=') + 6
			addr = ''
			while index < len(downline):
				addr += downline[index]
				index += 1
				if downline[index] == '\"':
					break
			return addr
		
		if item == 2:
			index = downline.find('encurl = urlM(') + 14
			addr = ''
			while index < len(downline):
				addr += downline[index]
				index += 1
				if downline[index] == ')':
					addr = eval(addr)
					return addr

def getMusic(keyword):
	keyword = urllib.quote(keyword.decode('utf-8').encode('gb2312'))
	addr = 'http://mp3.baidu.com/m?word=' + keyword	
	print addr
	webpage = urllib.urlopen(addr)
	weblines = webpage.readlines()
	classDown = 'class="btn_replace bg_btn t_down"'
	downlink = ''
	for webline in weblines:
		webline = ''.join(webline)
		if webline.find(classDown) < 0:
			continue
		index = webline.find('href') + 6
		addr1 = ''
		while index < len(webline):
			if webline[index] == '\"':
				break
			addr1 += webline[index]
			index += 1
		downpage = urllib.urlopen(addr1)
		downlines = downpage.readlines()
		downlink = getLink(downlines)
		
		if downlink == 'n-exist':
			continue
		else:
			break
	if downlink[0] == '/':
		downlink = 'http://mp3.baidu.com' + downlink

	return downlink
