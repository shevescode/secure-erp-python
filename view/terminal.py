import os
from model import util
from controller import sales_controller

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f"\n{title}: ")
    for index, i in enumerate(list_options):
        print(f"({index}) {i}")
    #FIXME: exit na koncu listy


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    pass
    #TODO: przenies implementacje


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    print(f"{label}")
    user_input = input("-->")

    return user_input
    #FIXME: input(label)


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    if labels == "sales":
        customer_id = sales_controller.get_customer_id_for_transaction()
        product = set_data("Enter product name: \n")
        price = set_data("Enter the price: \n")
        transaction_date = set_data("Enter the date (like 1996-11-30): \n")
        transaction_id = util.generate_id()
        return [transaction_id, customer_id, product, price, transaction_date]

    elif labels == "crm":
        name = set_data("Enter customer name:")
        mail = set_data("Enter customer email:")
        status = set_data("Subscription status (1: yes, 0: no):")
        id = util.generate_id()
        return [id, name, mail, status]
    #FIXME: na zadane etykiety odpowiada lista od uzytkownika

def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)

def console_clear():
    """Clears terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def set_data(message):
    """Asks for input to set new customer data (name, email, subscription, id, price, product, transaction date) and returns the input value"""
    console_clear()
    data = input(f"{message}\n")
    return data
