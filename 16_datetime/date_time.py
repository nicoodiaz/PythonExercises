from datetime import datetime, date, time
now = datetime.now()
print(now) #2023-05-22 18:30:41.550054
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)

date_string = '22 May, 2023'
date_object = datetime.strptime(date_string, '%d %B, %Y')
print(date_object)

today = date(2023, 5, 22)
new_year = date(2024, 1, 1)
time_left_ny = new_year - today
print(time_left_ny)
today = date(2023, 5, 22)
day_ener = date(1970, 1, 1)
diff = today - day_ener
print(diff)