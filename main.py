import sqlite3 as sql
from graphs import Graphs


def main():
    # Creating a connection to the database
    connection = sql.connect("otters.db")

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Executing the functions to create graphs from the data

    graph = Graphs(cursor)
    graph.create_line_graph_two_col("SELECT trend5yr, id FROM otter;", "id", "trend5yr", "Trend 5 Year",
                            "Changes in the 5 Year Trend for Sea Otters in California")
    graph.compare_two_datasets_with_query("SELECT pupratio FROM otter WHERE zonecode=\"n\";",
                               "SELECT pupratio FROM otter WHERE zonecode=\"o\";",
                               "Year", "Relative Pup Abundance (Ratio of Pups to Independent Animals)",
                               "Zone N", "Zone O", "Pup Ratio per Otter ID in Zone N vs Zone O")

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

    graph.create_single_line_plot(max_otter_dist, year, "Otter ID", "Otters per Square km of Habitat",
                                  "Max Sea Otter Distribution Per Year", "Maximum Sea Otter Density per Year")
    # Closing the connection
    connection.close()


# Entry point
if __name__ == "__main__":
    main()
