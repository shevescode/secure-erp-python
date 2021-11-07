from model.crm import crm
from model.util import generate_id
from view import terminal as view
from model import data_manager as data
from tabulate import tabulate



def list_customers():
    table = data.read_table_from_file("model/crm/crm.csv", separator=';')
    print(tabulate(table, headers=crm.HEADERS, tablefmt='fancy_grid', showindex=True))


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


def update_customer():
    #TODO: zrobic funkcje change.. uniwersalne
    view.console_clear()
    list_customers()
    table = data.read_table_from_file("model/crm/crm.csv", separator=';')
    operation = int(view.get_input("Which customer info would you like to update?"))

    for index, i in enumerate(table):
        if operation == index:
            i[0] = crm.change_id(i[0])
            i[1] = crm.change_name(i[1], "name")
            i[2] = crm.change_name(i[2], "email")
            i[3] = crm.change_name(i[3], "status")
    data.write_table_to_file("model/crm/crm.csv", table, separator=';')

def delete_customer():
    view.console_clear()
    list_customers()
    table = data.read_table_from_file("model/crm/crm.csv", separator=';')
    operation = int(view.get_input("Which customer would you like to delete?"))
    for index, i in enumerate(table):
        if operation == index:
            option = input("Are you sure? Y/N\n")
            if option == "y" or option == "yes":
                table.remove(i)
                data.write_table_to_file("model/crm/crm.csv", table, separator=';')
            elif option == "n" or option == "no":
                break
    view.console_clear()
    list_customers()

def get_subscribed_emails():
    list_of_subscribed_emails = []
    table = data.read_table_from_file("model/crm/crm.csv", separator=';')
    print(tabulate(table, headers=crm.HEADERS, tablefmt='fancy_grid', showindex=True))

    for i in table:
        if i[3] == "1":
            x = []
            x.append(i[2])
            list_of_subscribed_emails.append(x)

    print(tabulate(list_of_subscribed_emails, headers=["Subscribed emails"], tablefmt='fancy_grid', showindex=True))

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
