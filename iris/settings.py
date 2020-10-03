# All project related settings
import os

# Project Folder
PROJECT_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

# Name of the folder where data resides
DATA_FOLDER_NAME = 'MMU-Iris-Database'

# Absolute path to Dataset Folder
DATA_FOLDER_PATH = os.path.abspath(os.path.join(PROJECT_FOLDER_PATH, os.path.pardir, DATA_FOLDER_NAME))



# Testing Purpose
if __name__=="__main__":
    def print_nicely(text, path):
        print("{:<25} \t:\t {}".format(text, path))

        
    print("Project Settings::\n")
    print_nicely("Project Folder", PROJECT_FOLDER_PATH)
    print_nicely("Dataset Folder Name", DATA_FOLDER_NAME)
    print_nicely("Datset Folder", DATA_FOLDER_PATH)