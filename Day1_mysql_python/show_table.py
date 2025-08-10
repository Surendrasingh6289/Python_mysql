# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="root",
  passwd ="",
  database="College"
)

print(dataBase)
    

mycursor = dataBase.cursor()

mycursor.execute("Show tables;")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print("College database created")


