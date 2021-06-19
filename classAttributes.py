class Person:
     number_of_people = 0 # This is a class attributes so it is specific to the class and would be same for all instances.

     def __init__(self, name):
          self.name = name
          Person.add_person() #This incraments when a new instance of the class is created.

          @classmethod
          def number_of_people_(cls):
               return class.number_of_people
          
          @classmethod
          def add_person(cls):
               cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Jack")

print(p1.number_of_people)
print(Person.number_of_people) #Since number_of_people is a class attribute we can do this; it is not specific to any class instances.

Person.number_of_people = 8 #Since it is a class attribute we can change it like this.
print(p2.number_of_people)

print(Person.number_of_people_())