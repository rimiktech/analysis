# Write a function to created a alarm in form of msg ?
def alarm_clock(hr, min, sec):
  while True:
      alarm_time = (f"{hr}: {min}: {sec}")
      current_time = datetime.datetime.now().strftime("%H:%M:%S")
      if current_time == alarm_time:
          time.sleep(1)
print("Time to wake up, buddy!")


