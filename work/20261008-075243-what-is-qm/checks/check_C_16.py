# Check-yourself question: "If an atom's ladder had only three rungs, how many different colours"
# Expected answer: 3 (drops 3->2, 3->1, 2->1), distinct for generic or hydrogen-like spacing
from itertools import combinations
E = [-13.6/n**2 for n in (1, 2, 3)]
gaps = sorted({round(E[j]-E[i], 6) for i, j in combinations(range(3), 2)})
print("distinct gaps:", gaps, "count", len(gaps))
print("PASS" if len(gaps) == 3 else "FAIL")
