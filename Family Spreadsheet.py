from python_gedcom_2.element.individual import IndividualElement
from python_gedcom_2.parser import Parser
import pandas as pd
from tkinter import filedialog
import os
from datetime import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta
import re

df = pd.DataFrame()

# Path to your `.ged` file
file_path = r'C:\Users\nuajd15\Desktop\Personal\ancestry\gedcom\Davis20230929.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

root_child_elements = gedcom_parser.get_root_child_elements()

def test():
# Iterate through all root child elements
    for element in root_child_elements:

        # Is the `element` an actual `IndividualElement`? (Allows usage of extra functions such as `surname_match` and `get_name`.)
        if isinstance(element, IndividualElement):

            id = element.get_pointer()[2:-1]
            (first, last) = element.get_name()
            cod = ''
            for i in element.get_child_elements():
                if i.get_tag() == '_DCAUSE':
                    for j in i.get_child_elements():
                        if j.get_tag() == 'NOTE':
                            cod = '\t' + j.get_value()

            if cod != '':
                print('{}: {} {}'.format(id, first, last))
                print(cod)

def date_difference(date_str_1, date_str_2):

    def extract_four_digit_year(input_string):
        # in case the date parser doesn't find a date ("abt YYYY")

        # Define the regular expression pattern for a four-digit year
        year_pattern = r'\b\d{4}\b'

        # Use re.findall to find all occurrences of the pattern in the string
        try:
            match = re.findall(year_pattern, input_string)[0]
            year = datetime(int(match), 1, 1)

            return year
        except:
            return None

    def parse_date(date_str):
        try:
            # Parse the date string using dateutil.parser
            parsed_date = parser.parse(date_str)
            return parsed_date
        except ValueError:
            # Error on any blanks or "abt YYYY"
            yr = extract_four_digit_year(date_str)
            return yr
        
    def timedelta_to_years(delta):
        # Use relativedelta to convert timedelta to years
        rd = relativedelta(seconds=delta.total_seconds())

        # Calculate the total number of years
        years = rd.years + rd.months / 12.0 + rd.days / 365.25

        # Round down to the nearest integer
        return int(years)

    date_1 = parse_date(date_str_1)
    date_2 = parse_date(date_str_2)

    if date_1 is not None and date_2 is not None:
        date_diff = abs(date_1 - date_2)
        return timedelta_to_years(date_diff)
    else:
        return None

def create_dict():
    global df
    fam = {}
    for element in root_child_elements:
        temp_dict = {}
        if isinstance(element, IndividualElement):
            note = '' # Any findings from the Python processing

            (first, last) = element.get_name()
            if last is None:
                if len(first.split(' ')) > 1:
                    note = 'Check if last name is written into first name.'

            gender = element.get_gender()

            birth = element.get_birth_data()[0]
            death = element.get_death_data()[0]

            cod = None
            for i in element.get_child_elements():
                if i.get_tag() == '_DCAUSE':
                    for j in i.get_child_elements():
                        if j.get_tag() == 'NOTE':
                            cod = j.get_value()
            
            temp_dict['First'] = first
            temp_dict['Last'] = last
            temp_dict['Gender'] = gender
            temp_dict['Birth'] = birth
            temp_dict['Death'] = death
            temp_dict['Occupation'] = element.get_occupation()
            temp_dict['COD'] = cod
            temp_dict['Age'] = date_difference(birth, death)
            temp_dict['Note'] = note

            # temp_dict['Fun_Fact'] = None
            # temp_dict['Blood_Rel'] = None
            # temp_dict['Relation'] = None

        idn = element.get_pointer()[2:-1]
        if temp_dict == {}:
            continue
        else:
            fam[idn] = temp_dict

    print('{} individuals'.format(len(fam)))

    df = pd.DataFrame.from_dict(fam, orient='index')

def export_results():
    global df
    fn = filedialog.asksaveasfilename(defaultextension=".xlsx")
    df.to_excel(fn, index=False)
    os.system('start EXCEL.EXE "{}""'.format(fn))
        
# for element in root_child_elements:
#     # Is the `element` an actual `IndividualElement`? (Allows usage of extra functions such as `surname_match` and `get_name`.)
#     if isinstance(element, IndividualElement) and len(element.get_census_data())>0:
#         print(element.get_census_data())

# test()

create_dict()
export_results()