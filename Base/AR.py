import numpy as np



def AR(T, rho, rank = 1):
    P = np.zeros((T, T))
    for i in range(T):
        for j in range(i - rank, i):
            if i >= 0 and j >= 0:
                P[i, j] = 1
    return np.linalg.inv(np.eye(T) - rho * P)
