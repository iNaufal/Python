import numpy as np

a = np.array(([1,2,3],[3,4,5]), dtype = float)

#create matrix with function
def kuadrat(baris,kolom):
  return kolom**2

def jumlah(baris,kolom):
  return (kolom + baris)

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)

#create array or matrix with iterable
i = (x*2 for x in range(5))
d = np.fromiter(i, dtype = int)

#multitype array
dtipe = [('name','S255'), ('height', int)]
data = [
  ('veno', 170),
  ('mare', 168),
  ('ven', 175)
]
e = np.array(data, dtype = dtipe)

print(a)
print(b)
print(c)
print(d)
print(e)
print(e[0])