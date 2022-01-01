import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt


def five_year_trend_graph(cursor):
    # Creates a line graph of the changes in the 5 year trend of the Sea Otters population
    # throughout the 29 years of surveying

    # Creating an SQL query to get the data for the 5 Year Trend and id from the database
    select_data = "SELECT trend5yr, id FROM otter;"

    # Creating a Pandas DataFrame that contains the data
    df = pd.DataFrame(data=cursor.execute(select_data).fetchall(), columns=["trend5yr", "id"])

    # Setting the x and y value for plotting the graph
    x = df["id"]
    y = df["trend5yr"]

    # Sizing the graph
    plt.figure(figsize=(15, 4))

    # Plotting the graph
    plt.plot(x, y, color="red", label="Trend 5 Year")

    # Creating a legend
    plt.legend()

    # Labelling
    plt.xlabel("Otter Data ID")
    plt.ylabel("Rate of Change of Otters per Square km of Habitat")
    plt.title("Changes in the 5 Year Trend for Sea Otters in California")

    # Displaying
    plt.show()


def zone_n_v_o(cursor):
    # The function creates a graph comparing the Pup Ratio between the Sea Otters in Zone N
    # and the Sea Otters in Zone O

    # Creating SQL queries to get the Pup Ratio from Zone N and Zone O
    select_zone_n = "SELECT pupratio FROM otter WHERE zonecode=\"n\";"
    select_zone_o = "SELECT pupratio FROM otter WHERE zonecode=\"o\";"

    # Executing the queries
    pupratio_n = cursor.execute(select_zone_n).fetchall()
    pupratio_o = cursor.execute(select_zone_o).fetchall()

    # Sizing the graph
    plt.figure(figsize=(14, 4))

    # Plotting the graph
    plt.plot(pupratio_n, color="red", label="Zone N")
    plt.plot(pupratio_o, color="blue", label="Zone O")

    # Creating a legend
    plt.legend()

    # Labelling
    plt.xlabel("Year")
    plt.ylabel("Relative Pup Abundance (Ratio of Pups to Independent Animals)")
    plt.title("Pup Ratio per Otter ID in Zone N vs Zone O")

    # Displaying
    plt.show()


def max_sea_otter_distribution_chart(cursor):
    # Find the maximum sea otter density for each year and plots the data in a line graph

    # Creating two empty lists
    max_otter_dist = []
    year = []

    # A for loop the creates and executes an SQL query to find the max otter density for each year, which
    # is then appended to a list
    for i in range(1985, 2014):
        select_data = "SELECT MAX(dens) FROM otter WHERE year=\"" + str(i) + "\";"
        max_otter_dist.append(cursor.execute(select_data).fetchone())

    # A for loop that creates a list to serve as the x-axis for the graph
    for i in range(1985, 2014):
        year.append(i)

    # Plotting the graph
    plt.plot(year, max_otter_dist, color="red", label="Max Sea Otter Distribution Per Year")

    # Labelling
    plt.xlabel("Otter ID")
    plt.ylabel("Otters per Square km of Habitat")
    plt.title("Maximum Sea Otter Density per Year")

    # Displaying
    plt.show()


def main():
    # Creating a connection to the database
    connection = sql.connect("otters.db")

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Executing the functions to create graphs from the data
    five_year_trend_graph(cursor)
    max_sea_otter_distribution_chart(cursor)
    zone_n_v_o(cursor)

    # Closing the connection
    connection.close()


if __name__ == "__main__":
    main()
