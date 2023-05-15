from db import *

def index():
    title = name()
    popp = popularity()
    data = []
    for i in range(len(title)):
        data.append({title[i],popp[i]})  
    print(data)
    print()
    print(type(title))
    print(type(data))

index()