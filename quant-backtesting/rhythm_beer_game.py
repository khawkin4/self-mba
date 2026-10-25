#!/usr/bin/env python3
"""Beer Game in the frequency domain: 4-stage chain, white-noise retail demand.
Prints variance amplification and the frequency band where the bullwhip concentrates, by shipping delay.

Run:  python3 quant-backtesting/rhythm_beer_game.py
"""
import numpy as np
from scipy.signal import welch, csd
rng=np.random.default_rng(1); T=20000
def chain(L,alpha=0.3,beta=0.3,stages=4):
    d=10+rng.normal(0,1,T); flows=[d]; inp=d
    for s in range(stages):
        inv=0.0; pipe=[10.0]*L; fc=10.0; out=np.zeros(T)
        for t in range(T):
            inv+=pipe.pop(0)-inp[t]; fc+=0.2*(inp[t]-fc)
            o=max(0,fc+alpha*(20-inv)+beta*(fc*L-sum(pipe))); pipe.append(o); out[t]=o
        flows.append(out); inp=out
    return flows
for L in (1,2,4):
    f=chain(L); fr,pd=welch(f[0],nperseg=512); _,pf=welch(f[-1],nperseg=512)
    g=pf/pd; k=np.argmax(g[1:])+1
    _,cxy=csd(f[0],f[1],nperseg=512)
    print(f"delay {L}wk: variance ratio factory/retail = {f[-1].var()/f[0].var():6.1f}  peak gain {g[k]:7.1f} at period {1/fr[k]:5.1f} wk")
