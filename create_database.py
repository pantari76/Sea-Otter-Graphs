import csv
import sqlite3 as sql


def create_database(cursor):
    # defining the table
    create_table = '''CREATE TABLE otter(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    perimeter DECIMAL NOT NULL,
                    area DECIMAL NOT NULL,
                    depth DECIMAL NOT NULL,
                    atos DECIMAL NOT NULL,
                    hab DECIMAL NOT NULL,
                    acres DECIMAL NOT NULL,
                    hectacres DECIMAL NOT NULL,
                    zonecode DECIMAL NOT NULL,
                    zone DECIMAL NOT NULL,
                    year DECIMAL NOT NULL,
                    polyid DECIMAL NOT NULL,
                    dens DECIMAL NOT NULL,
                    pupratio DECIMAL NOT NULL,
                    lindens DECIMAL NOT NULL,
                    trend5yr DECIMAL NOT NULL,
                    sect DECIMAL NOT NULL);
                    '''

    # Executing the command to make the database
    cursor.execute(create_table)

    # Opening the csv file
    file = open("Otters.csv")

    # Reading the csv file
    contents = csv.reader(file)

    # A string that contains an SQL query that inserts the data from the csv file into the database
    insert_records = "INSERT INTO otter (id, perimeter, area, depth, atos, hab, acres, hectacres, zonecode, zone, " \
                     "year, polyid, dens, pupratio, lindens, trend5yr, sect) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, " \
                     "?, ?, ?, ?, ?, ?, ?)"

    # Executing the query
    cursor.executemany(insert_records, contents)


def print_database(cursor):
    # An SQL query to get all the information from the database for printing
    select_all = "SELECT * FROM otter"
    rows = cursor.execute(select_all).fetchall()

    # Output to console
    for r in rows:
        print(r)


def main():
    # Connecting to the database
    connection = sql.connect('otters.db')

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    create_database(cursor)
    print_database(cursor)

    # Committing the changes to the database
    connection.commit()

    # Closing the connection with the database
    connection.close()


if __name__ == "__main__":
    main()
