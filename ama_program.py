import csv
import pandas as pd
from ama_functions import *

#TODO: add to this program
    # clean the data using your functions 
        # Birth and death dates
    # write the cleaned data into a new csv file (optional but helpful for next step)
    # put the cleaned data into a dataframe
    #    - use your cereal_analysis python file as a template to read from csv

if __name__ == "__main__":

    with open('alumni_anonymized.csv') as records:
        reader = csv.reader(records)
        entries = [] #this will store the rows in dictionary form
        next(reader)  #skip header
        count = 0
        for row in reader:
            new_row = dict()
            new_row['ID'] = row[3]
            new_row['Exit_Year'] = clean_exit_year(row[1])
            new_row['Last_Name'] = row[0]
            entries.append(new_row)

    with open('alumni_clean.csv', 'w', newline='') as new_file:
        csv_writer = csv.DictWriter(new_file,fieldnames=['ID','Last_Name','Exit_Year'])
        csv_writer.writeheader()
        csv_writer.writerows(entries)