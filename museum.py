from flask import Flask, render_template, redirect, url_for,session, request

app = Flask(__name__)
app.secret_key="salut"

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("room1"))
    return render_template("login.html")

@app.route("/room/1")
def room1():
    if "username" in session:
        username = session["username"]
        return render_template("room/1.html", username=username)
    else:
        return redirect(url_for("login"))


@app.route("/room/2")
def room2():
    if "username" in session:
        username = session["username"]
        return render_template("room/2.html", username=username)
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()