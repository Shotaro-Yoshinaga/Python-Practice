import datetime

today = datetime.datetime.today()

#今日の日付
print(today)

#明日の日付
print(today + datetime.timedelta(days=1))