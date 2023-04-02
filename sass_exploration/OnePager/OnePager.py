from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def webpage():
    return render_template('OnePager.html')

if __name__ == "__main__":  
    app.debug = True        
    app.run()