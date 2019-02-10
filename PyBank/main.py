import os
import csv
Profit=[]

# Path to collect data from the Resources folder
budgetCSV = os.path.join('budget_data.csv')

# Read in the CSV file
with open(budgetCSV, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Create variable months
    # Count number of rows and store as months
    Months = 0
    for row in csvreader:
        Months += 1
    
        #Create Variable Total
        # Sum all values in column 2
        
        Profit.append(float(row[1]))
    
        # Create list of yearly change - value in column 2 from next row less present row
    change=[]
    for i in range(1, len(Profit)):
        change.append((float(Profit[i]-float(Profit[i-1]))))

     # Calculate average, greatest increase and decrease
    averagechange = sum(change) / float(Months-1)
    greatestIncrease = max(change) 
    greatestdecrease = min(change)

    # Print Summary
    print("Financial Analysis") 
    print("--------------------")   
    print("Total Months:" + str(Months))
    print("Total:" + str(sum(Profit)))
    print("Average Change:" + str(averagechange))
    print("Greatest Increase in Profits:" + str(greatestIncrease))
    print("Greatest Decrease in Profits:" + str(greatestdecrease))

# Set variable for output file
output_file = os.path.join("FinancialAnalysis.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile) 

# Print to the CSV output
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------"])
    writer.writerow(["Total Months:" + str(Months)])
    writer.writerow(["Total:" + str(sum(Profit))])
    writer.writerow(["Average Change:" + str(averagechange)])
    writer.writerow(["Greatest Increase in Profits:" + str(greatestIncrease)])
    writer.writerow(["Greatest Decrease in Profits:" + str(greatestdecrease)])
    