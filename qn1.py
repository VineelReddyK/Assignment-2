import numpy as np
#generating 15 random integers from 1 to 20
a=np.random.randint(1,20,(15))
print('15 random numbers from 1 to 20 : ',a)

#Reshape the array to 3 by 5
b=a.reshape(3,5)
print('array is : \n',b)

#Print array shape
print('shape of the array is ',np.shape(b))

#Replace the max in each row by 0
maxNum = np.amax(b, axis=1)
print('maximum vakues in each row :', maxNum)

d = np.where(np.isin(b,maxNum), 0, b)
print('replacing 0 with maximum value in each row :\n',d)