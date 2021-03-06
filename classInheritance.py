# class Cat:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age
     
#      def speak(self):
#           print("Meow")
     
# class Dog:
#      def __init__(self, name, age):
#           self.name = name
#           self.age = age
     
#      def speak(self):
#           print("Bark")

# Here both the classes are similar, infact only the speak method varies hence we can define a parent calass and inherit it in cat and dog class.

class Pet:
     def __init__(self, name, age):
          self.name = name 
          self.age = age

     def show(self):
         print(f"i am {self.name} and I am {self.age} years old") 

class Cat(Pet):
     def __init__(self, name, age, color):
          super().__init__(name, age)
          self.color = color

     def speak(self):
          print("Meow")

class Dog(Pet):
     def speak(self):
          print("Bark")

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34)
c.show()
