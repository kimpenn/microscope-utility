import os
from config import root_directory, LOOP, ROUND, DEBUG_FLG
from handler import try_mkdir, organize_folder
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.DEBUG)  # logging.DEBUG, logging.INFO


def main():
    logging.info(f"Programming running with Debug Mode: {DEBUG_FLG}")
    #########################################
    # Step 1: Set up Parameters
    ##########################################
    # File Prefixes ----------
    file_base_name1 = "Brightfield_10msec_image_"
    file_base_name2 = "DAPI_10msec_image_"
    file_base_name3 = "GFP_GFP_10msec_image_"
    file_base_name4 = "Cy 3_Cy3_50msec_image_"
    # Source Directory ----------
    directory1 = os.path.join(root_directory, "Brightfield")
    directory2 = os.path.join(root_directory, "DAPI")
    directory3 = os.path.join(root_directory, "GFP")
    directory4 = os.path.join(root_directory, "Cy 3")
    # Destination Directory ----------
    move_directory1 = directory1
    move_directory2 = directory2
    move_directory3 = directory3
    move_directory4 = directory4

    ##########################################
    # Step 2: Create Directories
    ##########################################
    logging.info("Creating Directories...")
    try_mkdir(root_directory, "Analytical Model Fitting")
    try_mkdir(root_directory, "Analysis Code")
    try_mkdir(root_directory, "DAPI Analysis")
    try_mkdir(root_directory, "DAPI+BF")
    try_mkdir(root_directory, "GFP ImageJ Analysis")
    try_mkdir(root_directory, "Cy 3 ImageJ Analysis")

    ##########################################
    # Step 3: Organize the folders
    ##########################################
    logging.info("Organizing Directories...")
    organize_folder(directory1, move_directory1, file_base_name1, loop=LOOP, around=1, debug=DEBUG_FLG)
    organize_folder(directory2, move_directory2, file_base_name2, loop=LOOP, around=1, debug=DEBUG_FLG)
    organize_folder(directory3, move_directory3, file_base_name3, loop=LOOP, around=ROUND, debug=DEBUG_FLG)
    organize_folder(directory4, move_directory4, file_base_name4, loop=LOOP, around=ROUND, debug=DEBUG_FLG)


if __name__ == "__main__":
    main()
