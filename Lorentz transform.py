import numpy as np
import matplotlib.pyplot as plt
x=None # length for unmoving reference frame, if not given, write none
t=5 # time for unmoving reference frame, if not given, write none
y=0 #length
z=0 #length
xp= 0 #xprime, if not given, write none
tp= None #tprime,if not given, write none
yp=y#doesn't get transformed because all motion is on the x axis for this class
zp=z#doesn't get transformed because all motion is on the x axis for this class
c=1 #length per time, make sure that you write something here
v=0.6 #length per time,if not given, write none
if v==None:
    if x!=None and t!=None:
        v=x/t#from dx/dt
    elif xp!=None and tp!=None:
        v=xp/tp #from dx/dt
B=v/c
gamma=1/np.sqrt(1-B**2)

if xp==None and tp==None: #to find the x and x' or t and t' if one isn't given
    tp=gamma*(t-B*x/c)#the basic t' lorentz transformation given by the class eq sheet
    xp=gamma*(x-B*t*c)#the basic x' lorentz transformation given by the class eq sheet
elif x==None and t==None:
    t=gamma*(tp+B*xp/c)#the basic t inverse lorentz transformation given by the class eq sheet
    x=gamma*(xp+B*tp*c)#the basic x inverse lorentz transformation given by the class eq sheet
elif t==None and xp==None:
    t=(tp*gamma+(B*x*gamma*gamma))/(c*(1+(B*gamma)**2))#found by isolating t after turning x' in terms of x and t
    xp=gamma*(x-B*t*c)#the basic x' lorentz transformation given by the class eq sheet
elif x==None and tp==None:
    x=(xp*gamma+(B*t*gamma*gamma))/((1+(B*gamma)**2))#found by isolating x after turning x' in terms of x and t
    tp=gamma*(t-B*x/c) #the basic t' lorentz transformation given by the class eq sheet
else:
    print("you either have all the information that you need, or not enough information, just use a normal calculator and look at your inputs or the problem again")
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
plt.xlabel("ΔX")
plt.ylabel("cΔt")
if I>0:#for timelike
    a=np.linspace(-(x+4),(x+4))#this is sort of 
    b= np.sqrt(a**2+I) 
    f=plt.plot(a,b)
    plt.plot([0, X], [0, y1], 'go-', label=' world line 1', linewidth=2)
    plt.plot([0, xp], [0, y2], 'b-', label=' world line 2', linewidth=2,)
    plt.plot(0,0,'ko',label='Point A'); plt.legend();
    plt.plot(X,y1,'ro',label='Point B in S'); plt.legend();
    plt.plot(xp,y2,'co',label="Point B in S'"); plt.legend();
else:#for spacelike and lightlike
    b=np.linspace(-(x+4),(x+4))
    a= np.sqrt(b**2-I)
    f=plt.plot(a,b)
    plt.plot([0, X], [0, y1], 'go-', label=' world line 1', linewidth=2)
    plt.plot([0, np.sqrt((-I))], [0, 0], 'b-', label=' world line 2', linewidth=2,)
    plt.plot(0,0,'ko',label='Point A'); plt.legend();
    plt.plot(X,y1,'ro',label='Point B in S'); plt.legend();
    plt.plot(np.sqrt((-I)),0,'co',label="Point B in S'"); plt.legend();
plt.grid()
plt.show()
