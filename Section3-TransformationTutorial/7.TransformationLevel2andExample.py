import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 
import matplotlib.transforms as transforms

""" fig, ax=plt.subplots()
x=np.random.randn(1000)
ax.hist(x,30)
ax.set_title(r'$\sigma=1 \/ \dots\/sigma=2$',fontsize=16)
trans=transforms.blended_transform_factory(ax.transData,ax.transAxes) 
rect=mpatches.Rectangle((1,0),width=1,height=1,transform=trans,color='yellow',alpha=0.5)
ax.add_patch(rect)
plt.show() """


""" fig, ax=plt.subplots(figsize=(5,4))
x,y=10*np.random.rand(2,1000)
ax.plot(x,y*10.,'go',alpha=0.2)
circ=mpatches.Circle((2.5,2),1.0,transform=fig.dpi_scale_trans,facecolor='blue',alpha=0.75)
ax.add_patch(circ)
plt.show() """


""" fig, ax=plt.subplots(figsize=(7,2))
x,y=10*np.random.rand(2,1000)
ax.plot(x,y*10.,'go',alpha=0.2)
circ=mpatches.Circle((2.5,2),1.0,transform=fig.dpi_scale_trans,facecolor='blue',alpha=0.75)
ax.add_patch(circ)
plt.show() """


""" fig, ax=plt.subplots()
xdata, ydata = (0.2,0.7),(0.5,0.5)
ax.set_xlim((0,1))
trans=(fig.dpi_scale_trans+
        transforms.ScaledTranslation(xdata[0],ydata[0],ax.transData))
circle=mpatches.Ellipse((0,0),150/72,130/72,angle=40,fill=None,transform=trans)
ax.add_patch(circle)
plt.show() """


fig, ax=plt.subplots()
x=np.arange(0.,2.,0.01)
y=np.sin(2*np.pi*x)
line,=ax.plot(x,y,lw=3,color='blue')
dx,dy=2/72.,-2/72.
offset = transforms.ScaledTranslation(dx,dy,fig.dpi_scale_trans)
shadow_transform=ax.transData+offset
ax.plot(x,y,lw=3,color='gray',transform=shadow_transform,zorder=0.5*line.get_zorder())
ax.set_title('Creating a shadow effect with and offset transform')
plt.show()