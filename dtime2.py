from datetime import datetime, timedelta

text = '01/01/25 12:10:03.234567'

formatter = '%d/%m/%y %H:%M:%S.%f'
x = datetime.strptime(text, formatter)
print(x)
print(type(x))