from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
username = "hi"
password = "hello"

@app.route("/", methods = ["GET", "POST"])
def root():
    if (session.has_key("name")):
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for("login"))


@app.route("/login", methods = ["GET", "POST"])
def login():
    #if person is still logged in, return the Welcome page
    if(session.has_key("name")):
        return render_template("welcome.html", name = session["name"])
    #if something was posted / a submit button was pressed...
    if (request.method == "POST"):
        #This is something extra. Just on my error page I have a button that returns to login page so this checks for it
        if(request.form.has_key("backLogin")):
            return redirect(url_for("login"))
        #If the person just inputted the login info, check for errors
        usr = request.form["userName"]
        usrPass = request.form["password"]
        #if the info matches with account, save the session and return the Welcome page
        if(usr == username and usrPass == password):
            session["name"] = usr
            return redirect(url_for("welcome"))
        #if the password is wrong but the username is right, tell user that password is wrong
        elif(usr == username):
            flash("Wrong password")
            return render_template("error.html")
        #if username is wrong, tell the user either the account does not exist or the username is wrong
        else:
            flash("Username is incorrect or the account does not exist")
            return render_template("error.html")
    #Else if the user just started, return the login "page"
    return render_template("base.html")

@app.route("/logOut", methods = ["GET", "POST"])
def logOut():
    #if user is currently logged in, log them out by removing their name in session
    if (session.has_key("name")):
        session.pop("name")
    #then return the login page 
    return redirect(url_for("root"))

@app.route("/welcome", methods = ["GET", "POST"])
def welcome():
    return render_template("welcome.html", usrName = session["name"])

if __name__ == "__main__":
    app.debug = True
    app.run()
