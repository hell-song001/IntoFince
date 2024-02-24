# Import necessary libraries
import pandas as pd  
import json
import os
import re

# Define the source and destination file paths
source_file = os.path.abspath(os.path.join(os.path.dirname("."), "data/raw"))
dest_file = os.path.abspath(os.path.join(os.path.dirname("."), "data/processed"))

# Function to get files of a specific type from a directory
def get_files(path, filetype):
    files = os.listdir(path)  # List all files in the directory
    files2 = []  # Initialize an empty list to store the files of the desired type
    for item in files:  # Loop through each file
        x = re.search(filetype + "$", item)  # Check if the file is of the desired type
        if x:  # If the file is of the desired type
            files2.append(x.string)  # Add the file to the list
        
    return files2  # Return the list of files


#  Read data file from folder: Return JSON format
def process_file(filename):
        data = pd.read_csv(filename)

        try:
            indicators = data["Indicator Name"].unique()
        except Exception as e:
            print(e)
            indicators = data["Indicator Code"].unique()

        data_list = []

        for ind in indicators:

            try:
                content = data[data["Indicator Name"] == ind]
            except Exception:
                content = data[data["Indicator Code"] == ind]

            cont_dict = {year: value for year, value in zip(content["Year"], content["Value"])}
            data_list.append({ind: cont_dict})
            
        save_at = os.path.join(dest_file, str(os.path.basename(filename)).replace(".csv", ".json"))
        with open(save_at, "+a") as jf:
                json.dump(data_list, jf)


if __name__ == "__main__":
    csv_files = get_files(source_file, "csv")
    for file in csv_files:
        process_file(os.path.join(source_file, file))
     
# Function to get the year and value for a given indicator name

# Loop through each unique indicator

# Open the JSON file in append mode
  # Dump the data list into the JSON file

# The JSON file will have the format ["Indicator Name":{year1:value, year2:value...}]
#This code is used to process a CSV file containing economic and growth data for Tanzania. 
#It extracts the data for each unique indicator and stores it in a JSON file in the format 
#["Indicator Name":{year1:value, year2:value...}].