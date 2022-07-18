import time

user_access = False
user = ["abc"]
upass = ["123"]
global index
cout = 1

def create_uname_password():

    uname = input("enter the uname ::: ")
    upassword = input("enter the pasword:::")

    user.append(uname)
    upass.append(upassword)

    print('uname and password is stored succesfully\n')

def login_window():

    global cout

    print("login by using uname and password\n")

    uname = input("enter the uname ::: ")
    upassword = input("enter the pasword:::")

    index = user.index(uname)

    if cout == 1 :
        freepass = True
        print("you have already logined \n")

    if uname == user[index]and upassword == upass[index] or freepass:

        print("login succss")
        cout  = cout +1
        collecting_data(uname,upassword)
        instruction = " "
        terminate = True
        while terminate:

            instruction = input("enter instruction:: ")

            if instruction == "open":
                print("door is open")
            elif instruction == "close":
                print("door is closed \n\n")
                terminate = False
            else:
                print("invalid input\n")

        print(cout)
        instruction = input("enter to quit the process or type quit for temination \n")
        if instruction == "quit":
            print("process is terminate")
            login_window()

    else:

        print("authentication failed")
        login_window()


def collecting_data(uname,upassword):

    user = uname
    upass = upassword
    current_time = time.localtime() # get struct_time
    time_string = time.strftime("%y-%m-%d, %H:%M:%S", current_time)
    print(f"Door last open at {time_string}")

    with open("log.txt","a") as f:

        f.write(f"user ::: {user} on {time_string} with pasword ::: {upass} \n")
        f.close()

def main():

    print("""
                        welcome

             choose the option according to need

             a. create login id
             b. for login """)

    a = input()

    if a == 'a':
        create_uname_password()
        login_window()
    elif a == 'b':
        login_window()
    else:
        print("invalid keyword")
        main()


if __name__ == '__main__':
    main()
