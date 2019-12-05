# support.py
# Support functions for various AOC solutions...

import os

def read_data(fullfile):
    # Use "with" function for clean method to open / close data file
    with open(fullfile) as file:
        data = file.read()
        return data

def read_lines(filename):
    # Use "with" function for clean method to open / close data file
    with open(fullfile) as file:
        data = file.readlines()
        return data

def load_input(filename):
    print("Loading Input File: " + filename)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return read_data(root_dir + "/input_files/" + filename)