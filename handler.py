import errno
import glob
import os
import shutil
from config import LOOP, IMG_EXT, PADDING, START_NUM


def try_mkdir(root_directory, new_dir):
    try:
        os.mkdir(os.path.join(root_directory, new_dir))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass


def organize_folder(src_dir, des_dir, file_base_name):
    the_file_name = file_base_name + str(LOOP) + IMG_EXT
    if not os.path.exists(os.path.join(src_dir, the_file_name)):
        print(f"[organize_folder] ERR: file {the_file_name} does not exist!")
    else:
        #  Rename files under the input directory
        for file in os.listdir(src_dir):
            new_name = file.replace(file_base_name, "").replace(IMG_EXT, "")
            new_name = new_name.zfill(PADDING)
            print(new_name)
            new_filename = file_base_name + new_name + ".tif"
            os.rename(os.path.join(src_dir, file),
                      os.path.join(src_dir, new_filename))

        # Create directories by indices across the loop
        for x in range(0, LOOP):
            try_mkdir(des_dir, "Position " + str(x).zfill(3))

        # Put the images into the new directories by indices
        for file in glob.glob(os.path.join(src_dir, "*" + IMG_EXT)):
            new_name = file.replace(file_base_name, "").replace(IMG_EXT, "")
            new_name = int(new_name)
            folder = (new_name - START_NUM) % LOOP

            new_move_directory = os.path.join(des_dir,
                                              "Position " + str(folder).zfill(3))
            full_path_old = os.path.join(src_dir, file)
            full_path_new = os.path.join(new_move_directory, file)
            print(new_name)

            shutil.move(full_path_old, full_path_new)
