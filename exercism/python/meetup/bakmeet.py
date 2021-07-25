import calendar

def meetup(year, month, week, day_of_week):
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
  month = calendar.monthcalendar(year, month)
  dates = [month[a][day] for a in range(len(month))]
  
  if dates[-1] == 0:
    dates.pop()

  teenth_date = 0
  if week == "teenth":
    for a in dates:
      for b in teenth:
        if a == b:
          teenth_date = a
          return year,month,teenth_date

  if week == "1st":
    return year,month,dates[0]