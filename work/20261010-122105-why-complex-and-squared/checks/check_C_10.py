# Claim: "So with two exits a non-power rule survives everything the sorters measure, up to their error bars."
# Test: a sorter (polarizing splitter) rotated to any angle measures Malus's law; compare f with cos^2.
import numpy as np
ang=np.radians(np.linspace(0,90,9001)); x=np.cos(ang)
g=(1-x**2)*(2*x**2-1)
for eps in (0.8,0.1,0.01):
    dev=eps*x**2*g; i=np.argmax(abs(dev))
    print(f"eps={eps}: max |f - cos^2| = {abs(dev).max():.4f} at {np.degrees(ang[i]):.1f} deg; at 30 deg: {eps*0.75*0.25*0.5:.4f}")
print("At the table's settings (x^2 = 0, 1/2, 1) f equals cos^2 exactly:", [float(v) for v in (0,0.5*(1+0),1)])
print("FAIL as written if 'the sorters' includes a splitter at other angles: Malus's law at 30 deg differs by 0.094*eps;")
print("true statement: it survives the two-exit total and reproduces the 0/50/100 table; intermediate-angle Malus data only bound eps.")
print("FAIL")
