import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi ( PersonID, Nome_proprio , Razza , Peso , Eta ) VALUES (%s, %s, %s, %s, %s)"

x = 1

for x in range(5):


    PersonID = input("PersonID ") 
    Nome_proprio = input("Nome_proprio ") 
    Razza = input("Razz a") 
    Peso = input("Peso ") 
    Eta = input("Eta ")
    val = (PersonID, Nome_proprio, Razza, Peso, Eta)

    print(val)
    mycursor.execute(sql, val)


mydb.commit()


print(mycursor.rowcount, "was inserted.")