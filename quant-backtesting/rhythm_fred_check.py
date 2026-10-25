#!/usr/bin/env python3
"""Rhythm check on the cached FRED series: which "cycles" survive a family-wise significance test,
plus direct calendar folds (VIX by weekday, core PCE by month of quarter / January).

Run:  python3 quant-backtesting/rhythm_fred_check.py _ingest/raw/2026-10-04/data/fred
"""
import sys, numpy as np, csv, datetime as dt
from scipy.signal import periodogram, welch
from scipy.stats import chi2
D=sys.argv[1]
def load(n):
    t,v=[],[]
    for r in csv.DictReader(open(f"{D}/{n}.csv")):
        try: v.append(float(r[n])); t.append(dt.date.fromisoformat(r['observation_date']))
        except: pass
    return np.array(t),np.array(v)
def fw(label,x,unit):
    x=x-x.mean(); f,p=periodogram(x,detrend='linear',window='hann'); f,p=f[1:],p[1:]
    # smooth-background null: local median of neighbouring bins (robust to red/any colour)
    from scipy.ndimage import median_filter
    bg=median_filter(p,size=max(9,len(p)//40),mode='nearest')/np.log(2)
    N=len(p); thr=chi2.ppf(1-0.01/N,2)/2   # family-wise 1% across all N frequencies
    s=p/bg/thr; i=np.argsort(s)[::-1][:3]
    print(f"{label}: "+"; ".join(f"{1/f[k]:.1f} {unit} -> {s[k]:.2f}{' *' if s[k]>1 else ''}" for k in i))
fred=D
t,v=load('PCEPILFE'); m=np.diff(np.log(v))*1200; tt=t[1:]
fw("Core PCE m/m (all)",m,"mo"); sel=np.array([d.year>=1990 for d in tt]); fw("Core PCE m/m 1990+",m[sel],"mo")
for lo,hi in [(1959,1989),(1990,2009),(2010,2026)]:
    s=np.array([lo<=d.year<=hi for d in tt]); mm=m[s]; mo=np.array([d.month for d in tt[s]])
    q=[round(mm[(mo-1)%3==k].mean()-mm.mean(),2) for k in range(3)]
    print(f"   {lo}-{hi} month-of-quarter deviation (ann. %pts):",q, " Jan dev:",round(mm[mo==1].mean()-mm.mean(),2))
t,v=load('VIXCLS'); dl=np.diff(np.log(v)); fw("VIX daily log chg",dl,"td")
wd=np.array([d.weekday() for d in t[1:]])
for lo,hi in [(1990,2007),(2008,2026)]:
    s=np.array([lo<=d.year<=hi for d in t[1:]]); print(f"   VIX {lo}-{hi} weekday mean %:",[round(dl[s&(wd==k)].mean()*100,2) for k in range(5)])
t,v=load('NFCI'); fw("NFCI weekly level",v,"wk"); fw("NFCI weekly change",np.diff(v),"wk")
t,v=load('MORTGAGE30US'); fw("Mortgage weekly chg",np.diff(v),"wk")
t,v=load('FEDFUNDS'); fw("Fed funds monthly chg",np.diff(v),"mo"); fw("Fed funds level",v,"mo")
t,v=load('T10Y3M'); fw("10y-3m daily chg",np.diff(v),"td")
t,v=load('BAA10Y'); fw("Baa-10y spread daily chg",np.diff(v),"td")
