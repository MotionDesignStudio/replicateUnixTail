#!/usr/bin/env python3.5

import subprocess
#
import os
#
import inspect


def replicateUnixTail (file_source, start_from=0, increment_in_bytes=-1024):
	#This feel hackish I noticed that this gives me an extra blank line that does
	#not exist in the file
	start_from=start_from+1
	mylist = list()
	init_bytes=0
	f = open(file_source, "rb+")

	#This will check that the file size is not smaller than the increment_in_bytes
	#If it is set increment_in_bytes to the max size of the file size
	if os.path.getsize(file_source) < abs ( increment_in_bytes ) :
		#print ("Less Than")
		increment_in_bytes= os.path.getsize(file_source) * -1
		f.seek (increment_in_bytes, 2 )
		tmp = f.read().decode("utf-8")
		mylist= tmp.split('\n')
		print (printOutputList(mylist))
	else:
		while True:
			init_bytes+=increment_in_bytes
			f.seek (init_bytes, 2 )
			tmp = f.read().decode("utf-8")
			mylist= tmp.split('\n')	
			if len(mylist) > start_from :
				f.seek (init_bytes, 2 )
				tmp = f.read().decode("utf-8")
				mylist= tmp.split('\n')	
				print (printOutputList(mylist[-start_from:]))
				break


def printOutputList (mylist):
	# Begin check which function is calling printOutputList
	cur_frame = inspect.currentframe()
	cal_frame = inspect.getouterframes(cur_frame, 2)
	# End check which function is calling printOutputList
	# I had to do this because replicateUnixTail2 does not need the lines break added
	mystring=''
	for lines in mylist:
		if cal_frame[1][3] != 'replicateUnixTail2' :
			mystring+=lines+"\n"
		else:
			mystring+=lines
	return mystring

def replicateUnixTail2 (file_source, start_from=0, increment_in_bytes=-1024):
	f = open(file_source, "rb+").readlines()
	print (printOutputList( f[-start_from:] ))
	

def replicateUnixTail3 (file_source,  startfrom=None):
	mt_tail_output=subprocess.call(['tail', str(startfrom), file_source])
	print (mt_tail_output)


#replicateUnixTail (file_source="street.txt", start_from=10, increment_in_bytes=-256 )

#replicateUnixTail2 (file_source="street.txt", start_from=10, increment_in_bytes=-256 )

#replicateUnixTail3 (file_source="street.txt", startfrom=-10 )


