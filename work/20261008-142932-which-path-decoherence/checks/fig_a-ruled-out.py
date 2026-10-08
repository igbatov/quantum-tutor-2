import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-ruled-out.png"
rows = [["a kick blurs the stripes*", "no stripes only when the\ntag pushes hard enough", "1998 atoms: push ~100,000 times\ntoo weak, stripes gone"],
        ["someone must read the record", "stripes until it is read", "1998 atoms, 2002 photons (b):\nnobody reads anything, stripes gone"],
        ["the tag smudges the wave", "smudged for good", "2002 (c): stripes inside\neach sorted group"],
        ["one slit, and the tag reports it", "no stripes in any subset", "2002 (c): stripes in the\n+45° and −45° groups"]]
fig, ax = plt.subplots(figsize=(9, 4.2)); ax.axis("off")
t = ax.table(cellText=rows, colLabels=["the picture", "what it predicts", "what was seen (which kills it)"], loc="center", cellLoc="left", colWidths=[0.3, 0.3, 0.4])
t.auto_set_font_size(False); t.set_fontsize(9.5); t.scale(1, 2.6)
for (r, c), cell in t.get_celld().items():
    if r == 0: cell.set_text_props(weight="bold"); cell.set_facecolor("#dddddd")
ax.set_title("Four pictures, and the observation that rules each out")
fig.text(0.02, 0.03, "*For records made by bouncing something off the particle the kick picture gives the right numbers; it fails only for kick-free tags.", fontsize=8.5)
fig.tight_layout(); fig.savefig(OUT, dpi=150); print(OUT)
