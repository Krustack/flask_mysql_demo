from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"name":"robert","grade":"grade10"}
    return render_template('index.html',school=school,student=student)
app.run()



