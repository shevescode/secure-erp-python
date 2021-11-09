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


DATAFILE = "model/sales/sales.csv"
HEADERS = "Id", "Customer", "Product", "Price", "Date"
