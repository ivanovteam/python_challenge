 # First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budgetdata.csv')

# defining the variables, and lists
mcount = 0
nettotal = []
months = []
netchangelist = []
total = 0
average = 0
i = 0
profitchange = 0
totalprofitchange = 0
increase = 0
decrease = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
increaseindex = 0
decreaseindex = 0
#  Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   

    # counts the total amount of rows
    for row in csvreader:
        # counts the total amount of rows
        mcount += 1
        #creates a list with all the totals
        nettotal.append(int(row[1]))
        # creates a list with the months
        months.append(str(row[0]))
        #calculate the total from the list
        total = sum(nettotal)
        
    
    # priints the total months and the total amount 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {mcount}")
    print(f"Total: {total}")
    
    
    
    #  finding the average change and increase and decrease
    for i in range(1, len(nettotal)):

        profitchange = (nettotal[i] - nettotal[i-1])
        # saving the profitchange in a list
        netchangelist.append(profitchange)
        
        #  comparing the increase and saving it in greatest increase with the date and the value
        if profitchange > greatest_increase[1]:
            greatest_increase[0]= months[i]
            greatest_increase[1] = profitchange
            
        # comparing the increase and saving it in greatest decrease with the date and the value
        elif profitchange < greatest_decrease[1]:
            greatest_decrease[0] = months[i]
            greatest_decrease[1]= profitchange
           
    # caluclates the total change   
    totalprofitchange = sum(netchangelist)/len(netchangelist)

    # printing th avergage change and greatest increase and decrease   
    print(f"Average change: {round(totalprofitchange,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${round(greatest_increase[1])})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${round(greatest_decrease[1])})")

# creates an analysis file in the analysis folder
output_file = os.path.join('..', 'analysis','analysis.csv')

#  Open the output file
with open(output_file, "w") as datafile:  
    # writes all the amounts in the file formated the same way as in the printing.
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Months: {mcount}\n")
    datafile.write(f"Total: {total}\n")
    datafile.write(f"Average Change: ${round(totalprofitchange,2)}\n")
    datafile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${round(greatest_increase[1])})\n")
    datafile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${round(greatest_decrease[1])})\n")  



    