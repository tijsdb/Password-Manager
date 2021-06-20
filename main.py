import SECRETKEY as S
from prettytable import PrettyTable
import random

x = PrettyTable()
key = int(input("Password for password manager: "))


def autogenerate(length_password):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ123456789(,._-*~'<>/|!@#$%^&)+="
    pswd = ""

    for i in range(0, length_password):
        pswd = pswd + random.choice(characters)

    return pswd


if key == S.SECRET_KEY:

    while True:
        print("""
    [1]  search in passwords
    [2]  add new password
    [3]  show all passwords
    [Q]  Quit
    
        """)

        choice = input(">")

        if choice == "1":
            subject = input("\nWhat are you looking for?: ")

            with open("passwords.txt", 'r', encoding="utf8") as f:
                for line in f:
                    if subject in line:
                        line = line.split(";")

                        print(f"""
    Site: {line[0]}
    E-mail: {line[1]}
    Username: {line[2]}
    Password: {line[3]}
    """)

        if choice == "2":
            auto_generate = input("Do you want to auto generate your password? (y/n) ")

            if auto_generate == "n".lower():
                site = input("\nSite: ")
                email = input("E-mail: ")
                username = input("Username: ")
                password = input("Password: ")

                userinfo = f"{site};{email};{username};{password}\n"

                with open('passwords.txt', 'a') as f:
                    f.write(userinfo)

            if auto_generate == "y".lower():
                site = input("\nSite: ")
                email = input("E-mail: ")
                username = input("Username: ")
                length = int(input("Password length: "))

                password = autogenerate(length)
                print(f"Your password is {password}")

                userinfo = f"{site};{email};{username};{password}\n"

                with open('passwords.txt', 'a') as f:
                    f.write(userinfo)

        if choice == "3":
            x.field_names = ["Site", "E-mail", "Username", "Password"]

            with open("passwords.txt", 'r', encoding="utf8") as f:
                for line in f:
                    line = line.split(";")
                    x.add_row([line[0], line[1], line[2], line[3]])

                print(x)

        if choice == "q".lower():
            quit()

else:
    print("access denied")
