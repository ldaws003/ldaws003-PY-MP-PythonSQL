"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect(":memory")
cursor = conn.cursor()


# Create a dogs table with autoincrementing ID
def create_dogs_table():

    cursor.execute("""CREATE TABLE dog(
    id SERIAL PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INT)""")
    conn.commit()


# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):

    cursor.execute(f'INSERT INTO dog (name, breed, age) VALUES ({name}, {breed}, {age})')
    conn.commit()


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():
    # return the rows
    cursor.execute("SELECT * FROM dog")
    return cursor.fetchall()
