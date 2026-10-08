# Claims: "field is much stronger near one pole"; "pushes ... along the line from one pole to the other";
# "bands join at their ends, where the field is weaker"
# Model: knife-edge pole tip ~ 2D line source at origin, beam slit at height z0 below, long along x.
import numpy as np
ok=True
z0=1.0
def Bmag(x,z): return 1/np.hypot(x,z)          # |B| ~ 1/r near the sharp edge
def dBdz(x,z,h=1e-6): return (Bmag(x,z+h)-Bmag(x,z-h))/(2*h)
def dBdx(x,z,h=1e-6): return (Bmag(x+h,z)-Bmag(x-h,z))/(2*h)
# stronger near knife edge (z small) than far (toward groove pole at z=3)
print("|B| near edge (z=0.5):",Bmag(0,0.5)," near other pole (z=3):",Bmag(0,3)); ok&=Bmag(0,.5)>3*Bmag(0,3)
# force on beam centre along z only
print("grad at x=0: dB/dx=",round(dBdx(0,z0),6)," dB/dz=",round(dBdz(0,z0),4)); ok&=abs(dBdx(0,z0))<1e-6
xs=np.array([0,0.5,1,2,3])
for x in xs: print(f"x={x}: |B|={Bmag(x,z0):.3f}  |dB/dz|={abs(dBdz(x,z0)):.3f}")
ok &= np.all(np.diff(Bmag(xs,z0))<0) and np.all(np.diff(abs(dBdz(xs,z0)))<0)
print("splitting (prop. to gradient) shrinks toward slit ends -> bands join; field magnitude also falls there")
print("PASS" if ok else "FAIL")
