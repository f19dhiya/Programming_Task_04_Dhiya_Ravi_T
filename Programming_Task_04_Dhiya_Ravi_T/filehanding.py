def get_student_details():
    print("=== Enter Student Details ===\n")
    name    = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")
    branch  = input("Enter Branch: ")
    marks   = input("Enter Marks: ")
    return name, roll_no, branch, marks


def save_to_file(name, roll_no, branch, marks):
    file = open("student_data.txt", "w")
    file.write(f"Name: {name}\n")
    file.write(f"Roll No: {roll_no}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Marks: {marks}\n")
    file.close()
    print("\n✅ Student Record Saved Successfully!")


def read_from_file():
    print("\nReading File...")
    print("=" * 30)
    file = open("student_data.txt", "r")
    contents = file.read()
    file.close()
    print(contents)
    print("=" * 30)


name, roll_no, branch, marks = get_student_details()
save_to_file(name, roll_no, branch, marks)
read_from_file()