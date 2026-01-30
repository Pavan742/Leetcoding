global_arr = [123,234,3454,554,645,47,554,34,3454,34,34,65,34,54,345,243,3,345]
global_str = "Hello World, please welcome pavan"

# 🔥 BASIC CODING (Warm-up but compulsory)

# # Reverse a string without using built-in functions 
# for i in range(len(global_str) -1, -1, -1):
#     print(global_str[i], end='')

# # Reverse words in a sentence
# mywords = []
# for i in global_str.split():
#     mywords.append(i[::-1])
# print(' '.join(mywords))

# Check if a string is palindrome
# global_str = 'gadag'
# output = ''
# for i in my_palindrom:
#     output += i
# print(output == my_palindrom)
# # instead this approach because above is O(n^2)
# my_str = 'gadag'
# left, right = 0, len(my_str) - 1
# output = True
# while left < right:
#     if my_str[left] != my_str[right]:
#         output = False
#         break
#     left += 1
#     right -= 1
# print(output)
# or 
# print(my_str == my_str[::-1])

# # Count vowels and consonants in a string
# global_str = "Hello World! Python is fun."
# my_set = {'a','e','i','o','u'}
# count = 0
# for i in global_str.lower():
#     if i in my_set:
#         count += 1
# print(count)

# # Find factorial (iterative & recursive)
# n = 5
# output = 1
# for i in range(2, n+1):
#     output = output * i
# print(output)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(n))

# Fibonacci series (n terms)
# n = 10
# result = []
# i, j = 0, 1
# for _ in range(1, n+1):
#     result.append(i)
#     i, j = j, j + i
# print(result)
# seen = {}
# def fibo(n):
#     if n <= 1:
#         return n 
#     if n in seen:
#         return seen[n]
#     seen[n] = fibo(n - 1) + fibo(n - 2)
#     return seen[n]
# print(fibo(n))

# # Find largest / smallest number in a list
# largest = float('-inf')
# smallest = float('inf')
# for i in range(len( global_arr)):
#     if  global_arr[i] > largest:
#         largest =  global_arr[i]
#     if  global_arr[i] < smallest:
#         smallest =  global_arr[i]
# print(smallest, largest)
# # or
# smallest = min( global_arr)
# largest = max( global_arr)

# # Find 2nd largest and largest number in a list
# largest = float('-inf')
# sec_largest = float('-inf')
# for i in range(len( global_arr)):
#     if  global_arr[i] > largest:
#         sec_largest = largest
#         largest =  global_arr[i]
#     elif largest >  global_arr[i] > sec_largest:
#         sec_largest =  global_arr[i]
# print(sec_largest, largest)

# # Swap two numbers without temp variable
# a, b = 5, 10
# a,b = b, a
# print(a, b)
# or
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a, b)

# Remove duplicates from a list
# my_set = set()
# for i in range(len( global_arr)):
#     if  global_arr[i] not in my_set:
#         my_set.add( global_arr[i])
# print(list(my_set))
# or
# print(list(set( global_arr)))

# # Count frequency of characters in a string
# my_dict = {}
# for i in global_str:
#     my_dict[i] = my_dict.get(i, 0) + 1
#     # or
#     # if i in my_dict:
#     #     my_dict[i] += 1
#     # else:
#     #     my_dict[i] = 1
# print(my_dict)



# 🔥 LIST / ARRAY PROBLEMS (VERY COMMON)

# # Find duplicate elements in a list
# output = []
# my_set = set()
# for i in range(len(global_arr)):
#     if global_arr[i] in my_set:
#         output.append(global_arr[i])
#     else:
#         my_set.add(global_arr[i])
# print(output)

# # Find missing number in range 1…n
# arr_inp = [1,2,3,4,6,7,8]
# n = len(arr_inp) + 1
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(arr_inp)
# output = expected_sum - actual_sum
# print(output)

# # Find second largest element
# largest = float("-inf")
# sec_largest = float("-inf")
# for i in range(len(global_arr)):
#     if global_arr[i] > largest:
#         sec_largest = largest
#         largest = global_arr[i]
#     elif largest > global_arr[i] > sec_largest:
#         sec_largest = global_arr[i]
# print(largest, sec_largest)

# # Sort list without using sort()
# n = len(global_arr)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if global_arr[j] > global_arr[j+1]:
#             global_arr[j], global_arr[j+1] = global_arr[j+1], global_arr[j]
# print(global_arr)

# # Rotate array by k positions 
# k = 62
# k = k % len(global_arr)
# removed = global_arr[:k]
# del global_arr[:k]
# global_arr.extend(removed)
# print(global_arr)

