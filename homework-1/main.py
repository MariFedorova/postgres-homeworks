"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="1234"
)
try:
    with conn:
        with conn.cursor() as cur:
            #with open('../homework-1/north_data/customers_data.csv', encoding="CP1251") as csvfile:
                #reader = csv.reader(csvfile)
                #data = list(reader)
                #for row in data:
                    #cur.execute('INSERT INTO customers  VALUES (%s, %s, %s)', (row[0],row[1], row[2]))

            with open('../homework-1/north_data/employees_data.csv', encoding="CP1251") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")

                for row in reader:
                    cur.execute('INSERT INTO employee  VALUES (%s, %s, %s,%s, %s, %s)', (row["employee_id"],row["first_name"], row["last_name"], row["title"],row["birth_date"], row["notes"]))

            with open('../homework-1/north_data/orders_data.csv', encoding="CP1251") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    cur.execute('INSERT INTO orders  VALUES (%s, %s, %s, %s, %s)', (row["order_id"],row["customer_id"], row["employee_id"], row["order_date"],row["ship_city"]))

finally:
    conn.close()
