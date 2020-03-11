import os, shutil
import schedule
import time

def backupFiles():
    #Where to get the fiels from to back up (test path on Mac - will change for server machine)
    sourcePath = "/users/justinwest/Desktop/Server/"

    #Where to copy the files to (test path on Mac - will change for server machine)
    destinationPath = "/Volumes/SERVERFILES/"

    #World folder path (test path on Mac)
    worldFolderPath = "/users/justinwest/Desktop/Server/world"

    #World folder destination (test path on Mac)
    worldFolderDest = "/Volumes/SERVERFILES/world"

    #Loop through the destination folder
    for item in os.listdir(destinationPath):

    	#Grab each item in the folder and add it to the path
        filePath = os.path.join(destinationPath, item)

        #Individually delete each item
        try:
            if os.path.isfile(filePath) or os.path.islink(filePath):
                os.unlink(filePath)
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath)

        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (filePath, e))

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

schedule.every().day.at("20:30").do(backupFiles)

while True:
    schedule.run_pending()
    time.sleep(60)

    #TO-DO:
    # First check the destination path - delete previous files / overwrite them
    # Add timing functionality to continuously backup the files in a certain time interval