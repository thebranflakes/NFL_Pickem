from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "secretKEYsoSECRET"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        session["username"] = username
        return redirect(url_for("username"))
    else:
        return render_template("login.html")


@app.route("/username")
def username():
    if "username" in session:
        username = session["username"]
        return f"<h1>{username}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/admin/")
def admin():
    return redirect(url_for("home", name="Admin!"))


if __name__ == "__main__":
    app.run(debug=True)
