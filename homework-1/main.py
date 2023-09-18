"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="password",
    )
    return conn


def fill_customers_table():
    csv_data = []  # Создаем пустой список для хранения данных из CSV файла

    with open('./north_data/customers_data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for item in csvreader:
            csv_data.append(item)

    with get_connection() as conn:
        with conn.cursor() as cursor:
            for item in csv_data:
                customer_id, company_name, contact_name = item
                query = "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s);"
                cursor.execute(query, (customer_id, company_name, contact_name))


def fill_orders_table():
    csv_data = []  # Создаем пустой список для хранения данных из CSV файла

    with open('./north_data/orders_data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for item in csvreader:
            csv_data.append(item)

    with get_connection() as conn:
        with conn.cursor() as cursor:
            for item in csv_data:
                order_id, customer_id, employee_id, order_date, ship_city = item
                query = ("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
                         "VALUES (%s, %s, %s, %s, %s);")
                cursor.execute(query, (order_id, customer_id, employee_id, order_date, ship_city))


def fill_employees_table():
    csv_data = []  # Создаем пустой список для хранения данных из CSV файла

    with open('./north_data/employees_data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for item in csvreader:
            csv_data.append(item)

    with get_connection() as conn:
        with conn.cursor() as cursor:
            for item in csv_data:
                employee_id, first_name, last_name, title, birth_date, notes = item
                query = ("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                         "VALUES (%s, %s, %s, %s, %s, %s);")
                cursor.execute(query, (employee_id, first_name, last_name, title, birth_date, notes))


def main():
    fill_customers_table()
    fill_employees_table()
    fill_orders_table()


if __name__ == '__main__':
    main()