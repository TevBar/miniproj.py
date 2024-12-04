# validators.py

import datetime
import re

def validate_library_id(library_id):
    pattern = r'^[A-Za-z0-9]{4,10}$'
    return re.match(pattern, library_id) is not None

def validate_date(date_text):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date_text):
        try:
            year, month, day = map(int, date_text.split('-'))
            datetime.date(year, month, day)
            return True
        except ValueError:
            return False
    return False

def validate_non_empty(text):
    return bool(text and text.strip())

def validate_choice(choice, options):
    return choice in options
