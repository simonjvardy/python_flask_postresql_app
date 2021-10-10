import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask.extensions.sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


"""
Render the user input landing page
"""


@app.route("/")
@app.route("/user_form")
def user_form():
    return render_template("user_form.html")


"""
Post the form data to the database
"""

@app.route("/add_data", methods=["GET", "POST"])
def add_data():
    if request.method == 'POST':
        email = request.form["input_email"]
        height = request.form["input_height"]
        print(email)
        print(height)
        flash("Success! An email has been sent to you confirming your data")
        return redirect(url_for("user_form"))


if __name__ == "__main__":
    app.debug = True
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")))