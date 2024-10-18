# import necessary modules
import sys
import os
import json

# global variables
INPUT_DATA = None

# custom functions
def track_customers(data):
    pass

def track_items():
    global INPUT_DATA
    pass

def main():
    # read filename from script arguments
    file_name = sys.argv[1]
    global INPUT_DATA 

    # fetch json data from the input file
    with open(file_name, 'r') as input_file:
        INPUT_DATA = json.load(input_file)

    # create customers.json
    track_customers(INPUT_DATA)      # with passing data reference 

    # create items.json
    track_items()                # without passing data reference 

if __name__=="__main__":
    main()