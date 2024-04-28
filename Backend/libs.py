import socket
from time import sleep

pc_name = socket.gethostname()

def welcome_message(): #for manipulation
  style = "#" * (len(pc_name) + 6) #len for total variable
  print(style)
  print(f"## {pc_name} ##")
  print(style)

def exit_program():
  print("Program will be stop immediately")
  sleep(1)
  print("3...")
  sleep(1)
  print("2...")
  sleep(1)
  print("1...")
  sleep(1)
  print("Program has been ended")
  exit()

#optional for debugger
if __name__ == '__main__':
  welcome_message()
  exit_program()