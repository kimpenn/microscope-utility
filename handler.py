import errno
import glob
import logging
import os
import shutil
from config import IMG_EXT, PADDING, START_NUM


def try_mkdir(root_directory, new_dir, debug=True):
    if not debug:
        try:
            os.mkdir(os.path.join(root_directory, new_dir))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            pass
    else:
        logging.debug(f"[try_mkdir] Will create {os.path.join(root_directory, new_dir)}")


def organize_folder(src_dir, des_dir, file_base_name, loop, around=1, debug=True):
    logging.info(f"------ Organizing {file_base_name} ------")

    the_file_name = file_base_name + str(loop*around) + IMG_EXT
    the_file_name_padding = file_base_name + str(loop * around).zfill(PADDING) + IMG_EXT
    if not os.path.exists(os.path.join(src_dir, the_file_name_padding)) and \
            not os.path.exists(os.path.join(src_dir, the_file_name)):
        logging.error(src_dir)
        logging.error(f"[organize_folder] ERR: source file {os.path.join(src_dir, the_file_name_padding)} "
                      f"does not exist! "
                      f"The file may already be moved?")
        logging.error(f"[organize_folder] ERR: source file {os.path.join(src_dir, the_file_name_padding)} "
                      f"does not exist! "
                      f"The file may already be moved?")
        # D:\research\kim - lab\microscope\data\mock - data\Brightfield\Brightfield_BF_1msec_image_00240
    else:
        #  Rename files under the input directory
        for file in os.listdir(src_dir):

            if "Position" in file:
                # Only rename of Images.
                continue

            new_name = file.replace(file_base_name, "").replace(IMG_EXT, "")
            new_name = new_name.zfill(PADDING)
            new_filename = file_base_name + new_name + ".tif"
            os.rename(os.path.join(src_dir, file),
                      os.path.join(src_dir, new_filename))

        # Create directories by indices across the loop
        for x in range(0, loop):
            try_mkdir(des_dir, "Position " + str(x).zfill(3), debug=debug)

        # Put the images into the new directories by indices
        counter = 1
        for file in glob.glob(os.path.join(src_dir, "*" + IMG_EXT)):

            if counter % 10 == 0:
                logging.info(f"Progress in {file_base_name} : {counter}/ {loop*around}")

            the_file_name = os.path.basename(file)

            new_name = the_file_name.replace(file_base_name, "").replace(IMG_EXT, "")
            new_name = int(new_name)
            folder = (new_name - START_NUM) % loop

            new_move_directory = os.path.join(des_dir,
                                              "Position " + str(folder).zfill(3))
            full_path_old = file
            full_path_new = os.path.join(new_move_directory, the_file_name)
            logging.debug(new_name)

            if debug:
                logging.debug(f"full_path_old: {full_path_old}")
                logging.debug(f"full_path_new: {full_path_new}")
            else:
                shutil.move(full_path_old, full_path_new)

            counter += 1

