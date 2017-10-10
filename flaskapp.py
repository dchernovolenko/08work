#!/usr/bin/env python
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
username = "hi"
password = "hello"
app.secret_key = "haha"
@app.route("/")
def root():
        if not session.get("user"):
            return redirect(url_for('login'))
        else:
            return redirect(url_for('welcome'))


@app.route("/login", methods = ["GET", "POST"])
def login():
    try:
        if request.args["name"] == username and request.args["pass"] == password:
            session["user"] = username
            return redirect(url_for('welcome'))
        elif request.args["name"] == username and request.args["pass"] != password:
            return render_template("error.html", err = "wrong pass")
        elif request.args["name"] != username and request.args["pass"] == password:
            return render_template("error.html", err = "wrong user")
        else:
            return render_template("error.html", err = "both wrong")
        if not bool(session):
            return render_template("login.html")
    except:
            return render_template("login.html")

@app.route("/welcome")
def welcome():
    return render_template('welcome.html')

@app.route("/logout", methods =["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('root'))


if __name__ == "__main__":
        app.debug = True
        app.run()
