friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Bob", "age": 50},
    {"name": "Goerge", "Age": 43}
]

print(friends[1]["name"])


t = [3, 7]
a, b = t
print(a, b)

student_attendance = {"Rolf": 67, "Bob": 56, "Rafal": 76}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
