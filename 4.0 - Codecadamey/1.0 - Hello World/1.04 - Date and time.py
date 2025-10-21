from datetime import datetime
#This is awsome: you get 6dp on the seconds
now = datetime.now()
print (now)

current_year = now.year
current_month = now.month
current_day = now.day

print(now.year)
print(now.month)
print(now.day)

print ("%02d/%02d/%04d" % (now.month, now.day, now.year))

print (now.hour)
print (now.minute)
print (now.second)
print ('%02d:%02d:%04d' % (now.hour, now.minute, now.second))

print ("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))

