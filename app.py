
from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure application
app = Flask(__name__)

db = SQL("sqlite:///score.db")

ID = [1256, 9876, 2376, 2199, 3301]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/score", methods=["POST"])
def score():
    db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam) VALUES(?, ?, ?, ?, ?)", 1256, 4, 15, 4, 66)
    db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam) VALUES(?, ?, ?, ?, ?)", 9876, 3, 20, 5, 65)
    db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam) VALUES(?, ?, ?, ?, ?)", 2376, 5, 15, 4, 50)
    db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam) VALUES(?, ?, ?, ?, ?)", 2199, 5, 14, 3, 60)
    db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam) VALUES(?, ?, ?, ?, ?)", 3301, 3, 18, 4, 55)
    db.execute("UPDATE score SET Total = (SELECT SUM(Quizz1+MidTermTest+Quizz2+Exam) FROM score)")

    Max = db.execute("SELECT MAX(Total) FROM score")
    Min = db.execute("SELECT MIN(Total) FROM score")
    Avg = db.execute("SELECT AVG(Total) FROM score")

    ids = request.form.get("id")
    # convert id to integer
    id = int(ids)
    if ids not in ID:
        return render_template("index.html", Max=Max, Min=Min, Avg=Avg)
    else:
        scoreid = db.execute("SELECT * FROM score WHERE id = ", id)
        # save G with total to check grade
        G = db.execute("SELECT Total FROM scoreWHERE id = ", id)
        if G.Total >= 90:
            Grade = 'A'
            return render_template("scores.html", scoreid=scoreid, Grade=Grade)
        elif G.Total >= 80 or G.Total <=89:
            Grade = 'B'
            return render_template("scores.html", scoreid=scoreid, Grade=Grade)
        elif G.Total >= 70 or G.Total <=79:
            Grade = 'C'
            return render_template("scores.html", scoreid=scoreid, Grade=Grade)
        elif G.Total >= 60 or G.Total <=69:
            Grade = 'D'
            return render_template("scores.html", scoreid=scoreid, Grade=Grade)
        else:
            Grade = 'F'
            return render_template("scores.html", scoreid=scoreid, Grade=Grade)
