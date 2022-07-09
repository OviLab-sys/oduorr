nb = int(input('Please enter the number of books bought for this month: '))
if nb == 0:
    print(str(0) + ' points awarded')
elif nb == 1:
    print(str(6) + ' points awarded')
elif nb == 2:
    print(str(16) + ' points awarded')
elif nb == 3:
    print(str(32) + ' points awarded')
else:
    print(str(60) + ' points awarded')

