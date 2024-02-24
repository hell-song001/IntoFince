# Import necessary libraries
import pandas as pd  
import json
import os
from matplotlib import pyplot

from scripts.raw_to_json import get_files

# Define the source and destination file paths
dest_file = os.path.abspath(os.path.join(os.path.dirname("."), "data/processed"))

files = get_files(dest_file, "json")

def plot_data(filename):
    with open(filename, "r") as f:
        jx = json.loads(f.readline())
    jx = jx[0]
    data = pd.DataFrame(jx)

    data.plot()
    pyplot.show()
    input()

if __name__ == "__main__":
    for f in files:
        plot_data(os.path.join(dest_file, f))