import csv
import pandas as pd
from ama_functions import *

if __name__ == "__main__":

    with open('alumni_anonymized.csv') as records:
        reader = csv.reader(records)
        entries = [] #this will store the rows in dictionary form
        next(reader)  #skip header
        count = 0
        for row in reader:
            new_row = dict()
            new_row['Id'] = int(row[3])
            new_row['Exit_Year'] = clean_exit_year(row[1])
            new_row['Last_Name'] = row[0]
            new_row['Birth_Year'] = clean_dob(row[4])
            # Age at exit year
            if new_row['Birth_Year'] and new_row['Exit_Year']:
                exit_age = new_row['Exit_Year'] - new_row['Birth_Year']
                new_row['Age_at_Exit'] = exit_age
                # Filter 7 to 24 exit age
                if 7 <= exit_age <= 24:
                    entries.append(new_row)

    with open('alumni_clean.csv', 'w', newline='') as new_file:
        csv_writer = csv.DictWriter(new_file,fieldnames=['Id','Last_Name','Exit_Year','Birth_Year','Age_at_Exit'])
        csv_writer.writeheader()
        csv_writer.writerows(entries)