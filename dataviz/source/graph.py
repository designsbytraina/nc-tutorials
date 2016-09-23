"""
Data Visualization Project - New Coder Tutorials

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
from parse import parse, RAW


def visualize_days(parsed_data):
    """Visualize data by day of week"""

    # Make 'counter' from iterating through each line of parsed_data
    # Counts how many incidents happen on each day of the week
    # Note use of list comprehension for finding keys in dicts
    counter = Counter(item["DayOfWeek"] for item in parsed_data)

    # Alternate for loop construction -
    # for item in parsed_data:
    #     counter = Counter(item["DayOfWeek"])

    # Separate the x-axis data (DaysOfWeek) in the 'counter' variable 
    # from the y-axis data (no. of incidents per day)
    data_list = [
                  counter["Monday"],
                  counter["Tuesday"],
                  counter["Wednesday"],
                  counter["Thursday"],
                  counter["Friday"],
                  counter["Saturday"],
                  counter["Sunday"]
                ]

    # A tuple of strings to use for x-axis labels
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # With y-axis data, assign to a matplotlib plot instance
    plt.plot(data_list)

    # Assign labels to the plot from day_tuple
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph to file to render visualization
    plt.savefig("graph-days.png")

    # Close figure
    plt.clf()


def visualize_type(parsed_data):
    """Visualize data by category in a bar graph"""

    # Returns a dict where it sums the total incidents per Category
    counter = Counter(item["Category"] for item in parsed_data)

    # Alternate for loop construction -
    # for item in parsed_data:
    #     counter = Counter(item["Category"])

    # Set the x-axis labels based on the keys in counter, order irrelevant
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis using numpy .arange(), returns list
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar to be plotted
    width = 0.5

    # Assign data to a bar plot, like plt.plot()
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick locations on x-axis, may need to adjust
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Add room so labels aren't cut off in graph, may need to adjust
    plt.subplots_adjust(bottom=0.4)

    # Make graph larger, controls window size
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph to file to render visualization
    plt.savefig("graph-type.png")

    # Close figure
    plt.clf()


def main():
    # Parse data to pass to visualize functions, returns list of dicts
    parsed_data = parse(RAW, ",")

    visualize_days(parsed_data)
    visualize_type(parsed_data)


########################

if __name__ == "__main__":
    main()
