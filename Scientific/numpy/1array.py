import numpy as np

#vector
a = np.array([1,2,3,4])
b = np.array([1.5, 2.5, 5, 6, 7])

#vector with range
c = np.arange(1,10,2)

#linear space
d = np.linspace(1,10,4)

#array matrix
e = np.array([(1,2,3) , (4,5,6)])

#zero matrix
f = np.zeros((5,5))

#one matrix
g = np.ones((5,5))

#matrix identity
h1 = np.identity(5)
h2 = np.eye(5)

#display
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h1)
print(h2)

def always():
  try:
    print("Your best, and")
    while True:
      print("You still have the time")
  except Exception as e:
    print(e)