import csv
import sys

# import pandas as pd
import pyproj
import numpy as np

# Lucky clover farm
START_LAT = 45.081679
START_LON = -84.774588


def gps_to_cartesian(csv_file, origin):
    # Extract origin latitude and longitude
    origin_lat, origin_lon = origin

    wgs84 = pyproj.CRS("EPSG:4326")
    utm = pyproj.CRS("EPSG:32616")
    # transformer_utm_to_wgs84 = pyproj.Transformer.from_crs(utm, wgs84, always_xy=True)
    transformer_wgs84_to_utm = pyproj.Transformer.from_crs(wgs84, utm, always_xy=True)

    start_x, start_y = transformer_wgs84_to_utm.transform(origin_lon, origin_lat)


    with open(csv_file, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        print("Header:", type(header))
        data=[]
        data.append(header)
        i = 1
        for row in csvreader:
            lat = float(row[4])
            lon = float(row[5])
            # Convert GPS coordinates to UTM Zone 16N
            x, y = transformer_wgs84_to_utm.transform(lon, lat)
            row[6] = x - start_x
            row[7] = y - start_y
            data.append(row)
            i=i+1
            print("Row:", row)
    
    return data


def main(input_file_name, lat, long):
    csv_file = '../data/' + input_file_name 
    filename,ext = input_file_name.split('.')
    origin = (lat, long)  # Example: Lucky clover farm
    result = gps_to_cartesian(csv_file, origin)
    with open('../data/' +filename+'_output.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(result)

def check_if_float(arg):
    return isinstance(arg, float)

if __name__=="__main__":
    print(len(sys.argv))
    if len(sys.argv) == 4:
        if check_if_float(sys.argv[2]) or check_if_float(sys.argv[3]):
            print("Please provide correct latitude, and longitude.")   
        else:
            main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Please provide an input file name, latitude, and longitude.")   
        

    
        
    
        

    
    # main()


# Example usage
# csv_file = 'your_file.csv'
# origin = (40.7128, -74.0060)  # Example: New York City coordinates
# result = gps_to_cartesian(csv_file, origin)
# print(result.head())
