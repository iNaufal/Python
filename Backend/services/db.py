import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_minimarket"
)

#insert item to db MySQL
def insert_item(code_inv, name_inv, price_inv, stock_inv):
  cursor = db.cursor() #execution query
  cursor.execute("INSERT INTO inventory (code_inv, name_inv, price_inv, stock_inv) VALUES (%s, %s, %s, %s)", (code_inv, name_inv, price_inv, stock_inv))
  db.commit()

  if cursor.rowcount > 0:
    print("\nData has been Added\n")
  else:
    print("\nData failed to add\n")
    
#get item from db
def fetch_item():
  cursor = db.cursor()
  cursor.execute("SELECT * FROM inventory")
  return cursor.fetchall()

