from generator.simple import generate_password
from manager.password_manager import add_entry, get_entry, list_entries
import pyperclip

def view_password():
    # ask for service and username/email, then print result
    service = input("Enter the service (github, gmail): ").strip()
    username = input("Enter the username or email: ").strip()
    password = get_entry(service, username)
    
    if password is None:
        print("Could not find a password for those credentials.")
    else:
        print(f"\nUsername & Password for {service} is:\n")
        print(f"Username: {username}")
        print(f"Password: {password}\n")

def create_new_password():
    # ask for service, username/email, prompt_int, then ask to save
    service = input("Service name (e.g., github, gmail): ").strip()
    username = input("Username or email: ").strip()
    
    length = prompt_int("Enter a password length (e.g., 12): ")
    password = generate_password(length)
    
    print(f"""
                    Service: {service}
                    Username: {username}
                    Password: {password}
        """)
    save = input("Would you like to save these credentials? ('y' or 'n'): ").strip().lower()
    
    if save == "y":
        add_entry(service, username, password)
        print("\nPassword saved!\n")
    elif save == "n":
        print("\nPassword not saved!\n")

def prompt_int(message: str) -> int:
    # ask user for a valid int
    while True:
        value = input(message)
        try:
            return int(value)
        except ValueError:
            print("Enter a valid number.")


def view_all():
    data = list_entries()
    
    if not data:
        print("No passwords saved yet.")
    for service, username in data.items():
        print(f"\nService: {service}")
        for name, password in username.items():
            print(f"Username: {name}")
            print(f"Password: {password}\n")

def main_menu():
    """
    This is the main function that runs when you start the program.
    For now, it just asks the user for a password length and prints a password.
    """
    
    print("===== PASSWORD GENERATOR =====")
    print("1. Create new password")
    print("2. View a password")
    print("3. List all services/usernames")
    print("4. Quit")
    
    while True:
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            create_new_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            view_all()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")
    
    
# this makes sure main() runs only when you run 'python main.py'
# and not when this file is imported from somewhere else
if __name__ == "__main__":
    main_menu()