
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
class_name = input("Enter class/grade: ")
section = input("Enter section: ")
math_marks = float(input("Enter Marks for Math: "))
science_marks = float(input("Enter Marks for Science: "))
total_marks = math_marks + science_marks
percentage = (total_marks / 200) * 100
print("\n==============================")
print("       STUDENT DETAILS        ")
print("==============================")
print(f"Name        :   {student_name
}")
print(f"Roll Number : {roll_number}")
print(f"Class       : {class_name} ({section})")
print(f"Total Marks : {total_marks}/200")
print(f"Percentage  : {percentage:.2f}%")
print("==============================")