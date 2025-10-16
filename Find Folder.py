'''
Contributor(s): Riley Becker

Purpose: Used for testing to access folders in my directory (file explorer)
'''

import os

#Run this first to see what path (in your directory) this file is downloaded in
import os
print(os.getcwd())

#Run this to see whether the listed file is in your directory
path = "C:/RocketPy/NACA0012-radians.txt"
print("File exists:", os.path.exists(path))

#Run this to see all the files in your directory currently
folder = "C:/RocketPy"  # change if needed
print("Files in folder:", os.listdir(folder))


