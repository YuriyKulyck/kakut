from flask import *

from DBManager import DBManager

app = Flask("Kahoot")
db_name = "kakut.db"
app.secret_key = "123"
@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quiz()
    return render_template("index.html", quizzes=quizzes)

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/quiz/<int:quiz_id>")
def get_quest(quiz_id):
    db_manager = DBManager(db_name)
    questions = db_manager.get_que(quiz_id)
    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0

    return redirect(url_for("show_question", quiz_id=quiz_id))

@app.route("/quiz/<int:quiz_id>/question")
def show_question(quiz_id):
    number = session["quest_index"]
    q = session["questions"][number]
    db_manager = DBManager(db_name)
    options = db_manager.get_options(q[0])

    return str(q) + "<br>" + str(options)