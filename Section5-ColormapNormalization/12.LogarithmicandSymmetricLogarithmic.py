import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

""" N=100
X,Y=np.mgrid[-3:3:complex(0,N),-2:2:complex(0,N)]
Z1 = np.exp(-(X)**2 - (Y)**2)
Z2 = np.exp(-(X*10)**2 - (Y*10)**2)
Z = Z1 + 50+Z2
fig,ax = plt.subplots(2,1)
pcm = ax[0].pcolor(X,Y,Z,
norm = colors.LogNorm(vmin=Z.min(),vmax=Z.max()),
cmap = 'PuBu_r')
fig.colorbar(pcm,ax=ax[0],extend='max')
pcm=ax[1].pcolor(X,Y,Z,cmap='PuBu_r')
fig.colorbar(pcm,ax=ax[1],extend='max')
fig.show() """


N=100
X,Y=np.mgrid[-3:3:complex(0,N),-2:2:complex(0,N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
Z = (Z1-Z2)*2
fig,ax = plt.subplots(2,1)
pcm = ax[0].pcolormesh(X,Y,Z,
norm = colors.SymLogNorm(linthresh=0.03,linscale=0.03,
vmin=-1.0,vmax=1.0),
cmap = 'RdBu_r')
fig.colorbar(pcm,ax=ax[0],extend='both')
pcm=ax[1].pcolormesh(X,Y,Z,cmap='RdBu_r',vmin=-np.max(Z))
fig.colorbar(pcm,ax=ax[1],extend='both')
fig.show()