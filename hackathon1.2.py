wa = int(input('Please enter the wall area in square feet: '))
pg = float(input('Please enter price per gallon: '))

print('The number of gallons of paint required = ', end=' ')
gn = wa//115
print(gn)

print('The hours of Labor required = ', end=' ')
lh = wa*8//115
print(lh)

print('The cost of the paint = ', end=' ')
pc = wa*pg//115
print(pc)

print('The labour charges = ', end= ' ')
lc = wa*32//23
print(lc)

print('The paint job will cost: ', end=' ')
tc = pc + lc
print(tc)