def get_student_info():
    print("=== Enter Student Details ===\n")

    name     = input("Enter Student Name: ")
    roll_no  = input("Enter Roll Number: ")
    branch   = input("Enter Branch (e.g. CSE, ECE): ")
    semester = input("Enter Semester: ")

   
    student = {
        "name"     : name,
        "roll_no"  : roll_no,
        "branch"   : branch,
        "semester" : semester
    }

    return student



def display_student_info(student):
    print("\n")
    print("=" * 30)
    print("      Student Information")
    print("=" * 30)
    print(f"  Name     : {student['name']}")
    print(f"  Roll No  : {student['roll_no']}")
    print(f"  Branch   : {student['branch']}")
    print(f"  Semester : {student['semester']}")
    print("=" * 30)



student_data = get_student_info()


display_student_info(student_data)