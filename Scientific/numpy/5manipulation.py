import numpy as np

a = np.array(([1,2,3],
              [4,5,6]))

print('matrix a dengan ukuran:', a.shape)
print(a)

#transposematrix
print('transpose matrix dari a:')
print(a.transpose())
# print(np.transpose(a))
# print(a.T)

#flatten array, vector baris
print('flatten matrix a:')
print(a.ravel())
# print(np.ravel(a))

#reshape matrix
print('reshape matrix a:')
print(a.reshape(3,2))

#resize matrix
print('resize matrix a:')
a.resize(3,2)
print(a)
print('matrix a dengan ukuran:', a.shape)