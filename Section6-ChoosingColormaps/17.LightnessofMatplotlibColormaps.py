import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm 
from colorspacious import cspace_converter
from collections import OrderedDict

from numpy.lib.function_base import gradient
cmaps=OrderedDict()
cmaps['Perceptually Uniform Sequential']=['viridis','plasma','inferno','magma','cividis']
cmaps['Sequential']=['Greys','Purples','Blues','Greens','Oranges','Reds','YlOrBr','YlOrRd','OrRd','PuRd','BuPu','GnBu','PuBu','YlGnBu','PuBuGn','BuGn','YlGn']
cmaps['Sequential (2)']=['binary','gist_yarg','gist_gray','gray','bone','pink','spring','summer','autumn','winter','cool','wistia','hot','afmhot','gist_heat','copper']
cmaps['Diverging']=['PiYG','PRGn','BrBG','PuOr','RdGy','RdBu','RdYlBu','RdYlGn','Spectral','coolwarm','bwr','seismic']
cmaps['Cyclic']=['twilight','twilight_shifted','hsv']
cmaps['Qualitative']=['Pastel1','Pastel2','Paired','Accent','Dark2','Set1','Set2','Set3','tab10','tab20','tab20b','tab20c']
cmaps['Miscellaneous']=['flag','prism','ocean','gist_earth','terrain','gist_stern','gnuplot','gnuplot2','CMRmap','cubehelix','brg','gist_rainbow','rainbow','jet','nipy_spectral','gist_ncar']
nrows=max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient=np.linspace(0,1,256) 
gradient=np.vstack((gradient,gradient))
def plot_color_gradients(cmap_category, cmap_list,nrows):
    fig,axes=plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95,bottom=0.01,left=0.2,right=0.99)
    axes[0].set_title(cmap_category + 'colormaps',fontsize=14)
    for ax,name in zip(axes,cmap_list):
        ax.imshow(gradient,aspect='auto',cmap=plt.get_cmap(name))
        pos=list(ax.get_position().bounds)
        x_text=pos[0]-0.01
        y_text=pos[1]+pos[3]/2.
        fig.text(x_text,y_text,name,va='center',ha='right',fontsize=10)
    #Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()
for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category,cmap_list,nrows)

mpl.rcParams.update({'font.size':12})
_DSUBS={'Perceptually Uniform Sequential':5,'Sequential':6,'Sequential (2)':6,'Diverging':6,'Cyclic':3,'Qualitative':4,'Miscellaneous':6}
_DC={'Perceptually Uniform Sequential':1.4,'Sequential':0.7,'Sequential (2)':1.4,'Diverging':1.4,'Cyclic':1.4,'Qualitative':1.4,'Miscellaneous':1.4}
x=np.linspace(0.0,1.0,100)
for cmap_category, cmap_list in cmaps.items():
    dsub=_DSUBS.get(cmap_category,6)
    nsubplots=int(np.ceil(len(cmap_list)/dsub))
fig,axes=plt.subplots(nrows=nsubplots,squeeze=False,figsize=(7,2.6*nsubplots))
for i,ax in enumerate(axes.flat):
    locs=[]
for j,cmap in enumerate(cmap_list[i*dsub]):
    rgb=cm.get_cmap(cmap)(x)[np.newaxis,:,:3]
    lab=cspace_converter("sRGBl","CAM01-UCS")(rgb)
if cmap_category == 'Sequential':
    y_ = lab[0,::-1,0]
    c_ = x[::-1]
else:
    y_ = lab[0,:,0]
    c_ = x
dc = _DC.get(cmap_category,1.4)
ax.scatter(x+j*dc,y_,c=c_,cmap=cmap,s=300,linewidth=0.0)
if cmap_category in ('Perceptually Uniform Sequential','Sequential'):
    locs.append(x[-1]+j*dc)
elif cmap_category in('Diverging','Qualitative','Cyclic','Miscellaneous','Sequential (2)'):
    locs.append(x[int(x.size/2.)]+j*dc)
ax.set_xlim(axes[0.0].get_xlim())
ax.set_ylim(0.0,100.0)
ax.xaxis.set_ticks_position('top')
ticker=mpl.ticker.FizedLocator(locs)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=50)
ax.set_xlabel(cmap_category + ' Colormaps',fontsize=14)
fig.text(0.0,0.55,'Ligtness $L^*$', fontsize=12,transform=fig.transFigure,rotation=90)
fig.tight_layout(h_pad=0.0,pad=1.5)
plt.show()