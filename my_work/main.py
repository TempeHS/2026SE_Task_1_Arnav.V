
#make login function
#make logged in screen
#make change password function
passwords = []
usernames = []

def main():
    print("1. Register")
    print("2. Login")
    print("3. Quit")

    option = int(input("Enter choice: "))

    if option == 1:
        register()
    elif option == 2:
        login()
    elif option == 3:
        quit()
    else:
        print("Invalid option")

        main()

def register():
    input("What's your name? ").appendinput(usernames)
    input("What's your password? ").appendinput(passwords)

    print("Registered!")
    main()
    return

def login():
    name_login = input("Enter username: ")
    password_login = input("Enter password: ")
    for i in usernames(i)
        lines = file.readlines(username, password)
        

#incomplete do this later

def logged_in():
    print("1. Logout")
    print("2. Change password")
    choice = int(input("Enter choice: "))
    if choice == 1:
        quit()
    elif choice == 2:
        change_password()

def quit():
    exit()

main()