# Student Data Manager

# Dictionary to store student data
students = {
    "Arun": 85,
    "Meera": 92,
    "Rahul": 78,
    "Sneha": 88,
    "Kiran": 95
}

# Calculate class average
total_marks = sum(students.values())
average = total_marks / len(students)

# Find topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Function to assign grade
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

# Display results
print("----- Student Data -----")
for name, mark in students.items():
    print(f"{name}: {mark} marks, Grade: {assign_grade(mark)}")

print("\n----- Summary -----")
print(f"Class Average: {average:.2f}")
print(f"Topper: {topper} with {top_marks} marks")