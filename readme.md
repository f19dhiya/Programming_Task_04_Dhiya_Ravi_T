# Programming Task 04 – Functions, File Handling & Student Management System

**Course:** Python Programming
**Task:** Task 04
**Topics Covered:** Functions, Modular Programming, File Handling, Data Storage, Logging

---

## What is This Task About?

This task is about learning how to break a program into small, reusable pieces called functions.
Instead of writing everything in one big block, each job gets its own function.
We also learn how to save data into files so information is not lost when the program closes.

---

## Folder Structure

```
Programming_Task_04_Akhil_vargise_S/
│
├── calculator_functions.py
├── student_manager.py
├── marks_analyzer.py
├── file_handling.py
├── password_vault.py
├── log_generator.py      
│
└── README.md
```

---

## Part A – Calculator with Functions

**File:** `calculator_functions.py`

### What it does
Shows a menu with four operations. The user picks one, enters two numbers,
and the program calls the right function to calculate and display the result.

### How it works

Each operation has its own function: `addition()`, `subtraction()`,
`multiplication()`, and `division()`. The user picks a number from the menu
and the program calls whichever function matches that choice.

Division has a special check — if the second number is zero, it returns
an error message instead of crashing.

### Sample Output
```
=== Simple Calculator ===

1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter Choice: 1
Enter First Number: 10
Enter Second Number: 20

Result: 30.0
```

---

## Part B – Student Information Manager

**File:** `student_manager.py`

### What it does
Collects a student's name, roll number, branch, and semester through
two separate functions — one to collect the data and one to display it neatly.

### How it works

`get_student_info()` asks the user for all four details and stores them
in a dictionary. A dictionary holds data as labelled pairs like
`"name": "Soham"` so each piece is easy to find by name.

`display_student_info()` receives that dictionary and prints everything
inside a formatted box.

### Sample Output
```
==============================
      Student Information
==============================
  Name     : Soham Patel
  Roll No  : 101
  Branch   : CSE
  Semester : 5
==============================
```

---

## Part C – Marks Analysis System

**File:** `marks_analyzer.py`

### What it does
Takes marks for 5 subjects and uses separate functions to calculate
the total, percentage, and grade. Then displays everything in a neat report.

### How it works

`get_marks()` loops through 5 subjects and collects a mark for each one,
storing them all in a list.

`calculate_total()` uses Python's built-in `sum()` function to add all
marks in the list.

`calculate_percentage()` divides the total by 500 (5 subjects × 100)
and multiplies by 100 to get the percentage.

`calculate_grade()` compares the percentage against the grade boundaries
using a chain of `if / elif / else` conditions and returns the right letter.

`display_results()` prints everything together in a clean report with
a motivational message based on the grade.

### Grade Criteria

| Percentage | Grade |
|-----------|-------|
| 90 and above | A |
| 80 and above | B |
| 70 and above | C |
| 60 and above | D |
| Below 60 | F |

### Sample Output
```
===================================
        Marks Analysis Report
===================================
  Subject 1  :  92.0
  Subject 2  :  88.0
  Subject 3  :  76.0
  Subject 4  :  91.0
  Subject 5  :  85.0
-----------------------------------
  Total Marks  :  432.0 / 500
  Percentage   :  86.40%
  Grade        :  B
  👍 Great work! Almost there.
===================================
```

---

## Part D – File Handling Challenge

**File:** `file_handling.py`

### What it does
Collects student details, saves them into a text file called
`student_data.txt`, then reads the file back and displays the contents.

### How it works

`get_student_details()` collects name, roll number, branch, and marks
from the user.

`save_to_file()` opens `student_data.txt` in write mode using `"w"`.
Write mode creates the file if it does not exist, or replaces it if
it already does. Each detail is written on its own line using `file.write()`.
The file is closed after writing.

`read_from_file()` opens the same file in read mode using `"r"`,
reads everything with `file.read()`, and prints it to the screen.

