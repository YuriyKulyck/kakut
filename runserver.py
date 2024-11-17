from flask import *

from DBManager import DBManager

app = Flask("Kahoot")
db_name = "kakut.db"
@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quiz()
    return render_template("index.html", quizzes=quizzes)

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

app.run()