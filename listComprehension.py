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

#Same with 
