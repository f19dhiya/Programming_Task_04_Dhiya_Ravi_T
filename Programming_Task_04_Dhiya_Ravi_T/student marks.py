def get_marks():
    print("=== Enter Marks for 5 Subjects ===\n")

    marks = []  

    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject} (out of 100): "))
        marks.append(mark) 

    return marks


def calculate_total(marks):
    total = sum(marks)  
    return total



def calculate_percentage(total):
   
    percentage = (total / 500) * 100
    return percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def display_results(marks, total, percentage, grade):
    print("\n")
    print("=" * 35)
    print("        Marks Analysis Report")
    print("=" * 35)

    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

    for i in range(5):
        print(f"  {subjects[i]}  :  {marks[i]}")

    print("-" * 35)
    print(f"  Total Marks  :  {total} / 500")
    print(f"  Percentage   :  {percentage:.2f}%")
    print(f"  Grade        :  {grade}")
    print("=" * 35)

    if grade == "A":
        print("  🌟 Outstanding! Keep it up!")
    elif grade == "B":
        print("  👍 Great work! Almost there.")
    elif grade == "C":
        print("  🙂 Good effort. Keep improving.")
    elif grade == "D":
        print("  📚 You passed. Study harder next time.")
    else:
        print("  ⚠️  You need to work harder. Don't give up!")

    print("=" * 35)


marks = get_marks()

total      = calculate_total(marks)
percentage = calculate_percentage(total)
grade      = calculate_grade(percentage)


display_results(marks, total, percentage, grade)