import numpy as np # to install the numpy package
'''a=[5,7,9,11,15]
a=np.array(a)  # to call the array of homogenous items listed
print(a)
print(a.dtype) # to know the data type in array
print(type(a))
b=np.array(a,dtype='int32') # to represent the array of items in int32 format
print(b.dtype)
b=np.array(a,dtype='int64') # to represent the array of items in int64 format
print(b.dtype)
b=np.array(a,dtype='str') # to represent the array of items in string format
print(b.dtype)
b=np.array(a,dtype='float') #to represent the array of items in floating number format
print(b.dtype)
print(a.ndim) # to know the n dimension of provided array of items
print(a.shape) # To get the shape(in case of number the total elements in array) of data
print(a.size)''' # to get the size,i.e, total number of elements

'''c=['cat','mat','hat','bat','rat']
c=np.array(c)
print(c)
print(c.ndim)
print(c.size)
print(c.shape)
print(c.dtype)
print(type(c))
c=np.array(c,dtype='str')
print(c)'''

'''array_2d=np.array([(10,15,20),(50,60,70),(90,80,100)],dtype='int64') # for a list of tuples in array have to mention the datatype be int32/int64/string/float to be called for print
# the main thing is have to write the sequence in correct format,specification of datatype is execptional
print(array_2d)
print(array_2d.dtype)
print(type(array_2d))
print(array_2d.ndim) # provides the dimension of array
print(array_2d.shape) # gives the shape; 1st total arrays=3(here),then number of elements in arrays=3(here)
print(array_2d.size) # total number of elements'''

'''float_dta=np.array([(2.6,5),(7.8,3),(1,5.5),(11,12.0),(6.2,6.5)])
print(float_dta)
print(float_dta.ndim)
print(float_dta.dtype)
print(float_dta.shape)
print(float_dta.size)
print(type(float_dta))'''

complex=np.array([[3,5],[5,4],[9,8]],dtype='complex')
print(complex) # make the array of elements in complex format
print(type(complex))
print(complex.dtype)
print(complex.itemsize)
print(complex.data)

'''seq=np.arange(7) # make the array  of items in an order
print(seq)
seq=np.arange(0,51,10)# provide 1st & last number and the equal division of arrangement
print(seq)
seq=np.arange(20,30)
print(seq)

line_space=np.linspace(0,5,10) # 2 end points with specified number of in between values equally
print(line_space)

from numpy import pi # call pi function

res=np.linspace(0,pi*5,2)
print(res)
sine_val=np.sin(res) # sine values for specified numbers
print('\nSine Value:\n',sine_val)'''


'''print(complex.shape)
resh=complex.reshape(3,3)
print(resh)
print(resh.shape)

a= np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(a.shape)

b=a.reshape(12,1) # reshape a into another order
print(b)
print(b.shape) # reshaped 'a',by specifying columns and rows

c=b.reshape(resh.shape[0],4) # to reshape b with elements of array 'resh'
print(c)'''

'''sqr=np.sqrt(np.array([a])) # to find square root of list
print(sqr)
sqr=np.sqrt(np.array([1,2,3])) # find square root of specific numbers
print(sqr)'''

'''init=np.zeros([2,4]) # 2 times init 4 zeroes
print(init)

ones=np.ones([3,5]) # 3 times ones for 5; 3 rows and 5 columns
print(ones)'''

'''oneD=np.ravel(a) # can convert a one dimensional array to multidimension by flattened it using 'ravel' function
print(oneD)
print(oneD.shape)

print('Min. Value:',a.min())
print('Max Value:',a.max())'''

'''print(a)
row_sum=a.sum(axis=0)
print('Sum of Row:',row_sum)
col_sum=a.sum(axis=1)
print('Sum of Column:',col_sum)'''

'''a=np.array([2,4,6])
b=np.array([5,10,15])
print('\nSum=',a+b)
print('Difference=',a-b)
print('Product=',a*b)
print('Division=',a/b)
print('Dot Product=',a.dot(b))
print('Dot Product=',b.dot(a))
print(a.dot(b))'''

'''sqr=np.sqrt(np.array([1,2,3]))
print(sqr)
print(np.std(sqr))'''# to know standard deviation of group elements

'''a=np.arange(11) # indexing starts from 0,1,2...11; so altogether number list from 0-10
print(a)
print(a[3])
print(a[0:6])
print(a[10])
print(a[-10])
print(a[-3])'''

b=np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(b)
print(b.shape)
print(b[0,2])
print(b[2,0])
print(b[:,2])
print(b[2,:])
print(b[:1,:])
print(b[0,:])
print(b[:,0])
print(b[:,:])
print(b[:-2,0])
print(b[0,:-2])
print(b[:1,:2])
print(b[:2,:3]) # 2 rows include 3 columns
print(b[:4,:3])
print(b[:-2,:-1])