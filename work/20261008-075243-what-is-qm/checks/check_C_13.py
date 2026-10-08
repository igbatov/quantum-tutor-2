# Claim: "for many electrons the pattern lives in a space with three dimensions per electron, so beyond a few electrons exact computation is impractical"
# Illustration: storing psi on a modest grid of 20 points per coordinate
for N in (1, 2, 3, 4, 6, 10):
    pts = 20**(3*N)
    print(f"N={N}: {3*N} dims, {pts:.1e} grid values, {pts*8/1e9:.1e} GB")
ok = 20**(3*4)*8/1e9 > 1e5   # 4 electrons already > 100 TB at coarse resolution
print("PASS" if ok else "FAIL")
