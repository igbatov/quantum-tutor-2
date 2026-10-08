# Figure labels vs text/captions: b-shadow ("cos 30° ≈ 0.866", "sin 30° = 0.5", "0.866² ≈ 0.75",
# "0.5² = 0.25", "0.75 + 0.25 = 1") and b-three-filters (counts 100,0 / 100,50,25; same bar scale).
# Also regenerate both PNGs from their scripts in a temp dir and confirm they match the files on disk.
import os, re, tempfile, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.image as mpimg
here = os.path.dirname(os.path.abspath(__file__)); figs = os.path.join(here, "..", "figures")
ok = True
cv, sh = np.cos(np.radians(30)), np.sin(np.radians(30))
labels = {"cos30 label 0.866": abs(cv-0.866) < 5e-4, "sin30 label 0.5": abs(sh-0.5) < 1e-12,
          "0.866^2 ~ 0.75": abs(0.866**2-0.75) < 5e-3, "cos30^2 = 0.75": abs(cv**2-0.75) < 1e-12,
          "0.75+0.25=1": abs(cv**2+sh**2-1) < 1e-12}
print(labels); ok &= all(labels.values())
def chain(fs):
    n, s, out = 100.0, 0, [100.0]
    for a in fs: n *= np.cos(np.radians(a-s))**2; s = a; out.append(n)
    return np.round(out, 9)
r1, r2 = chain([90]), chain([45, 90]); print("row1", r1, "row2", r2)
ok &= np.allclose(r1, [100, 0]) and np.allclose(r2, [100, 50, 25])
txt = open(os.path.join(here, "..", "final-B.md")).read()
ok &= "from 0 to 25" in txt and "0.75 to get through, 0.25 to be blocked" in txt
tmp = tempfile.mkdtemp(dir=here)  # temp dir inside the run folder, removed at end
for name in ["b-shadow", "b-three-filters"]:
    src = open(os.path.join(here, f"fig_{name}.py")).read()
    src = re.sub(r'out = os\.path\.join\(here, "\.\.", "figures", "[^"]+"\)', f'out = {os.path.join(tmp, name + ".png")!r}', src)
    exec(compile(src, name, "exec"), {"__file__": os.path.join(here, f"fig_{name}.py"), "__name__": "__main__"})
    a, b = mpimg.imread(os.path.join(tmp, name + ".png")), mpimg.imread(os.path.join(figs, name + ".png"))
    same = a.shape == b.shape and np.max(np.abs(a-b)) < 1e-6
    print(name, "on disk", b.shape, "regenerated identical:", same); ok &= same
import shutil; shutil.rmtree(tmp)
print("PASS" if ok else "FAIL")
