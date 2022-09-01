from flask import Flask,render_template,request, session, redirect, url_for, escape
#import module flask_mysql จำเป็นต้อง pip install flask_mysqldb ในcmd
from flask_mysqldb import MySQL
import secrets
secret_key = secrets.token_hex(16)
# example output, secret_key = 000d88cd9d90036ebdd237eb6b0db000
app = Flask(__name__) 
app.config['SECRET_KEY'] = secret_key
#คำสั่งเปิดsql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'user'
mysql = MySQL(app)
#สิ้นสุดคำสั่ง


@app.route('/')
def index():
    school = {"subject":"flask","teacher":"Wisanu","grade":"grade12"}
    student = {"a","b","c","d","e"}
    #คำสั่งconnection cursor เพื่อเปิด mysql
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO user VALUES("pretz","12345678") ''')
    mysql.connection.commit()
    cursor.close()
    #สิ้นสุดคำสั่ง
    return render_template('index.html',school=school,student=student)

@app.route('/signin',methods = ['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username =="ppzz" and password =="1234":
        session['username'] = username
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
   session.pop('username', None)
   return redirect(url_for('index'))

app.run()



