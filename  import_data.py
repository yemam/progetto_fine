import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Serial_Killers")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS Serial_Killers.assasins (
    Name VARCHAR(100) NOT NULL,
    Country VARCHAR(100),
    Years_active INTEGER,
    Proven_victims VARCHAR(100),
    Possible_victims VARCHAR(100),
    Notes VARCHAR(3000),
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM Serial_Killers.assasins")
mydb.commit()

#Read data from a csv file
assasin_data = pd.read_csv('./serial_killers.csv', index_col=False, delimiter = ',')
assasin_data = assasin_data.fillna('Null')
print(assasin_data.head(20))

#Fill the table
for i,row in assasin_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO Serial_Killers.assasins VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Tabella inserita BETCH!!")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM Serial_Killers.assasins")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)