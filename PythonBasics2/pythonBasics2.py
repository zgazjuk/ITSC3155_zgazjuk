# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  count = 0
  for i in range(0, n + 1):
    if i % 3 == 0:
      count = count + 1
  return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  longestRepeated = ''
  previousCount = 0
  count = 0
  for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
      count = count + 1
    else:
      count = previousCount
    if count > previousCount:
      longestRepeated = s[i]
      previousCount

  return longestRepeated


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  list1 = []
  list2 = []
  for i in range(0, (len(s) + 2) // 2):
    if s[i] == " ":
      continue
    else:
      list1.append(s[i].lower())
  for i in range((len(s))// 2,  len(s)):
    if s[i] == " ":
      continue
    else:
      list2.append(s[i].lower())
  print(list1)
  print(list2[::-1])
  if list1 == list2[::-1]:
    return True
  else:
    return False



  return
