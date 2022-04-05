# 1 Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  total = 0
  for int in range(1, n + 1):
    total += int
  return total


# 2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  return max(nums)
largest([10, 4, 2, 231, 91, 54])


#  3 Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrances(str1, str2):
  return str1.count(str2)


# 4 Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  total = 1
  for num in args:
    total *= num
  return total
