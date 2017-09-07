# MultiCopy
These are four individual programs that do similar things depending on the users needs.

# filecopy.py & beginscopy.py
This program moves files with a user supplied suffix (E.G. .txt) or beginning of a file name. Takes a source and destination via command line using sys.argv.

# containscopy.py
This program moves files by using a regex to match file names against. It also takes a source and destination.

# multicopy.py
This program requires the most user involvement. As with the others it requires a src and destination commandline input via sys.argv. It uses a regex like containscopy but will then prompt for the number of series to look for and will ask whether a new directory needs to  be made to contain the files. By far the most useful program for people who need to clean up download folders or have several similar named files that need to be organized.

If you see any improvements that can be made feel free to use github to give feed back or issue a commit. 