### Sample Output
```
✅ Student Record Saved Successfully!

Reading File...
==============================
Name: Soham
Roll No: 101
Branch: CSE
Marks: 85
==============================
```

---

## Part E – Password Vault Simulator

**File:** `password_vault.py`

### What it does
A simple menu-driven vault where you can save website credentials
and view all saved records. Everything is stored inside `vault.txt`.

### How it works

`add_password()` asks for a website name, username, and password then
opens `vault.txt` in append mode using `"a"`. Append mode adds new data
to the end of the file without deleting what was already saved.

`view_passwords()` opens the file in read mode and prints all saved
records. It uses a `try / except` block so if the file does not exist
yet, it shows a friendly message instead of crashing.

`show_menu()` prints the three options every time the loop runs.

The `while True` loop keeps the program running until the user chooses
to exit.

### Sample Output
```
==============================
     🔐 Password Vault
==============================
1. Add New Password
2. View All Passwords
3. Exit
==============================
Enter Choice: 2

=== Saved Passwords ===

==============================
Website  : Gmail
Username : user@gmail.com
Password : Test@123
```

---

## Bonus – Log File Generator

**File:** `log_generator.py`

### What it does
Every time an activity happens inside the program, it records the date,
time, program name, and activity description into `activity_log.txt`.
This simulates the kind of logging used in real cybersecurity systems.

### How it works

`get_current_time()` uses Python's `datetime` module to get the current
date and time and formats them into readable strings.

`log_activity()` opens `activity_log.txt` in append mode and writes a
new entry with all four details every time it is called.

`view_logs()` reads and prints the entire log file. It also handles the
case where the file does not exist yet using `try / except`.

The program automatically logs an exit entry when the user chooses
option 3, so every session is fully recorded.

### Sample Output
```
========================================
Date         : 2026-06-13
Time         : 10:45:32
Program Name : Log File Generator
Activity     : Opened the vault
========================================
Date         : 2026-06-13
Time         : 10:46:01
Program Name : Log File Generator
Activity     : User exited the program
========================================
```

---

## Concepts Used — Quick Reference

| Concept | What it means | Used in |
|--------|--------------|---------|
| `def` | Defines a reusable function | All parts |
| `return` | Sends a value back from a function | A, B, C |
| Dictionary `{}` | Stores data as labelled key-value pairs | B |
| List `[]` | Stores multiple values in one variable | C |
| `sum()` | Adds all values in a list automatically | C |
| `open("file", "w")` | Opens a file to write and replace content | D |
| `open("file", "a")` | Opens a file to add to existing content | E, Bonus |
| `open("file", "r")` | Opens a file to read its content | D, E, Bonus |
| `file.write()` | Writes a line of text into a file | D, E, Bonus |
| `file.read()` | Reads the entire file as one string | D, E, Bonus |
| `try / except` | Handles errors without crashing the program | E, Bonus |
| `while True` | Keeps the program running until exit | E, Bonus |
| `break` | Exits a loop when the user chooses to leave | E, Bonus |
| `datetime` module | Gets the current date and time | Bonus |
| `"a"` append mode | Adds to a file without deleting old data | E, Bonus |

---

## How to Run

```bash
python calculator_functions.py
python student_manager.py
python marks_analyzer.py
python file_handling.py
python password_vault.py
python log_generator.py
```


---

## What I Learned From This Task

- Functions make programs cleaner and easier to understand because
  each function does exactly one job.
- Passing data between functions using parameters and return values
  keeps everything organised and avoids repeating code.
- File handling lets programs remember data even after they close —
  this is the foundation of any real application that stores information.
- Append mode is important when you want to keep adding records without
  losing old ones, like a vault or a log file.
- The `try / except` block is essential for handling situations like
  a missing file gracefully instead of letting the program crash.
- Logging is a core concept in cybersecurity — tracking who did what
  and when is how systems detect suspicious activity.

---
