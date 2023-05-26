from flask import render_template
from flask import Flask
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Serial_Killers"
)

mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/assasins')
def assasinslist():
    mycursor.execute("SELECT * FROM assasins")
    myresult = mycursor.fetchall()
    return render_template('assasins.html', assasins=myresult)
