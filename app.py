import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


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
        print(email)
        return redirect(url_for("user_form"))


if __name__ == "__main__":
    app.debug = True
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")))