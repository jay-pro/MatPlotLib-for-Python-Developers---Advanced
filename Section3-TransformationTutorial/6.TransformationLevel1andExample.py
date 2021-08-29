import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 

""" fig=plt.figure()
for i, label in enumerate(('A','B','C','D')):
    ax=fig.add_subplot(2,2,i+1)
    ax.text(0.05,0.95,label,transform=ax.transAxes,fontsize=16,fontweight='bold',va='top')
plt.show() """


fig, ax = plt.subplots()
x,y=10*np.random.rand(2,1000)
ax.plot(x,y,'go',alpha=0.2)
circ=mpatches.Circle((0.5,0.5),0.25,transform=ax.transAxes,facecolor='blue',alpha=0.75)
ax.add_patch(circ)
plt.show()
