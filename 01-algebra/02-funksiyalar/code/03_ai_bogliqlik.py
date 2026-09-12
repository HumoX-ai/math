#!/usr/bin/env python3
"""
G bloki — Funksiyalar va AI / Functions and AI
  G1 chiziqli model · G2 sigmoid · G3 ReLU'lardan funksiya (+ sin(x) taxmini)
  G4 normalizatsiya · G5 L(w) parabola + gradient descent
Talab: pip install numpy   (matplotlib bo'lsa — grafik ham chizadi)
"""
import os
import numpy as np

LINE = "═" * 72
rng_ = np.random.default_rng(0)
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots"); os.makedirs(OUT, exist_ok=True)
    PLOT = True
except ImportError:
    PLOT = False

print(LINE + "\nG1 — CHIZIQLI MODEL: narx = w·maydon + b\n" + LINE)
A = np.array([[40.0, 1.0], [80.0, 1.0]]); y_ = np.array([70.0, 130.0])
w, b = np.linalg.solve(A, y_)
print(f"  w = {w:g} (ming $/m²),  b = {b:g} (ming $)      (kutilgan 1.5, 10)")
print(f"  narx(60) = {w*60 + b:g}                            (kutilgan 100)")

print("\n" + LINE + "\nG2 — SIGMOID\n" + LINE)
sig = lambda z: 1/(1 + np.exp(-z))
for v in (0, 1, -1, 2, -2):
    print(f"  σ({v:>2}) = {sig(v):.3f}")
zs = np.linspace(-10, 10, 2001)
print(f"  σ(x) + σ(−x) = 1 ?  max |xato| = {np.max(np.abs(sig(zs) + sig(-zs) - 1)):.2e}   ✓")
print(f"  0 < σ < 1 ?  min={sig(zs).min():.6f}, max={sig(zs).max():.6f}   ✓ (chegaraga yetmaydi)")
print(f"  σ(x) ≥ 0.5  ⟺  x ≥ 0 ?  {np.all((sig(zs) >= 0.5) == (zs >= 0))}   ✓")
print(f"  Monoton o'suvchi ?  {np.all(np.diff(sig(zs)) > 0)}   ✓")

print("\n" + LINE + "\nG3 — ReLU'LARDAN FUNKSIYA QURISH\n" + LINE)
relu = lambda z: np.maximum(0, z)
xs = np.linspace(-4, 6, 1001)
y3 = relu(xs - 1) + relu(1 - xs)
print(f"  ReLU(x−1) + ReLU(1−x) = |x−1| ?  max |xato| = {np.max(np.abs(y3 - np.abs(xs - 1))):.1e}   ✓")
print(f"  2 + ReLU(x−2) = max(x,2) ?        max |xato| = {np.max(np.abs(2 + relu(xs - 2) - np.maximum(xs, 2))):.1e}   ✓")

print("\n  Tajriba: N ta tasodifiy ReLU neyron bilan sin(x) ni taxminlash (0..2π)")
xg = np.linspace(0, 2*np.pi, 400); target = np.sin(xg)
for N in (2, 5, 20, 200):
    W1 = rng_.normal(size=N); b1 = rng_.uniform(-2*np.pi, 2*np.pi, size=N)
    H = relu(np.outer(xg, W1) + b1)                       # yashirin qatlam: 400 × N
    Hb = np.column_stack([H, np.ones(len(xg))])
    W2, *_ = np.linalg.lstsq(Hb, target, rcond=None)      # oxirgi chiziqli qatlamni o'rgatish
    with np.errstate(all="ignore"):                       # macOS BLAS soxta warning'ini yashirish
        approx = np.einsum("ij,j->i", Hb, W2)
    assert np.all(np.isfinite(approx))
    print(f"    N = {N:>3} neyron  →  o'rtacha xato = {np.mean(np.abs(approx - target)):.4f}")
    if PLOT and N in (2, 20, 200):
        plt.plot(xg, approx, label=f"N={N}")
if PLOT:
    plt.plot(xg, target, "k--", label="sin(x)"); plt.legend(); plt.title("ReLU-tarmoq sin(x) ni taxminlaydi (bo'lakli chiziqli)")
    plt.grid(alpha=0.3); p = os.path.join(OUT, "07_relu_sin.png"); plt.savefig(p, dpi=120); plt.close(); print(f"    ✓ {p}")
