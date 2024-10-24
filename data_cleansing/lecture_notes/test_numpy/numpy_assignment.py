import numpy as np
import math
arr = np.array([[1.2, 1.4, 1.6, 1.8],
       [2.3, 2.5, 2.7, 2.9],
       [3.4, 3.6, 3.8, 4. ]], dtype=np.float32)

print(arr)

print(type(arr))

print(arr.shape)

print(arr.dtype)

''''''
arr1= [1.2, 1.4, 1.6, 1.8]
arr2=[2.3, 2.5, 2.7, 2.9]
arr3=[3.4, 3.6, 3.8, 4. ]

sq_arr1=(math.sqrt(i) for i in arr1)
sq_arr2=(math.sqrt(i) for i in arr2)
sq_arr3=(math.sqrt(i ) for i in arr3)
arr_sqrt=np.vstack((arr1,arr2,arr3))
print(arr_sqrt)
''''''

arr_sqrt=np.sqrt(arr)
print(arr_sqrt)

arr2
