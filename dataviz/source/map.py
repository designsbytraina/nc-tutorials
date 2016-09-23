"""
Data Visualization Project - New Coder Tutorials

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot as a map.

Part III: Take the data we parsed earlier and create a different format
for rendering a map. Here, we parse through each line item of the
CSV file and create a geojson object, to be collected into one geojson
file for uploading to gist.github.com.
"""

import geojson

from parse import parse, RAW


def create_map(parsed_data):
    """Creates a GeoJSON file.

    Returns a GeoJSON file that can be rendered in a GitHub
    Gist at gist.github.com. Just copy the output file and
    paste into a new Gist, then create either a public or
    private gist. GitHub will automatically render the GeoJSON
    file as a map.
    """

    # Define type of geojson to be created
    geo_map = {"type": "FeatureCollection"}

    # Declare empty list for points to graph
    point_list = []

    # Iterate through data to create geojson document
    # Using enumerate() to get the line and index/line number
    for index, line in enumerate(parsed_data):
        # Skip zeroes, essentially skips errors in data for lat/lng
        if line['X'] == "0" or line['Y'] == "0":
            continue

        # Setup a temp dict for each iteration to append to point_list
        data = {}

        # Assign line items to geojson fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # Append each data dict to point_list
        point_list.append(data)

    # Build geomap point by adding point_list items to geomap dict
    for point in point_list:
        geo_map.setdefault('features', []).append(point)

    # Save map as geojson file, using 'with' will auto-close file when done
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))


def main():
    # Parse data to pass to visualize functions, returns list of dicts
    parsed_data = parse(RAW, ",")

    return create_map(parsed_data)


########################

if __name__ == "__main__":
    main()