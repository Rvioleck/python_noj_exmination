import re

def validate_date(date):
    regex = "^\d{4}[-/.]\d{1,2}[-/.]\d{1,2}$"
    if re.findall(regex, date):
        return True
    return False

date = input()
while date != '':
    print(validate_date(date))
    date = input()