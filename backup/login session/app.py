from flask import Flask,render_template,request, session, redirect, url_for, escape
import secrets
secret_key = secrets.token_hex(16) #สุ่มเลขมาเป็น tokenเพื่อใช้session
# example output, secret_key = 000d88cd9d90036ebdd237eb6b0db000
app = Flask(__name__) 
app.config['SECRET_KEY'] = secret_key #นำtokenมาใช้
@app.route('/')
def index():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"Tuu","Pom","Por","Robert","Ae"}
    return render_template('index.html',school=school,student=student)

@app.route('/signin',methods = ['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username =="ppzz" and password =="1234":
        session['username'] = username #เมื่อตรวจสอบว่าเงื่อนไขเป็นจริงนำข้อมูลusernameมาเก็บในsession
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

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)#ลบsession usernameออก
   return redirect(url_for('index'))

app.run()



