from database_manager import login, sign_up
import user as us
def menu():
    print("-"*8 + "Welcome" + "-"*8)
    print(" "*4 + "Choose an option")
    print(" "*4 + "1.login")
    print(" "*4 + "2.sign_up")
    print(" "*4 + "0.exit")
    opt = input()

    if opt == "1":
        name, password, id = login()
    elif opt == "2":
        name, password, id = sign_up()
    else:
        print("exiting app")
        quit()

    user = us.user(name,password,id)

    while True:
         print("*"*8 + "Welcome " + f"{name} " + "*"*8)

         print("    1.Create a new password")
         print("    2.View all acounts stored for a certain app")
         print("    3.View all acounts stored for a certain email app")
         print("    4.View all accounts stored for a certain username")
         print("    5.View all information stored for your account")
         print("    0.Exit app")
         option = input()
         if option == "1":
            user.new_password()
         elif option == "2":
            user.app_accounts()
         elif option == "3":
            user.email_users()
         elif option == "4":
            user.username_accounts()
         elif option == "5":
            user.show_all()
         elif option == "0":
            print("Bye-Bye!")
            break
         else:
            print("Didn't you read your options?")   

         print("\n \n")

if __name__ == "__main__":
    menu()
