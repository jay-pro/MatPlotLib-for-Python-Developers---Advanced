import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

""" verts = [(0.,0.),(0.,1.),(1.,1.),(1.,0.),(0.,0.)]
codes=[Path.MOVETO,
       Path.LINETO,
       Path.LINETO,
       Path.LINETO,
       Path.CLOSEPOLY,]
path=Path(verts,codes)
fig, ax = plt.subplots()
patch=patches.PathPatch(path, facecolor = 'orange',lw=2)
ax.add_patch(patch)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2) 
plt.show()"""

verts = [(0.,0.),(0.2,1.),(1.,0.8),(0.8,0.)]
codes=[Path.MOVETO,
       Path.CURVE4,
       Path.CURVE4,
       Path.CURVE4,]
path=Path(verts,codes)
fig, ax = plt.subplots()
patch=patches.PathPatch(path, facecolor = 'none',lw=2)
ax.add_patch(patch)
xs, ys = zip(*verts)
ax.plot(xs,ys,'x--',lw=2,color='black',ms=10)
ax.text(-0.05,-0.05,'PO')
ax.text(0.15,1.05,'P1')
ax.text(1.05,0.85,'P2')
ax.text(0.85,-0.05,'P3')
ax.set_xlim(-0.1,1.1)
ax.set_ylim(-0.1,1.1)
plt.show()