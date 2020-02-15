import os
import shutil

#Where to get the fiels from to back up (sample path)
sourcePath = "/users/justinwest/Desktop/Server/"

#Where to copy the files to (sample path)
destinationPath = "/Volumes/SERVERFILES/"

#Get the files in the source directory 
sourceFiles = os.listdir(sourcePath)

#Loop through the files
for individualFile in sourceFiles:
	fullFileName = os.path.join(sourcePath, individualFile)

	#If they are legitimate files, copy them to destination directory
	if os.path.isfile(fullFileName):
		shutil.copy(fullFileName, destinationPath)



#TO-DO:
# Copy world directory from within the server directory
# First check the destination path - delete previous files / overwrite them