"""Plp Hackathon Question 1 part 1"""

from datetime import *

date = datetime.now().date()
wn = date.strftime('%w')

print('Date:', date)

if wn == 0:
    print('Day: Sun')
elif wn == 1:
    print('Day: Mon')
elif wn == 2:
    print('Day: Tue')
elif wn == 3:
    print('Day: Wed')
elif wn == 4:
    print('Day: Thr')
elif wn == 5:
    print('Day: Fri')
else :
    print('Day: Sat')
    
w = int(wn)

if w >= 1 and w <= 5:
    print('Fare: 100')
elif w == 6:
    print('Fare: 60')
else:
    print('Fare: 80')
