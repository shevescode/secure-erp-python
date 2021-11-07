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


def change_name(name):
    view.console_clear()
    print(f"Actual name is {name}")
    user_input = input("Would you like to set a new name? Y/N\n").lower()
    if user_input == "y" or user_input == "yes":
        view.console_clear()
        print(f"Actual name is {name}")
        new_name = set_name()
        view.console_clear()
        print(f"Actual name is {name}")
        print(f"New name is {new_name}")
        option = input("Would you like to overwrite the old name? Y/N\n")
        if option == "y" or option == "yes":
            return new_name
        elif option == "n" or option == "no":
            return name
    elif user_input == "n" or user_input == "no":
        return name
    else:
        print("fuck off YES OR NO")

def change_email(email):
    view.console_clear()
    print(f"Actual email is {email}")
    user_input = input("Would you like to set a new email? Y/N\n").lower()
    if user_input == "y" or user_input == "yes":
        view.console_clear()
        print(f"Actual email is {email}")
        new_email = set_email()
        view.console_clear()
        print(f"Actual email is {email}")
        print(f"New email is {new_email}")
        option = input("Would you like to overwrite the old email? Y/N\n")
        if option == "y" or option == "yes":
            return new_email
        elif option == "n" or option == "no":
            return email
    elif user_input == "n" or user_input == "no":
        return email
    else:
        print("fuck off YES OR NO")

def change_subscribed(status):
    view.console_clear()
    print(f"Actual subscription status is {status}")
    user_input = input("Would you like to set a new subscription status? Y/N\n").lower()
    if user_input == "y" or user_input == "yes":
        view.console_clear()
        print(f"Actual subscription status is {status}")
        new_status = set_subscribed()
        view.console_clear()
        print(f"Actual subscription status is {status}")
        print(f"New subscription status is {new_status}")
        option = input("Would you like to overwrite the old subscription status? Y/N\n")
        if option == "y" or option == "yes":
            return new_status
        elif option == "n" or option == "no":
            return status
    elif user_input == "n" or user_input == "no":
        return status
    else:
        print("fuck off YES OR NO")


DATAFILE = "model/crm/crm.csv"
HEADERS = "id", "name", "email", "subscribed"