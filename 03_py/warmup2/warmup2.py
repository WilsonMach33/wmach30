def string_times(str, n):
  return str*n #returns string str n times

print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Oh Boy!', 2))
print('\n')

def string_splosion(str):
  x = 0
  ans = ""
  while x < len(str): #index x is less than length of str
    ans += str[:x+1] #adds everything of string up to that index
    x+=1 #increment index
  return ans

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('Kitten'))
print('\n')

def array_front9(nums):
  if 9 in nums: #check so index doesn't throw error
    return nums.index(9) >= 0 and nums.index(9) < 4
  return False

print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([5, 5]))
print('\n')

def front_times(str, n):
  return str[:3]*n #upto the first 3 chars of str, n times

print(front_times('Chocolate', 2))
print(front_times('Abc', 3))
print(front_times('', 4))
print('\n')

def last2(str):
  count = 0
  i = 0
  while i  < len(str) - 2: #until the 3rd last char in str
    if str[-2:] in str[i:i+2]: #checks if last two chars (:-2) equals len 2 substring at i
      count+=1
    i+=1
  return count

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('13121312'))
print('\n')

def array123(nums):
  return 1 in nums and 2 in nums and 3 in nums

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 2]))
print(array123([]))
print('\n')

def string_match(a, b):
  #interesting DISCO here is that if the index range is out of bounds of str,
  #it would return an empty str for the out of range parts
  #e.g. a = "hello", a[4:9] returns: o
  count = 0
  for i in range(len(a)-1): #i increments until last index of a
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('hello', 'he'))
print(string_match('aabbccdd', 'abbbxxd'))
print('\n')

def string_bits(str):
  return str[::2] #uses the step, skips 2

print(string_bits('Hello'))
print(string_bits('Heeololeo'))
print(string_bits('Chocoate'))
print('\n')

def array_count9(nums):
  #iterates through list and checks if 9
  count = 0
  for x in nums:
    if x == 9:
      count +=1
  return count

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([]))
print('\n')
