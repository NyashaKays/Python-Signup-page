from random import randint
username = 0
password = 0
login_username = "NKats"
login_password = "Caroline18112020"
password_attempts = 3

print('''
Welcome!
AFM IN ZIMBABWE
''')
selection = input("Login or Signup: ").lower()

if selection == 'login':
    while password_attempts > 0:
        username = input('Enter your username: ')
        if username == login_username:
            while password_attempts > 0:
                password_attempts -= 1
                password = input("Enter your password: ")
                if login_password == password:
                    print("welcome! Nyashadzashe Katsidzira")
                    break
                else:
                    if password_attempts > 0:
                        print(f"incorrect password! {password_attempts} attempts left!")
                    else:
                        print(f'''
{password_attempts} attempts left. Account blocked!
Email support@afminzim.org
                        ''')
        else:
            print("Username is Incorrect!")
elif selection == 'signup':
    name = input("Enter your fullname: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    assembly = input("Enter your assembly name: ")
    city = input("Enter your city: ")
    username = input("Create username: ")
    password = input("Enter your password: ")
    confirmation = input("Confirm your password: ")

    if password == confirmation:
        otp = randint(1000, 9999)
        print(f'''
Welcome!
Account successfully created
go to {email} to verify your account
Your verification code is {otp}
        ''')
    else:
        while password != confirmation:
            print("passwords don't match!")
            password = input("Enter your password: ")
            confirmation = input("Confirm your password: ")

            if password == confirmation:
                otp = randint(1000, 9999)
                print(f'''
Welcome!
Account successfully created
go to {email} to verify your account
Your verification code is {otp}
        ''')