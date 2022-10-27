from student import Student

student_list = []
student = Student('Tom', 23, '10086')
student_list.append(student)

student = Student('Harry', 25, '10010')
student_list.append(student)

# [student1, student2, student3, ...]
# list1 = []
# for i in student_list:
#     list1.append(i.__dict__)
# print(list1)

list1 = [i.__dict__ for i in student_list]
print(list1)

f = open('student.data', 'w', encoding='utf-8')
f.write(str(list1))
f.close()