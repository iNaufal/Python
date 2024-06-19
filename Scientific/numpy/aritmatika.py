import numpy as np

#list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

#result elementwise operation
hasil1 = a+b
hasil2 = anp+bnp
print(hasil1)
print(hasil2)

hasil3 = anp-bnp
print(hasil3)

hasil4 = anp*bnp
print(hasil4)

hasil5 = anp/bnp
print(hasil5)

hasil6 = anp**2
print(hasil6)

#multidimensi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil7 = c + d
hasil8 = c * d
print(hasil7)
print(hasil8)