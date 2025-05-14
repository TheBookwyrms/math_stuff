import numpy as np


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[4, 3, 5],
              [7, 8, 9],
              [1, 6, 2]])

prediction = np.array([[1*4+2*7+3*1, 1*3+2*8+3*6, 1*5+2*9+3*2],
                       [4*4+5*7+6*1, 4*3+5*8+6*6, 4*5+5*9+6*2],
                       [7*4+8*7+9*1, 7*3+8*8+9*6, 7*5+8*9+9*2]])

c = a@b

#print(a)
#print(b)
#print(a+b)
#print(c)
#print(c/prediction)



m = np.array([
        [1,2,3],
        [5,7,11],
    ])

print(m, m.shape, m.T.shape)
mte = np.array([
    [1,   1],
    [0,  1],
    [0,  -1],
])
print(mte)
print(m@mte)
#print(m@(np.linalg.inv(m)))

mt = m.T
m_left_inverse = mt @ np.linalg.inv(m@mt)
print(m_left_inverse)
print(m@m_left_inverse)

#print(n, n.shape, n.T.shape)
#print(m@n)
#print(n@m)
#print(m@(m.T))
#print(n@(n.T))
#print(m@(m.T)@np.eye(2))
#print(n@(n.T)@np.eye(3))