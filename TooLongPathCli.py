# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:56:30 2018

@author: Qaisar.Tanvir

NOTE: 
Intent of this code script is just solve a windows error and correct it. Any users who use it are soley responsible for any potential harm caused to any person machine or object.
Additionally, this code comes under No Harm License, For further details read the license file in the repo.
Any malicious use of this code by any user/person is not the authors responsibility in any capacity. Those malicious users/people will be soley responsible in any court of law
PLEASE BEAWARE OF ANY MISUSE 
"""
import os
import shutil
import sys
import argparse

# initiate the parser
parser = argparse.ArgumentParser()  
parser.add_argument("-rm", "--remove", help="Removes too long folders", action="store_true")
parser.add_argument("-cp", "--copy", help="Copies too long source folder items to destination folder", action="store_true")
parser.add_argument("-cr", "--create", help="Makes recusive folders inside a folder", action="store_true")
parser.add_argument("-src", "--source", help="Source path of the folder")
parser.add_argument("-dst", "--destination", help="Destination path of the folder")
parser.add_argument("-f_name", "--folder_name", help="Folder Name, Dont use special characters")
# read arguments from the command line
args = parser.parse_args()

# Remove directory which has too long path recursively
def remove_dir(path):
    abs_path = os.path.abspath(path)
    ext_path = r"\\?\%s" % abs_path
    try:
        print(ext_path)
        shutil.rmtree(ext_path)
    except FileNotFoundError:
        print("The system cannot find the path specified: '%s'" % path)

# Copy too long directory tree from one folder to other
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        s = r"\\?\%s" % s
        d = r"\\?\%s" % d
        print("Copying :" + s)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

# Making recursive directories (to experiment too long paths)
def makedirs(dst_path, name, iterations):
    abs_path = os.path.abspath(dst_path)
    #dir_name = path.split("\\")[-1] # Last name if absolute path
    ext_path = r"\\?\%s" % abs_path
    for _ in range(iterations):
        ext_path += r"\%s" % name
    try:
        os.makedirs(ext_path)
    except FileExistsError:
        print('Directory already exists')

# for deletion
if args.remove and args.source:  
    print("Remove scripts started")
    rmv_path = str(args.source)
    remove_dir(rmv_path)     

# for copy
if args.copy and args.source and args.destination:  
    print("Copy scripts started")
    src_path = str(args.source)
    dst_path = str(args.destination)
    copytree(src_path, dst_path)

# for create
if args.create and args.destination: 
    print("Create scripts started")
    dst_path = str(args.destination)
    if args.folder_name is NULL:
        dir_name = "Delete me if you can"
    else:
        dir_name = str(args.folder_name)
    makedirs(dst_path, dir_name, 500)
