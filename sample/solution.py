# import necessary modules
import sys
import os
import json

# global variables
INPUT_DATA = None

# custom functions
def track_customers(data):
    # initialize customers dictionary
    customers_dict = dict()

    # store customer details in dictionary
    for order in data:
        customers_dict[order["phone"]] = order["name"]

    # creating output file in respective folder
    os.chdir('../output')
    output_directory = os.getcwd()
    customers_json_path = os.path.join(output_directory, "customers.json")

    # write customer details to output file
    with open(customers_json_path, 'w') as customer_json:
        json.dump(customers_dict, customer_json, indent=4)

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
    # track_items()                # without passing data reference 

if __name__=="__main__":
    main()