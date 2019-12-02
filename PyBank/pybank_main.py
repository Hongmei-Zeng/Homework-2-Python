import csv
from datetime import datetime

# extract data of "Date" and "Profit/Loss"(PL), group into two lists for later analysis uses
with open(r"C:\Users\Mei\Desktop\UT Data Analysis Bootcamp\Homework-2-Python\Original Tasks\Instructions\PyBank\Resources\budget_data.csv", "r") as file:
    csv_file = csv.reader(file)
    file_date = []
    file_PL = []
    for row in csv_file:
        file_date.append(row[0])
        file_PL.append(row[1])
    file_date.pop(0)  # remove the header'Date' which became 1st element in file_date
    file_PL.pop(0)    # remove the header'Profit/Losses'

# 1st analysis on the total number of months in the dataset:
    new_dt = []
    for idx in range(len(file_date)):
        date_str = file_date[idx]
        date_object = datetime.strptime(date_str, "%b-%Y") # convert str elements into date format
        new_dt.append(date_object)

    new_dt.sort()                       # find the earliest&latest dates to get the difference
    begin_dt = new_dt[0]
    end_dt = new_dt[len(new_dt) - 1]
    days_diff = end_dt - begin_dt
    num_mths = int(days_diff.days / 30) # calculate into months
    print("Total Months:", num_mths)

# 2nd analysis on the net total amount of "Profit/Losses" over the entire period:
    new_PL = []
    for idx in range(len(file_PL)):
        PL_str = file_PL[idx]
        PL_amount = int(PL_str)
        new_PL.append(PL_amount)
    total_PL = sum(new_PL)
    print(f'Total Amount of Profit/Losses is: ${total_PL:,.0f}'.replace('$-', '-$')) # print "Profit/Losses" in currency

# 3rd analysis on the average of the chages in "Profit/Loss" over the entire period: 
    change_list = []
    for idx in range(len(file_PL) - 1): # (the total of elements - 1) substraction operations 
        change_mthly = new_PL[idx + 1] - new_PL[idx]
        change_list.append(change_mthly)
    total_change = sum(change_list)
    change_avg = total_change / len(change_list)  
    print(f'Average Change is: ${change_avg:,.2f}'.replace('$-', '-$'))
    
# 4th analysis on the greatest increase in Profits over the entire period:
    greatest_incrs_P = max(change_list)
    idx_incrs_change = change_list.index(greatest_incrs_P) # determine the index of "greatest_incrs_P" in its list
    idx_incrs_file_PL = idx_incrs_change + 1               # deduce backwards, greatest_incrs_P = file_PL[idx_in_change + 1] - file_PL[idx_in_change]
    date_in_file = file_date[idx_incrs_file_PL]            # the index of a date has the same index of its matching Profits/Losses in file/file_date/file_PL
    print(f'Greatest Increase in Profits is: ${greatest_incrs_P:,.0f}'.replace('$-', '-$'), 'Achieved in', date_in_file)

# 5th analysis on the greatest decrease in Losses over the entire period:
    greatest_decrs_L = min(change_list)
    idx_decrs_change = change_list.index(greatest_decrs_L) # same logic as 4th task
    idx_decrs_file_PL = idx_decrs_change + 1               
    date_in_file = file_date[idx_decrs_file_PL]              
    print(f'Greatest Decrease in Losses is: ${greatest_decrs_L:,.0f}'.replace('$-', '-$'), 'Happened in', date_in_file)

file.close()