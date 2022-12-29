import numpy as np
'''array_stats=[[1,2,3],[4,5,-6],[9,8,5]]
print(array_stats)
print(np.min(array_stats))
print(np.min(array_stats,axis=0))
print(np.min(array_stats,axis=1))
array_1D=np.array([1,2,3])
print(array_1D)
array_2D=np.array([[1,2,3],[3,6,7]])
print(array_2D)
anumpy_basic=np.array([1,2,809,"A"])
print(anumpy_basic.itemsize)
array_acc=np.array([[1,2,6],[2,5,7]])
print(array_acc[1,2])
print(array_acc[ :,0:2])'''
#data_from_text=np.genfromtxt('numpy.txt',delimiter=',')
#print(data_from_text)55
#function
def numpy_function(x,y,z):
    return 10*x+y+z
b=np.fromfunction(numpy_function,(3,2,4),dtype=int)
print(b)