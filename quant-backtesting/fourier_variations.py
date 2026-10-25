#!/usr/bin/env python3
"""
Stress-test the Fourier pricing demo: vary one thing at a time and see what moves.

  A. Model behaviour   — what each Heston/jump parameter does to the volatility smile
  B. Maturity          — why stochastic vol alone can't produce short-dated skew, and jumps can
  C. Numerics          — when the Fourier methods and Monte Carlo break, and how to tell
  D. Another asset class — credit portfolio losses with the same multiply-the-fingerprints trick

Run:  python3 quant-backtesting/fourier_variations.py
"""
import time
import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

import fourier_pricing_demo as fp

BASE = dict(fp.HESTON)
K_SMILE = np.array([80, 90, 100, 110, 120], dtype=float)

def implied_vol(K, price):
    intrinsic = max(fp.S0 - K * np.exp(-fp.r * fp.T), 0.0)
    if price <= intrinsic + 1e-10:
        return float("nan")
    return brentq(lambda s: fp.bs_closed_form(K, s) - price, 1e-4, 5.0)

def smile(params, strikes=K_SMILE, jumps=None, T=1.0):
    fp.T = T
    var_guess = max(params["v0"], params["theta"]) + (0.03 if jumps else 0)
    cf = lambda u: fp.cf_heston(u, **params) * (fp.cf_jumps(u, **jumps) if jumps else 1)
    prices = fp.cos_method(cf, strikes, N=512, var_guess=var_guess)
    out = np.array([implied_vol(K, p) for K, p in zip(strikes, prices)])
    fp.T = 1.0
    return out

def show_smiles(title, label, cases, strikes=K_SMILE):
    print(f"\n{title}")
    print("  " + f"{label:>14}" + "".join(f"{'K=' + str(int(k)):>9}" for k in strikes) + "     skew 90→110")
    for name, ivs in cases:
        skew = (ivs[1] - ivs[3]) * 100
        print("  " + f"{name:>14}" + "".join(f"{v*100:8.1f}%" for v in ivs) + f"   {skew:+6.1f} pts")

def header(s):
    print("\n" + "=" * 78 + f"\n{s}\n" + "=" * 78)

# ---------------------------------------------------------------------------
header("A. MODEL BEHAVIOUR — change one parameter, hold the rest at the demo values")

show_smiles("A1. rho (correlation between price and vol) → sets the SLOPE of the smile", "rho",
            [(f"{rho:+.1f}", smile({**BASE, "rho": rho})) for rho in (-0.9, -0.5, 0.0, 0.5)])
print("  → Negative rho: vol spikes when price falls → expensive downside puts (equities).")
print("    rho ≈ 0: symmetric smile (typical of major FX pairs). Positive: upside skew")
print("    (some commodities — supply shocks push price AND vol up).")

show_smiles("A2. sigma (vol of vol) → sets the CURVATURE: how fat both tails are", "vol-of-vol",
            [(f"{s:.2f}", smile({**BASE, "sigma": s, "rho": 0.0})) for s in (0.1, 0.3, 0.5, 0.8)])
print("  → Shown with rho = 0 so the effect isn't mixed with slope. More vol-of-vol =")
print("    more extreme outcomes both ways = higher wings.")

show_smiles("A3. Jump intensity (expected jumps per year, each avg −10%)", "jumps/yr",
            [(f"{lam:.1f}", smile(BASE, jumps={**fp.JUMPS, "lam": lam})) for lam in (0.0, 0.25, 0.5, 1.0)])
print("  → At a 1-year expiry, jumps mostly raise the LEVEL of every vol, not the slope (the")
print("    90→110 skew even shrinks a little). Their slope effect lives at short expiries — see B.")

