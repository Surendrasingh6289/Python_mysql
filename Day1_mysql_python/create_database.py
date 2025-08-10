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

mycursor.execute("CREATE TABLE College")

print("College database created")


