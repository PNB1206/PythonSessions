from random import shuffle
import time
from datetime import date




today = date.today()
print(today)

print('This year ',date.today().year)
print('This month ', date.today().month)
print('Today date is ',date.today().day)


print(date.isoformat(today))
print(date.ctime(today))


my_list = ['Java', 'Python', 'Java Script', 'PHP']

localtime = time.asctime(time.localtime(time.time()))
print(localtime)


shuffle(my_list)
print(my_list)




