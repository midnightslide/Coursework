import os
import csv

# Path to collect data from the Resources folder
from pathlib import Path 
wwedata = Path('C:/Users/TITAN/Desktop/PythonStuff/LearnPython/Wednesday12052018/WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def get_percentages(wrestler_data):

    # Find the total number of matches wrestled
    matches_total = int(wrestler_data[1]) + int(wrestler_data[2]) + int(wrestler_data[3])
    # Find the percentage of matches won
    matches_won = (int(wrestler_data[1]) / matches_total) * 100
    # Find the percentage of matches lost
    matches_lost = (int(wrestler_data[2]) / matches_total) * 100
    # Find the percentage of matches drawn
    matches_draw = (int(wrestler_data[3]) / matches_total) * 100
    
    if(matches_lost > 50):
        wrestler_type = "Jobber"
    else:
        wrestler_type = "Superstar"
    
    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {wrestler_data[0]}")
    print(f"WIN PERCENT: {matches_won}")
    print(f"Stats for {matches_lost}")
    print(f"Stats for {matches_draw}")
    
# Read in the CSV file
with open(wwedata, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'get_percentages()' function
        if(name_to_check == row[0]):
            get_percentages(row)
