#!/usr/bin/env python3
"""G bloki — daraja/ildiz va AI: norm, √n, He init, RMSNorm, lr schedule. Talab: numpy (matplotlib ixtiyoriy)."""
import os
import numpy as np
LINE = "═" * 72
rng = np.random.default_rng(0)
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots"); os.makedirs(OUT, exist_ok=True); PLOT = True
except ImportError:
    PLOT = False

print(LINE + "\nG1 — L2 NORM\n" + LINE)
for v in ([3, 4], [1, 2, 2], [1, 1, 1, 1]):
    print(f"  ‖{v}‖ = {np.linalg.norm(v):g}")
u = np.array([3.0, 4.0]); print(f"  birlik vektor (3,4)/5 = {u/np.linalg.norm(u)},  normasi = {np.linalg.norm(u/np.linalg.norm(u)):g}")
for n in (64, 512):
    print(f"  ‖n={n} ta 1‖ = √{n} = {np.sqrt(n):.3f}")

print("\n" + LINE + "\nG2 — √d TAJRIBASI: n ta tasodifiy ±1 ning yig'indisi ~√n\n" + LINE)
print(f"  {'d':>5} {'√d':>8} {'std(q·k) tajriba':>18} {'max|q·k|':>10}  {'std/√d':>7}")
for d in (16, 64, 256, 1024):
    Q = rng.choice([-1.0, 1.0], size=(20000, d)); K = rng.choice([-1.0, 1.0], size=(20000, d))
    dots = np.einsum("ij,ij->i", Q, K)
    print(f"  {d:>5} {np.sqrt(d):>8.2f} {dots.std():>18.2f} {np.abs(dots).max():>10.0f}  {dots.std()/np.sqrt(d):>7.3f}")
print("  ➜ std(q·k) ≈ √d (oxirgi ustun ≈ 1), d EMAS. Shuning uchun QKᵀ/√d.")
print(f"  ballar [64,16,0]/√64 = {np.array([64, 16, 0])/8}")
print("\n  Softmax'ga ta'siri (d=256, tasodifiy 5 ta ball):")
sc = rng.normal(size=5) * 16          # std ≈ √256 = 16 bo'lgan xom ballar
sm = lambda z: np.exp(z - z.max())/np.exp(z - z.max()).sum()
print(f"    xom ballar:        {np.round(sc, 1)}  →  softmax {np.round(sm(sc), 3)}   ← bitta tokenga yig'ildi (to'yingan)")
print(f"    ÷√256 = ÷16:       {np.round(sc/16, 2)}  →  softmax {np.round(sm(sc/16), 3)}   ← taqsimlangan")

print("\n" + LINE + "\nG3 — He INIT: std = √(2/n_in)\n" + LINE)
for n_in in (8, 128, 512, 2048):
    print(f"  n_in={n_in:>5}: √(2/{n_in}) = {np.sqrt(2/n_in):.5f}")
print(f"  std=0.05 → n_in = 2/0.05² = {2/0.05**2:.0f}")
print("\n  Tajriba: 10 qatlamli ReLU tarmoqdan signal o'tishi (n=512), chiqish std'si:")
n = 512; xin = rng.normal(size=(1000, n))
for name, std in (("std=1 (noto'g'ri)", 1.0), ("std=1/√n (Xavier)", 1/np.sqrt(n)), ("std=√(2/n) (He)", np.sqrt(2/n))):
    h = xin.copy()
    with np.errstate(all="ignore"):                       # std=1 holatida overflow — maqsadli
        for _ in range(10):
            h = np.maximum(0, h @ rng.normal(scale=std, size=(n, n)))
    print(f"    {name:>20}: std(chiqish) = {h.std():.3e}   {'← PORTLADI' if h.std() > 1e3 else ('← SO`NDI' if h.std() < 1e-2 else '← barqaror ✓')}")

print("\n" + LINE + "\nG4 — RMS va RMSNorm\n" + LINE)
xv = np.array([1.0, -2.0, 2.0, 4.0])
rms = lambda v: np.sqrt(np.mean(v**2))
print(f"  x = {xv},  x² = {xv**2},  Σ/n = {np.mean(xv**2)},  RMS = {rms(xv)}")
xn = xv / rms(xv)
print(f"  x/RMS = {xn},  RMS(x/RMS) = {rms(xn):g}   ✓")
print(f"  x · (mean(x²))^(−1/2) = {xv * np.mean(xv**2)**-0.5}   ← bir xil, rsqrt ko'rinishi")

print("\n" + LINE + "\nG5 — LEARNING RATE SCHEDULE\n" + LINE)
for t in (1, 4, 100, 10_000):
    print(f"  η(t={t:>6}) = 0.1/√t = {0.1/np.sqrt(t):.4f}")
print(f"  η < 0.001 ⟺ √t > 100 ⟺ t > 10 000.   Tekshir t=10 001: {0.1/np.sqrt(10001):.6f}")
d_model, warm = 512, 4000
noam = lambda t: d_model**-0.5 * np.minimum(t**-0.5, t * warm**-1.5)
ts = np.arange(1, 40001)
print(f"  Noam (d=512, w=4000): peak t=w → {noam(warm):.3e}  (= 1/√{d_model*warm} = 1/{np.sqrt(d_model*warm):.0f})")
for t in (1, 1000, 4000, 16000, 40000):
    print(f"    t={t:>6}: η = {noam(t):.3e}")
print(f"  t<w o'sadimi: {np.all(np.diff(noam(ts[:warm])) > 0)}   t>w kamayadimi: {np.all(np.diff(noam(ts[warm:])) < 0)}")
if PLOT:
    plt.plot(ts, noam(ts)); plt.axvline(warm, color="r", ls="--", label="t = warmup")
    plt.xlabel("t (step)"); plt.ylabel("η"); plt.title("Noam schedule: d^(−0.5)·min(t^(−0.5), t·w^(−1.5))"); plt.legend(); plt.grid(alpha=0.3)
    p = os.path.join(OUT, "01_noam_lr.png"); plt.savefig(p, dpi=120); plt.close(); print(f"  ✓ {p}")

print("\n" + LINE + "\nBONUS — SCALING LAW  L = (N_c/N)^0.076\n" + LINE)
for N in (1e8, 1e9, 1e10, 1e11):
    print(f"  N={N:.0e}: L ∝ N^(−0.076) = {N**-0.076:.4f}")
print(f"  N 10× → L × 10^(−0.076) = {10**-0.076:.3f}  →  {100*(1-10**-0.076):.0f}% pasayish")
print(LINE)
