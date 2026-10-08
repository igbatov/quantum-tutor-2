import os, sys, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hcommon_C import vac_nm, air_nm
from scipy import constants as k
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures', 'c-ladder-lines.png')
plt.rcParams.update({'font.size': 10})
def wl_rgb(w):
    # Bruton's approximation, with intensity falloff at the edges
    if w < 380 or w > 750: return (0, 0, 0)
    if w < 440: r, g, b = -(w-440)/60, 0, 1
    elif w < 490: r, g, b = 0, (w-440)/50, 1
    elif w < 510: r, g, b = 0, 1, -(w-510)/20
    elif w < 580: r, g, b = (w-510)/70, 1, 0
    elif w < 645: r, g, b = 1, -(w-645)/65, 0
    else: r, g, b = 1, 0, 0
    f = 0.3+0.7*(w-380)/40 if w < 420 else (0.3+0.7*(750-w)/50 if w > 700 else 1)
    return tuple(min(1, max(0, c*f)) for c in (r, g, b))
Ry = k.physical_constants['Rydberg constant times hc in eV'][0]/(1+k.m_e/k.m_p)
E = {n: -Ry/n**2 for n in range(1, 7)}
fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.5, 5.2), gridspec_kw={'width_ratios': [1, 1.25]})
for n, e in E.items():
    axL.hlines(e, 0, 1, color='k', lw=1.6)
    ylab = {1: e, 2: e, 3: -1.95, 4: -1.15, 5: -0.35, 6: 0.45}[n]
    axL.plot([1.0, 1.08], [e, ylab], color='0.4', lw=0.7)
    axL.text(1.1, ylab, f'rung {n}  ({e:.2f} eV)', va='center', fontsize=8.5)
axL.hlines(0, 0, 1, color='k', lw=1.2, ls='--')
axL.plot([1.0, 1.08], [0, 1.25], color='0.4', lw=0.7)
axL.text(1.1, 1.25, 'electron set free (0 eV)', va='center', fontsize=8.5)
names = {3: 'red', 4: 'blue-green', 5: 'blue-violet', 6: 'violet'}
xs = {3: 0.2, 4: 0.36, 5: 0.52, 6: 0.68}
for n in (3, 4, 5, 6):
    lam = air_nm(vac_nm(n, 2)); c = wl_rgb(lam)
    axL.annotate('', xy=(xs[n], E[2]), xytext=(xs[n], E[n]), arrowprops=dict(arrowstyle='-|>', color=c, lw=2.2, mutation_scale=14))
    axL.text(xs[n], -3.75, f'{lam:.0f} nm {names[n]}', fontsize=8, rotation=90, va='top', ha='center')
lam21 = vac_nm(2, 1)
axL.annotate('', xy=(0.86, E[1]), xytext=(0.86, E[2]), arrowprops=dict(arrowstyle='-|>', color='0.5', lw=2.2, ls='--', mutation_scale=14))
axL.text(0.89, -8.5, f'{lam21:.0f} nm:\nultraviolet,\ninvisible', fontsize=8, ha='left', va='center', color='0.3')
axL.set_xlim(0, 1.85); axL.set_ylim(-14.5, 1.8)
axL.set_xticks([]); axL.set_ylabel('energy (eV)')
axL.set_title('Hydrogen energy ladder (to scale)', fontsize=10.5)
for s in ('top', 'right'): axL.spines[s].set_visible(False)
# right panel: spectra
wl = np.linspace(380, 700, 1200)
rainbow = np.array([wl_rgb(w) for w in wl])[None, :, :]
axR.imshow(np.repeat(rainbow, 20, axis=0), extent=[380, 700, 1.15, 2.0], aspect='auto')
axR.add_patch(plt.Rectangle((380, 0), 320, 0.85, color='black'))
for n in range(3, 10):
    lam = air_nm(vac_nm(n, 2))
    if n <= 6:
        axR.vlines(lam, 0, 0.85, color=wl_rgb(lam), lw=2.5)
        axR.text(lam, -0.08, f'{lam:.0f}', ha='center', va='top', fontsize=8.5)
    else:
        axR.vlines(lam, 0, 0.85, color=(0.35, 0.0, 0.45), lw=1.0, ls=':')
axR.annotate('fainter lines from rungs 7, 8, 9\n(397, 389, 384 nm: near-ultraviolet,\nbarely visible)', xy=(390, 0.5), xytext=(497, 0.45),
             fontsize=7.5, color='white', va='center', arrowprops=dict(arrowstyle='->', color='white', lw=0.8))
axR.text(382, 2.07, 'hot glowing solid (lamp filament): continuous rainbow', fontsize=9, va='bottom')
axR.text(382, 0.92, 'glowing hydrogen: separate bright lines (labelled in nm)', fontsize=9, va='bottom')
axR.set_xlim(380, 700); axR.set_ylim(-0.45, 2.45); axR.set_yticks([])
axR.set_xlabel('wavelength (nm)', labelpad=14)
axR.set_title('Spectra seen through a prism', fontsize=10.5)
fig.suptitle('Each coloured line is one drop between two rungs: separate rungs give separate colours', fontsize=11.5)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(out, dpi=150)
print('saved', os.path.abspath(out))
