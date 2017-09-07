#! python3
import shutil, os, sys

cFrom = sys.argv[1]
dest = sys.argv[2]
fType= input('What file type?')
movedCount = 0

for f in os.listdir(cFrom):
	if f.endswith(fType) == True:
		shutil.copy(os.path.join(cFrom, f), dest)
		movedCount += 1
		print ('Moved %s file.' % f)
	elif f.endswith(fType) == False:
		print('Did not move %s file.' % f)

print ('Moved %d files.' % movedCount)			

