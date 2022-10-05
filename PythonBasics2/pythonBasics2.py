# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).
import math;
def count_threes(n):
  multiple = {
    "9": 0,
    "6": 0,
    "3": 0
  }
  for key in multiple:
    for i in n:
      if key == i:
        multiple[key] = multiple[key] + 1

  if multiple["3"] > multiple["6"] and multiple["3"] > multiple["9"]:
    return 3
  elif multiple["6"] > multiple["3"] and multiple["6"] > multiple["9"]:
    return 6
  elif multiple["9"] > multiple["6"] and multiple["9"] > multiple["3"]:
    return 9
  else:
    return None





# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  chars = {}
  arr = []
  lastChar = ''
  for i in s:
    if i not in chars.keys():
      # Adding to the dictionary with initial value of 1
      chars[i] = 1
    else:
      if i == lastChar:
        chars[i] = chars[i] + 1

    lastChar = i


  maxChar = max(chars, key=chars.get)
  arr.append(maxChar)
  for key in chars:
    if key != maxChar:
      if chars[key] == chars[maxChar]:
        arr.append(key)
      elif chars[key] > chars[maxChar]:
        arr.append(key)
        arr.remove(maxChar)

  return arr









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
