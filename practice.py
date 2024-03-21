"""def date_formatter(time):
  start_time = time.split(':', maxsplit = 1)
  start_hour = start_time[0]
  start_minute, start_ap = start_time[1].split()

  if start_ap == 'PM':
    start_hour = start_hour + 12

  return start_hour, start_minute"""

days_of_week = {
  1:'Sunday',
  2:'Monday',
  3:'Tuesday',
  4:'Wednesday',
  5:'Thursday',
  6:'Friday',
  7:'Saturday'
} 

def add_time(start, duration, start_dow = ""):
  start_day = 0
  start_time = start.split(':', maxsplit = 1)
  start_hour = start_time[0]
  start_minute, start_ap = start_time[1].split()

  if start_ap == 'PM':
    start_hour = int(start_hour) + 12



  dur_day = 0
  dur_hour, dur_minute = duration.split(':')



  end_dow = ""
  end_hour = (int(start_hour) + int(dur_hour))
  end_day = (int(start_day) + int(dur_day))
  end_minute = (int(start_minute) + int(dur_minute))
  end_ap = ""
  time_string = ""
  end_words = ""

  if end_minute >= 60:
    end_hour += end_minute // 60
    end_minute = end_minute % 60


  if end_hour >= 24:
    end_day += end_hour // 24
    end_hour = end_hour % 24


  if start_dow != "":
    days = days_of_week.values()
    start_dow_index = list(days).index(start_dow.title()) + 1
    end_dow_index = int(start_dow_index) + int(end_day)
    print(f'Start: {start_dow_index} - {start_dow} End: {end_dow_index}')
    if end_dow_index > 6:
      end_dow_index = (int(end_dow_index) % 7)
    end_dow = days_of_week[end_dow_index]
    print(f'end_index: {end_dow_index}, end DOW: {end_dow}')

  if start_dow == "":
    end_dow = ""

  if end_day == 1:
    time_string = '(next day)'

  if end_day > 1:
    time_string = f'({end_day} days later)'

  if end_dow and time_string == "":
    end_words = ""

  if end_dow != "":
    end_words = ', ' + end_dow + ' ' + time_string if time_string != '' else ', ' + end_dow

  if time_string != "":
    end_words = ', ' + end_dow + ' ' + time_string if end_dow != '' else ' ' + time_string



  end_ap = 'PM' if end_hour >= 12 else 'AM'
  end_hour = end_hour if end_hour <= 12 else int(end_hour) - 12
  end_hour = 12 if end_hour == 0 else end_hour
  #return(f"{end_hour}:{end_minute:02} {end_ap}{end_words}")
  
  print(f'Start Day: {start_day}, Hour: {start_hour}, Min: {start_minute}')
  print(f'Duration Day: {dur_day}, Hour: {dur_hour}, Min: {dur_minute}')
  print(f'End Day: {end_day}, DOW: {end_dow}, Hour: {end_hour}, Min: {end_minute}, AP: {end_ap}')


  #return hour, minute, ap
    #return new_time

#print(add_time("9:15 PM", "5:30"))

#print(add_time("2:59 AM", "24:00"))

#test high duration
#print(add_time("8:16 PM", "466:02"))

#test no change
#print(add_time("5:01 AM", "0:00"))

#test 24 w day
#print(add_time("2:59 AM", "24:00", "saturDay"))

# test high duration w day - return Monday
#print(add_time("8:16 PM", "466:02", "tuesday"))

# test 2 days later w day - return Friday
#print(add_time("11:59 PM", "24:05", "Wednesday"))

# test same period w day
print(add_time("3:30 PM", "2:12", "Monday"))