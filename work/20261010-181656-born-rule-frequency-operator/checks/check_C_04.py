# Claims: N=4,p=0.8: "1 + 4 + 6 = 11 of the 16 ... weight 0.0016 + 0.0256 + 0.1536 = 0.181";
# N=20: "by number 0.588 ... by weight about 0.0026, count peaking at m = 10 (0.176), weight at m = 16 (0.218)"
import math
from scipy.stats import binom
ok=True
cnt=sum(math.comb(4,m) for m in range(3)); ws=[math.comb(4,m)*0.8**m*0.2**(4-m) for m in range(3)]
print("N=4 count",cnt,"weights",[round(x,4) for x in ws],"total",sum(ws))
ok&= cnt==11 and abs(sum(ws)-0.1808)<1e-9 and all(abs(a-b)<1e-9 for a,b in zip(ws,[.0016,.0256,.1536]))
num=sum(math.comb(20,m) for m in range(11))/2**20; wt=binom.cdf(10,20,0.8)
share=[math.comb(20,m)/2**20 for m in range(21)]; wm=[binom.pmf(m,20,0.8) for m in range(21)]
print("N=20 share by number m<=10",num,"weight",wt)
print("count peak m",share.index(max(share)),max(share),"weight peak m",wm.index(max(wm)),max(wm))
ok&= abs(num-0.588)<5e-4 and abs(wt-0.0026)<1e-4 and share.index(max(share))==10 and abs(max(share)-0.176)<5e-4 and wm.index(max(wm))==16 and abs(max(wm)-0.218)<5e-4
# "By number, most branches see a frequency near 1/2 whatever p is": share by number within 0.05 of 1/2 for large N
for N in [20,100,1000]:
    m=range(N+1); s=sum(math.comb(N,k) for k in m if abs(k/N-0.5)<=0.05)/2**N; print(" N",N,"share by number within 0.05 of 1/2:",round(s,4))
# Check-yourself answer (N=4, p=0.9) for notes
print("Check-yourself: weight m<=2 at p=0.9:",binom.cdf(2,4,0.9),"fraction",11/16)
print("PASS" if ok else "FAIL")
