from flask import Flask, session, render_template, request, redirect, url_for
from db import *
from func import *  
import sqlite3
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register_page():
    if( request.method == "GET"): # display page
        return render_template("testing.html")
    Input0 = request.form.get("username")
    Input1 = request.form.get("password")
    return render_template("testing.html", data = Input0)


if __name__ == "__main__":
    app.debug = True
    app.run()