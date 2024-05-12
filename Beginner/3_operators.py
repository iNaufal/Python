#Arithmetic Operators
print("Arithmetic Operators")
#Penjumlahan
print(20 + 6)
apple = 7
orange = 11
fruits = apple + orange #with variable
print(fruits)

#Pengurangan
budget = 20000
spend = 15000
remaining = budget - spend
print("Remaining:", remaining)

#Perkalian
panjang = 20
lebar = 5
luas = panjang * lebar
print(luas)

#Pembagian
gift = 20
child = 5
gpc = gift / child
print("Gift per child:", gpc)

#Modulus
number1 = 15
number2 = 10
results = number1 % number2
print("the results from number1", number1, "and", number2, "is", results)

#Pangkat
number3 = 10
number4 = 2
results2 = number3 ** number4
print(results2)

#Pembagian Bulat
print(20//3)

#Assignment Operators in variables
print("\nAssignment Operators")
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x %= 3
print(x)
print("and more: //= , **=, &=, |=, ^=, >>=, <<=, :=")


#Comparison Operators
print("\nComparison Operators")
print(1 == 1)
print(1 == 2)
print(2 != 2)
print(2 != 3)
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)

#Logical Operators
print("\nLogical Operators")
x = 5
print(x > 6 and x < 10) #kedua logic harus sesuai

x = 5
print(x > 3 or x < 4) #salah 1 logic harus sesuai

x = 5
print(not(x > 3 and x < 10))

#Identity Operators
print("\nIdentity Operators")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)

x = ["apple", "banana"]
y = ["apple", "watermelon"]
z = x
print(x is not z)

#Membership Operators
print("\nMembership Operators")
x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("banana" not in x)

#Bitwise Operators
print("\nBitwise Operators")
print(5&5)
print(5|3)
print(5^3)
print(~5)
print(5<<3)
print(5>>3)