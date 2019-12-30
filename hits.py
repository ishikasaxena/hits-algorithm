import numpy as np
import math

# Hyperlink Induced Topic Search Given an Adjacency Matrix 
# for a web graph
def hits(A):
    hubVectorLst = []
    transpose = np.transpose(A)
    n = len(A[0]) 
    for i in range(n):
        hubVectorLst.append(1)
    hubVector = np.array(hubVectorLst)
    authorityVector = np.dot(transpose, hubVector)
    hubVector = np.dot(A, authorityVector)
    print("Hub Vector: ", hubVector)
    print("Authority Vector: ", authorityVector)

A = [[0, 1, 1, 1],
     [1, 1, 1, 0],
     [0, 0, 1, 1],
     [0, 0, 1, 0]]

B = [[0, 0, 1],
     [0, 0, 1],
     [0, 0, 0]]

print("HITS Algorithm on ", A)
hits(A)
print("\nHITS Algorithm on ", B)
hits(B)