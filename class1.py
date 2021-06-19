class Dog:
     
     def __init__(self, name, age):
          self.name = name
          self.age = age
     def bark(self):
          print("Bark")
     def get_age(self):
          print (self.age)
     def set_age(self, age):
          self.age = age

d = Dog("Tim", 50)
d.set_age(60)
print (d.age)
 