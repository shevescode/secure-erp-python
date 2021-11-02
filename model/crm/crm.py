""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


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


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
