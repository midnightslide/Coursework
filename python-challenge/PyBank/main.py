
#budget homework
import csv
import pandas as pd

budget_data = "C:\\Users\\TITAN\\Desktop\\PythonStuff\\USCLOS201811DATA3\\03_python\\homework\\Instructions\\PyBank\\Resources\\budget_data.csv"
budget_im = pd.read_csv(budget_data, encoding="UTF-8")

# The total number of months included in the dataset
month_count = len(budget_im)

# The total net amount of "Profit/Losses" over the entire period
count = budget_im["Profit/Losses"].sum()

# The average change in "Profit/Losses" between months over the entire period
budget_im["shifted_column"] = budget_im["Profit/Losses"].shift(1)
budget_im["difference"] = budget_im["Profit/Losses"] - budget_im["shifted_column"]
avg_change = budget_im["difference"].mean()

# The greatest increase in profits (date and amount) over the entire period
budget_maxdate = budget_im["Date"][budget_im["Profit/Losses"].idxmax()]
budget_max = budget_im["Profit/Losses"].max()

# The greatest decrease in losses (date and amount) over the entire period
budget_mindate = budget_im["Date"][budget_im["Profit/Losses"].idxmin()]
budget_min = budget_im["Profit/Losses"].min()

# print all of the financial info into the terminal
print(f'Financial Analysis')
print(f'----------------------------')
print(f' Total Months: {month_count}')
print(f' Total: ${count}')
print(f' Average Change: ${round(avg_change)}')
print(f' Greatest Increase in Profits: {budget_maxdate}, (${budget_max})')
print(f' Greatest Decrease in Profits: {budget_mindate}, (${budget_min})')

# Output all of the information that was printed into the terminal and save into txt file

output_file = "C:\\Users\\TITAN\\Desktop\\PythonStuff\\Budget_Summary.txt"

with open(output_file,"w") as file:
  
    file.write(f'Financial Analysis')
    file.write("\n")
    file.write(f'----------------------------')
    file.write("\n")
    file.write(f' Total Months: {month_count}')
    file.write("\n")
    file.write(f' Total: ${count}')
    file.write("\n")
    file.write(f' Average Change: ${round(avg_change)}')
    file.write("\n")
    file.write(f' Greatest Increase in Profits: {budget_maxdate}, (${budget_max})')
    file.write("\n")
    file.write(f' Greatest Decrease in Profits: {budget_mindate}, (${budget_min})')