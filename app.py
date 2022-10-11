from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretKEYsoSECRET"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["nm"]
        session["username"] = username
        return redirect(url_for("username"))
    else:
        if "username" in session:
            return redirect(url_for("username"))
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/username")
def username():
    if "username" in session:
        username = session["username"]
        return render_template("user.html")
    else:
        return redirect(url_for("login"))


@app.route("/admin/")
def admin():
    return redirect(url_for("home", name="Admin!"))


if __name__ == "__main__":
    app.run(debug=True)
