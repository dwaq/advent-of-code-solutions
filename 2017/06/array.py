import numpy as np

a = np.array([1, 2, 3])
l = len(a)
b = np.array([4, 5, 6])
data = np.vstack([a,b])

c = np.array([1, 2, 3])

data2 = np.vstack([data,c])


print set(a) == set(b)
print set(a) == set(c)

x=0
y=1

while(x<len(data2)):
    while(y<len(data2)):
        print data2[x], data2[y], set(data2[x]) == set(data2[y])
        y=y+1
    x=x+1