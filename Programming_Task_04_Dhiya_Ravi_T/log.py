import datetime

def get_current_time():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    return date, time

def log_activity(program_name, activity):
    date, time = get_current_time()

    file = open("activity_log.txt", "a")
    file.write("=" * 40 + "\n")
    file.write(f"Date         : {date}\n")
    file.write(f"Time         : {time}\n")
    file.write(f"Program Name : {program_name}\n")
    file.write(f"Activity     : {activity}\n")
    file.close()

def view_logs():
    print("\n📋 Activity Log:\n")
    try:
        file = open("activity_log.txt", "r")
        contents = file.read()
        file.close()
        if contents == "":
            print("No logs found yet.")
        else:
            print(contents)
    except FileNotFoundError:
        print("No log file found yet.")

def show_menu():
    print("=" * 40)
    print("       🛡️  Log File Generator")
    print("=" * 40)
    print("1. Log a New Activity")
    print("2. View All Logs")
    print("3. Exit")
    print("=" * 40)

program_name = "Log File Generator"

while True:
    show_menu()
    choice = input("Enter Choice: ")

    if choice == "1":
        activity = input("Enter Activity Description: ")
        log_activity(program_name, activity)
        print("\n✅ Activity logged successfully!\n")

    elif choice == "2":
        view_logs()

    elif choice == "3":
        log_activity(program_name, "User exited the program")
        print("\n👋 Goodbye! Your activity has been logged.")
        break

    else:
        print("\n⚠️  Invalid choice. Enter 1, 2 or 3.\n")