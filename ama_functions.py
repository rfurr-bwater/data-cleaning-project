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
    result = result[0]
    if len(result) == 2:
        result = "19"+result
    return result

def clean_dob_dod(date_str:str) -> tuple:
    '''Takes in a date string and returns a tuple containing the birth and death years'''

    regex_death = r'Died\S\s*|DOD\S\s*'
    regex_birth = r'DOB\S\s*'
    regex_datestring = r'\d+'

    birth_yr = None
    death_yr = None

    result_death = re.findall(regex_death,date_str)
    if result_death:
        print(re.findall(r'\d+',date_str))
    return (birth_yr,death_yr)

clean_dob_dod("Died: 04/05/1953")