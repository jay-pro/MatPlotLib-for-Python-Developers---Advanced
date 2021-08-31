import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm 
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from collections import OrderedDict

virdis=cm.get_cmap('viridis',12)
print(virdis)
print(virdis(0.56))
print('viridis.colors',virdis.colors)
print('viridis(range(12))',virdis(range(12)))
print('viridis(np.linspace(0,1,12))',virdis(np.linspace(0,1,12)))
print('viridis(np.linspace(0,1,15))',virdis(np.linspace(0,1,15)))
viridis=cm.get_cmap('viridis',256)
newcolors=viridis(np.linspace(0,1,256))
pink=np.array([248/256,24/256,148/256,1])
newcolors[:25,:]=pink
newcmp=ListedColormap(newcolors)
def plot_examples(cms):
    np.random.seed(19680801)
    data=np.random.randn(30,30)
    fig,axs=plt.subplots(1,2,figsize=(6,3),constrained_layout=True)
    for[ax, cmap]in zip(axs,cms):
        psm=ax.pcolormesh(data,cmap,rasterized=True,vmin=4,vmax=4)
        fig.colorbar(psm,ax=ax)
    plt.show()
""" plot_examples([viridis,newcmp]) """

""" viridisBig=cm.get_cmap('viridis',512)
newcmp=ListedColormap(viridisBig(np.linspace(0.25,0.75,256)))
plot_examples([viridis,newcmp]) """

""" top=cm.get_cmap('Orange',128)
bottom=cm.get_cmap('Blues',128)
newcolors=np.vstack((top(np.linspace(0,1,128)),bottom(np.linspace(0,1,128))))
newcmp=ListedColormap(newcolors,name='OrangeBlue')
plot_examples([viridis,newcmp]) """

""" N=256
vals=np.ones((N,4))
vals[:,0]=np.linspace(90/256,1,N)
vals[:,1]=np.linspace(39/256,1,N)
vals[:,2]=np.linspace(41/256,1,N)
newcmp=ListedColormap(vals)
plot_examples([viridis,newcmp]) """

cdict={'red':[[0.0,0.0,0.0],
                [0.5,1.0,1.0],
                [1.0,1.0,1.0]],
    'green':[[0.0,0.0,0.0],
            [0.25,0.0,0.0],
            [1.0,1.0,1.0]],
    'blue':[[0.0,0.0,0.0],
            [0.5,0.0,0.0],
            [1.0,1.0,1.0]]}
def plot_linearmap(cdict):
    newcmp=LinearSegmentedColormap('testCmap',segmenteddata=cdict,N=256)
    rgba=newcmp(np.linspace(0,1,256))
    fig,ax=plt.subplots(figsize=(4,3),constrained_layout=True)
    col=['r','g','b']
    for xx in [0.25,0.5,0.75]:
        ax.axvline(xx,color='0.7',linearstyle='--')
    for i in range(3):
        ax.plot(np.arange(256)/256,rgba[:,i],color=col[i])
    ax.set_xlabel('index')
    ax.set_ylabel('RGB')
    plt.show()
plot_linearmap(cdict)