import matplotlib.pyplot as plt
import matplotlib as mpl 

""" fig, ax=plt.subplots(figsize=(6,1))
fig.subplots_adjust(bottom=0.5)
cmap=mpl.cm.cool 
norm=mpl.colors.Normalize(vmin=5,vmax=10)
cbl=mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm, orientation='horizontal')
cbl.set_label('some units')
fig.show() """


""" fig, ax=plt.subplots(figsize=(6,1))
fig.subplots_adjust(bottom=0.5)
cmap=mpl.cm.colors.ListedColormap(['red','green','blue','cyan'])
cmap.set_over('0.25')
cmap.set_under('0.75')
bound=[1,2,4,7,8]
norm=mpl.colors.BoundaryNorm(bound,cmap.N)
cb2=mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm,boundaries=[0]+bound+[13],exten='both',tick=bound,spacing='propotional',orientation='horizontal')
fig.show() """


""" fig, ax=plt.subplots(figsize=(6,1))
fig.subplots_adjust(bottom=0.5)
cmap=mpl.cm.colors.ListedColormap(['royalblue','cyan','yellow','orange'])
cmap.set_over('red')
cmap.set_under('blue')
bound=[-1.0,-0.5,0.0,0.5,1.0]
norm=mpl.colors.BoundaryNorm(bound,cmap.N)
cb3=mpl.colorbar.ColorbarBase(ax,cmap=cmap,norm=norm,boundaries=[-10]+bound+[10],exten='both',extenfrac='auto',ticks=bound,spacing='uniform',orientation='horizontal')
cb3.set_label('custom extension lengths, some other units')
fig.show() """


