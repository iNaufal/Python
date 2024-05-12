#Boolean
print(True)
print(False)

#String
print("Let's learning Python") #you can use ""
print('Make it easy') # or this ''

#Integer
print(20)

#Float
print(3.49)

#Hexadecimal
print(hex(0xFF))

#Complex
x = complex('3+5j')
print(x)

#List: the data can be modified
print([1,2,3,4,5])
print(["apple", "Mango", "Watermelon"])

#Tuple: the data cannot be modified
print((1,2,3,4,5))
print(("apple", "Mango", "Watermelon"))

#Dictionary
print({
  'name': 'Veno', 'Role': 'Tank', 'Level':100
})
biodata = {"nama":"Andi", 'umur':21} #variable
print(biodata) #proses print from variable
print(type(biodata)) #check the data type

fruits = (("apple", "Mango", "Watermelon"))
print(type(fruits))

number = ([1,2,3,4,5])
print(type(number))