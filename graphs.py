import pandas as pd
import matplotlib.pyplot as plt


# A class that allows the user to make graphs easier
class Graphs:
    def __init__(self, cursor):
        self.cursor = cursor

    # A function to create a line graph from two columns in the the database
    def create_line_graph_two_col(self, query, x, y, label, title):
        # fetching data from the SQL database
        df = pd.DataFrame(data=self.cursor.execute(query).fetchall(), columns=[y, x])

        # Sizing the graph
        plt.figure(figsize=(15, 4))

        # Plotting the graph
        plt.plot(df[x], df[y], color="red", label=label)

        # Creating a legend
        plt.legend()

        # Labelling
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)

        # Displaying
        plt.show()

    # A function to create a graph comparing two queries (such as comparing the Pup Ratio between
    # the Sea Otters in Zone N and the Sea Otters in Zone O
    def compare_two_datasets_with_query(self, query1, query2, x, y, label1, label2, title):

        # Executing the queries
        data1 = self.cursor.execute(query1).fetchall()
        data2 = self.cursor.execute(query2).fetchall()

        self.compare_two_datasets(data1, data2, x, y, label1, label2, title)

    # A helper function that creates the plot
    def compare_two_datasets(self, ds1, ds2, x, y, label1, label2, title):
        # Sizing the graph
        plt.figure(figsize=(14, 4))

        # Plotting the graph
        plt.plot(ds1, color="red", label=label1)
        plt.plot(ds2, color="blue", label=label2)

        # Creating a legend
        plt.legend()

        # Labelling
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)

        # Displaying
        plt.show()

    # A function that allows the user to input any two arrays and create a single line plot
    def create_single_line_plot(self, ds1, ds2, x, y, label, title):
        plt.plot(ds2, ds1, color="red", label=label)

        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)

        plt.show()
