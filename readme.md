# Microscope Utility
This repository is a python program based Syung-Hun's code to organize the output of microscope.

It is recommended to open the project in Pycharm in the Microscope computer, go to `main.py`, and then click green run button near `if __name__ == "__main__":`.

## Test with Mock Data

Since the real microscope images are very large, it would be convient to make a reduplication of the data but only with the file names. In [Windows](https://stackoverflow.com/questions/39515442/replicate-a-directory-file-structure-with-empty-files), it can be done by 

```
robocopy \mydir \mydir_structure /create /e
```
