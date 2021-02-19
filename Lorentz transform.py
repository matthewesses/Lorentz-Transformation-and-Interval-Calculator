import numpy as np
x=2.4*10**8 #meters for moving reference frame
t=1 #seconds for moving reference frame
y=0 #meters
z=0 #meters
xp= None #xprime
tp= None #tprime
yp=y
zp=z
c=3*10**8 #meters per second
v=None #meters per second
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
I=x**2+(c*t)**2+y**2+z**2 #the value for the interval

#prints the values
print("Distance x: ",x,"meters")
print("Time t:", t,"seconds")
print("Velocity is", v, "meters/second")
print("Beta is",B)
print("Gamma is", gamma)
print("The interval is", I, "meters squared")
print("Distance x': ",xp,"meters")
print("Time t':", tp,"seconds")
