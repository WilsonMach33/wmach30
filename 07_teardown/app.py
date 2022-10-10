'''
Young Lions Crying At War :: Ameer Alnasser, Yat Long Chan, Wilson Mach
SoftDev pd08
K07 -- Web dev *
2022-10-4
time spent: 0.5hrs
'''


from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?



@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?
app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
*   If two functions are defined consecutively, only the first one will be run
python3 app.py -> typing hte link given into the web browser gives us the output of the function written without needing (print(hello_world())
*   127.0.0.1 is our home directory, only local
*   Flask is installed only if package is installed
*   if ctrl C is hit, 127.0.0.1 is unreachable

QCC:
0.  Line 12 utilized a similar syntax as the java constructor
1.  the forward slash is utilized when we navigate directories
2.  the output will be printed inside of the directory with the app, with the #3 name from the constructor
4.  It will  appear on the webpage of the route
5.  java also has object-oriented programming, as seen on line 21 wih the call of a method from app  
...
INVESTIGATIVE APPROACH:
Our team jumped to running the command, then working it out backwards. We did not realize the URL until QAF traffic (before the team shuffle)
'''