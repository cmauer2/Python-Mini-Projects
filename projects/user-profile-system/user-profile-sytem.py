# user profile system
# user can create a profile, edit it, and view it
# user needs to create a profile, then sign in with it. then they can view it
# req's: user creation, user auth, profile viewer, account manager (edit profile pw or username)

# description: user can login/signup, after that they can add, remove, or view accounts.
# make each logged in user unique. (each user has different accounts paired to them)
# add an edit feature

import json

filename = "users-auth.json"

def add_account(data):
    return signup(data)

def edit_account(data):
    pass

def remove_account(data):
    accounts = data['accounts']
    while True:
        view_account(data)
        try:
            choice = int(input("Which account would you like to remove: "))
            accounts.remove(accounts[choice - 1])
            print("\nAccount successfully removed.")
            save_file(data)
            if len(accounts) == 0:
                main()
            break
        except ValueError:
            print("\nPlease enter one of the numbers.")
            continue
    
def view_account(data):
    accounts = data['accounts']
    print()
    for idx, account in enumerate(accounts):
        print(f"{idx + 1}. Username: {account['Username']} | Password: {account['Password']}")

def home_display(data):
    print("Welcome to your Password Manager!")
    while True:
        print("\n1. Add Account")
        print("2. Remove Account")
        print("3. View Account(s)")
        print("4. Edit Account(s)")
        print("5. Signout\n")
        choice = input("Choose an option: ")
        if choice == '1':
            add_account(data)
        elif choice == '2':
            remove_account(data)
        elif choice == '3':
            view_account(data)
        elif choice == '4':
            edit_account(data)
        elif choice == '5':
            print("You have signed out")
            break
        else:
            print("Please chose between 1-4.")
            continue
def load_file():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except:
        return {"accounts": [] }

def save_file(data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
        
def signup(data):
    while True:
        username = input("Choose a username: ")
        password = input("Create a password for this account: ")
        pw_confirmation = input("Enter your password again: ")
        if password == pw_confirmation:
            data["accounts"].append({'Username': username, 'Password': password})
            print("Account added.")
            save_file(data)
            break
        else:
            print("Passwords did not match.")
            continue
    

def login(data):
    login_successful = False
    username_input = input("Username: ")
    password_input = input("Password: ")
    for users in data['accounts']:
        if users["Username"] == username_input and users["Password"] == password_input:
            login_successful = True
            break
    if login_successful == True:
        print("Login Successful!")
        home_display(data)
    else:
        print("Invalid login.")
        

def main():
    data = load_file()
    while True:
        choice = input("Would you like to login or signup? (q to exit): ").lower().strip()
        
        if choice == 'signup':
            signup(data)
        elif choice == 'login':
            login(data)
        elif choice == 'q':
            break
        else:
            print("Incorrect option.")
            continue
        
if __name__ == '__main__':
    main()
    