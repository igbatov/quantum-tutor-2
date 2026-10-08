# Re-run of round-one checks for claims unchanged in final-C.md (shift by same fraction, D lines apart, size,
# 254 nm = 4.9 eV, spiral in ~1e-11 s, no orbiting / pilot-wave at rest, half-waves, ladder crowding,
# 4x energy, balance at Bohr radius, < 1 us lifetimes, many-electron cost, collapse rate, precision, check-yourself).
import subprocess, sys, os
d = os.path.dirname(os.path.abspath(__file__)); ok = True
for i in ['02','03','04','05','06','07','08','09','10','11','12','13','14','15','16']:
    out = subprocess.run([sys.executable, os.path.join(d, f'check_C_{i}.py')], capture_output=True, text=True, timeout=900).stdout.strip().splitlines()
    res = out[-1] if out else 'ERROR'; print(f"check_C_{i}: {res}"); ok &= res == 'PASS'
print("PASS" if ok else "FAIL")
