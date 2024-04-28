import main

def start():
  while True :
    print("This is Minimarket Apps!")
    
    back_menu = input("Back to menu? [y/n] ")
    if back_menu == "y":
      main.menu()

  if __name__ == "__main__":
    start()