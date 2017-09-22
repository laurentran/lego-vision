import os
import shutil

imagePath = os.path.join(os.getcwd(),'uploads')
trainPath = os.path.join(os.getcwd(),'data2','train')
testPath = os.path.join(os.getcwd(),'data2','validation')

files = os.listdir(imagePath)

temp = ''
first = True
newTrainDir = ''
newTestDir = ''
for f in files:
    if not f.startswith("."):
        part = f.split('_')

        if first:
            temp = part[0]
            first = False
            newTrainDir = os.path.join(trainPath, temp)
            os.mkdir(newTrainDir)
            newTestDir = os.path.join(testPath, temp)
            os.mkdir(newTestDir)
        if part[0] != temp: #if new dir needs to be created
            temp = part[0]
            newTrainDir = os.path.join(trainPath, temp)
            os.mkdir(newTrainDir)
            newTestDir = os.path.join(testPath, temp)
            os.mkdir(newTestDir)
        # copy file to new location

        if part[1] != '0.png':
            if part[1] == '2.png' or part[1] == '12.png' or part[1] == '22.png':
                dest = os.path.join(newTestDir, f)
            else:
                dest = os.path.join(newTrainDir, f)
            source = os.path.join(imagePath,f)
            shutil.copy2(source, dest)
