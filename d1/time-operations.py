'''
Create a function which will be accept the duration in string format, parse the duration and will return the timedelta object.
Input can be hours only, hours:minutes or hours in decimal.

for example:
    Input: "15"
    Output: timedelta(hours=15, minutes=0)

    Input: "15.5"
    Output: timedelta(hours=15, minutes=30)

    Input: "15:50"
    Output: timedelta(hours=15, minutes=50)

    Input: ".5"
    Output: timedelta(hours=0, minutes=30)


We have a function which accepts the duration in string format, parse the duration and will return the timedelta object.
here input for this funcion can be hours only, hours:minutes or hours in decimal.

Now, please add a new function which will convert duration timedelta value to decimal value. 
Please note that only consider the days, hours, minutes and ignore the seconds and milliseconds.

'''

from datetime import datetime, timedelta

def parse_duration(duration):
    hours = None
    minutes = None

    if duration.isdigit():
        hours = int(duration)
    elif ":" in duration:
        duration_split = duration.split(":")
        hours = int(duration_split[0])
        minutes = int(duration_split[1])
    elif "." in duration:
        if duration.index(".") == 0:
            duration = "0" + duration
        duration_split = duration.split(".")
        hours = int(duration_split[0])
        minutes = int(60 * float("." + duration_split[1]))

    if minutes is None:
        minutes = 0

    if hours and minutes:
        return timedelta(hours=hours, minutes=minutes)
    else:
        return None



def to_decimal(duration):
    hours = duration.total_seconds() // 3600
    seconds = duration.total_seconds() % 3600
    minutes = int(((seconds // 60) / 60) * 100)
    return hours + minutes * .01
    

to_decimal(timedelta(hours=50, minutes=25))