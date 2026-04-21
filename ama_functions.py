'''Functions for data cleaning'''
import re
# re.findall(pattern,string)
# re.search(pattern,string)

def clean_exit_year(year_str:str) -> None|int:
    '''Takes in a year string for exit year, returns an int with the exit year'''
    regex = r'\d+'
    result = re.findall(regex,year_str)
    if not result:
        return None
    year = result[0]
    if len(year) == 2:
        year = "19"+year
    if year[0:2] == "20":
        year = "19"+year[2:4]
    return int(year)

def clean_dob(date_str:str) -> int | None:
    '''Takes in a date string and returns an int with the birth year'''
    regex_dob = r'DOB\S*\s*\d{1,2}\/\d{1,2}\/(\d{2,4})'
    regex_birth = r'Born\S*\s*\d{1,2}\/\d{1,2}\/(\d{2,4})'
    regex_dmy = r'\d{2}\S+(\d{2})'
    regex_my = r'DOB\S*\s*\S*\s*(\d{4})'

    # DOB
    result = re.findall(regex_dob,date_str)
    if result:
        year = result[0]
        if len(year) == 2:
            year = "19"+year
        if year[0:2] == "20":
            year = "19"+year[2:4]
        return int(year)
    
    # Born
    result = re.findall(regex_birth,date_str)
    if result:
        year = result[0]
        if len(year) == 2:
            year = "19"+year[0]
        if year[0:2] == "20":
            year = "19"+year[2:4]
        return int(year)
    
    # For cases like 28-Aug-30
    result = re.findall(regex_dmy,date_str)
    if result:
        year = result[0]
        if len(year) == 2:
            year = '19'+year
        return int(year)
    
    # DOB: May 1947
    result = re.findall(regex_my,date_str)
    if result:
        return int(result[0])

    return None

if __name__ == "__main__":
    # Test script
    a = "Born: 04/18/1873"
    b = "DOB:  08/03/25"
    c = "28-Aug-30"
    d = "DOB: October 1966"
    ls = [a,b,c,d]
    for l in ls:
        print(clean_dob(l))