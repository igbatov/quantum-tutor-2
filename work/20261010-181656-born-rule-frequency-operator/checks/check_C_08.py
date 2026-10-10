# Claims: "standard deviation of the frequency is sqrt(p(1-p)/N), the same expression as the floor of Model 2's parabola"
# and Model 2 Pros: "finite-N floor p(1-p)/N is the same expression as the measured 1/sqrt N scatter"
import sympy as sp
p,N=sp.symbols('p N',positive=True)
floor=p*(1-p)/N; sd=sp.sqrt(p*(1-p)/N)
same=sp.simplify(floor-sd)==0
print("floor",floor,"SD",sd,"equal?",same,"; floor == SD^2?",sp.simplify(floor-sd**2)==0)
print("numeric N=100 p=0.8: floor",float(floor.subs({p:0.8,N:100})),"SD",float(sd.subs({p:0.8,N:100})))
print("PASS" if same else "FAIL")
