from flask import Flask, render_template, request, flash, redirect
from surveys import satisfaction_survey as survey

app =Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"

responses = []

@app.route("/")
def home_page():
    """Renders title and instrutions"""

    return render_template('start-survey.html', survey = survey)

@app.route("/questions/<int:qid>", methods=["post","get"])
def question_page(qid):
    question = survey.questions[qid]

    if (len(responses) == len(survey.questions)):
        return redirect("/completed")
    if (len(responses) != qid):
        flash("Please no skipping ahead. Thank you.")
        return redirect(f"/questions/{len(responses)}")
    
    return render_template("questions.html", num = qid, question = question)



@app.route('/answer', methods=["post"])
def answer_question():
    answer = request.form["answer"]
    responses.append(answer)
    if (len(responses) == len(survey.questions)):
        return redirect("/completed")
    else:
        return redirect(f"/questions/{len(responses)}")  
    
@app.route("/completed")
def completed_survey():
    return render_template("completed.html")