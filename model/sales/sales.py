""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from typing import MutableMapping
from model import data_manager, util
from view import terminal as view
import os

def change_ids(id, label):
    """Prints actual transactio id and customer id, asks for new id's and returns new id's to be changed in file"""
    while True:
        view.console_clear()
        print(f"Actual {label} is {id}")
        user_input = input(
            f"Would you like to set a new {label}? Enter 'yes' or 'no'\n").lower()
        if user_input == "yes":
            view.console_clear()
            print(f"Actual {label} is {id}")
            if label == "transaction_id":
                new_id = util.generate_id()
            elif label == "customer_id":
                new_id = util.generate_id()

            while True:
                view.console_clear()
                print(f"Actual {label} is {id}")
                print(f"New {label} is {new_id}")
                option = input(
                    f"Would you like to overwrite the old {label}? Enter 'yes' or 'no'\n")
                if option == "yes":
                    return new_id
                elif option == "no":
                    return id
                else:
                    continue

        elif user_input == "no":
            return id
        else:
            continue

def change_transaction_data(data, label):
    """Prints actual data, asks for new transaction data and returns new transaction data to be changed in file"""
    while True:
        view.console_clear()
        print(f"Actual {label} is {data}")
        user_input = input(
            f"Would you like to set a new {label}? Enter 'yes' or 'no'\n").lower()
        if user_input == "yes":
            view.console_clear()
            print(f"Actual {label} is {data}")
            if label == "product":
                new_data = view.set_data("Write product name: ")
            elif label == "price":
                new_data = view.set_data("Write new price of the product: ")
            elif label == "transaction_date":
                new_data = view.set_data(
                    "Write transaction date: ")

            while True:
                view.console_clear()
                print(f"Actual {label} is {data}")
                print(f"New {label} is {new_data}")
                option = input(
                    f"Would you like to overwrite the old {label}? Enter 'yes' or 'no'\n")
                if option == "yes":
                    return new_data
                elif option == "no":
                    return data
                else:
                    continue

        elif user_input == "no":
            return data
        else:
            continue



DATAFILE = "model/sales/sales.csv"
HEADERS = "Id", "Customer", "Product", "Price", "Date"
