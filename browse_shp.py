import geopandas as gpd
import csv
import sys

def map_field_type(pandas_type):
    """
    Map Pandas/GeoPandas types to GIS-like descriptive types.
    """
    if pandas_type == "int64":
        return "Integer (64 bit)"
    elif pandas_type == "float64":
        return "Decimal (double)"
    elif pandas_type == "object":
        return "Text (string)"
    elif pandas_type == "geometry":
        return "Geometry"
    else:
        return str(pandas_type)

def browse_shp(input_shapefile):

    try:
        # Load the shapefile
        shapefile_data = gpd.read_file(input_shapefile)
    except Exception as e:
        print(f"Error reading shapefile: {e}")
        return None

    # Extract fields and map types
    fields_info = [{"Field Name": field_name, "Type": map_field_type(str(dtype))} 
                   for field_name, dtype in shapefile_data.dtypes.items()]

    return fields_info


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <input_shapefile>")
        sys.exit(1)

    # Command-line argument
    input_shapefile = sys.argv[1]

    # Process the shapefile
    fields_info = browse_shp(input_shapefile)

    if fields_info:
        # Write results to CSV
        output_csv = "fields_and_types.csv"
        try:
            with open(output_csv, mode='w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=["Field Name", "Type"])
                writer.writeheader()
                writer.writerows(fields_info)
            print(f"Field names and types successfully written to '{output_csv}'.")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")
    else:
        print("Failed to process the shapefile.")