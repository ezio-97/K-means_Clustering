from scipy.io import loadmat
from matplotlib import pyplot as plt
import numpy as np

data = loadmat('data.mat')
X = [[element for element in upperElement] for upperElement in data['X']]

X = np.array(X)
x_1 = [X[i][0] for i in range(len(X))]
x_2 = [X[i][1] for i in range(len(X))]

#plot data

plt.scatter(x_1, x_2)
plt.show()



C = np.array([[2.0 ,3.0], [6.0,2.0], [8.0,5.0]])

def Closest_centroid(X, C):
    idx = []
    for i in range(len(X)):
        temp = np.zeros((3,1))

        for j in range(len(C)):
            temp[j] = np.sqrt(np.sum(np.square(X[i] - C[j])))

        temp = temp.tolist()
        index_value = temp.index(min(temp))

        idx.append(index_value)
    return np.array(idx)

def Compute_Centroids(C, idx):

    for i in range (len(C)):
        ls = []
        lk=[]
        for j in range(len(X)):
            if idx[j] == i:
                ls.append(X[j][0])
                lk.append(X[j][1])
        ls=np.array(ls)
        lk=np.array(lk)
        C[i] = [np.mean(ls), np.mean(lk)]

    return C

def Iterate(n):
    for i in range(n):
        x=Closest_centroid(X, C)
        Compute_Centroids(C,x)
    print('new_centroids', C)

    c_1 = [C[i][0] for i in range(len(C))]
    c_2 = [C[i][1] for i in range(len(C))]

    # plot data

    plt.scatter(c_1, c_2, marker='x')
    plt.show()

n = 10
Iterate(n)


