from model.crm import crm
from model.util import generate_id
from view import terminal as view
from model import data_manager as data
from tabulate import tabulate



def list_customers():
    table = data.read_table_from_file("model/crm/crm.csv", separator=';')
    print(table)
    for index, i in enumerate(table):
        print(f"{index + 1}", i)
    print(tabulate(table, headers=crm.HEADERS, tablefmt='fancy_grid', showindex=True))
    # view.print_error_message("Not implemented yet.")


def add_customer():
    table = data.read_table_from_file("model/crm/crm.csv", separator=';')
    name = crm.set_name()
    mail = crm.set_email()
    status = crm.set_subscribed()
    id = generate_id()
    record = id, name, mail, status
    row = [

                record[0],
                record[1],
                record[2],
                record[3],

    ]
    table.append(row)
    data.write_table_to_file("model/crm/crm.csv", table, separator=';')
    # view.print_error_message("Not implemented yet.")


def update_customer():
    view.print_error_message("Not implemented yet.")


def delete_customer():
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


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
