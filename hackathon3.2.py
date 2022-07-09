from random import *
import string


value = input('Please enter a new password: ')
symbols = "!@#$%^&*()-{}[]\|?/,.<>`~=+"
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
strong =  poor + average + symbols
if value == poor:
   print('Password too weak, please try again!: ', end='')
   value =input()
elif value == average:
   print('Password strength is average, please try again: ', end='')
   value = input()
elif value == strong:
   print('Password strength is EXECELLENT!')
   entry = value
   seed(entry)
   for i in range(20):
      x= randrange(100,1001)
      print(x)




