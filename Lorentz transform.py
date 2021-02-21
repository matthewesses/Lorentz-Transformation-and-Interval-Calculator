import numpy as np
import matplotlib.pyplot as plt
x=10 # length for unmoving reference frame
t=40 # time for unmoving reference frame
y=0 #meters
z=0 #meters
xp= None #xprime
tp= None #tprime
yp=y
zp=z
c=1 #length per time
v=None #length per time
if v==None:
    if x!=None and t!=None:
        v=x/t
    elif xp!=None and tp!=None:
        v=xp/tp
B=v/c
gamma=1/np.sqrt(1-B**2)

if xp==None and tp==None: #to find the x and x' or t and t' if one isn't given
    tp=gamma*(t-B*x/c)
    xp=gamma*(x-B*t*c)
elif x==None and t==None:
    t=gamma*(tp+B*xp/c)
    x=gamma*(xp+B*tp*c)
elif t==None and xp==None:
    t=(tp*gamma+(B*x*gamma*gamma))/(c*(1+(B*gamma)**2))
    xp=gamma*(x-B*t*c)
elif x==None and tp==None:
    x=(tp*gamma+(B*t*gamma*gamma))/((1+(B*gamma)**2))
    tp=gamma*(t-B*x/c)
I=0-x**2+(c*t)**2-y**2-z**2 #the value for the interval

#prints the values
print("Distance x: ",x)
print("Time t:", t,)
print("Velocity is:", v)
print("Beta is",B)
print("Gamma is", gamma)
print("The interval is", I)
if I<0:
    print("spacelike")
if I>0:
    print("timelike")
elif I==0:
    print("lightike")
print("Distance x' : ",xp,)
print("Time t':", tp)
#plotting the minkowski diagram
X=x
y1= t
y2= tp
a=np.linspace(-(x+4),(x+4))
b= np.sqrt(a**2+I)
f=plt.plot(a,b)
plt.xlabel("ΔX")
plt.ylabel("cΔt")
if I>0:
    plt.plot([0, X], [0, y1], 'go-', label=' world line 1', linewidth=2)
    plt.plot([0, xp], [0, y2], 'b-', label=' world line 2', linewidth=2,)
    plt.plot(0,0,'ko',label='Point A'); plt.legend();
    plt.plot(X,y1,'ro',label='Point B in S'); plt.legend();
    plt.plot(xp,y2,'co',label="Point B in S'"); plt.legend();
else:
    plt.plot([0, X], [0, y1], 'go-', label=' world line 1', linewidth=2)
    plt.plot([0, np.sqrt(I)], [0, 0], 'b-', label=' world line 2', linewidth=2,)
    plt.plot(0,0,'ko',label='Point A'); plt.legend();
    plt.plot(X,y1,'ro',label='Point B in S'); plt.legend();
    plt.plot(np.sqrt(-I),0,'co',label="Point B in S'"); plt.legend();
plt.grid()
plt.show()
