# Check-yourself claim: "ladder had only three rungs, how many different colors ... at most"
# Answer intended: 3 (pairs 3->2, 3->1, 2->1); verify distinct for hydrogen-like and generic ladder
from itertools import combinations
import numpy as np
pairs = list(combinations([1,2,3],2))
E = {n:-13.6/n**2 for n in [1,2,3]}
gaps = sorted(round(E[j]-E[i],6) for i,j in pairs)
print("pairs", pairs, "gaps eV", gaps)
print("PASS" if len(pairs)==3 and len(set(gaps))==3 else "FAIL")
