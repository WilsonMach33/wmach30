"""
Eric Sohel and William Mach

QSS: "hello"
"""

import random 

# make dict
# take data file
# delete first + last line
# splice by line into list
# if no quotations, splice by comma
# SPLICE BY THE LAST COMMA THAT EXISTS
# iterate through list and put in dict
# randomly pick
    # var = randrange(0, 99.9, 0.1)
    # sum counter
    # while(



my_dict = {}

#open text file in read mode 
file_content = open("occupations.csv", "r")
#read file into a string
data = file_content.read()
#close file
file_content.close()


#seperate everyline 
spliced_data = data.split("\n")
#removes last line twice because of empty line 
spliced_data.pop() 
spliced_data.pop()
spliced_data.pop(0)


for x in spliced_data:
    #find index of right most comma 
    lastcommapos = x.rfind(",")
    
    #set values accordingly in the dictionary
    #percentages are stored as floats 
    my_dict[ (x[0:lastcommapos]) ] = float( x[lastcommapos+1:len(x)] )
    

# *** weighted average randomizer *** 

#999 instead of 99.9 because randrange does not work with floats
#this will generate all increments of .1 from 0 to 99.8 inclusive

randompick = random.randrange(0, 999, 1)
counter = 0

#every job gets its own set of numbers. Ex: buisness and financial gets 6.2 - 11.2
for x in my_dict:
    
    #uncomment this line to see the math 
    #print (randompick / 10)
    
    if(counter > randompick / 10):
        print(x)
        break
    counter += my_dict[x]