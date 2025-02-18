from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("room1"))

@app.route("/room/1")
def room1():
    return render_template("room/1.html")

@app.route("/room/2")
def room2():
    return render_template("room/2.html")

if __name__ == "__main__":
    app.run()