# ---------------------------------------------------------------------------
header("B. MATURITY — the classic reason desks add jumps")
print("  Same parameters, different expiries. Strikes scaled to ±1 standard deviation")
print("  of the move so short and long expiries are comparable.")
print(f"\n  {'expiry':>8}  {'Heston skew':>12}  {'Bates skew':>11}    (implied vol at −1sd minus +1sd)")
for T in (0.05, 0.1, 0.25, 0.5, 1.0, 2.0):
    sd = 0.2 * np.sqrt(T)
    ks = np.array([fp.S0 * np.exp(-sd), fp.S0, fp.S0 * np.exp(sd)])
    h = smile(BASE, ks, T=T)
    b = smile(BASE, ks, jumps=fp.JUMPS, T=T)
    print(f"  {T*12:6.1f}mo  {(h[0]-h[2])*100:+10.2f} pts  {(b[0]-b[2])*100:+9.2f} pts")
print("  → Heston's skew shrinks at short expiries (8.5 pts at 1y → 3.8 at 2 weeks): diffusion")
print("    needs time to move vol. Jumps add the most skew exactly there (+1.4 pts at 2 weeks)")
print("    and wash out at long expiries, where many small jumps average into a near-normal")
print("    move. Real index options show steep short-dated skew — hence Bates and its cousins.")

# ---------------------------------------------------------------------------
header("C. NUMERICS — where each method breaks")

cfh = lambda u: fp.cf_heston(u, **BASE)
ref = fp.cos_method(cfh, K_SMILE, N=4096, L=16)

print("\nC1. COS: number of cosine terms (accuracy vs the 4,096-term reference)")
for n in (16, 32, 64, 128, 256):
    err = np.abs(fp.cos_method(cfh, K_SMILE, N=n) - ref).max()
    print(f"    N={n:>4}   max error ${err:.2e}")
print("  → Converges exponentially fast: 64 terms already gives sub-cent accuracy.")

print("\nC2. Carr-Madan FFT: grid size and damping alpha")
for N, eta, alpha in [(1024, 0.25, 1.5), (4096, 0.25, 1.5), (4096, 0.05, 1.5), (16384, 0.1, 1.5),
                      (4096, 0.25, 0.1), (4096, 0.25, 10.0)]:
    err = np.abs(fp.carr_madan_fft(cfh, K_SMILE, N=N, eta=eta, alpha=alpha) - ref).max()
    print(f"    N={N:>6} eta={eta:<5} alpha={alpha:<5} max error ${err:.2e}")
print("  → FFT ties the frequency step (eta) to the strike spacing (2π/(N·eta)): shrink eta")
print("    without raising N and the strike grid gets coarse, so interpolation error grows.")
print("    Too small an alpha (0.1) wrecks it ($1.51 off); alpha=10 happened to be fine here.")
print("    Best FFT ~$0.0004 vs COS ~$0.000007, with fewer knobs. Why COS is now preferred.")

print("\nC3. Very short expiry, deep out-of-the-money (where Fourier is hardest)")
fp.T = 0.02   # ~1 week
ks = np.array([90.0, 95.0, 105.0, 110.0])
ref_s = fp.cos_method(cfh, ks, N=8192, L=20)
for name, px in [("COS N=128", fp.cos_method(cfh, ks, N=128)),
                 ("COS N=1024", fp.cos_method(cfh, ks, N=1024)),
                 ("FFT N=4096", fp.carr_madan_fft(cfh, ks)),
                 ("FFT N=65536", fp.carr_madan_fft(cfh, ks, N=65536, eta=0.05))]:
    print(f"    {name:<12} " + "  ".join(f"K={int(k)}: {p:9.5f}" for k, p in zip(ks, px))
          + f"   max err ${np.abs(px - ref_s).max():.1e}")
fp.T = 1.0
print("  → COS sizes its range to the expiry, so even 128 terms is exact for a 1-week option.")
print("    FFT's strike grid doesn't adapt: K=105 is off by $0.0003 on a $0.027 option — tiny")
print("    in dollars but ~1% relative error, which is what matters when quoting OTM vol.")

print("\nC4. Monte Carlo: two different errors — noise (paths) and bias (time steps)")
print("    reference (COS) at K=100:", f"{ref[2]:.4f}")
print(f"    {'paths':>8} {'steps':>6} {'price':>9} {'±1se':>7} {'error':>8} {'time':>8}")
for paths, steps in [(10_000, 252), (100_000, 252), (400_000, 252),
                     (200_000, 12), (200_000, 52), (200_000, 1000)]:
    t = time.perf_counter()
    px, se = fp.monte_carlo(np.array([100.0]), "heston", paths=paths, steps=steps)
    dt = time.perf_counter() - t
    print(f"    {paths:>8,} {steps:>6} {px[0]:9.4f} {se[0]:7.4f} {px[0]-ref[2]:+8.4f} {dt:7.2f}s")