print("  ➜ Ko'proq neyron = ko'proq bukilish = egri chiziqqa yaqinroq. Universal approximation intuitsiyasi.")

print("\n" + LINE + "\nG4 — NORMALIZATSIYA = CHIZIQLI FUNKSIYA\n" + LINE)
data = np.array([10.0, 20.0, 40.0, 50.0])
mm = (data - data.min())/(data.max() - data.min())
mu, sd = data.mean(), data.std()
z = (data - mu)/sd
print(f"  min-max:  {mm}            k = {1/(data.max()-data.min()):.4f}, b = {-data.min()/(data.max()-data.min()):.4f}")
print(f"  μ = {mu:g}, σ = {sd:.4f}")
print(f"  z-score:  {np.round(z, 3)}     k = {1/sd:.4f}, b = {-mu/sd:.4f}")
print(f"  teskari:  σz + μ = {sd*z + mu}   ← asl ma'lumot qaytdi ✓")
print(f"  z ning o'rtachasi = {z.mean():.1e}, std = {z.std():.4f}   (0 va 1 bo'lishi kerak)")

print("\n" + LINE + "\nG5 — LOSS PARABOLA + GRADIENT DESCENT\n" + LINE)
X = np.array([1.0, 2.0, 3.0]); Y = np.array([2.0, 4.0, 5.0])
Lw = lambda w: np.sum((w*X - Y)**2)
a_, b_, c_ = np.sum(X**2), -2*np.sum(X*Y), np.sum(Y**2)
print(f"  L(w) = {a_:g}w² + ({b_:g})w + {c_:g}                (kutilgan 14w² − 50w + 45)")
w_star = -b_/(2*a_)
print(f"  w* = −b/2a = {w_star:.6f} = 25/14,   L(w*) = {Lw(w_star):.6f} = 5/14")
print(f"  L(1) = {Lw(1.0):g},  L(2) = {Lw(2.0):g}   (ikkalasi ham L(w*) dan katta)")

print("\n  Gradient descent:  w ← w − η·L'(w),   L'(w) = 2·Σx(wx − y) = 28w − 50")
grad = lambda w: 2*np.sum(X*(w*X - Y))
w_gd, eta = 0.0, 0.02
hist = [w_gd]
for k in range(1, 31):
    w_gd -= eta*grad(w_gd); hist.append(w_gd)
    if k in (1, 2, 3, 5, 10, 20, 30):
        print(f"    qadam {k:>2}: w = {w_gd:.6f}   L = {Lw(w_gd):.6f}")
print(f"  ➜ 30 qadamda w → {w_gd:.6f} ≈ w* = {w_star:.6f}.  Parabola cho'qqisiga tushdi.")
print(f"  ⚠️  η chegarasi (oldingi mavzu F2!):  0 < η < 2/(2a) = 2/28 ≈ {2/28:.4f}.  η = 0.1 bo'lsa portlaydi:")
w_bad = 0.0
for k in range(5):
    w_bad -= 0.1*grad(w_bad)
    print(f"    η=0.1, qadam {k+1}: w = {w_bad:.2f}")

if PLOT:
    wg = np.linspace(-0.5, 4, 400)
    plt.plot(wg, [Lw(v) for v in wg], lw=2, label="L(w) = 14w² − 50w + 45")
    plt.plot(hist, [Lw(v) for v in hist], "ro-", ms=4, lw=1, label="gradient descent (η=0.02)")
    plt.plot(w_star, Lw(w_star), "g*", ms=15, label=f"w* = 25/14")
    plt.xlabel("w"); plt.ylabel("L(w)"); plt.legend(); plt.grid(alpha=0.3); plt.title("Loss — parametr funksiyasi")
    p = os.path.join(OUT, "08_loss_parabola.png"); plt.savefig(p, dpi=120); plt.close(); print(f"  ✓ {p}")

print("\n" + LINE + """
XULOSA
  y = kx + b                 →  nn.Linear, weight & bias
  f∘g, (ax+b)∘(cx+d) chiziqli →  depth, aktivatsiya kerak
  ReLU yig'indilari          →  bo'lakli chiziqli, universal approximation
  (x − μ)/σ                  →  normalization (siljish + siqish)
  L(w) parabola              →  loss landscape, gradient descent cho'qqiga
""" + LINE)
