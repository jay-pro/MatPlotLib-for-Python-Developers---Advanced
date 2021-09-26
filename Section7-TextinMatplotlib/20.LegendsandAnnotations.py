import matplotlib
import matplotlib.pyplot as plt

fig=plt.figure()
fig.suptitle('bold figure subtitle',fontsize=14,fontweight='bold')
ax=fig.add_subplot(111)
ax=fig.subplots_adjust(top=0.85)
ax.set_titlle('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.text(3,8,'boxed italics text in data coords',style='italic',bbox={'facecolor':'red','alpha':0.5,'pad':10})
ax.text(2,6,r'an equation: $E=mc^2$',fontsize=15)
ax.text(3,2,'unicode: Institu fur Festkorperphysik')
ax.text(0.95,0.01,'colored text in axes coords',
        verticalalignment='bottom',horizontalalignment='right',
        transform=ax.transAxes, color='green',fontsize=15)
ax.plot([2],[1],'o')
ax.annotate('annotate',xy=(2,1),xytext=(3,4),
            arrowprops=dict(facecolor='black',shrink=0.05))
ax.axis([0,10,0,10])
plt.show()

import numpy as np
x1=np.linspace(0.0,5.0,100)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
fig,ax=plt.subplots(figsize=(5,3))
fig.subplots_adjust(bottom=0.15,left=0.2)
ax.plot(x1,y1)
ax.set_xlabel('time[s]')
ax.set_ylabel('Damped oscillation[V]')
plt.show()

fig,ax=plt.subplots(figsize=(5,3))
fig.subplots_adjust(bottom=0.15,left=0.2)
ax.plot(x1,y1)
ax.set_xlabel('time[s]')
ax.set_ylabel('Damped oscillation[V]')
plt.show()

from matplotlib.font_manager import FontProperties
font=FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_style('italic')
fig,ax=plt.subplots(figsize=(5,3))
fig.subplots_adjust(bottom=0.15,left=0.2)
ax.plot(x1,y1)
ax.set_xlabel('time[s]',fontsize='large',fontweight='bold')
ax.set_ylabel('Damped oscillation[V]',fontproperties=font)
plt.show()

2:32 (video 20)