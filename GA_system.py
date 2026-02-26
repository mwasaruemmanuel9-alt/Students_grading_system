# JKUAT Biostatistics Student Grading System

print("=== JKUAT Biostatistics Grading System ===")

# Student details
student_name = input("Enter student name: ")

# Core Units
sta_2130 = float(input("Fundamentals of Biostatistics (STA 2130): "))
sta_2210 = float(input("Fundamentals of Epidemiological Methods (STA 2210): "))
sta_2436 = float(input("Modeling Infectious Diseases (STA 2436): "))
sta_2434 = float(input("Statistical Genetics (STA 2434): "))
sta_2439 = float(input("Project in Biostatistics (STA 2439): "))

# Common University Units
hrd_2101 = float(input("Communication Skills (HRD 2101): "))
hrd_2102 = float(input("Development Studies & Social Ethics (HRD 2102): "))
szl_2111 = float(input("HIV/AIDS (SZL 2111): "))
hrd_2401 = float(input("Entrepreneurship Skills (HRD 2401): "))

# Calculations
total = (
    sta_2130 + sta_2210 + sta_2436 + sta_2434 + sta_2439 +
    hrd_2101 + hrd_2102 + szl_2111 + hrd_2401
)

average = total / 9

# Grade determination
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

# Output
print("\n--- Student Results ---")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average Mark:", round(average, 2))
print("Overall Grade:", grade)
