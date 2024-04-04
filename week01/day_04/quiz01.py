# datetime

import datetime as dt

today = dt.date.today()
print(f'Todays date is {today.strftime("%B %d, %Y")}')

start_date = dt.date(2022, 5, 10)
end_date = dt.date(2000, 11, 12)

days = start_date - end_date

print(f'Remaining days are: {days}')