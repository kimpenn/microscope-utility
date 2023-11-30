# Introduction

This repository is a Python program to organize the output of microscope.

It is recommended to open the project in Pycharm in the Microscope computer, go to `main.py`, and then click the green run button near `if __name__ == "__main__":`.

## Main

This file contains code for organizing files based on position numbers. Multi-channel microwell array images are sorted over a time course into folders for each position. 

## Config

This file contains parameters for file organization. `root_directory` is an address to provide input. `LOOP` is the number of positions in a microwell array, always 240. `ROUND` is the number of loops of imaging. This code calls `main` to run the file organization.  

## Test with Mock Data

Since the real microscope images are very large, it would be convient to make a reduplication of the data but only with the file names. In [Windows](https://stackoverflow.com/questions/39515442/replicate-a-directory-file-structure-with-empty-files), it can be done by 

```
robocopy \mydir \mydir_structure /create /e
```
