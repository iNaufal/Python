import random
import main

def start():
  while True:
    cave = "|_|"
    caves = [cave] * 4 #convert to array []

    cave_position = random.randint(1, 4)
    tmp_caves = caves.copy() #temporrary array and duplicate the variable with shallowCopy
    caves[cave_position - 1] = "|>.<|" #-1 agar tidak dari 0

    #join array must in bottom copy and 
    caves = "".join(caves)
    tmp_caves = "".join(tmp_caves)

    print(f"Hello! Please attention the cave \n{tmp_caves}\n")

    #you must convert to integer
    select_cave = int(input("you can select one the cave [1 / 2 / 3 / 4]: "))

    if select_cave == cave_position:
      print(f" {caves} \n You're Right!")
    else:
      print(f"{caves} \n You're Wrong! ")
      
    play_again = input("\nDo you want to continue the game? [y/n]")
    if play_again == "n":
      main.menu()

if __name__ == '__main__':
  start()