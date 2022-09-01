from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'user'
mysql = MySQL(app)
@app.route('/')
def hello():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM user''')
    rows=cursor.fetchall()
    cursor.close()
    return render_template('index.html',datas= rows)

@app.route('/student')
def add():
    return render_template('adddata.html')

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):
        cursor = mysql.connection.cursor()
        cursor.execute(''' DELETE FROM user WHERE username=%s ''' ,(id_data,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('hello'))
    

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        username=request.form['fname']
        password=request.form['lname']
        # phone=request.form['phone']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO user VALUES(%s,%s)''',(username,password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('hello'))
        

app.run(debug=True)






