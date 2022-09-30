"""
Eric Sohel and Wilson Mach
Time take: 2 hours

OPS: 
1. takes in file "krewes.txt" and reads it
2. iterate through the string
3. keep a counter of current characters, e, and adjust another counter of current category data, counter
4. If character is "$", skips 3 characters and update counter
5. If character is "@", inputs the strings in each category in the dictionary. 
6. After dictionary is formed from steps above, randomly choose a devo and returns the period and ducky in a string
7. Splits the string by the ":" to get period and ducky.
8. Prints out devo, period, and ducky.

DISCO: 
1. How to read a file and convert it into a string
2. how to use split() to separate strings by a specified character

QCC: 
1. There was probably a way to use split to more efficient produce a program than we did. 
"""

import random

def makeDict(data):
    # makes dictionary of devo names
    name = {}
    
    # temporary storage of categorical data
    tempPeriod = ""
    tempName = ""
    tempDucky = ""
    
    # charater counter, e, and category counter, counter
    e=0
    counter = 0
    
    # iterates through string
    while(e <= len(data)):
        # if character == "@" or it is the last character, saves the devo's info in the dictionary and clears the string storages. 
        # updates category counter and character counter by 3 
        if data[e:e+1] == "@" or e==len(data):
            name[tempName] = tempPeriod + ":" + tempDucky
           
            tempPeriod = ""
            tempName = ""
            tempDucky = ""
           
            counter = 0
            e+=3
            
        # if current character == "$", updates category counter and character counter by 3 
        elif data[e:e+1] == "$":
            counter+=1
            e+=3
        
        # else, adds the characters to the appropriate string storage as specified by the character counter
        else:
            if counter == 0:
                tempPeriod += data[e:e+1]
            elif counter == 1:
                tempName += data[e:e+1]
            elif counter == 2:
                tempDucky += data[e:e+1]
                
            # updates character counter
            e+=1
           
    return name

#opens file and reads it 
fileObject = open("krewes.txt", "r")
datas = fileObject.read()

#prints None if there is no data in the file
if(len(datas) == 0):
    print(None) 
#print(datas)

#make the dictionary with appropriate data categories
periods = makeDict(datas)
#print(periods)

#randomly chooses a devo
randomdevo = (random.choice(list(periods.keys())))

info = (periods[randomdevo])

#splits the string associated with devo name into period and ducky 
#prints the appropriate info
print(randomdevo)
print(info.split(":")[0])
print(info.split(":")[1])
