# Sea-Otter-Graphs

The purpose of the project was to create graphs of sea otter statistics in California using openly available data from the United States Geological Survey's ScienceBase. 
The repository contains two python scripts, a CSV file, and a database file. One of the python files creates an SQL database from the CSV file, and the other creates various graphs from the data in the database. The two main libraries used to create the graphs were the Pandas library and the MatPlotLib library. Sqlite3 was used to execute SQL queries in python. The CSV was taken from the Annual California Sea Otter Census — 1985-2014 Spring Census Summary: U.S. Geological Survey data release, and the database file is the result of the execution of the create_database.py file. 

Data was taken from: https://www.sciencebase.gov/catalog/item/5a32d390e4b08e6a89d88583
