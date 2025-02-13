from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/salle/1")

@app.route('/salle/<int:room_id>')
def room(room_id):
    return render_template("room.html", room_id=room_id)

if __name__ == '__main__':
    app.run()