# Student Grading System

print("=== Student Grading System ===")

# Input student details
student_name = input("Enter student name: ")

# Input marks
maths = float(input("Enter Maths marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))

# Calculate total and average
total = maths + english + science
average = total / 3

# Determine grade
if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n--- Result ---")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
