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
    Years_active VARCHAR(100),
    Proven_victims VARCHAR(100),
    Possible_victims VARCHAR(100),
    PRIMARY KEY(Name)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM Serial_Killers.assasins")
mydb.commit()

#Read data from a csv file
assasin_data = pd.read_csv('./serial_killers.csv', index_col=False, delimiter = ',')
assasin_data = assasin_data.fillna('Null')
max_length = 100
assasin_data = assasin_data.rename(columns={'Years active': 'Years_active'})
assasin_data['Years_active'] = assasin_data['Years_active'].str[:max_length]
print(assasin_data.head(20))

#Fill the table
for i, row in assasin_data.iterrows():
    cursor = mydb.cursor()
    sql = "INSERT INTO Serial_Killers.assasins (Name, Country, Years_active, Proven_victims, Possible_victims) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))
    print("Row inserted")
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM Serial_Killers.assasins")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)