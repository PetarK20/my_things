students = int(input("Enter the number of students: "))
data = {}

for _ in range(students):
    input1 = input("Enter student name and grade: ").split()
    student_name = input1[0]#1 елемент от сплита;име
    student_grade = float(input1[1])#2 елемент от сплита; оценки
    
    if student_name in data:
        data[student_name].append(student_grade)
    else:
        data[student_name] = [student_grade]

for key, value in data.items():
    average_grade = sum(value) / len(value)
    print(f"{key} -> {' '.join(map(str, value))} (avg: {average_grade:.2f})")