fk = 2 * BASE["kappa"] * BASE["theta"] / BASE["sigma"]**2
print("  → Two separate errors. Paths control NOISE (the ± column halves when paths x4).")
print("    Time steps control BIAS: 12 steps is clearly off (+0.07, ~3 se). From 52 steps on,")
print("    the bias is smaller than the noise, so you can't even see it without millions of")
print("    paths — and one unlucky run (100k) is 2.7 se out. You never quite know which.")
print(f"    Also: these parameters violate the Feller condition (2κθ/σ² = {fk:.2f} < 1), so")
print("    variance keeps hitting zero, where simple Euler schemes struggle. The Fourier")
print("    answer has neither problem — the reason to trust it for calibration.")

# ---------------------------------------------------------------------------
header("D. ANOTHER ASSET CLASS — credit portfolio loss distribution")
print("  100 loans, exposures $1–20mm, default probabilities 0.5%–5%, one shared economic")
print("  factor (one-factor Gaussian copula, correlation 0.15). Question: 99.9% loss quantile.")

rng = np.random.default_rng(1)
n_loans, rho_c = 100, 0.15
E = rng.integers(1, 21, n_loans)                 # exposures in $mm (integer units)
PD = rng.uniform(0.005, 0.05, n_loans)
c = norm.ppf(PD)
M = 2 ** int(np.ceil(np.log2(E.sum() + 1)))      # loss grid 0..M-1 ($mm)

t = time.perf_counter()
# Given the economy (factor z), loans default independently → the loss is a SUM of independent
# pieces → its fingerprint is the PRODUCT of each loan's fingerprint. Then average over z.
z, wz = np.polynomial.hermite_e.hermegauss(64)
wz = wz / wz.sum()
roots = np.exp(-2j * np.pi * np.arange(M) / M)   # evaluate generating function on roots of unity
pgf = np.zeros(M, dtype=complex)
for zi, wi in zip(z, wz):
    p = norm.cdf((c - np.sqrt(rho_c) * zi) / np.sqrt(1 - rho_c))
    pgf += wi * np.prod(1 - p[:, None] + p[:, None] * roots[None, :] ** E[:, None], axis=0)
pmf = np.real(np.fft.ifft(pgf))                  # the values ARE a DFT of the loss pmf → invert
pmf = np.clip(pmf, 0, None)
cdf = np.cumsum(pmf)
t_fft = time.perf_counter() - t

def q(cdf, a): return int(np.searchsorted(cdf, a))

t = time.perf_counter()
sims = 1_000_000
losses = np.empty(sims)
for start in range(0, sims, 100_000):
    Z = rng.standard_normal((100_000, 1))
    eps = rng.standard_normal((100_000, n_loans))
    default = np.sqrt(rho_c) * Z + np.sqrt(1 - rho_c) * eps < c
    losses[start:start + 100_000] = default @ E
t_mc = time.perf_counter() - t

print(f"\n  {'':>22}{'Fourier (exact)':>17}{'Monte Carlo 1M':>17}")
print(f"  {'expected loss $mm':>22}{(np.arange(M) * pmf).sum():17.2f}{losses.mean():17.2f}")
for a in (0.99, 0.999):
    print(f"  {f'{a*100:.1f}% quantile $mm':>22}{q(cdf, a):17d}{np.quantile(losses, a):17.0f}")
print(f"  {'time':>22}{t_fft*1e3:15.0f}ms{t_mc*1e3:15.0f}ms")
print("  → Same idea as options: losses add up, so fingerprints multiply. The 99.9% tail —")
print("    exactly where Monte Carlo has the fewest samples — comes out exact, with no noise.")
print("    This is how CreditRisk+ and many bank economic-capital engines work.")
