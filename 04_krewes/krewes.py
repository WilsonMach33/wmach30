```'''
Team Smartans: Wilson Mach, Joshua Liu, Aahan Mehta
DISCO:
    1. random.choice(n) returns a random element from n, which is a iterable object, like list or tuple
    2. dict.keys() returns a view object of the keys in a dictionary, which means its not iterable.
     Because of this, we have to typecast the view object into a list.
     how to cast variables in python: type(object)
QCC:
How does choice pick a random element?
Choice is more convenient in this case, since we don't have to do random shenanigans

OPS SUMMARY:
    1. Check if dictionary is empty
    2. Pick a random key after making a list of the keys in dictionary
    3. Checks if there aren't any elements in key
    4. Pick random element from dictionary in subsection key, using random.choice()
    5. Returns a list with both krewe member and period
    6. Prints output depending on situation (discovered by checks)
'''
import random

def getRandKrew(nums):
    if len(nums) == 0:
        return ["empty dict"]
    key = random.choice(list(nums.keys()))
    if len(nums[key]) == 0:
        return ["empty key"]
    return [random.choice(nums[key]), str(key)]

def printRandKrew(nums):
    x = getRandKrew(nums)
    if x[0] == "empty dict":
        print("empty dictionary")
    if x[0] == "empty key":
        print("dictionary has an empty key, which was randomly chosen")
    if len(x) == 2:
        print(x[0] + " from Pd. " + x[1])

krewes1 = {2:[], 3:[]}
krewes2 = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}
krewes3 = {}

printRandKrew(krewes1)
printRandKrew(krewes2)
printRandKrew(krewes3)```
