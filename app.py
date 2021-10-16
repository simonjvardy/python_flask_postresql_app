import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config = os.environ["SQLALCHEMY_DATABASE_URI"]
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = os.environ.get("SECRET_KEY")


# Database Model
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_


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