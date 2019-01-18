# TooLongUtility
A python based utility for windows to address/solve the error : "the file name is too long".

The utility provides the following operations for the folders which have this error
- Copy
- Remove
- Create (Just to check whether this works or not! )

## Requirements
- python 3+
### Libraries
- shutil

## Usage

**Create**

`python TooLongPathCli.py -cr -dst <destination folder path>`

**Remove**

`python TooLongPathCli.py -rm -src <folder and contents to be deleted>`

**Copy**

`python TooLongPathCli.py -cp -src <source folder path> -dst <destination folder path>`