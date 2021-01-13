import os, shutil
import schedule
import time

def backupFiles():
    sourcePath = "/users/justinwest/Desktop/Server/"
    destinationPath = "/Volumes/SERVERFILES/"
    worldFolderPath = "/users/justinwest/Desktop/Server/world"
    worldFolderDest = "/Volumes/SERVERFILES/world"

    for item in os.listdir(destinationPath):
        filePath = os.path.join(destinationPath, item)

        try:
            if os.path.isfile(filePath) or os.path.islink(filePath):
                os.unlink(filePath)
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (filePath, e))

    shutil.copytree(worldFolderPath, worldFolderDest)
    sourceFiles = os.listdir(sourcePath)

    for individualFile in sourceFiles:
    	fullFileName = os.path.join(sourcePath, individualFile)

    	if os.path.isfile(fullFileName):
    		shutil.copy(fullFileName, destinationPath)

schedule.every().day.at("20:30").do(backupFiles)

while True:
    schedule.run_pending()
    time.sleep(60)

#NOTE: Periodic timing shamelessly copied from a stack overflow example: https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day

    #TO-DO:
    # First check the destination path - delete previous files / overwrite them
    # Add timing functionality to continuously backup the files in a certain time interval
