import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

""" N=100
X,Y=np.mgrid[0:3:complex(0,N),0:2:complex(0,N)]
Z1 = (1+np.sin(Y*10.))*X**(2.)
fig,ax = plt.subplots(2,1)
pcm = ax[0].pcolormesh(X,Y,Z1,norm = colors.PowerNorm(gamma=0.5),
cmap = 'PuBu_r')
fig.colorbar(pcm,ax=ax[0],extend='max')
pcm=ax[1].pcolormesh(X,Y,Z1,cmap='PuBu_r')
fig.colorbar(pcm,ax=ax[1],extend='max')
fig.show() """


N=100
X,Y=np.mgrid[-3:3:complex(0,N),-2:2:complex(0,N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
Z = (Z1-Z2)*2
fig,ax = plt.subplots(3,1,figsize=(8,8))
ax=ax.flatten()
bounds = np.linspace(-1,1,10)
norm=colors.BoundaryNorm(boundaries=bounds,ncolors=256)
pcm = ax[0].pcolormesh(X,Y,Z,
norm = norm,
cmap = 'RdBu_r')
fig.colorbar(pcm,ax=ax[0],extend='both',orientation='vertical')
bounds = np.array([-0.25,-0.125,0,0.5,1])
norm=colors.BoundaryNorm(boundaries=bounds,ncolors=256)
pcm = ax[1].pcolormesh(X,Y,Z,
norm = norm,
cmap = 'RdBu_r')
fig.colorbar(pcm,ax=ax[1],extend='both',orientation='vertical')
pcm=ax[2].pcolormesh(X,Y,Z,
cmap='RdBu_r',vmin=-np.max(Z))
fig.colorbar(pcm,ax=ax[2],extend='both',orientation='vertical')
fig.show()