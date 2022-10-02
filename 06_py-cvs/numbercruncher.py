"""
Team SMH
Roster: Eric Sohel and Wilson Mach

DISCO:
    1. file methods:
        A. file.open() opens file
        B. file.close() closes file
        C. file.read() reads file
    2. string.split() splits strings by specified character
    3. list.pop() removes values from list
    4. string.maketrans() and string.translate() can be used to replace characters in string
    5. break breaks out of loop
    
QCC:
    1. how to find last element in a dictionary? We were trying to figure this out but couldn't
    find a good solution so we just accessed last element of the spliced_data list instead
    
HOW THIS SCRIPT WORKS:
    1. make dictionary
        A. open, read, close data file
        B. splice by line into list
        C. delete first + last line due to useless data
        D. splice by last comma in line
        E. iterate through spliced data, removes the the instances of '"' in job
        F. put job and percentage into dictionary
    2. randomly pick job with weighted percentage
        A. picks a random number between 0 and 999, inclusive of 0 and not 999 with a step of 1
        B. iterates through dictionary, adding up all percentages until it reaches a number greater than
        random number
        C. breaks out of loop and prints out job associated with percentage
        D. If no job has been printed after iteration, print last job

"""

import random 

# make dict
my_dict = {}

#open text file in read mode 
file_content = open("occupations.csv", "r")
#read file into a string
data = file_content.read()
#close file
file_content.close()


#separate everyline 
spliced_data = data.split("\n")

#removes last line and first line because of useless data 
spliced_data.pop() 
spliced_data.pop(0)

for x in spliced_data:
    #find index of right most comma 
    lastcommapos = x.rfind(",")
    
    #splice string to get job name
    job_old = x[0:lastcommapos]
    
    #replace all instances of '"' to ' ' 
    table = job_old.maketrans('"', ' ')
    job_old = job_old.translate(table)
    
    #get rid of leading and ending spaces resulting from character replacement
    job_new = job_old.strip()
    
    #set values accordingly in the dictionary
    #percentages are stored as floats
    my_dict[job_new] = float( x[lastcommapos+1:len(x)] )

# *** weighted average randomizer *** 

#999 instead of 99.9 because randrange does not work with floats
#this will generate all increments of .1 from 0 to 99.8 inclusive

randompick = random.randrange(0, 999, 1)
counter = 0
picked = False

#every job gets its own set of numbers. Ex: business and financial gets 6.2 - 11.2
for x in my_dict:
    #if counter is between two jobs, break out of loop and prints number 
    if(counter >= randompick / 10):
        print(x)
        picked = True
        break
    counter += my_dict[x]

#if iteration is finished and no job has been printed, print last job
if picked == False:
    last_one = spliced_data[len(spliced_data)-1]
    last_table = last_one.maketrans('"', ' ')
    last_one = last_one.translate(last_table)
    print(last_one.strip())
    