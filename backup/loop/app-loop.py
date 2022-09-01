from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"Tuu","Pom","Por","Robert","Ae"}
    return render_template('index.html',school=school,student=student)
app.run()



