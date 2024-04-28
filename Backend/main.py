from libs import welcome_message, exit_program
from games import venopy
from tools import minimarket

def menu():
  user_option = int(input(f"Menu Program:\n1. Games Venopy\n2. Minimarket\n3. Exit\n\nPlease Select: "))

  if user_option == 1:
    venopy.start()
  elif user_option == 2:
    minimarket.start()
  elif user_option == 3:
    exit_program()
  else:
    print("Please selected the menu!")

def main():
  welcome_message()
  menu()

#validasi maintain code
if __name__ == '__main__':
  main()