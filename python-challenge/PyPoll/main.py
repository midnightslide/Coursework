#election data homework
import pandas as pd
import csv

voter_data = "C:\\Users\\TITAN\\Desktop\\PythonStuff\\USCLOS201811DATA3\\03_python\\homework\\Instructions\\PyPoll\\Resources\\election_data.csv"
voter_df = pd.read_csv(voter_data, encoding="UTF-8")

# find the candidates and see the total votes for each one
cantot = voter_df['Candidate'].value_counts().to_frame()
cantot.columns = ['Votes']

# total number of votes
total = voter_df['Candidate'].value_counts().sum()

# find the winner
winner = (cantot.Votes.idxmax())

# tally up the vote counts and assign them for reference later
khanvotes = cantot.iloc[0]['Votes']
correyvotes = cantot.iloc[1]['Votes']
livotes = cantot.iloc[2]['Votes']
tooleyvotes = cantot.iloc[3]['Votes']

# find the overall percentage of votes and assign them for reference later
khanpct = (khanvotes / total) * 100
correypct = (correyvotes / total) * 100
lipct = (livotes / total) * 100
tooleypct = (tooleyvotes / total) * 100

# print results in bash
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total}')
print('-------------------------')
print(f'{cantot.index[0]}: {round(khanpct)}% ({khanvotes})')
print(f'{cantot.index[1]}: {round(correypct)}% ({correyvotes})')
print(f'{cantot.index[2]}: {round(lipct)}% ({livotes})')
print(f'{cantot.index[3]}: {round(tooleypct)}% ({tooleyvotes})')
print('-------------------------')
print(f' Winner: {winner} ')
print('-------------------------')

# Output all of the information that was printed into the terminal and save into txt file

output_file = "C:\\Users\\TITAN\\Desktop\\PythonStuff\\Voter_Summary.txt"

with open(output_file,"w") as file:
  
    file.write(f'Election Results')
    file.write("\n")
    file.write(f'-------------------------')
    file.write("\n")
    file.write(f'Total Votes: {total}')
    file.write("\n")
    file.write('-------------------------')
    file.write("\n")
    file.write(f'{cantot.index[0]}: {round(khanpct)}% ({khanvotes})')
    file.write("\n")
    file.write(f'{cantot.index[1]}: {round(correypct)}% ({correyvotes})')
    file.write("\n")
    file.write(f'{cantot.index[2]}: {round(lipct)}% ({livotes})')
    file.write("\n")
    file.write(f'{cantot.index[3]}: {round(tooleypct)}% ({tooleyvotes})')
    file.write("\n")
    file.write(f'-------------------------')
    file.write("\n")
    file.write(f' Winner: {winner}')
    file.write("\n")
    file.write(f'-------------------------')
    file.write("\n")