# # Find intersection of two lists
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [4, 5, 6, 7]
# output = []
# my_set = set(arr1)
# for i in arr2:
#     if i in my_set:
#         output.append(i)
# print(output)

# # Merge two sorted lists
# list1 = [1,2,4,6,7,9]
# list2 = [2,3,5,7,8]
# output = []
# left, right = 0, 0
# while left < len(list1) and right < len(list2):
#     if list1[left] > list2[right]:
#         output.append(list2[right])
#         right += 1
#     elif list1[left] < list2[right]:
#         output.append(list1[left])
#         left += 1
#     else:
#         output.append(list1[left])
#         output.append(list2[right])
#         right += 1
#         left += 1
# output.extend(list1[left:])
# output.extend(list2[right:])
# print(output)

# Move all zeros to end
# my_inp = [4,0,2,0,1]
# pos = 0
# for i in range(len(my_inp)):
#     if my_inp[i] == 0:
#         my_inp.pop(i)
#         my_inp.append(0)
# print(my_inp) # time complexity is O(n^2)
# for i in range(len(my_inp)):
#     if my_inp[i] != 0:
#         my_inp[pos] = my_inp[i]
#         pos += 1
#     print(my_inp)
# for i in range(pos, len(my_inp)):
#     my_inp[i] = 0
# print("my input ",my_inp)

# # Find pairs with given sum
# arr = [1, 2, 3, 4, 5]
# target = 6
# output = []
# # for i in range(len(arr)):
# #     for j in range(i + 1, len(arr)):
# #         arr_sum = arr[i] + arr[j]
# #         if arr_sum == target:
# #             output.append((arr[i], arr[j]))
# # print(output). # bruit force
# my_set = set()
# for i in arr:
#     needed = target - i
#     if needed in my_set:
#         output.append((needed, i))
#     my_set.add(i)
# print(output)

# # Find common elements in 3 lists
# arr1 = [1, 2, 3, 4]
# arr2 = [2, 3, 5]
# arr3 = [0, 2, 3, 6]
# output = []
# my_set1 = set(arr1)
# my_set2 = set(arr2)
# for i in arr3:
#     if i in my_set1 and i in my_set2:
#         output.append(i)
# print(output)


# 🔥 STRING PROBLEMS (ASKED A LOT)

# Check if two strings are anagrams
# Longest substring without repeating characters
# First non-repeating character
# Count words in a file/string
# Check if string contains only digits
# Remove special characters from string
# Find all permutations of a string
# Compress a string (aaabb → a3b2)



# 🔥 DICTIONARY / HASHING (IMPORTANT)

# Word frequency using dictionary
# Group anagrams
# Sort dictionary by value
# Find key with maximum value
# Merge two dictionaries
# Invert dictionary (value → key)



# 🔥 STACK / QUEUE PROBLEMS

# Implement stack using list
# Implement queue using deque
# Valid parentheses problem
# Reverse a stack
# Next greater element



# 🔥 LINKED LIST (ASKED IN PRODUCT COMPANIES)

# Reverse a linked list
# Detect loop in linked list
# Find middle of linked list
# Remove nth node from end



# 🔥 RECURSION (INTERVIEW FAVORITE)

# Print numbers from 1 to n (no loop)
# Sum of digits using recursion
# Reverse string using recursion
# Tower of Hanoi (basic understanding)



# 🔥 SEARCHING & SORTING

# Binary search implementation
# Linear search
# Bubble sort
# Selection sort
# Quick sort (logic)
# Find kth smallest element



# 🔥 MATRIX / 2D ARRAY

# Matrix transpose
# Sum of diagonals
# Rotate matrix 90 degrees
# Spiral traversal



# 🔥 FILE HANDLING (REAL BACKEND TASKS)

# Read file and count word frequency
# Find longest line in file
# Remove duplicate lines from file



# 🔥 PYTHON-SPECIFIC CODING (VERY IMPORTANT)

# Flatten a nested list
# Find memory-efficient way to read large file
# Custom iterator implementation
# Custom decorator (timing/logging)
# Generator for even numbers
# Context manager using with



# 🔥 DATABASE-STYLE LOGIC (OFTEN COMBINED)

# Find second highest salary (list/dict input)
# Employee-manager hierarchy
# Group records by department



# 🔥 REAL INTERVIEW TASKS (ACTUAL)

# Design a rate limiter (basic code)
# LRU cache implementation
# REST API pseudo-code for CRUD
# Pagination logic
# Retry mechanism with backoff
# Log analyzer (count errors per minute)