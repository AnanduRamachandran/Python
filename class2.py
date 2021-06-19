class Student: 
     def __init__(self, name, age, grade):
          self.name = name
          self.age = age
          self.grade = grade #0-100

     def get_grade(self):
          return self.grade

class Course:
     def __init__(self, name, max_students):
          self.name = name
          self.max_students = max_students
          self.students = []

     def add_student(self, student):
          if len(self.students) < self.max_students:
               self.students.append(student)
               print (student.name,'added')
          else:
                print(student.name, 'not added')

     def get_average_grade(self):
          value = 0
          for student in self.students:
               value += student.get_grade()

          return value/ len(self.students)

s1 = Student("Tim", 16, 55)
s2 = Student("Bill", 35, 60)
s3 = Student("Max", 34, 88)

c1 = Course("English", 2)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3) # This one wont be added

print(c1.students[1].name)
print(c1.name)
print(c1.get_average_grade())




