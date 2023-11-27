import csv
import random
import matplotlib.pyplot as plt

customers_data = []


def random_id_generator():
    return random.randint(200000, 300000)


def save_customer_to_csv(file):
    file_path = file

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(customers_data)


def add_customers():
    customer_name = input("Enter Customer Name : ")
    post_code = input("Enter Customer's Postal Code (Optional) : ")
    phone_no = input("Enter Customer's Phone Number (Optional) : ")
    record = [random_id_generator(), customer_name, post_code, phone_no]
    customers_data.append(record)
    file_path = input("Enter File Name to save your Data : ")
    save_customer_to_csv(file_path)
    print("\nCustomer Id is : ", record[0])


# Transactions
customer_transactions = []

customers_id = []


def get_customers_id():
    data_file = 'Customers.csv'

    with open(data_file, 'r') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for row in file_reader:
            if row:
                customers_id.append(row[0])


def customer_id_checker(inp_id):
    get_customers_id()

    for item in customers_id:
        if item == inp_id:
            return True

    return False


def save_transactions_to_csv(path):
    data_file = path

    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(customer_transactions)


def add_transaction():
    customer_id = input("Enter Customer's ID : ")
    while not customer_id_checker(customer_id):
        print("Customer ID not Found. Try Again.")
        customer_id = input("Enter Customer's ID : ")

    date = input("Enter Date : ")
    category = input("Enter Category : ")
    value = input("Enter Value : ")
    record = [date, random_id_generator(), customer_id, category, value]
    customer_transactions.append(record)
    file_path = input("Enter File Name to save your Data : ")
    save_transactions_to_csv(file_path)
    print("\nTransaction Id is : ", record[1])


# Search Records

# add_transaction()

customers_arr = []


def get_customers():
    data_file = 'Customers.csv'

    with open(data_file, 'r', newline='') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for row in file_reader:
            customers_arr.append(row)


def filter_customers():
    search_input = input("Type Customer Name to Search : ")
    get_customers()
    filtered_customers = [customer for customer in customers_arr if search_input.lower() in customer[1].lower()]
    print(filtered_customers)


# Filter Transactions

transactions_arr = []


def get_transactions():
    data_file = 'Transactions.csv'

    with open(data_file, 'r', newline='') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for row in file_reader:
            transactions_arr.append(row)


def filter_transactions():
    search_input = input("Type Category to Search : ")
    get_transactions()
    filtered_transactions = [transaction for transaction in transactions_arr if
                             search_input.lower() in transaction[3].lower()]
    print(filtered_transactions)


# filter using ID


def filter_transactions_using_id():
    search_input = input("Type ID of Customer to Search : ")
    get_transactions()
    filtered_transactions = [transaction for transaction in transactions_arr if
                             search_input in transaction[2]]
    print(filtered_transactions)


# Delete Transaction

def delete_transaction():
    data_file = 'Transactions.csv'

    trans_id = input("Enter Transaction ID to Delete Record : ")
    get_transactions()
    filtered_records = [record for record in transactions_arr if record[1] != trans_id]

    header = ['date', 'transaction_id', 'customer_id', 'category', 'value']

    with open(data_file, 'w', newline='') as file:
        # writer = csv.DictWriter(file, fieldnames=header)
        # writer.writeheader()
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(filtered_records)


# Delete Customer

def delete_customer():
    transaction_file = 'Transactions.csv'

    trans_id = input("Enter Customer ID to Delete Record : ")
    get_transactions()
    filtered_transactions = [record for record in transactions_arr if record[2] != trans_id]


    with open(transaction_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_transactions)

    get_customers()
    filtered_customers = [customer for customer in customers_arr if customer[0] != trans_id]

    customers_file = 'Customers.csv'

    with open(customers_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(customer_header)
        writer.writerows(filtered_customers)


def menu():
    print("Add Customers : ")
    add_customers()
    print("Add Transactions : ")
    add_transaction()
    print("Search any Customer's Record : ")
    filter_customers()
    print("Search Transactions ( Category ) : ")
    filter_transactions()
    print("Search Transactions Using ID : ")
    filter_transactions_using_id()
    print("Delete any Transaction ")
    delete_transaction()
    print("Delete any Customer : ")
    delete_customer()


menu()


def plot_graph1():
    get_transactions()
    get_customers()

    x_axis = []
    y_axis = []

    for k in range(0, 3):
        for j in range(1, 13):

            n = 0
            sum = 0

            for record in customer_transactions:
                if record[0][:7] == '202' + str(k) + '-' + "{:02d}".format(j):
                    sum += float(record[4])
                    n = n + 1
            if sum != 0:
                x_axis.append(sum)
                y_axis.append(n)

    plt.plot(x_axis, y_axis)

    plt.xlabel('Monthly Sales')
    plt.ylabel('No of Transactions(per month)')

    plt.show()


def plot_graph2():
    get_transactions()
    get_customers()

    customer_id = input("Enter Customer ID : ")
    customers_in_area = []

    x_axis = []
    y_axis = []

    for k in range(0, 3):
        for j in range(1, 13):

            n = 0
            sum = 0

            for record in customer_transactions:
                    if (record[2] == str(customer_id)) and record[0][:7] == '202' + str(k) + '-' + "{:02d}".format(j):
                        sum += float(record[4])
                        n = n + 1
            if sum != 0:
                x_axis.append(sum)
                y_axis.append(n)

    plt.plot(x_axis, y_axis)

    plt.xlabel('Monthly Sales')
    plt.ylabel('No of Transactions(per month)')

    plt.show()



def plot_graph3():
    get_transactions()
    get_customers()

    postal_code = input("Enter Postal Code  :")
    customers_in_area = []

    for customer in customers_arr:
        if postal_code == customer[2]:
            customers_in_area.append(customer[0])

    print(customers_in_area)
    x_axis = []
    y_axis = []

    no_of_customers = customers_in_area.__len__()
    for k in range(0, 3):
        for j in range(1, 13):

            n = 0
            sum = 0

            for record in customer_transactions:
                for m in range(0, no_of_customers):
                    if (record[2] == customers_in_area[m]) and record[0][:7] == '202' + str(k) + '-' + "{:02d}".format(
                            j):
                        sum += float(record[4])
                        n = n + 1
            if sum != 0:
                x_axis.append(sum)
                y_axis.append(n)

    plt.plot(x_axis, y_axis)

    plt.xlabel('Monthly Sales')
    plt.ylabel('No of Transactions(per month)')

    plt.show()


plot_graph3()



def print_all_customers():
    get_customers()
    print(customers_arr)