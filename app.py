
from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure application
app = Flask(__name__)

db = SQL("sqlite:///scores.db")

ID = [1256, 9876, 2376, 2199, 3301]

#هنا لو حذفت استعلام الإنشاء بيطلع لي خطأ مافيه جدول, ولو خليته بيطلع لي بعد المرة الأولى ان الجدول موجود
#db.execute("CREATE TABLE score (id INTEGER, Quizz1 INTEGER, MidTermTest INTEGER, Quizz2 INTEGER, Exam INTEGER, Total INTEGER, PRIMARY KEY(id))")
db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam, Total) VALUES(?, ?, ?, ?, ?, ?)", 1256, 4, 15, 4, 66, "(SELECT SUM(Quizz1+MidTermTest+Quizz2+Exam))")
db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam, Total) VALUES(?, ?, ?, ?, ?, ?)", 9876, 3, 20, 5, 65, "(SELECT SUM(Quizz1+MidTermTest+Quizz2+Exam))")
db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam, Total) VALUES(?, ?, ?, ?, ?, ?)", 2376, 5, 15, 4, 50, "(SELECT SUM(Quizz1+MidTermTest+Quizz2+Exam))")
db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam, Total) VALUES(?, ?, ?, ?, ?, ?)", 2199, 5, 14, 3, 60, "(SELECT SUM(Quizz1+MidTermTest+Quizz2+Exam))")
db.execute("INSERT INTO score (id, Quizz1, MidTermTest, Quizz2, Exam, Total) VALUES(?, ?, ?, ?, ?, ?)", 3301, 3, 18, 4, 55, "(SELECT SUM(Quizz1+MidTermTest+Quizz2+Exam))")


@app.route("/", methods=["GET", "POST"])
def index():
    Max = db.execute("SELECT MAX(Total) FROM score AS MTotal")
    Min = db.execute("SELECT MIN(Total) FROM score AS MTotal")
    Avg = db.execute("SELECT AVG(Total) FROM score AS ATOtal")
    return render_template("index.html", Max=Max, Min=Min, Avg=Avg)


@app.route("/score", methods=["POST"])
def score():
    ids = request.form.get("id")
    # convert id to integer
    id = int(ids)
    if ids not in ID:
        return render_template("index.html")
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
