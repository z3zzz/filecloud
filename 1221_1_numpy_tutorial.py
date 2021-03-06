# -*- coding: utf-8 -*-
"""실습1_Numpy_Tutorial (1221).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTMWQXrcLrnRy8U8U5NdkTlZOaUXDNiA

<p style="font-family: Arial; font-size:3.75em;color:black; font-style:bold"><br>
Numpy Tutorial
</p><br>


Reference: https://github.com/susanli2016/Machine-Learning-with-Python

핵심 내용:

- ndarrays: 계산의 편의를 위해 numpy에 내장되어있는 ndarray를 이용하는 함수
- Broadcasting: 사이즈가 다른 ndarray들의 계산을 위해서 numpy에 내장되어 있는 자동처리 함수 
- Input/Output: 파일 입출력.

조교
- 이정수 (KAIST AI 석사과정): bebeto@kaist.ac.kr
- 이상현 (KAIST AI 박사과정): shlee6825@kaist.ac.kr

<p style="font-family: Arial; font-size:3em;color:black; font-style:bold"><br>
Ndarray
</p><br>
"""

import numpy as np                 # numpy를 np로 작성하는 것이 convention
array_1d = np.array([3, 33, 333])  
print(type(array_1d))

# array의 shape 확인
print(array_1d.shape)

# array의 각 element 확인
print(array_1d[0], array_1d[1], array_1d[2])

# array의 첫번째 element를 바꾸기 
array_1d[0] =888            
print(array_1d)

array_2d = np.array([[11,12,13],
                     [21,22,23]])   

print(array_2d)

print("현재 array의 shape: ", array_2d.shape)                     
print("[0,0], [0,1], [1,0]의 값 확인: ", array_2d[0, 0], ", ",array_2d[0, 1],", ", array_2d[1, 0])

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Numpy의 내장함수로 지정된 값으로 ndarray 만들기
</p><br>

- argument는 size를 넣어주는 것이 기본
"""

import numpy as np

# zero vector 만들기 
zero_array = np.zeros((2,2))      
print(zero_array)

# 값을 지정하여서 해당 값으로 채워진 ndarray 만들기 

full_array = np.full((2,2), 9.0)  # 1st argument: ndarray shape / 2nd argument: value 
print(full_array)

# 대각선이 1로 구성된 ndrray 만들기 
eye_array = np.eye(2,2)
print(eye_array)

# 1로만 구성된 ndarray 만들기 
one_array = np.ones((1,2))
print(one_array)

# 0~! 사이의 임의의 실수로 구성된 ndarray 만들기 
random_array = np.random.random((2,2))
print(random_array)

# 범위를 지정하여서 ndarray를 생성
# argument: (start), stop, (step). ()는 default가 0 / stop 미만의 수까지 
# np.arange: https://github.com/TreB1eN/InsightFace_Pytorch/blob/master/model.py, Line 276


arange_array = np.arange(3)
print(arange_array)

arange_array2 = np.arange(3,7)
print(arange_array2)

arange_array3 = np.arange(3,7,2)
print(arange_array3)

arange_array4 = np.arange(3,8,2)
print(arange_array4)

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Array Indexing
</p><br>
"""

import numpy as np

array = np.array([[11,12,13,14],
                     [21,22,23,24],
                     [31,32,33,34]])
print(array)

# 특정 row와 column만을 indexing
slice_array = array[:2, 1:3] # [row, column]
print(slice_array)

slice_array = array[2:, 2:4] # [row, column]
print(slice_array)

slice_array = array[:, 2:4] # [row, column]
print(slice_array)

slice_array = array[1:3, :] # [row, column]
print(slice_array)

# row와 column의 indexing ndarray를 생성
col_indices = np.array([0, 1, 1])
print('\nCol indices picked : ', col_indices)

row_indices = np.arange(3)
print('\nRows indices picked : ', row_indices)

# 변화될 element의 row, col을 확인하기 위해 print
# zip 함수는 python 내장함수로써 짝을 지어주는 역할
for row,col in zip(row_indices,col_indices):
    print(row, ", ",col)

