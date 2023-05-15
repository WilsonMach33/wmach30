from flask import Flask, render_template
from db import *

app = Flask(__name__)

@app.route('/')
def index():
    title = name()
    popp = popularity()
    data = title+popp 
    return render_template('D3_test.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run()

    #   var data = {{ data|tojson }};