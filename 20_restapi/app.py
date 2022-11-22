'''
Shinji, Wilson
SoftDev
K<20> -- A RESTful Journey Skyward
<2022>-<11>-<21>
time spent: 0.8 hours
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