import re


def validate_pan_num(pan_num):
    pattern = r"^[A-Z]{5}\d{4}[A-Z]$"
    if not re.match(pattern, pan_num.upper()):
        return False
    return True


def validate_indian_phone_number(phone_number):
    pattern_intl = r"^\+91[1-9]\d{9}$"
    pattern_national = r"^0[1-9]\d{9}$"
    if re.match(pattern_intl, phone_number) or re.match(pattern_national, phone_number):
        return True
    return False
