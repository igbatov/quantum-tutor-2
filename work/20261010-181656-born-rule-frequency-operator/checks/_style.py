import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
plt.rcParams.update({"font.size":12,"axes.titlesize":12,"axes.labelsize":12,"legend.fontsize":10})
FIG=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures")
def save(fig,name):
    path=os.path.normpath(os.path.join(FIG,name+".png")); fig.savefig(path,dpi=150,bbox_inches="tight"); print("saved",path, os.path.exists(path))
