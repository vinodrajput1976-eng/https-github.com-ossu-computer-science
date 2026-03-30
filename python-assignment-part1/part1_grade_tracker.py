# part1_grade_tracker.py
# Student Grade Tracker - Complete Assignment Solution

# -------------------- Task 1 --------------------
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("\n--- Task 1 Output ---")
for student in raw_students:
    name = student["name"].strip().title()
    roll = int(student["roll"])
    marks = [int(m) for m in student["marks_str"].split(", ")]

    valid = all(word.isalpha() for word in name.split())
    print(f"{name} {'✓ Valid name' if valid else '✗ Invalid name'}")

    cleaned_students.append({"name": name, "roll": roll, "marks": marks})

    print("="*32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("="*32)

for student in cleaned_students:
    if student["roll"] == 103:
        print("\nSpecial Output:")
        print(student["name"].upper())
        print(student["name"].lower())


# -------------------- Task 2 --------------------
print("\n--- Task 2 Output ---")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

for i in range(len(subjects)):
    m = marks[i]
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"{subjects[i]} : {m} → {grade}")

total = sum(marks)
avg = round(total / len(marks), 2)

print("\nTotal:", total)
print("Average:", avg)

max_marks = max(marks)
min_marks = min(marks)

print("Highest:", subjects[marks.index(max_marks)], max_marks)
print("Lowest:", subjects[marks.index(min_marks)], min_marks)

new_subjects = 0

while True:
    sub = input("Enter subject name (or 'done'): ")
    if sub.lower() == "done":
        break

    marks_input = input("Enter marks: ")

    if not marks_input.isdigit():
        print("Invalid input!")
        continue

    m = int(marks_input)
    if m < 0 or m > 100:
        print("Marks must be between 0–100")
        continue

    subjects.append(sub)
    marks.append(m)
    new_subjects += 1

print("\nNew subjects added:", new_subjects)
print("Updated Average:", round(sum(marks)/len(marks), 2))


# -------------------- Task 3 --------------------
print("\n--- Task 3 Output ---")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("Name              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
averages = []

for name, marks in class_data:
    avg = round(sum(marks)/len(marks), 2)
    averages.append(avg)

    status = "Pass" if avg >= 60 else "Fail"

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    print(f"{name:<18} | {avg:^7} | {status}")

print("\nPassed:", pass_count)
print("Failed:", fail_count)

top_avg = max(averages)
top_index = averages.index(top_avg)

print("Topper:", class_data[top_index][0], top_avg)

class_avg = round(sum(averages)/len(averages), 2)
print("Class Average:", class_avg)


# -------------------- Task 4 --------------------
print("\n--- Task 4 Output ---")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print("1. Clean:", clean_essay)

print("\n2. Title Case:", clean_essay.title())

print("\n3. Count:", clean_essay.count("python"))

replaced = clean_essay.replace("python", "Python 🐍")
print("\n4. Replace:", replaced)

sentences = clean_essay.split(". ")
print("\n5. Sentences:", sentences)

print("\n6. Numbered Sentences:")
for i, s in enumerate(sentences, 1):
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")
