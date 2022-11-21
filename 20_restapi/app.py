from flask import Flask, render_template
import requests

app = Flask(__name__)

file = open('key_nasa.txt', 'r')
api_key = file.readline()
file.close()

url = "https://api.nasa.gov/planetary/apod"
start_date = "2022-11-20"

@app.route('/')
def homepage():
    params = {"api_key":api_key, "start_date":start_date}
    a = requests.get(url, params=params).json()

    return a
# render_template('main.html', api_key = api_key)
if __name__ == '__main__':
    app.debug = True
    app.run()
