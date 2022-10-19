import matplotlib.pyplot as pt
import numpy as np
x=np.array([ 22.2, 17.6, 8.8, 8, 7.7, 6.7])
y=['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
z=pt.pie(x,labels=y)
pt.show()