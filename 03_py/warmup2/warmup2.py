def string_times(str, n):
  return str*n

def string_splosion(str):
  x = 0
  ans = ""
  while x < len(str):
    ans += str[:x+1]
    x+=1
  return ans

def array_front9(nums):
  if 9 in nums:
    return nums.index(9) >= 0 and nums.index(9) < 4
  return False

def front_times(str, n):
  return str[:3]*n

def last2(str):
  count = 0
  i = 0
  while i  < len(str) - 2:
    if str[-2:] in str[i:i+2]:
      count+=1
    i+=1
  return count

def array123(nums):
  return 1 in nums and 2 in nums and 3 in nums

def string_match(a, b):
  count = 0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

def string_bits(str):
  return str[::2]

def array_count9(nums):
  count = 0
  for x in nums:
    if x == 9:
      count +=1
  return count
