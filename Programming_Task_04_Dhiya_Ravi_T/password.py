def add_password():
    website  = input("Enter Website Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    file = open("vault.txt", "a")
    file.write("=" * 30 + "\n")
    file.write(f"Website  : {website}\n")
    file.write(f"Username : {username}\n")
    file.write(f"Password : {password}\n")
    file.close()

    print("\n✅ Password saved successfully!\n")


def view_passwords():
    print("\n=== Saved Passwords ===\n")
    try:
        file = open("vault.txt", "r")
        contents = file.read()
        file.close()
        if contents == "":
            print("No records found. Add a password first.")
        else:
            print(contents)
    except FileNotFoundError:
        print("No vault found yet. Add a password first.")


def show_menu():
    print("=" * 30)
    print("     🔐 Password Vault")
    print("=" * 30)
    print("1. Add New Password")
    print("2. View All Passwords")
    print("3. Exit")
    print("=" * 30)


while True:
    show_menu()
    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        print("\n👋 Exiting Password Vault. Stay safe!")
        break
    else:
        print("\n⚠️  Invalid choice. Please enter 1, 2 or 3.\n")