nums = [1, 3, 5, 6, 8]

# I want 'n' for each 'n' un nums

my_list = [n for n in nums]
print(my_list)

# I want 'n*n' for each 'n' in nums

my_list = [n*n for n in nums]
print(my_list)

#using a map + lambda

my_list = map(lambda n: n*n, nums)
print (list(my_list)) #my_list was a map


#I want 'n' for each 'n' in nums if 'n' is even 

my_list = [n for n in nums if n%2 == 0]
print(my_list)

# Using a filter + lambda
my_list = filter(lambda n: n%2 == 0, nums)
print my_list

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print zip(names, heros) <-- To match both lists one to one

# I want a dict{'name': 'hero} for each name, hero in zip(name, heros)

#Using for loop
my_dict = {}
for name, hero in zip(name, heros):
     my_dict{name} = hero
print my_dict

#Using dictionary comprehension
my_dict = {name: hero for name, hero in zip (name, heros)}
print(my_dict)

#Set comprehension

# Using for loop
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
     my_set.add(n)
print my_set

#Using set comprehension
my_set = {n for n in nums}
print my_set
