import main
from services import db

def add():
  code_inv = input("Code Inventory: ")
  name_inv = input("Name: ")
  price_inv = int(input("Price: "))
  stock_inv = int(input("Stock: "))

  save = db.insert_item(code_inv, name_inv, price_inv, stock_inv)

def check():
  items = db.fetch_item()
  for item in items:
    code_inv = item[1]
    name_inv = item[2]
    price_inv = item[3]
    stock_inv = item[4]
    print(f'''
Code Inventory: {code_inv}
{name_inv} | Rp. {price_inv}
Stock: {stock_inv}
''')

def start():
  while True :
    menu = int(input("Menu:\n1. Add Inventory\n2. Check Inventory\n3. Back to Menu\n\nSilahkan Pilih: "))

    if menu == 1:
      add()
    elif menu ==  2:
      check()
    elif menu == 3:
      main.menu()
    else:
      break

  if __name__ == "__main__":
    start()