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


def set_name():
    # ask for name
    name = input("Write customer name:\n")
    return name

def set_email():
    # ask for email
    mail = input("Write customer mail:\n")
    return mail

def set_subscribed():
    # ask for subscibe status
    status = input("Subscribtion status:")
    return status

def change_id(id):
    view.console_clear()
    print(f"Actual id is {id}")
    user_input = input("Would you like to generate new id? Y/N\n").lower()
    if user_input == "y" or user_input == "yes":
        new_id = util.generate_id()
        view.console_clear()
        print(f"Actual id is {id}")
        print(f"New id is {new_id}")
        option = input("Would you like to overwrite the old id? Y/N\n")
        if option == "y" or option == "yes":
            return new_id
        elif option == "n" or option == "no":
            return id
    elif user_input == "n" or user_input == "no":
        return id
    else:
        print("fuck off YES OR NO")


def change_name(data, label):
    view.console_clear()
    print(f"Actual {label} is {data}")
    # user_input = input(f"Would you like to set a new {label}? Y/N\n").lower()
    try:
        user_input = input(f"Would you like to set a new {label}? Y/N\n").lower()
        if user_input == "y" or user_input == "yes":
            view.console_clear()
            print(f"Actual {label} is {data}")
            if label == "name":
                new_data = set_name()
            if label == "email":
                new_data = set_email()
            if label == "status":
                new_data = set_subscribed()
            view.console_clear()
            print(f"Actual {label} is {data}")
            print(f"New {label} is {new_data}")
            option = input(f"Would you like to overwrite the old {label}? Y/N\n")
            if option == "y" or option == "yes":
                return new_data
            elif option == "n" or option == "no":
                return data
            else:
                return data
        elif user_input == "n" or user_input == "no":
            return data

    except KeyError as err:
        view.print_error_message(err)


DATAFILE = "model/crm/crm.csv"
HEADERS = "id", "name", "email", "subscribed"
