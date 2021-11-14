from model.sales import sales
from view import terminal as view
from tabulate import tabulate
from model import data_manager as data
from model.util import generate_id
from controller import crm_controller
import os


def list_of_transactions():
    """Reads list of sales transactions from a file and prints it as a table"""
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    print(tabulate(table, headers=sales.HEADERS, tablefmt='fancy_grid', showindex=True))
    os.system('pause')


def add_transaction():
    """Allows for adding new transaction, overwrites a file and prints new table with complete list of transactions"""
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    row = view.get_inputs("sales")
    table.append(row)
    data.write_table_to_file("model/sales/sales.csv", table, separator=';')

    print(f"""Another transaction added:

    transaction ID: {row[0]}
    customer ID: {row[1]}
    product: {row[2]}
    price: {row[3]}
    transaction date: {row[4]}
    """)
    os.system('pause')
    view.console_clear()


def get_customer_id_for_transaction():
    """Reads file and returns the ID and Name of customers"""
    while True:
        view.console_clear()
        list_of_customers_id = []
        table = data.read_table_from_file("model/crm/crm.csv", separator=';')

        for i in table:
            x = []
            x.append(i[0])
            x.append(i[1])
            list_of_customers_id.append(x)
        print(tabulate(list_of_customers_id, headers=["ID", "Name"], tablefmt='fancy_grid', showindex=True))
        print("If you can't see the customer on the list, enter 'add' to add the new customer")
        while True:
            try:
                customer_index = input("Choose customer(index): \n")
                if int(customer_index) in range(len(list_of_customers_id)):
                    x = int(customer_index)
                    return list_of_customers_id[x][0]
            except ValueError:
                if str(customer_index) == "add":
                    crm_controller.add_customer()
                else:
                    continue
    os.system('pause')


def update_transaction():
    """Allows for updating any transaction from list and overwrites it in file"""
    view.console_clear()
    list_of_transactions()
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    updating_transaction = int(view.get_input(
        "Which transaction datas would you like to update?"))

    for index, value in enumerate(table):
        if updating_transaction == index:
            # value[0] = sales.change_ids(value[0], "transaction_id")
            # value[1] = sales.change_ids(value[1], "customer_id")
            value[2] = sales.change_transaction_data(value[2], "product")
            value[3] = sales.change_transaction_data(value[3], "price")
            value[4] = sales.change_transaction_data(value[4], "transaction_date")
    data.write_table_to_file("model/sales/sales.csv", table, separator=';')
    os.system('pause')


def delete_transaction():
    """Allows to choose transaction to delete and removes it from file"""
    view.console_clear()
    list_of_transactions()
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    operation = int(view.get_input("Which transaction would you like to delete?"))
    for index, transaction  in enumerate(table):
        if operation == index:
            option = input("Are you sure? Enter 'yes' or 'no'\n")
            if option == "yes":
                table.remove(transaction)
                data.write_table_to_file(
                    "model/sales/sales.csv", table, separator=';')
            elif option == "no":
                break
    view.console_clear()
    list_of_transactions()
    os.system('pause')




def get_biggest_revenue_transaction():
    """Reads file and returns the transaction with the biggest revenue"""
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    x = 0
    y = 0
    for index, value in enumerate(table):
        if float(value[3]) > x:
            y, x = index, float(value[3])

    view.console_clear()
    print(f"""Transaction with the biggest revenue is:

    transaction ID: {table[y][0]}
    customer ID: {table[y][1]}
    product: {table[y][2]}
    price: {table[y][3]}
    transaction date: {table[y][4]}
    """)
    os.system("pause")


def get_biggest_revenue_product():
    """Reads file and returns product name and price with the biggest achieved revenue """
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    product = 0
    cost = 0

    for index, value in enumerate(table):
        if float(value[3]) > cost:
            product = index
            cost = float(value[3])

    view.console_clear()
    print(f"""The biggest revenue has been achived thanks to product:

    product: {table[product][2]}
    price: {table[product][3]}
    """)
    os.system("pause")

def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    """Invokes (calls for) functions depending on user's input"""
    if option == 1:
        list_of_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    """Displays menu options"""
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    """Executes menu"""
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            view.console_clear()
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
