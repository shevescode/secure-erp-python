""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from typing import MutableMapping
from model import data_manager, util
from view import terminal as view

def set_customer_data(message):
    """Asks for input to set new customer data (name, email, subscription) and returns the input value"""
    view.console_clear()
    data = input(f"{message}\n")
    return data

def change_id(id):
    """Prints actual ID, calls for generate_id() to generate a new ID and returns new ID to be changed in file"""
    while True:
        view.console_clear()
        print(f"Actual id is {id}")
        user_input = input("Would you like to generate new id? Enter 'yes' or 'no'\n").lower()
        if user_input == "yes":
            new_id = util.generate_id()

            while True:
                view.console_clear()
                print(f"Actual id is {id}")
                print(f"New id is {new_id}")
                option = input("Would you like to overwrite the old id? Enter 'yes' or 'no'\n")
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


def change_data(data, label):
    """Prints actual data, asks for new data and returns new data to be changed in file"""
    while True:
        view.console_clear()
        print(f"Actual {label} is {data}")
        user_input = input(f"Would you like to set a new {label}? Enter 'yes' or 'no'\n").lower()
        if user_input == "yes":
            view.console_clear()
            print(f"Actual {label} is {data}")
            if label == "name":
                new_data = set_customer_data("Write customer name:")
            elif label == "email":
                new_data = set_customer_data("Write customer email:")
            elif label == "status":
                new_data = set_customer_data("Subscription status (1: yes, 0: no):")

            while True:
                view.console_clear()
                print(f"Actual {label} is {data}")
                print(f"New {label} is {new_data}")
                option = input(f"Would you like to overwrite the old {label}? Enter 'yes' or 'no'\n")
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



DATAFILE = "model/crm/crm.csv"
HEADERS = "id", "name", "email", "subscribed"
