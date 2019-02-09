import os
import csv
import collections as ct


# Path to collect data from the Resources folder
Electdata = os.path.join('election_data.csv')

# Read in the CSV file
with open(Electdata, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    votescand = ct.Counter()
    header = next(csvreader)

    Votes = 0
    candidates = []
    
    for row in csvreader:
      
        # list of candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
    
        # Count number of rows and store as months
        Votes += 1

        #Count votes per candidate
        candidate = row[2]
        votescand[candidate] += 1

    listcand = dict(votescand)

        
    s = sum(listcand.values())
    for k, v in listcand.items():
        pct = ("{0:.1%}".format(v / s))
        print(k, pct)
    

print(Votes)
print(candidates)
print(votescand)
print(votescand.most_common(1))
print(listcand)



 





    





