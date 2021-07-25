import calendar
import datetime

class MeetupDayException(Exception):
  pass

def meetup(year, month1, week, day_of_week):

  teenth = [x for x in range(13,20)]
  weekdays = {
    "Monday": calendar.MONDAY,
    "Tuesday": calendar.TUESDAY,
    "Wednesday": calendar.WEDNESDAY,
    "Thursday": calendar.THURSDAY,
    "Friday": calendar.FRIDAY,
    "Saturday": calendar.SATURDAY,
    "Sunday": calendar.SUNDAY,
  }

  day = weekdays[day_of_week]
  month = calendar.monthcalendar(year, month1)
  dates = [month[a][day] for a in range(len(month)) if month[a][day] != 0]

  if week == "teenth":
    return datetime.date(year,month1,int(''.join(map(str,[a for a in dates for b in teenth if a == b]))))

  if week == "last":
    return datetime.date(year,month1,dates[-1])

  try:
    return datetime.date(year,month1,dates[int(''.join(map(str,[a for a in range(1,6) if str(a) in week])))-1])
  except IndexError:
    raise MeetupDayException("more than 4 days")
