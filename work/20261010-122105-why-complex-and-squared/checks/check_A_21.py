# Figure request a-pnorm-circles: arc on the real (x, y) plane from (1,0) to (0,1) labelled
# "the interferometer's family U(phi), phi from 0 to pi". Test: is U(phi)(1,0) a real point
# (cos t, sin t)? Or only its sizes (|u|, |v|)?
import numpy as np
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
worst_mod = 0; on_real_arc = True
for p in np.linspace(0.1, np.pi-0.1, 50):
    u, v = H @ np.diag([np.exp(1j*p), 1]) @ H @ [1, 0]
    worst_mod = max(worst_mod, abs(abs(u)-np.cos(p/2)), abs(abs(v)-np.sin(p/2)))
    # is there a global phase making both components real?
    r = np.array([u, v])*np.exp(-1j*np.angle(u))
    on_real_arc &= abs(r[1].imag) < 1e-9
print('sizes (|u|,|v|) = (cos phi/2, sin phi/2): max dev', worst_mod)
print('U(phi)(1,0) equals a real point (cos t, sin t) up to overall phase:', on_real_arc,
      '| e.g. phi=pi/2:', np.round(H @ np.diag([1j, 1]) @ H @ [1, 0], 3))
print('FAIL (label as written): the real-plane arc is the rotation family R(phi/2); U(phi) traces it only in sizes'
      if worst_mod < 1e-12 and not on_real_arc else 'PASS')
