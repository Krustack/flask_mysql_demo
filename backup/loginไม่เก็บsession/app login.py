from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"Tuu","Pom","Por","Robert","Ae"}
    return render_template('index.html',school=school,student=student)

@app.route('/signin',methods = ['POST'])
def login(): #สร้างฟังชั่นlogin
    username = request.form['username'] #นำค่าในฟอร์ม usernameมาเก็บในตัวแปรusername
    password = request.form['password'] #นำค่าในฟอร์ม usernameมาเก็บในตัวแปรusername
    if username =="ppzz" and password =="1234": #นำค่ามาตรวจสอบ 
        return render_template('signin.html',signin={"username":"ยินดีต้อนรับคุณ"+username})
    else:
        return render_template('signin.html',signin={"username":"ข้อมูลไม่ถูกต้อง"})

@app.route('/page2')
def page2():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"Tuu","Pom","Por","Robert","Ae"}
    return render_template('page2.html',school=school,student=student)

@app.route('/page3')
def page3():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"Tuu","Pom","Por","Robert","Ae"}
    return render_template('page3.html',school=school,student=student)

@app.route('/page4')
def page4():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"Tuu","Pom","Por","Robert","Ae"}
    return render_template('page4.html',school=school,student=student)



app.run()



