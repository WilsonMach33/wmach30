'''
Mew: Shinji Kusakabe, Wilson Mach
SoftDev
K20 -- A RESTful Journey Skyward
2022-11-22
time spent: 0.8 hours

DISCO:
1. You can use the requests library to make HTTP requests
2. APIs are a good source of data
3. JSON can be used like a dictionary  

QCC: 
1. How can we make our own APIs?
'''

from flask import Flask, render_template
import requests
app = Flask(__name__)

with open('key_nasa.txt', 'r') as file:
    api_key = file.read()
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key

@app.route("/")
def display():
    req = requests.get(url)
    info = req.json()
    imgurl = info['hdurl']
    explanation = info['explanation']
    return render_template('main.html', img = imgurl, text = explanation)

if __name__ == "__main__":
    app.debug = True 
    app.run()