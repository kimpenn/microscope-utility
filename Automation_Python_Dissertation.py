import os
import glob
import shutil
import time
# FIX THIS LINE ##########################
root_directory = "E:/Syung-Hun/2020-06-26 (pHrodo Endo 6NBDG)/pHrodo_Endo_6NBDG/"
loop = 240
rnd = 40
filebasename1 = "Brightfield_10msec_image_"
filebasename2 = "DAPI_10msec_image_"
filebasename3 = "GFP_GFP_10msec_image_"
filebasename4 = "Cy 3_Cy3_50msec_image_"
##########################################
directory1 = root_directory + "Brightfield/"
directory2 = root_directory + "DAPI/"
directory3 = root_directory + "GFP/"
directory4 = root_directory + "Cy 3/"
# directory path for the files to be sorted out
movedirectory1 = directory1
movedirectory2 = directory2
movedirectory3 = directory3
movedirectory4 = directory4
padding = 5
startnumber = 1

try:
 os.mkdir(root_directory+"Analytical Model Fitting")
except OSError:
 if not os.path.isdir(root_directory+"Analytical Model Fitting"):
    raise
try:
 os.mkdir(root_directory+"Analysis Code")
except OSError:
 if not os.path.isdir(root_directory+"Analysis Code"):
    raise
try:
 os.mkdir(root_directory+"DAPI Analysis")
except OSError:
 if not os.path.isdir(root_directory+"DAPI Analysis"):
    raise
try:
 os.mkdir(root_directory+"DAPI+BF")
except OSError:
 if not os.path.isdir(root_directory+"DAPI+BF"):
    raise
try:
 os.mkdir(root_directory+"GFP ImageJ Analysis")
except OSError:
 if not os.path.isdir(root_directory+"GFP ImageJ Analysis"):
    raise

try:
 os.mkdir(root_directory+"Cy 3 ImageJ Analysis")
except OSError:
    if not os.path.isdir(root_directory + "Cy 3 ImageJ Analysis"):
        raise
    os.chdir(directory1)
    while os.path.exists(directory1 + filebasename1 + str(loop) + ".tif") == 0:
        time.sleep(60)
    else:
        for file in os.listdir(directory1):
            newname = file.replace(filebasename1, "").replace(".tif", "")
            newname = newname.zfill(padding)
            print(newname)
            new_filename = filebasename1 + newname + ".tif"
            os.rename(os.path.join(directory1, file), os.path.join(directory1, new_filename))
        for x in range(0, loop):
            try:
                os.mkdir(movedirectory1 + "Position " + str(x).zfill(3))
            except OSError:
                if not os.path.isdir(movedirectory1 + "Position " + str(x).zfill(3)):
                    raise
        for file in glob.glob("*.tif"):
            newname = file.replace(filebasename1, "").replace(".tif", "")
            newname = int(newname)
            folder = (newname - startnumber) % loop
            newmovedirectory = movedirectory1 + "Position " + str(folder).zfill(3) + "/"
            fullpathold = directory1 + file
            fullpathnew = newmovedirectory + file
            print(newname)
            shutil.move(fullpathold, fullpathnew)
        os.chdir(root_directory)
        open('BF_Padding_Locating_Done', 'a').close()


    os.chdir(directory2)
    while os.path.exists(directory2 + filebasename2 + str(loop) + ".tif") == 0:
        time.sleep(60)
    else:
        for file in os.listdir(directory2):
            newname = file.replace(filebasename2, "").replace(".tif", "")
            newname = newname.zfill(padding)
            print(newname)
            new_filename = filebasename2 + newname + ".tif"
            os.rename(os.path.join(directory2, file), os.path.join(directory2, new_filename))
        for x in range(0, loop):
            try:
                os.mkdir(movedirectory2 + "Position " + str(x).zfill(3))
            except OSError:
                if not os.path.isdir(movedirectory2 + "Position " + str(x).zfill(3)):
                    raise
        for file in glob.glob("*.tif"):
            newname = file.replace(filebasename2, "").replace(".tif", "")
            newname = int(newname)
            folder = (newname - startnumber) % loop
            newmovedirectory = movedirectory2 + "Position " + str(folder).zfill(3) + "/"
            fullpathold = directory2 + file
            fullpathnew = newmovedirectory + file
            print(newname)
            shutil.move(fullpathold, fullpathnew)
        os.chdir(root_directory)
        open('DAPI_Padding_Locating_Done', 'a').close()


    os.chdir(directory3)
    while os.path.exists(directory3 + filebasename3 + str(loop * rnd) + ".tif") == 0:
        time.sleep(60)
    else:
        for file in os.listdir(directory3):
            newname = file.replace(filebasename3, "").replace(".tif", "")
            newname = newname.zfill(padding)
            print(newname)
            new_filename = filebasename3 + newname + ".tif"
            os.rename(os.path.join(directory3, file), os.path.join(directory3, new_filename))
        for x in range(0, loop):
            try:
                os.mkdir(movedirectory3 + "Position " + str(x).zfill(3))
            except OSError:
                if not os.path.isdir(movedirectory3 + "Position " + str(x).zfill(3)):
                    raise
        for file in glob.glob("*.tif"):
            newname = file.replace(filebasename3, "").replace(".tif", "")
            newname = int(newname)
            folder = (newname - startnumber) % loop
            newmovedirectory = movedirectory3 + "Position " + str(folder).zfill(3) + "/"
            fullpathold = directory3 + file
            fullpathnew = newmovedirectory + file
            print(newname)
            shutil.move(fullpathold, fullpathnew)
        os.chdir(root_directory)
        open('GFP_Padding_Locating_Done', 'a').close()


    os.chdir(directory4)
    while os.path.exists(directory4 + filebasename4 + str(loop * rnd) + ".tif") == 0:
        time.sleep(60)
    else:
        for file in os.listdir(directory4):
            newname = file.replace(filebasename4, "").replace(".tif", "")
            newname = newname.zfill(padding)
            print(newname)
            new_filename = filebasename4 + newname + ".tif"
            os.rename(os.path.join(directory4, file), os.path.join(directory4, new_filename))
        for x in range(0, loop):
            try:
                os.mkdir(movedirectory4 + "Position " + str(x).zfill(3))
            except OSError:
                if not os.path.isdir(movedirectory4 + "Position " + str(x).zfill(3)):
                    raise
        for file in glob.glob("*.tif"):
            newname = file.replace(filebasename4, "").replace(".tif", "")
            newname = int(newname)
            folder = (newname - startnumber) % loop
            newmovedirectory = movedirectory4 + "Position " + str(folder).zfill(3) + "/"
            fullpathold = directory4 + file
            fullpathnew = newmovedirectory + file
            print(newname)
            shutil.move(fullpathold, fullpathnew)
        os.chdir(root_directory)
        open('Cy 3_Padding_Locating_Done', 'a').close()