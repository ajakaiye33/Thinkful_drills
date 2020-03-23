import numpy as np
x1 = np.arange(10, 50, 5)
x2 = np.arange(20, 60, 5)
y = np.arange(100, 500, 50)
# assume we want to predict x1a = 15 and x2b = 4
# write a function that uses K-nearest algorithm/distance formular where k = 4


def knn(prd1, prd2):
    cheky = []
    predy = np.sqrt((x1 - prd1)**2 + (x2 - prd2)**2)
    for i, b in zip(predy, y):
        cheky.append([i, b][1])
    print(sum(sorted(cheky[:4])))


print(knn(15, 4))
