#!/usr/bin/env python3
"""
Fourier option pricing, hands-on: price the same options three ways and compare.

  1. Carr-Madan FFT  (1999)  — one FFT gives a whole strip of strikes
  2. COS method      (2008)  — Fang & Oosterlee's faster successor
  3. Monte Carlo             — brute-force simulation, the "ground truth by sweat"

The idea in one line: we never know the probability density of the future price,
but we DO know its characteristic function phi(u) = E[exp(i*u*ln S_T)] in closed form.
Pricing = integrating payoff x density, and that integral can be done in Fourier space.

Run:  python3 quant-backtesting/fourier_pricing_demo.py
Needs numpy + scipy.
"""
import time
import numpy as np
from scipy.stats import norm

S0, r, T = 100.0, 0.03, 1.0
STRIKES = np.array([80, 90, 100, 110, 120], dtype=float)

# ---------------------------------------------------------------------------
# Characteristic functions — the "fingerprints" of each model's distribution of ln S_T
# ---------------------------------------------------------------------------

def cf_black_scholes(u, sigma=0.2):
    """ln S_T is normal, so its fingerprint is a Gaussian in u."""
    return np.exp(1j * u * (np.log(S0) + (r - 0.5 * sigma**2) * T) - 0.5 * sigma**2 * u**2 * T)

HESTON = dict(kappa=2.0, theta=0.04, sigma=0.5, rho=-0.7, v0=0.04)

def cf_heston(u, kappa, theta, sigma, rho, v0):
    """Heston (1993) stochastic volatility. The density has no closed form; this does.
    ('Little trap' form of Albrecher et al. 2007 — numerically stable.)"""
    iu = 1j * u
    d = np.sqrt((rho * sigma * iu - kappa) ** 2 + sigma**2 * (iu + u**2))
    g = (kappa - rho * sigma * iu - d) / (kappa - rho * sigma * iu + d)
    edt = np.exp(-d * T)
    C = (kappa * theta / sigma**2) * ((kappa - rho * sigma * iu - d) * T
                                      - 2 * np.log((1 - g * edt) / (1 - g)))
    D = (v0 / sigma**2) * (kappa - rho * sigma * iu - d) * (1 - edt) / (1 - g * edt)
    return np.exp(iu * (np.log(S0) + r * T) + C + D)

JUMPS = dict(lam=0.5, muJ=-0.10, sigJ=0.15)   # ~one jump every 2 years, avg -10%

def cf_jumps(u, lam, muJ, sigJ):
    """Merton lognormal jumps on their own (drift-compensated so the forward is unchanged)."""
    k = np.exp(muJ + 0.5 * sigJ**2) - 1
    return np.exp(lam * T * (np.exp(1j * u * muJ - 0.5 * sigJ**2 * u**2) - 1) - 1j * u * lam * k * T)

def cf_bates(u):
    """Bates = Heston + jumps. Adding an independent random component in price-space is a
    CONVOLUTION of densities. In Fourier space it is just a MULTIPLICATION. That's the whole trick."""
    return cf_heston(u, **HESTON) * cf_jumps(u, **JUMPS)

# ---------------------------------------------------------------------------
# Pricers
# ---------------------------------------------------------------------------

def bs_closed_form(K, sigma=0.2):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def carr_madan_fft(cf, strikes, N=4096, eta=0.25, alpha=1.5):
    """The call price as a function of log-strike isn't integrable, so damp it by exp(alpha*k),
    take its Fourier transform analytically from phi, then ONE inverse FFT returns calls on a
    grid of N log-strikes. Interpolate to the strikes we want."""
    lam = 2 * np.pi / (N * eta)                  # log-strike spacing (FFT ties eta and lam together)
    v = np.arange(N) * eta                       # integration grid in frequency space
    k0 = np.log(S0) - N * lam / 2                # centre the log-strike grid on ln S0
    psi = np.exp(-r * T) * cf(v - (alpha + 1) * 1j) / (alpha**2 + alpha - v**2 + 1j * (2 * alpha + 1) * v)
    simpson = (3 - (-1) ** np.arange(N) - (np.arange(N) == 0)) / 3   # 1/3, 4/3, 2/3, 4/3, ...
    x = np.exp(-1j * v * k0) * psi * eta * simpson
    k_grid = k0 + lam * np.arange(N)
    calls = np.exp(-alpha * k_grid) / np.pi * np.real(np.fft.fft(x))
    return np.interp(np.log(strikes), k_grid, calls)

