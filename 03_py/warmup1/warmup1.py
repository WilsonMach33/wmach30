def sleep_in(weekday, vacation):
  return not weekday or vacation

def diff21(n):
  if 21-n > 0 :
    return 21-n
  else:
    return -2 * (21 - n)

def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n) <= 10

def missing_char(str, n):
   return str[:n] + str[n+1:]

def pos_neg(a, b, negative):
  if negative:
    return a<0 and b<0
  else:
    return a*b <0


def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and  not b_smile)

def front_back(str):
  if len(str) == 1:
    return str
  return str[-1:] + str[1:len(str)-1] + str[:1]

def sum_double(a, b):
  if a == b:
    return 4*a
  return a+b

def makes10(a, b):
  return (a == 10 or b == 10) or a+b == 10

def not_string(str):
  if("not" in str[:3]):
    return str
  return "not " + str

def front3(str):
  if len(str)<3:
    return str*3
  return str[:3]*3
