# import necessary modules
import sys
import os
import json

# global variables
INPUT_DATA = None

# custom functions
# -------- function to store customer details to an output file --------
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


# -------- function to store item details to an output file --------
def track_items():
    # declare to use global variable
    global INPUT_DATA

    # create local class for order item 
    class Item:
        # class constructor
        def __init__(self, order_price):
            self.price = order_price
            self.count = 1

        # function to convert Item class object to dictionary
        def to_dict(self):
            return {
                'price': self.price,
                'orders': self.count
            }

    # initialize items dictionary
    items_dict = dict()

    # storing item details in dictionary in respective format
    for order in INPUT_DATA:
        # read order items
        order_items = order["items"]

        for item in order_items:
            # get item name
            item_name = item["name"]
            
            # check if item is ordered for the first time
            if item_name not in items_dict.keys():
                item_price = item["price"]
                item_entry = Item(item_price)
                items_dict[item_name] = item_entry
            else:
                item_entry = items_dict[item_name]
                item_entry.count += 1

    # sort items dictionary in alphabetical order
    items_dict = {key: items_dict[key] for key in sorted(items_dict)}

    # convert dictionary objects to dictionary to match json format
    for key, value in items_dict.items():
        items_dict[key] = value.to_dict()
        
    
    # creating output file in respective folder
    # os.chdir('../output') --> not needed as already changed by previous function
    output_directory = os.getcwd()
    items_json_path = os.path.join(output_directory, "items.json")

    # write item details to output file
    with open(items_json_path, 'w') as customer_json:
        json.dump(items_dict, customer_json, indent=4)


# entry function of code
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

# call entry function of file
if __name__=="__main__":
    main()