print('이전 Array:')
print(array)
array[row_indices, col_indices] += 100000
print()
print('이후 Array:')
print(array)

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Boolean Indexing
</p><br>
"""

# create a 3x2 array
array = np.array([[11, 12], 
                  [21, 22], 
                  [31, 32]])
print(array)

# 우리가 원하는 조건에 맞춰서 ndarray를 재구성 
# 기존 array와 같은 크기의 Boolean value로 구성된 ndarray 생성
condition = (array > 15)
print(condition)

# 실제 해당 값을 가진 ndarray를 출력 -> 1d array로 출력됨 
print(array[condition])

# 기존 shape을 유지하되 조건에 맞지 않는 값은 0으로 대체하고 싶은 경우 
# np.where 함수 사용 (condition, array, 대체 값)
# np.where: https://github.com/kakaoenterprise/Learning-Debiased-Disentangled/blob/master/learner.py, Line 528

print(np.where(array>15, array, 0))

# condition에 해당하는 값을 직접 변경
array[(array>15)] +=100
print(array)

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Datatypes
</p><br>
Data type: https://engineer-mole.tistory.com/85

"""

ex1 = np.array([11, 12]) 
print(ex1.dtype)

ex2 = np.array([11.0, 12.0]) 
print(ex2.dtype)

ex3 = np.array([11, 21], dtype=np.int32) 
print(ex3.dtype)

# 실수를 정수 형태로 변경
ex4 = np.array([11.1,12.7], dtype=np.int64)
print(ex4.dtype)
print()
print(ex4)

# 정수를 실수 형태로 변경
ex5 = np.array([11, 21], dtype=np.float64)
print(ex5.dtype)
print()
print(ex5)

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Arithmetic Array Operation
</p><br>
"""

x = np.array([[111,112],[121,122]], dtype=np.int)
y = np.array([[211.1,212.1],[221.1,222.1]], dtype=np.float64)

print(x)
print()
print(y)

# add
print(x + y)         
print()
print(np.add(x, y))

# subtract
print(x - y)
print()
print(np.subtract(x, y))

# multiply
print(x * y)
print()
print(np.multiply(x, y))

# divide
print(x / y)
print()
print(np.divide(x, y))

# square root
print(np.sqrt(x))

# exponent (e ** x)
print(np.exp(x))

# 두 행렬의 내적
x2d = np.array([[1,1],[1,1]])
y2d = np.array([[2,2],[2,2]])
print(x2d)
print(y2d)

print(x2d.dot(y2d))
print(np.dot(x2d, y2d))

# 두 벡터의 내적
a1d = np.array([9 , 9 ])
b1d = np.array([10, 10])

print(a1d)
print(b1d)

print(a1d.dot(b1d))
print(np.dot(a1d, b1d))

# 행렬과 벡터의 내적
print(x2d)
print(a1d)
print()
print(x2d.dot(a1d))
print(np.dot(x2d, a1d))

# sum
ex1 = np.array([[11,12],[21,22]])
print(ex1)

print(np.sum(ex1))          # add all members

print(np.sum(ex1, axis=0))  # columnwise sum

print(np.sum(ex1, axis=1))  # rowwise sum

# random array
x = np.random.randn(8)
print(x)

# another random array
y = np.random.randn(8)
print(y)

# returns element wise maximum between two arrays
print(np.maximum(x, y))

# reshaping array
arr = np.arange(20)
print(arr)

# reshape to be a 4 x 5 matrix
print(arr.reshape(4,5))

# Transpose
ex1 = np.array([[11,12],[21,22]])
print(ex1)
print(ex1.T)

# where로 indexing
x_1 = np.array([1,2,3,4,5])
y_1 = np.array([11,22,33,44,55])
condition = np.array([True, False, True, False, True])

out = np.where(condition, x_1, y_1)
print(out)

mat = np.random.rand(5,5)
print(mat)
print(np.where( mat > 0.5, 1000, -1))
print(np.where( mat > 0.5, mat, -1))

# any/all condition
arr_bools = np.array([ True, False, True, True, False ])
print(arr_bools.any()) # True가 하나라도 있으면 True
print(arr_bools.all()) # 전부 True여야 True

# 임의의 수 생성
Y = np.random.normal(size = (3,5))
print(Y)

Z = np.random.randint(low=2,high=50,size=4)
print(Z)

print(np.random.permutation(Z))  #return a new ordering of elements in Z
print(np.random.uniform(size=4)) #uniform distribution
print(np.random.normal(size=4))  #normal distribution

# ndarray 합치기 
K = np.random.randint(low=2,high=50,size=(2,2))
print(K)

print()
M = np.random.randint(low=2,high=50,size=(2,2))
print(M)

print(np.vstack((K,M)))                   # col-wise로 stack 
print(np.hstack((K,M)))                   # row-wise로 stack
print(np.concatenate([K, M], axis = 0))   # col-wise로 stack
print(np.concatenate([K, M.T], axis = 1)) # row-wise로 stack

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Statistical Methods
<br><br>
</p>
"""

