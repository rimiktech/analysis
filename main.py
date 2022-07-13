from calendar import week
from datetime import date,timedelta
import pandas as pd
import pdb

def __daygenerator(fromdate, todate, inclusive = True):
    days  = (todate - fromdate).days + 1
    result = [fromdate + timedelta(x) for x in range(days)]
    result = [ { "date": date, "working": date.weekday() > 4 } for date in result ]
    return result

'''
Please create a function who will count working days between given two dates including both dates.
It will consider holidays mentioned in a csv file also.
d1 = date(2022,6,4)
d2 = date(2022,6,30)
res = count_working_days(d1, d2)
'''
def count_working_days(fromdate, todate):
    holiday_dataset = pd.read_excel("data/HOLIDAY CAL-2022.xlsx")
    pdb.set_trace()
    return None

'''
Please create a function who will count days of all weekends between given two dates including both dates.
d1 = date(2022,6,4)
d2 = date(2022,6,30)
res = count_weekend_days(d1, d2)
'''
def count_weekend_days(fromdate, todate):
    daygenerator = __daygenerator(fromdate=fromdate, todate=todate)
    weekends = list(filter(lambda date: date["working"], daygenerator))
    return len(weekends)


import re
import pandas as pd

def check_for_special_chars(series):
    punc_series = series.astype(str).str.match('.*[@_!#$%^&*()<>?/|}{~:]+')
    result = punc_series.any()
    return result
    

series = pd.Series(['@', '54.2$'])
print(check_for_special_chars(series))