def validate_date(date):
    list = []
    if '-' in date:
        list = date.split('-')
    elif '.' in date:
        list = date.split('.')
    elif '/' in date:
        list = date.split('/')
    if len(list) != 3:
        return False
    month = int(list[1])
    day = int(list[2])
    if month <= 0 or month >= 13 or day <= 0 or day >= 32:
        return False
    return True

date = input()
while date != '':
    print(validate_date(date))
    date = input()