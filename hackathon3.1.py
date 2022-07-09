def fatcarlories(f):
    #returns amount of calories consumed from fats
    cf = f*9
    print(str(cf) + ' carlories consumed')

def carbocalories(c):
    #returns amount of calories consumed from carbohydrates
    ch = c*4
    print(str(ch) + ' calories consumed')
def fatCarbo(f, c):
    both = f*9 + c*4
    print(str(both) + ' calories consumed')

def main():
    
    running = True
    while running:
        command = input('(C)arbohydrates  (F)ats  (B)oth  (Q)uit: ')
        if command == 'C' or command == 'c':
            n = float(input('Please enter carbohydrates quantity in grams: '))
            print(carbocalories(c))
            
        elif command == 'F' or command == 'f':
            m = float(input('Please enter fats quantity in grams: '))
            print(fatcarlories(m))
            
        elif command == 'B' or command == 'b':
            n = float(input('Please enter carbohydrates quantity in grams: '))
            m = float(input('Please enter fats quantity in grams: '))
            print(fatCarbo(m, n))
            
        elif command == 'Q' or command == 'q':
            running = False
        else:
            print(command, 'is not a valid command')
        

main()