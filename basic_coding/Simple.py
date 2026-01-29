# writing all programs
arr_input = [123,234,3454,554,645,47,554,34,3454,34,34,65,34,54,345,243,3,345]
my_str = "Hello World!"
dict_list_input = {
    "a": [1, 2, 3],
    "b": [4, 5],
    "c": [],
    "d": [6]
}
list_of_tuple = [
    ("a", 10),
    ("b", 20),
    ("a", 5),
    ("c", 15),
    ("b", 5),
    ("a", 10)
]
dict_tuple = {
    "a": (1, 2, 2, 3),
    "b": (2, 3, 4, 5),
    "c": (3, 4, 6),
    "d": ()
}
dict_tuple_twist = {
    "a": [(1, 2), (2, 3)],
    "b": [(3, 4), (2, 5)],
    "c": [(1, 4)]
}

# # reverse a string without built-in
# new_str = ''
# for i in range(len(my_str) -1, -1, -1):
#   new_str += my_str[i]
# print(new_str)
# print()

# # concept of generators in Python
# def count_up_to(given_num):
#     count = 1
#     while count <= given_num:
#         yield count
#         count += 1

# for num in count_up_to(5):
#     print(num)
# print()

# # second largest number
# largest = float('-inf')
# sec_largest = float('-inf')

# for i in range(len(arr_input)):
#   if arr_input[i] > largest:
#     largest = arr_input[i]
#   elif arr_input[i] > sec_largest and arr_input[i] < largest:
#     sec_largest = arr_input[i]
    
# print("largest ",largest)
# print("sec_largest ",sec_largest)
# print()


# # find duplicates and 3 to each of them
# seen = {}
# output = []
# for i in range(len(arr_input)):
#   if arr_input[i] in seen:
#     output.append(arr_input[i] + 3)
#     seen[arr_input[i]] += 1
#   else:
#     seen[arr_input[i]] = 1
# print(output)
# print(seen)


# # if total inputs even then swap all the inputs with it's next elements else nope
# count = 0
# for i in arr_input:
#   count += 1
# if count % 2 == 0:
#   for i in range(1, len(arr_input), 2):
#     arr_input[i-1], arr_input[i] = arr_input[i], arr_input[i-1]
#   print(arr_input)
# else:
#   print("odd numbers")

# # print least count of string
# seen = {'aa':5, 'bb':4, 'cc':3, 'dd':8}
# least_num = float('inf')
# least_char = None
# for i, val in seen.items():
#   if val < least_num:
#     least_num = val
#     least_char = i
# print(least_char)


# # remove empty values and key and add list values
# seen = {}
# def total(val):
#   all_num = 0
#   for i in val:
#     all_num += i
#   return all_num

# for i, val in dict_input.items():
#   if len(val) == 0:
#     continue
#   else:
#     total_sum = total(val)
#     seen[i] = total_sum
# print(seen)


# # create dict where keys are first elements of tuples values are tuples of unique integers (no duplicates) order of insertion must be preserved
# seen = {}
# for i, val in list_of_tuple:
#     if i not in seen:
#         seen[i] = (val,)
#     elif val not in seen[i]:
#         seen[i] += (val,)
# print(seen) 


# # remove duplicates values of it's respective values of it's key and return the new dict with same ordered tuple
# seen = {}
# def new_func(myinp):
#     temp_set = set()
#     my_list = []
#     for i in myinp:
#         if i in temp_set:
#             continue
#         else:
#             temp_set.add(i)
#             my_list.append(i)
#     return tuple(my_list)

# for i, val in dict_tuple.items():
#     if len(val) > 1:
#         seen[i] = new_func(val)
#     elif len(val) == 1:
#         seen[i] = val
# print(seen)


# # invert this dictionary, i.e., produce a new dictionary where. Keys are the integers from all the tuples. Values are tuples of all original keys that had this integer

# my_dict = {}
# def performed(old_ind, tuple_inp):
#     for i in tuple_inp:
#         if i in my_dict and old_ind not in my_dict[i]:
#             my_dict[i] += (old_ind,)
#         elif i not in my_dict:
#             my_dict[i] = (old_ind,)
#         # if i not in my_dict:
#         #     my_dict[i] = {old_ind}
#         # else:
#         #     my_dict[i].add(old_ind)
    
# for i, val in dict_tuple.items():
#     performed(i, val)
# print(my_dict) 


# my_dict = {}
# def new_func(alp, val):
#     for i in val:
#         if i not in my_dict:
#             my_dict[i] = (alp,)
#         # else:
#         #     my_dict[i] += (alp,)
#         elif alp not in my_dict[i]:
#             my_dict[i] += (alp,)

# for i, val in dict_tuple.items():
#     new_func(i, val)
# print(my_dict)


# # new question
# new_dict = {}
# def new_func(i, val):
#     for a, b in val:
#         if a not in new_dict:
#             new_dict[a] = {i}
#         if b not in new_dict:
#             new_dict[b] = {i}
#         if i not in new_dict[a]:
#             new_dict[a].add(i)
#         if i not in new_dict[b]:
#             new_dict[b].add(i)

# for i, val in dict_tuple_twist.items():
#     new_func(i, val)
# print(new_dict) 


# # is subsequences
# str1 = 'avsfg'
# str2 = 'asdvsgdfasegs'
# x = len(str1)
# y = len(str2)
# i, j = 0, 0
# while i < x and j < y:
#   if str1[i] == str2[j]:
#     i += 1
#   j += 1
# print(i == x)


# # remove adjacent duplicates in string
s = "abbaca"


# reverse a string with numbers that takes a string as input and reverses the string while keeping the numbers in their original position
# num_str_input = 'Hello123World'
# or 'Hello123'



# find max and min values in a given list of tuples
# list_tuple_inp = [('V',60), ('VI',70), ('VII',75), ('VIII',72), ('IX', 78), ('X',70)]


# Find the paies in list which sum to my_sum
# my_List = [1,2,3,4,5,4,3,2,1], my_sum = 6


# reverse string
# my_str = 'Hello World!'


# Oops concept



# set_tuple_input = {('a', 3), ('b', 2), ('c', 5), ('d', 9),('e',7), ('f',6)}

# sorted_input = sorted(set_tuple_input, key=lambda x : x[1])
# print(sorted_input)
