#! python3
import shutil, os, sys, re

cFrom = sys.argv[1]
dest = sys.argv[2]
fType= input('Give a word from the file name:')
searchF = re.compile(fType)

movedCount = 0

for f in os.listdir(cFrom):
	if os.path.isdir(os.path.join(cFrom, f)) == False:
		fLow = f.lower()
		match = searchF.findall(fLow)	
		if len(match) > 0:
			shutil.copy(os.path.join(cFrom, f), dest)
			movedCount += 1
	else:
		pass	

print ('Moved %d files.' % movedCount)	