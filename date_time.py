from datetime import datetime, date, time, timedelta


# d = date(2012, 10, 25)
# print(d, type(d))
# t = time(12, 15, )
# print(t, type(t))
# # dt = d + t
# dt = datetime.combine(d, t)
# print(dt, type(dt))
# print(datetime.now().replace(microsecond=0))
# dtt = datetime.now()
# dtt = dtt.replace(hour=12, minute=12, second=30, year=2025, month=1, day=1)
# print(dtt)
# # dat = input('введите дату (дд.мм.гггг):')
# # date_ = datetime.strptime(dat, '%d.%m.%Y')
# # print(date_)
# dt = datetime.now()
# # d = dt.timetuple()
# # for i in d:
# #     print(i)
# print(dt.weekday())
# print(dt.isoweekday())
# cc = dt.isocalendar()
# print(cc)
# print(dt.strftime('%A %d %Y %B  %H:%M:%S'))
# print(dt.strftime('%A %d %Y %B  %X'))
# days = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
# print(days[dt.weekday()])
# dat = input('введите дату (дд.мм.гггг):')
# date_ = datetime.strptime(dat, '%d.%m.%Y')
# td = date_ - dt
# print(td)
# print(td.days)
birthday = input("Дата рождения (дд.мм.гггг): ")
birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
date_today = date.today()

year_=date_today.year
birth_day = birthday
birthday = birthday.replace(year=year_)
age_days = (date_today - birth_day).days
if birthday < date_today:
    birthday = birthday.replace(year=year_ + 1)
    age_days = ((date_today + timedelta(days=365)) - birth_day).days
elif birthday == date_today:
    print('Поздравляем с Днем рождения!')
    exit(0)

days_ =  (birthday-date_today).days
age = age_days / 365
print(f'Кол-во дней до дня рождения - "{days_}", Вам исполнится {age:.0f} лет')
print('Кол-во дней до дня рождения - \'{}\', Вам исполнится {} лет'.format(days_, age))
print('Кол-во дней до дня рождения - %d, Вам исполнится %d лет'% (days_, age))

