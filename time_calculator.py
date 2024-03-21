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
    if end_dow_index > 6:
      end_dow_index = (int(end_dow_index) % 7)
    end_dow = days_of_week[end_dow_index]

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
  return(f"{end_hour}:{end_minute:02} {end_ap}{end_words}")