from flask import Flask, session, render_template, request, redirect, url_for
import sqlite3
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register_page():
    if( request.method == "GET"): # display page
        return render_template("testing.html")
    
    a = request.form
    return render_template("testing.html", data = a)


if __name__ == "__main__":
    app.debug = True
    app.run()