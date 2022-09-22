def sleep_in(weekday, vacation):
  #returns true if it is not a weekday or if it's a vacation
  return not weekday or vacation

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))

def diff21(n):
  #checks if 21-n is positive
  if 21-n > 0 :
    #returns 21-n
    return 21-n
  #if 21-n is negative
  else:
    #returns -2*(21-n)
    return -2 * (21 - n)

print(diff21(19))
print(diff21(10))
print(diff21(21))

def near_hundred(n):
  #returns if number is 10 less than or greater than 100 or
  #10 less than or greater than 200
  return abs(100-n) <= 10 or abs(200-n) <= 10

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))

def missing_char(str, n):
   #returns the string with the character at n taken out
   return str[:n] + str[n+1:]

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

def pos_neg(a, b, negative):
  # if it's negative return if b and a is less than 0
  if negative:
    return a<0 and b<0
  else:
    # if it's not negative return if the product of a and b is negative
    return a*b <0

print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))

def parrot_trouble(talking, hour):
  # returns if the parrot was talking before 7 or after 12
  return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))

def monkey_trouble(a_smile, b_smile):
  # returns if a and b smiles or neither a and b smiles
  return (a_smile and b_smile) or (not a_smile and  not b_smile)

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

def front_back(str):
  # returns string if it's less than 1 in length
  if len(str) == 1:
    return str

  # returns a string after swapping first and last letter
  return str[-1:] + str[1:len(str)-1] + str[:1]

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))

def sum_double(a, b):
  # if a equals b, returns 4 *a
  if a == b:
    return 4*a
  # else, returns a + b
  return a+b

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))

def makes10(a, b):
  # returns if a is 10 or b is 10 or if a+b is 10
  return (a == 10 or b == 10) or a+b == 10

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))

def not_string(str):
  # if string starts with not, returns string
  if("not" in str[:3]):
    return str
  # else, returns str with "not" in front
  return "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))

def front3(str):
  # if string is shorter than 3 characters, print string 3x
  if len(str)<3:
    return str*3
  # prints the first 3 letters of string 3x
  return str[:3]*3

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))
