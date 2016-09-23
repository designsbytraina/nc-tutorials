"""
Data Visualization Project - New Coder Tutorials

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""


import csv

# Global variable, path to csv to work with
RAW = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file
    open_csv = open(raw_file)

    # Read CSV file, data is a generator
    data = csv.reader(open_csv, delimiter=delimiter)

    # Setup an empty list to hold parsed_data
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = data.next()

    # Iterate over each row of the csv file, combine together field + value
    for row in data:
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    open_csv.close()

    # Return parsed_data
    return parsed_data


def main():
    # Call our parse function and give it the needed parameters
    new_data = parse(RAW, ",")

    # Let's see what the data looks like!
    print new_data


########################

if __name__ == "__main__":
    main()