import os, shutil

#Where to get the fiels from to back up (test path on Mac - will change for server machine)
sourcePath = "/users/justinwest/Desktop/Server/"

#Where to copy the files to (test path on Mac - will change for server machine)
destinationPath = "/Volumes/SERVERFILES/"

#World folder path (test path on Mac)
worldFolderPath = "/users/justinwest/Desktop/Server/world"

#World folder destination (test path on Mac)
worldFolderDest = "/Volumes/SERVERFILES/world"

#Copy the world folder to destination
shutil.copytree(worldFolderPath, worldFolderDest)

#Get the files in the source directory 
sourceFiles = os.listdir(sourcePath)

#Loop through the files (might not be needed - investigate later)
for individualFile in sourceFiles:
	fullFileName = os.path.join(sourcePath, individualFile)

	#If they are legitimate files, copy them to destination directory
	if os.path.isfile(fullFileName):
		shutil.copy(fullFileName, destinationPath)

#TO-DO:
# First check the destination path - delete previous files / overwrite them