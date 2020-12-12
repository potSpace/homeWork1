from datetime import datetime, timedelta

dt_now = datetime.now()
print(dt_now)

delta = timedelta(days=1)
delta2 = timedelta(days=30)
yesterday = dt_now - delta
print(yesterday)

tomorrow = dt_now + delta
print(tomorrow)

dt_30 = dt_now - delta2
print(dt_30)