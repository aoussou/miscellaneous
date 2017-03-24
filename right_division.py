''' 

right-matrix division operator

solves the equation x*A = b

in MATLAB/Octave mrdivide(a,b) or a/b (forward slash)

'''


import numpy as np

def rdiv(A,B):
    
    return np.transpose(np.linalg.solve(np.transpose(A),np.transpose(B)))  