# (2,4)의 임의의 실수로 구성된 행렬
arr = 10 * np.random.randn(2,5)
print(arr)

# 모든 수의 평균
print(arr.mean())

# 행으로 평균 구하기
print(arr.mean(axis = 1))

# 열로 평균 구하기
print(arr.mean(axis = 0))

# 모든 수의 합
print(arr.sum())

# 행으로 중앙값 구하기
print(np.median(arr, axis = 1))

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Sorting
<br><br>
</p>
"""

# 임의의 1d-array 생성
unsorted_array = np.random.randn(10)
print(unsorted_array)

# ndarray 복사 후 sorting 진행
sorted_array = np.array(unsorted_array)
sorted_array.sort()

print('이전 unsorted:', unsorted_array)
print()
print('이후 sorted:', sorted_array)

array = np.array([1,2,1,4,2,1,4,2])

print(np.unique(array))

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Set Operations
<br><br>
</p>
"""

s1 = np.array(['desk','chair','bulb'])
s2 = np.array(['lamp','bulb','chair'])
print(s1, s2)

print( np.intersect1d(s1, s2) ) # 교집합

print( np.union1d(s1, s2) ) # 합집합

print( np.setdiff1d(s1, s2) ) # s1-s2

print(np.in1d(s1, s2)) # s1에 s1과 s2 공통적으로 있는 element가 있는지에 대한 boolean ndarray

"""<p style="font-family: Arial; font-size:3em;color:black; font-style:bold"><br>
Broadcasting
<br><br>
</p>
"""

import numpy as np

# original array 생성
original_array = np.zeros((4,3))
print(original_array)

# 더할 ndarray
add_rows = np.array([1, 0, 2])
print(add_rows)

# original array에 add_rows를 더함
''' 
original array (4,3)과 add_rows (3,)의 shape이 다름
-> numpy의 broadcasting이 (3,)을 자동적으로 (4,3)으로 변형후 덧셈을 진행
'''
result = original_array + add_rows  
print(result)

# 행단위가 아닌 열단위로도 진행
add_cols = np.array([[0,1,2,3]])
add_cols = add_cols.T

print(add_cols)

result = original_array + add_cols 
print(result)

add_scalar = np.array([1])  
print(original_array+add_scalar)

"""Example from the slides:"""

# 3x4 matrix
arrA = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])
print(arrA)

# 4x1 array
arrB = [0,1,0,2]
print(arrB)

# 두 행렬의 덧셈
print(arrA + arrB)

"""<p style="font-family: Arial; font-size:3em;color:black; font-style:bold"><br>
파일 입출력
<br><br>
</p>

<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Binary format
<br><br>
</p>
"""

x = np.array([ 23.23, 24.24] )

import os
os.makedirs('./data', exist_ok=True) # data라는 폴더 생성

np.save('./data/array.npy', x)

np.load('./data/array.npy')

"""<p style="font-family: Arial; font-size:2em;color:black; font-style:bold"><br>
Text format
<br><br>
</p>
"""

np.savetxt('./data/array.txt', X=x, delimiter=',')

np.loadtxt('./data/array.txt', delimiter=',')