def cos_method(cf, strikes, N=256, L=12.0, var_guess=0.04):
    """Expand the (unknown) density in a cosine series on [a, b]. The series coefficients ARE
    the characteristic function sampled at k*pi/(b-a). Price puts (numerically stabler),
    then convert to calls with put-call parity."""
    c1 = np.log(S0) + r * T
    width = L * np.sqrt(var_guess * T)
    a, b = c1 - width, c1 + width
    k = np.arange(N)
    w = k * np.pi / (b - a)
    phi_part = np.real(cf(w) * np.exp(-1j * w * a))
    phi_part[0] *= 0.5                           # the "Σ'" — first term gets half weight

    out = []
    for K in strikes:
        c, d = a, np.log(K)                      # put pays K - e^y for y in [a, ln K]
        chi = (np.cos(w * (d - a)) * np.exp(d) - np.cos(w * (c - a)) * np.exp(c)
               + w * np.sin(w * (d - a)) * np.exp(d) - w * np.sin(w * (c - a)) * np.exp(c)) / (1 + w**2)
        psi = np.empty(N)
        psi[0] = d - c
        psi[1:] = (np.sin(w[1:] * (d - a)) - np.sin(w[1:] * (c - a))) / w[1:]
        Vk = 2 / (b - a) * (K * psi - chi)
        put = np.exp(-r * T) * np.sum(phi_part * Vk)
        out.append(put + S0 - K * np.exp(-r * T))
    return np.array(out)

def monte_carlo(strikes, model="heston", paths=200_000, steps=252, seed=7):
    """Simulate the paths day by day and average the payoffs. Full-truncation Euler for Heston."""
    rng = np.random.default_rng(seed)
    dt = T / steps
    p = HESTON
    lnS = np.full(paths, np.log(S0))
    v = np.full(paths, p["v0"])
    jump_drift = 0.0
    if model == "bates":
        j = JUMPS
        jump_drift = -j["lam"] * (np.exp(j["muJ"] + 0.5 * j["sigJ"]**2) - 1)
    for _ in range(steps):
        z1 = rng.standard_normal(paths)
        z2 = p["rho"] * z1 + np.sqrt(1 - p["rho"]**2) * rng.standard_normal(paths)
        vp = np.maximum(v, 0.0)
        lnS += (r + jump_drift - 0.5 * vp) * dt + np.sqrt(vp * dt) * z1
        v += p["kappa"] * (p["theta"] - vp) * dt + p["sigma"] * np.sqrt(vp * dt) * z2
        if model == "bates":
            n = rng.poisson(JUMPS["lam"] * dt, paths)
            lnS += n * JUMPS["muJ"] + np.sqrt(n) * JUMPS["sigJ"] * rng.standard_normal(paths)
    ST = np.exp(lnS)
    payoff = np.maximum(ST[:, None] - strikes[None, :], 0.0)
    price = np.exp(-r * T) * payoff.mean(axis=0)
    stderr = np.exp(-r * T) * payoff.std(axis=0) / np.sqrt(paths)
    return price, stderr

def timed(fn, *a, repeat=1, **kw):
    t = time.perf_counter()
    for _ in range(repeat):
        out = fn(*a, **kw)
    return out, (time.perf_counter() - t) / repeat

def table(title, rows, cols):
    print(f"\n{title}")
    print("  " + "".join(f"{c:>12}" for c in cols))
    for row in rows:
        print("  " + "".join(f"{x:>12.4f}" if isinstance(x, float) else f"{x:>12}" for x in row))

# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 72)
    print("STEP 1 — Sanity check on Black-Scholes, where we know the exact answer")
    print("=" * 72)
    cf = lambda u: cf_black_scholes(u)
    exact = bs_closed_form(STRIKES)
    fft = carr_madan_fft(cf, STRIKES)
    cos = cos_method(cf, STRIKES)
    table("Call prices, sigma = 20%", [(int(K), e, f, c, abs(f - e), abs(c - e))
          for K, e, f, c in zip(STRIKES, exact, fft, cos)],
          ["strike", "exact", "FFT", "COS", "FFT err", "COS err"])
    print("\n  → Both Fourier methods recover the textbook formula from the fingerprint alone.")

    print("\n" + "=" * 72)
    print("STEP 2 — Heston: no closed-form density, so Fourier vs simulation")
    print("=" * 72)
    print(f"  params: {HESTON}")
    cfh = lambda u: cf_heston(u, **HESTON)
    fft, t_fft = timed(carr_madan_fft, cfh, STRIKES, repeat=50)
    cos, t_cos = timed(cos_method, cfh, STRIKES, repeat=50)
    (mc, se), t_mc = timed(monte_carlo, STRIKES, "heston")
    table("Call prices", [(int(K), f, c, m, s, abs(f - c)) for K, f, c, m, s in zip(STRIKES, fft, cos, mc, se)],
          ["strike", "FFT", "COS", "MonteCarlo", "MC ±1se", "|FFT-COS|"])
    print(f"\n  time for all 5 strikes:   FFT {t_fft*1e3:7.2f} ms   COS {t_cos*1e3:7.2f} ms   "
          f"Monte Carlo {t_mc*1e3:9.0f} ms")
    print(f"  → Monte Carlo is ~{t_mc/t_cos:,.0f}x slower than COS, and still has noise of ±{se.max():.3f}.")

    # Implied vols show what Heston is *for*: a skew Black-Scholes can't produce
    from scipy.optimize import brentq
    ivs = [brentq(lambda s: bs_closed_form(K, s) - p, 1e-4, 3) for K, p in zip(STRIKES, cos)]
    print("\n  Implied vol by strike (Black-Scholes would be a flat line):")
    for K, iv in zip(STRIKES, ivs):
        print(f"    K={int(K):>4}  {iv*100:5.1f}%  " + "█" * int(iv * 200))
    print("  → rho = -0.7 (vol rises when price falls) creates the equity-style downside skew.")

    print("\n" + "=" * 72)
    print("STEP 3 — Add jumps: convolution in price-space = multiplication in Fourier space")
    print("=" * 72)
    print(f"  jumps: {JUMPS}")
    print("  The entire code change:  cf_bates(u) = cf_heston(u) * cf_jumps(u)")
    cos_b = cos_method(cf_bates, STRIKES, var_guess=0.06)
    (mc_b, se_b), t_mcb = timed(monte_carlo, STRIKES, "bates")
    table("Call prices", [(int(K), h, c, m, s) for K, h, c, m, s in zip(STRIKES, cos, cos_b, mc_b, se_b)],
          ["strike", "Heston", "Bates COS", "Bates MC", "MC ±1se"])
    print("\n  → In simulation, jumps meant a new Poisson draw every step of every path.")
    print("    In Fourier space they were one multiplication — and the two still agree.")

    print("\n" + "=" * 72)
    print("STEP 4 — Why desks care: calibration")
    print("=" * 72)
    strikes40 = np.linspace(70, 130, 40)
    _, t40 = timed(cos_method, cfh, strikes40, repeat=20)
    _, t_mc40 = timed(monte_carlo, strikes40, "heston", paths=50_000, steps=100)
    evals = 2000
    print(f"  Fitting Heston to a 40-option surface takes ~{evals:,} optimizer evaluations.")
    print(f"    COS:          {t40*1e3:6.2f} ms per surface  → {t40*evals:8.1f} s total")
    print(f"    Monte Carlo:  {t_mc40*1e3:6.0f} ms per surface  → {t_mc40*evals/60:8.1f} min total "
          f"(with 4x fewer paths, and noise that confuses the optimizer)")
    print("\n  → Fourier to calibrate; Monte Carlo afterwards for path-dependent exotics the")
    print("    Fourier methods can't handle (barriers, Asians, autocallables).")
