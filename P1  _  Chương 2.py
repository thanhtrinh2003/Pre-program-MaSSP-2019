import numpy as np
import matplotlib.pyplot as plt

A = np.linspace(-2, 2)
B3 = 3-A
B2 = 2-A
B1 = 1-A
B0 = -A
B_3 = -3-A
B_2 = -2-A
B_1 = -1-A
d0 = A*0
d1 = A
    
plt.subplot(2,2,1)
plt.plot(A, B3, 'r-')
plt.plot(A, B2, 'r-')
plt.plot(A, B1, 'y-')
plt.plot(A, B0, 'g-')
plt.plot(A, B_3, 'b-')
plt.plot(A, B_2, 'm-')
plt.plot(A, B_1, 'c-')
plt.plot(A, d0, 'k-')
plt.plot(d0, A, 'k-')
plt.ylabel("b")
plt.xlabel("a")
plt.grid()
plt.axis([-2, 2, -2, 2])
plt.title("y=ax+b;x=1")
a1=-2
while a1<=2 :
    b1=1-a1
    plt.plot(a1,b1,'yo')
    a1=a1+0.2
b2=-2
while b2<=2 :
    a2=(b2**2)/2-1
    plt.plot(a2,b2,'bo')
    b2=b2+0.2
plt.show()

plt.subplot(2,2,2)
a1=-2
while a1<=2 :
    b1=1-a1
    x1= np.linspace(-2,2)
    y1= a1*x1+b1
    plt.plot(x1,y1,'y-')
    a1=a1+0.2
b2=-2
while b2<=2 :
    a2=(b2**2)/2-1
    x2= np.linspace(-2,2)
    y2= a2*x2+b2
    plt.plot(x2,y2,'b-')
    b2=b2+0.2
plt.axis([-2, 2, -2, 2])
plt.title("y=ax+b")
plt.show()




