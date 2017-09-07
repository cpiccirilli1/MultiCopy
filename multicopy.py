#!/usr/bin/python3/
import shutil, os, sys, re

copyFrom = sys.argv[1]
dest = sys.argv[2]

print('How many series are we moving?')
numSeries = int(input(": "))
movedCount = 0

for i in range(numSeries):
	whichSeries= input('Give a word from the file name:')
	wslower = whichSeries.lower()
	searchF = re.compile(wslower)
	print ('Does %s series need a new folder? Y/n' % whichSeries)
	seriesF = input(': ')
	seriesf = seriesF.lower()

	if seriesf == 'y':
		print ('What would you like to name your folder?')
		folderName = input(': ')
		os.makedirs(os.path.join(dest, folderName))
		print ('Folder created for %s.' % folderName)
			
	elif seriesf == 'n':
		print('Ok. We wont create a folder for %s.' % whichSeries)
		print('Which folder would you like me to move it to?')
		folderName = input(': ')
	else:
		pass


	for f in os.listdir(copyFrom):
		if os.path.isdir(os.path.join(copyFrom, f)) == False:
			try:
				fLow = f.lower()
				match = searchF.findall(fLow)	
				if len(match) > 0:
					shutil.move(os.path.join(copyFrom, f), os.path.join(dest, folderName))
					#os.path.unlink(os.path.join(copyFrom, f))
					movedCount += 1
			except OSError:
				print('Unable to move %s.' % match )
		else:
			pass	

print ('Moved %d files.' % movedCount)	