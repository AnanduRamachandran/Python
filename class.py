class Dog:
     
     def __init__(self, name, age):
          self.name = name
          self.age = age
     def bark(self):
          print("Bark")
     def get_age(self):
          print (self.age)

d = Dog("Tim", 50)
d2 = Dog("Bill", 70)

print(d.name)
print(d2.name)

d2.get_age()