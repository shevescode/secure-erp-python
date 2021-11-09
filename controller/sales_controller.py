from model.sales import sales
from view import terminal as view
from tabulate import tabulate
from model import data_manager as data
from model.util import generate_id
from controller import crm_controller
import os


def list_transactions():
    """Reads list of sales from a file and prints it as a table"""
    table = data.read_table_from_file("model/sales/sales.csv", separator=';')
    print(tabulate(table, headers=sales.HEADERS, tablefmt='fancy_grid', showindex=True))


def add_transaction():
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
        print(list_of_customers_id)
        print("If you can't see the customer on the list, enter 'add' to add the new customer")
        while True:
            try:
                customer_index = input("Choose customer(index): \n")
                if int(customer_index) >= 0:
                    return list_of_customers_id[customer_index][0]
            except ValueError:
                if str(customer_index) == "add":
                    crm_controller.add_customer()
                else:
                    continue


def update_transaction():
    view.print_error_message("Not implemented yet.")


def delete_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
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
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            view.console_clear()
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
