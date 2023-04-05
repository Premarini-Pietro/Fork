from flask import render_template
from flask import Flask
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CLASH_ROYALE"
)

mycursor = mydb.cursor()


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', name='Pietro')

######################################

@app.route('/units')
def unitlist():
    mycursor.execute("select * from Clash_Unit")
    myresult = mycursor.fetchall()
    return render_template('clash_units.html', units=myresult)
