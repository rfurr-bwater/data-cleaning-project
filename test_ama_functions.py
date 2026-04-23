from ama_functions import *

def test_clean_exit_year_four_digit_year():
	assert clean_exit_year("2001") == 2001

def test_clean_exit_year_two_digit_year():
	assert clean_exit_year("Class of 53") == 1953

def test_clean_exit_year_no_year():
	assert clean_exit_year("No listed year.") is None

def test_clean_dob_dod():
	result = clean_dob("Died: 04/05/1953")
	assert len(result) == 2

def test_clean_dob_dod_default():
	assert clean_dob("Died: 04/05/1953") == (None, None)
