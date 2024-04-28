import random
from libs import welcome_message

welcome_message("WELCOME TO MY PYTHON CODING")

#lets to try looping
#practice 3
username = input("Please enter the name: ")
while username == "":
  username = input("Please enter the name: ")

while True:
  cave = "|_|"
  caves = [cave] * 4 #convert to array []

  cave_position = random.randint(1, 4)
  tmp_caves = caves.copy() #temporrary array and duplicate the variable with shallowCopy
  caves[cave_position - 1] = "|>.<|" #-1 agar tidak dari 0

  #join array must in bottom copy and 
  caves = "".join(caves)
  tmp_caves = "".join(tmp_caves)

  print(f'''
  Hello {username}! Please attention the cave 
  {tmp_caves}
  ''')

  #validation confirmation yes or no
  def get_confirmation(prompt): #function reusable
    while True: #looping
      response = input(prompt).strip().lower()
      if response == 'yes' or response == 'y':
        return True
      elif response == 'no' or response == 'n':
        exit()
      else:
        print("Please enter 'yes' or 'no'.")

  #you must convert to integer
  select_cave = int(input("you can select one the cave [1 / 2 / 3 / 4]: "))
  confirmation = get_confirmation("Are you sure select {}? (yes/no): ".format(select_cave))

  if select_cave == cave_position:
    print(f" {caves} \n You're Right!")
  else:
    print(f"{caves} \n You're Wrong! ")
    
  play_again = input("\nDo you want to continue the game? [y/n]")
  if play_again == "n":
    break
  
print("Program has ended")