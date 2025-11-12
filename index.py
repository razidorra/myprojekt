
# # 1. list
# list_empty = [] #empty list
# list  = [1, 2, 3] # list with elements
# list.append(1) # adding element to list
# print( list_empty[0]) # accessing first element of list

# #  From another data structure (tuple → list)
# tuple_data = (10, 20, 30) # tuple with elements
# list_from_tuple = list(tuple_data) # converting tuple to list
# print("List from tuple:", list_from_tuple ) # printing the list

# # 2. tuple
# tuple_empty = () # empty tuple
# print("Empty tuple:", tuple_empty) # printing empty tuple
# tuple_data = ("apple" , "banana" , "cherry") # tuple with values
# print("Tuple with elements:", tuple_data) # printing tuple with elements  

# list_data = [100, 200, 300] # list with elements
# tuple_from_list = tuple(list_data) # converting list to tuple
# print("Tuple from list:", tuple_from_list) # printing the tuple

# #3 dcitionary
# dict_values = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# abdul = tuple(dict_values)
# print("Dictionary with predefined values:", abdul)

# # From another data structure (list of tuples → dict)
# list_of_tuples = [('a', 1), ('b',2), ('c',3)]
# dict_from_list = dict(dict_values)
# print("Dictionary from list of tuples:", dict_from_list)

# #4 set
# set_values = {1, 2, 3, 4, 4, 5}  # duplicates automatically removed
# print("Set with predefined values:", set_values)

# # From another data structure (list → set)
# list_for_set = [10, 20, 20, 30]
# set_from_list = set(list_for_set)
# print("Set from list:", set_from_list)



# list and tuple 

# list = [1, 2, 3, 4, 5]
# tuple = (6, 7, 8, )
# print("my_list[1:4]:", list[1:4])  
# print("my_tuple[-2:]:", tuple[-2:]) 

# list.insert(2, 10)
# print("Updated list:", list)


# list = [1, 2, 3, 4, 5 ]
# tuple = ("apple ", "banana", "cherry" "tomato")
# dict = {'john': 30, 
#         'razieh': 25,
#         'abdul' : 27 ,
#         }

# unqiue_set = {'a', 'b', 'c', 'd', 'e' }

# for number in list:
#   print(number)

# for name , age in dict.items():
#   print(f"{name} is {age} years old.")

# sentence = "This is a test sentence this is good"
# abdul = sentence.lower()
# words = abdul.split()
# word_count = {}
# for word in words:
#   if word in word_count:
#     word_count[word] += 3
#   else:
#     word_count[word] = 1
 

# # Print the resulting dictionary
# print("Word Frequency Dictionary:")
# print(word_count)

# List of visitors (some names appear multiple times)
visitors = [
    "Alice", "Bob", "Charlie", "Alice", "Diana", 
    "Bob", "Eve", "Charlie", "Frank", "Eve"
]

# Convert the list into a set to remove duplicates
unique_visitors = set(visitors)

# Count the number of unique visitors
unique_count = len(unique_visitors)

# Print results
print("Unique visitors:", unique_visitors)
print("Total unique visitors:", len(unique_visitors))
