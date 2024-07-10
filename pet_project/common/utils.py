import re

def validate_phone_number(phone_number):
    pattern = re.compile(r'^\+?[1-9]\d{11}')
    return bool(pattern.match(phone_number))