
import random

students = ['Al', 'Kagome', 'Indu', 'Colton', 'Cheryl', 'Mitchell', 'Angie']
absent_students = ['Al']
group_size = 3

for absent_student in absent_students:
    students.remove(absent_student)

random.shuffle(students)

# [['Kagome', 'Indu', 'Colton'], ['Cheryl', 'Mitchell', 'Angie']]
groups = [[] for i in range(len(students)//group_size)]
print(groups)
for i in range(len(students)):
    groups[i % len(groups)].append(students[i])
