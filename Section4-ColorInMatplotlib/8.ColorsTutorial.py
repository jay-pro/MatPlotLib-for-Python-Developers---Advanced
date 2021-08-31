""" import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 

th=np.linspace(0,2*np.pi,128)
def demo(sty):
    mpl.style.use(sty)
    fig,ax=plt.subplots(figsize=(3,3))
    ax.set_title('style: {!r}'.format(sty),color='C0')
    ax.plot(th,np.cos(th),'C1',label='C1')
    ax.plot(th,np.sin(th),'C2',label='C2')
    ax.legend()
demo('default')
demo('seaborn')
plt.show() """

import numpy as np
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch 
import matplotlib.pyplot as plt
overlap = {name for name in mcd.CSS4_COLORS
            if "xkcd:" + name in mcd.XKCD_COLORS}
fig = plt.figure(figsize=[4.8,16])
ax = fig.add_axes([0,0,1,1])
for j,n in enumerate(sorted(overlap, reverse=True)):
    weight = None
    cn=mcd.CSS4_COLORS[n]
    xkcd=mcd.XKCD_COLORS["xkcd:" + n].upper()
    if cn == xkcd:
        weight = 'bold'
    r1=mpatch.Rectangle((0.j),1,1,color=cn)
    r2=mpatch.Rectangle((1,j),1,1,color=xkcd)
    txt=ax.text(2,j+.5,''+n,va='center',fontsize=10,weight=weight)
    ax.add_patch(r1)
    ax.add_patch(r2)
    ax.axhline(j,color='k')
ax.text(.5,j+1.5,'x11',ha='center',va='center')
ax.text(1.5,j+1.5,'xkcd',ha='center',va='center')
ax.set_xlim(0,3)
ax.set_ylim(0,j+2)
plt.show()

