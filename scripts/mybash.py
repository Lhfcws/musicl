#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import getopt,sys
from files import inFile

def bash():
	warninfo = 'Please read the help to input the correct commands.\n'
	helpinfo = 'terminal bash:\n	musicl -d my_love\n	music1 -f songs.txt\n	musicl -d my_love happy_you\n	musicl -h\n	musicl -v\nIt doesn\'t support multi option like:\n 	musicl -d my_love -f songs.txt			%Wrong\nor	 musicl -h -v					%Wrong\nor	 musicl -d my_way my_love -h				%Wrong\nOption -f doesn\'t support multi files like:\n  	musicl -f a.txt b.txt   			%Wrong\n\nFile format:\n[my love]Westlife		%Singer can be omitted\n[only you]\n'
	versioninfo = 'musicl v1.0.0\nProduced by # Lhfcws #'
	if (len(sys.argv) > 1):
		try:
			opts, args = getopt.getopt(sys.argv[1:], 'f:hvd')
		except getopt.GetoptError():
			print warninfo + helpinfo

		if len(opts) > 1:
			print warninfo + helpinfo
			return False

	else:
		print warninfo + helpinfo
		return False

	for opt in opts:
		if opt[0] == '-h':
			print helpinfo
		elif opt[0] == '-v':
			print versioninfo
		elif opt[0] == '-f':
			if len(args) > 0:
				print warninfo + helpinfo
				return False
			return inFile(opt[1])
		elif opt[0] == '-d':
			return args
		#else return opt[0]
	
	return True
