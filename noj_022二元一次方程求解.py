def quadratic_equation(a1, b1, c1, a2, b2, c2):
    # 行列式求解二元一次方程组
    q = a1*b2 - a2*b1
    q1 = b2*c1 - b1*c2
    q2 = a1*c2 - a2*c1
    if q == 0:
        print('error')
    else:
        print("{:.3f} {:.3f}".format(q1/q, q2/q))

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
quadratic_equation(a, b, c, d, e, f)


# import numpy as np
# def quadratic_equation(a, b, c, d, e, f):
#     # 行列式求解二元一次方程组
#     q1 = np.matrix([[c, b], [f, e]])
#     q2 = np.matrix([[a, c], [d, f]])
#     q = np.matrix([[a, b], [d, e]])
#     if np.linalg.det(q) == 0:
#         print('error')
#     else:
#         print("{:.3f} {:.3f}".format(np.linalg.det(q1)/np.linalg.det(q), np.linalg.det(q2)/np.linalg.det(q)))
#