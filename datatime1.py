import locale
from datetime import datetime 

locale.setlocale(locale.LC_TIME, 'ru_RU')
dt_now = datetime.now()
print(dt_now.strftime('%A-%d-%B-%Y'))