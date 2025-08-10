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

insertQuery = """ 
            INSERT INTO student (name,roll_no) VALUES ('surendra',12)"""

mycursor.execute(insertQuery)
print("no of rows inserted: ",mycursor.rowcount)
print("inserted id: ",mycursor.lastrowid)

dataBase.commit()
dataBase.close()