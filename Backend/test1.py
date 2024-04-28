import random

cave_position = random.randint(1, 4)

#lets to try array
hobbies = ["Coding", "Football", "Basketball", "Hiking"]
index = 1

print(hobbies)
print(hobbies[0]) #index array alway from 0
print(hobbies[1])
print(hobbies[2])
print(hobbies[3])
print(hobbies[3 - index])

last_data = len(hobbies) - 1 #find last data array
print(f"Last data is {hobbies[last_data]}")

#temporrary data
tmp_hobbies = hobbies
print(f"hobbies = {hobbies}")

tmp_hobbies[1] = "Surfing"
print(f"tmp_hobbies = {tmp_hobbies}")
print("")

#practice 2
username = input("Please enter the name: ")

cave = "|_|"
caves = [cave] * 4 #convert to array []
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
def get_confirmation(prompt):
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