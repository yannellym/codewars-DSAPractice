Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

test_00:
most_frequent_char('bookeeper') # -> 'e'

def most_frequent_char(s):
  max_char = ''
  store = {}
  
  for char in s:
    if char not in store:
      store[char] = 1
    store[char] += 1
  return max(store, key = store.get) 
