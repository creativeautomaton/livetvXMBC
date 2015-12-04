#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import re
import os

team = raw_input("Select Your Team: ")
html = urllib2.urlopen('http://livetv.sx/de/videorecords/?team='+team).read()
tuples = re.findall(r'(<b>\w* \&ndash; \w*</b>)|(/de/showvideo/\d*\w*/hidescore/)', html)

currentGame = False
for tuplee in tuples:
    if not tuplee[1] :
    	currentGame = False
    	print tuplee[0].replace("<b>","").replace("</b>","").replace("&ndash;","-")
    	download = raw_input("Watch this game? (y,n)")
    	if download is "y":
    		currentGame = True
    else:
    	if(currentGame==True):
    		print "Please Wait until the download is going on..."
    		videosite=urllib2.urlopen("http://livetv.sx"+tuplee[1]).read()
    		iframe = re.search(r'http[s]??://vk.com/video_ext.php\?[&;\w\d=-]*',videosite).group(0)
    		videoiframe=urllib2.urlopen(iframe).read()
    		urls = re.findall(r'http[s]??://[\w\d./]*.mp4',videoiframe)
    		start = raw_input("Start this video ? "+urls[::-1][0]+" (y,n)")
    		if start is "y":
    			os.system("open -a /Applications/VLC.app/Contents/MacOS/VLC "+urls[::-1][0])
