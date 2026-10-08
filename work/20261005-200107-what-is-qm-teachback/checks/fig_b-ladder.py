import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy.constants import physical_constants
plt.rcParams['font.size'] = 11
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'b-ladder.png')
RH = physical_constants['Rydberg constant'][0]/(1+physical_constants['electron-proton mass ratio'][0])
lam = {n: 1e9/(RH*(1/4-1/n**2))/1.000277 for n in (3, 4, 5, 6)}  # air wavelengths, nm
E = {n: -13.6/n**2 for n in range(1, 7)}

def wl_rgb(w):
    if w < 440: r, g, b = -(w-440)/60, 0, 1
    elif w < 490: r, g, b = 0, (w-440)/50, 1
    elif w < 510: r, g, b = 0, 1, -(w-510)/20
    elif w < 580: r, g, b = (w-510)/70, 1, 0
    elif w < 645: r, g, b = 1, -(w-645)/65, 0
    else: r, g, b = 1, 0, 0
    f = 0.3+0.7*(w-380)/40 if w < 420 else (0.3+0.7*(700-w)/55 if w > 645 else 1)
    return (max(r, 0)*f, max(g, 0)*f, max(b, 0)*f)

names = {3: 'red', 4: 'blue-green', 5: 'blue-violet', 6: 'violet'}
fig = plt.figure(figsize=(7, 7.5))
ax = fig.add_axes([0.12, 0.36, 0.55, 0.6])
for n, en in E.items():
    ax.hlines(en, 0, 1, color='black', lw=1.8)
    ylab = {3: -2.3, 4: -1.1, 5: 0.1, 6: 1.3}.get(n, en)  # spread crowded labels
    ax.annotate(f'level {n}' + (' (lowest)' if n == 1 else ''), xy=(1.0, en), xytext=(1.08, ylab),
                va='center', fontsize=10, annotation_clip=False,
                arrowprops=dict(arrowstyle='-', color='gray', lw=0.7) if n in (3, 4, 5, 6) else None)
ax.hlines(0, 0, 1, color='black', lw=1.2, linestyles='dashed')
ax.text(0.5, 0.25, 'electron set free (energy 0)', ha='center', va='bottom', fontsize=10)
xs = {3: 0.15, 4: 0.37, 5: 0.59, 6: 0.81}
for n in (3, 4, 5, 6):
    c = wl_rgb(lam[n])
    ax.annotate('', xy=(xs[n], E[2]), xytext=(xs[n], E[n]),
                arrowprops=dict(arrowstyle='-|>', color=c, lw=2.5, mutation_scale=15))
    ax.text(xs[n]+0.02, (E[2]+E[n])/2 - 0.3, f'{lam[n]:.0f} nm\n{names[n]}', fontsize=8.5, va='center')
ax.text(0.03, -8.5, 'drops to level 1 give ultraviolet light,\ninvisible to us', fontsize=9.5, style='italic')
ax.set_ylim(-14.5, 2.0); ax.set_xlim(0, 1)
ax.set_yticks([]); ax.set_xticks([])
ax.set_ylabel('energy')
for s in ('top', 'right', 'bottom'): ax.spines[s].set_visible(False)
ax.set_title('Hydrogen energy ladder: rungs crowd together toward the top', fontsize=11)
# spectra
wl = np.linspace(380, 700, 800)
rgb = np.array([wl_rgb(w) for w in wl])
ax1 = fig.add_axes([0.12, 0.2, 0.8, 0.07])
ax1.imshow(rgb[np.newaxis, :, :], aspect='auto', extent=[380, 700, 0, 1])
ax1.set_yticks([]); ax1.set_xticks([])
ax1.set_title('glowing hot solid: every color', fontsize=10, loc='left')
ax2 = fig.add_axes([0.12, 0.07, 0.8, 0.07])
ax2.set_facecolor('black'); ax2.set_xlim(380, 700); ax2.set_ylim(0, 1)
for n in (3, 4, 5, 6):
    ax2.axvline(lam[n], color=wl_rgb(lam[n]), lw=3.5)
    ax2.text(lam[n], 1.05, f'{lam[n]:.0f}', ha='center', va='bottom', fontsize=8)
ax2.set_yticks([]); ax2.set_xticks([400, 450, 500, 550, 600, 650, 700])
ax2.set_xlabel('wavelength (nm)')
ax2.set_title('hydrogen gas: only certain colors', fontsize=10, loc='left', pad=14)
fig.savefig(out, dpi=150); print('saved', os.path.abspath(out))
