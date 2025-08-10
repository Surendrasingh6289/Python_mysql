# importing required libraries
import mysql.connector
def CreateTable():
    dataBase = mysql.connector.connect(
      host ="localhost",                # Localhost for local connection
      user ="root",
      passwd ="",
      database="College"
    )

    print(dataBase)
    

    mycursor = dataBase.cursor()

    Tablename = "CREATE TABLE student (name VARCHAR(255),roll_no INT)"
    mycursor.execute(Tablename)

    print("Created student in college")

CreateTable()
