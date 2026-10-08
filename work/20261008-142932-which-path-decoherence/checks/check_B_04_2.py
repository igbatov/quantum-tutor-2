# Captions: b-dust-grain "solid curve runs about 9% below the dashed line", "dips to about 0.87 event times
# near Δx ≈ 0.7λ before settling at 1"; b-pairs-of-routes "levels off at exp(−number of scatterings): about
# 0.37 after one scattering time", "dips to about 0.32 near Δx ≈ 0.7λ", "effectively 0 after ten or a hundred",
# "narrows as 1/√(number of scatterings)".
import numpy as np
r = np.logspace(-2, 1, 6000); lam = np.linspace(0.7, 1.3, 2001)
om = np.mean(1-np.sinc(2*r[:, None]/lam[None, :]), axis=1)          # smoothed 1 - overlap
tf = 1/om; ref = 6/(2*np.pi)**2/r**2
below = 1 - tf[0]/ref[0]
big = r > 0.5; i = np.argmin(np.where(big, tf, np.inf))
print(f"dust: curve below dashed by {below:.1%} at Δx/λ=0.01; dip {tf[i]:.3f} event times at Δx/λ={r[i]:.2f}; at Δx/λ=10: {tf[-1]:.3f}")
f1 = np.exp(-om); j = np.argmin(f1)
print(f"pairs N=1: plateau (Δx/λ 3..10) {f1[r>3].mean():.3f} (1/e = {np.exp(-1):.3f}); dip {f1[j]:.3f} at Δx/λ={r[j]:.2f}")
f10, f100 = np.exp(-10*om), np.exp(-100*om)
print(f"N=10 max for Δx/λ>0.5: {f10[big].max():.1e}; N=100: {f100[big].max():.1e}")
def width(N): return r[np.argmin(abs(np.exp(-N*om)-np.exp(-1)))]
w = [width(N) for N in (1, 10, 100)]
print(f"1/e widths: {w[0]:.3f}, {w[1]:.4f}, {w[2]:.4f}; ratio 10→100: {w[1]/w[2]:.3f} (√10 = 3.162)")
ok = abs(below-0.09)<0.01 and abs(tf[i]-0.87)<0.01 and 0.6<r[i]<0.8 and abs(f1[r>3].mean()-0.37)<0.01 \
     and abs(f1[j]-0.32)<0.01 and 0.6<r[j]<0.8 and f10[big].max()<1e-3 and abs(w[1]/w[2]-np.sqrt(10))<0.1
print("PASS" if ok else "FAIL")
