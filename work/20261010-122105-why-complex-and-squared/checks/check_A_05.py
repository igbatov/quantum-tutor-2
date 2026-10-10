# Claims (d): "a detector in arm 1 ... counts half the photons, tilting does not change that";
# "Block arm 2: each exit now receives one quarter"; rules-out table: chances only gives
# "1/4 + 1/4 = 1/2 at every tilt, yet at phi=pi it gets nothing"; balls give "50/50 at every tilt".
import numpy as np
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
ok = True
for phi in np.linspace(0, 4*np.pi, 97):
    z = np.exp(1j*phi); P = np.diag([z, 1])
    arms = P @ H @ np.array([1, 0])
    ok &= abs(abs(arms[0])**2 - 0.5) < 1e-12
    b2 = H @ np.array([arms[0], 0]); b1 = H @ np.array([0, arms[1]])
    ok &= np.allclose(abs(b2)**2, [0.25, 0.25]) and np.allclose(abs(b1)**2, [0.25, 0.25])
    ok &= np.allclose(b2, [z/2, z/2])
    full = H @ arms
    chances_only = abs(b1[0])**2 + abs(b2[0])**2
    ok &= abs(chances_only - 0.5) < 1e-12
z = np.exp(1j*np.pi); full = H @ np.diag([z, 1]) @ H @ np.array([1, 0])
ok &= abs(full[0])**2 < 1e-12
# balls: random 50/50 at each splitter, delay irrelevant
ball_exit1 = 0.5*0.5 + 0.5*0.5
ok &= ball_exit1 == 0.5
# check-yourself answer: phi=0, arm 2 blocked -> exit 1 gets 1/4
print('arm1 count 1/2, blocked 1/4 each, chances-only 1/2, QM exit1 at pi =', round(abs(full[0])**2, 15), ', balls', ball_exit1)
print('PASS' if ok else 'FAIL')
