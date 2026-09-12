#!/usr/bin/env python3
"""
Grafiklar — PNG fayllar plots/ papkasiga.
⚠️  Avval QO'LDA chiz. Bu — solishtirish uchun.
Talab: pip install numpy matplotlib
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
os.makedirs(OUT, exist_ok=True)


def axes_style(ax, title, xlim=(-5, 5), ylim=(-5, 5)):
    ax.axhline(0, color="k", lw=0.8)
    ax.axvline(0, color="k", lw=0.8)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.grid(True, alpha=0.3); ax.set_title(title)
    ax.set_aspect("equal", adjustable="box")


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.tight_layout(); fig.savefig(p, dpi=120); plt.close(fig)
    print(f"  ✓ {p}")


print("Grafiklar chizilmoqda...")

# 1 ── Galereya (§5)
xs = np.linspace(-5, 5, 1000)
fig, axs = plt.subplots(2, 4, figsize=(16, 8))
gallery = [
    ("f(x) = 2  (o'zgarmas)", lambda v: np.full_like(v, 2.0)),
    ("f(x) = x", lambda v: v),
    ("f(x) = x²", lambda v: v**2),
    ("f(x) = x³", lambda v: v**3),
    ("f(x) = |x|", np.abs),
    ("f(x) = √x", lambda v: np.where(v >= 0, np.sqrt(np.clip(v, 0, None)), np.nan)),
    ("f(x) = 1/x", lambda v: np.where(np.abs(v) > 1e-9, 1/v, np.nan)),
]
for ax, (title, fn) in zip(axs.flat, gallery):
    ax.plot(xs, fn(xs), lw=2); axes_style(ax, title)
axs.flat[-1].axis("off")
axs.flat[-1].text(0.05, 0.5, "7 asosiy funksiya.\nHar birini qo'lda\n3 marta chiz.", fontsize=13)
save(fig, "01_galereya.png")

# 2 ── Chiziqli: B2, B3, B7 (§6)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].plot(xs, -3*xs + 6, lw=2, label="y = −3x + 6")
axs[0].plot([0, 2], [6, 0], "ro"); axs[0].legend(); axes_style(axs[0], "B2: kesmalar (0,6), (2,0)", (-2, 5), (-3, 8))
axs[1].plot(xs, 2*xs - 1, lw=2, label="y = 2x − 1")
axs[1].plot(xs, 2*xs + 4, lw=2, ls="--", label="parallel: 2x + 4")
axs[1].plot(xs, -xs/2 + 2, lw=2, ls=":", label="perpend.: −x/2 + 2")
axs[1].legend(fontsize=8); axes_style(axs[1], "B3: parallel va perpendikulyar")
axs[2].plot(xs, 2*xs + 1, lw=2, label="2x + 1"); axs[2].plot(xs, -xs + 7, lw=2, label="−x + 7")
axs[2].plot(xs, 2*xs - 3, lw=2, ls="--", label="2x − 3 (parallel)")
axs[2].plot(2, 5, "ro", ms=8); axs[2].annotate("(2, 5)", (2, 5), xytext=(2.5, 6))
axs[2].legend(fontsize=8); axes_style(axs[2], "B7: kesishish / parallel", (-2, 6), (-4, 10))
save(fig, "02_chiziqli.png")

# 3 ── Kvadrat: C1, C2, C6 (§7)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
q1 = xs**2 - 6*xs + 5
axs[0].plot(xs, q1, lw=2); axs[0].plot([1, 5], [0, 0], "go"); axs[0].plot(3, -4, "ro")
axs[0].axvline(3, color="r", ls="--", alpha=0.5); axes_style(axs[0], "C1: x²−6x+5, cho'qqi (3,−4)", (-1, 7), (-5, 8))
q2 = -2*xs**2 + 8*xs - 3
axs[1].plot(xs, q2, lw=2); axs[1].plot(2, 5, "ro"); axes_style(axs[1], "C2: −2x²+8x−3, max 5", (-1, 5), (-6, 7))
ts = np.linspace(0, 4, 400); hh = -5*ts**2 + 20*ts
axs[2].plot(ts, hh, lw=2); axs[2].axhline(15, color="r", ls="--", label="h = 15")
axs[2].fill_between(ts, 15, hh, where=hh >= 15, alpha=0.3, label="h ≥ 15 ⟺ t∈[1,3]")
axs[2].plot(2, 20, "ro"); axs[2].legend(fontsize=8)
axs[2].axhline(0, color="k", lw=0.8); axs[2].grid(alpha=0.3); axs[2].set_title("C6: h(t) = −5t²+20t")
axs[2].set_xlabel("t (s)"); axs[2].set_ylabel("h (m)")
save(fig, "03_kvadrat.png")

# 4 ── Xossalar: D2 (toq), D6 (juft W), D5 (qo'ng'iroq) (§8)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].plot(xs, xs**3 - 4*xs, lw=2); axs[0].plot([-2, 0, 2], [0, 0, 0], "go")
axes_style(axs[0], "D2: x³−4x (toq, nollar −2,0,2)", (-3.5, 3.5), (-6, 6))
axs[1].plot(xs, xs**2 - 2*np.abs(xs), lw=2); axs[1].plot([-1, 1], [-1, -1], "ro"); axs[1].plot([-2, 0, 2], [0, 0, 0], "go")
axes_style(axs[1], "D6: x²−2|x| (juft, W-shakl, min −1)", (-4, 4), (-2, 6))
axs[2].plot(xs, 1/(1 + xs**2), lw=2); axs[2].axhline(1, color="r", ls="--", alpha=0.5); axs[2].axhline(0, color="r", ls="--", alpha=0.5)
axes_style(axs[2], "D5: 1/(1+x²), E = (0, 1]", (-5, 5), (-0.5, 1.5))
save(fig, "04_xossalar.png")

# 5 ── Almashtirishlar: E1, E2 (§9)
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].plot(xs, xs**2, "k", lw=2, label="x²")
axs[0].plot(xs, xs**2 + 3, lw=1.5, label="x² + 3  (↑3)")
axs[0].plot(xs, (xs - 2)**2, lw=1.5, label="(x−2)²  (→2)")
axs[0].plot(xs, -xs**2, lw=1.5, label="−x²  (aks)")
axs[0].plot(xs, 2*xs**2, lw=1.5, label="2x²  (cho'zish)")
axs[0].plot(xs, (xs + 1)**2 - 4, lw=1.5, label="(x+1)²−4  (←1, ↓4)")
axs[0].legend(fontsize=8); axes_style(axs[0], "E1: x² almashtirishlari", (-5, 5), (-6, 8))
axs[1].plot(xs, np.abs(xs), "k", lw=2, label="|x|")
axs[1].plot(xs, np.abs(xs - 3) + 2, lw=2, label="|x−3|+2, cho'qqi (3,2)")
axs[1].plot(xs, -np.abs(xs + 1), lw=2, label="−|x+1|, cho'qqi (−1,0)")
axs[1].plot([3, -1], [2, 0], "ro"); axs[1].legend(fontsize=8); axes_style(axs[1], "E2: |x| almashtirishlari", (-5, 7), (-5, 6))
save(fig, "05_almashtirishlar.png")

# 6 ── E7 tarmoq, F4 bo'lakli, G3 |x−1| (§10, §12)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
relu = lambda z: np.maximum(0, z)
y_net = -(relu(2*xs - 1)) + 3
axs[0].plot(xs, y_net, lw=2, label="L₂(σ(L₁(x)))")
axs[0].plot(xs, -(2*xs - 1) + 3, "r--", lw=1, label="σ siz: −2x+4 (chiziqli)")
axs[0].plot(0.5, 3, "ro"); axs[0].legend(fontsize=8); axes_style(axs[0], "E7: mini tarmoq — bo'lakli chiziqli", (-2, 4), (-2, 6))
pw = np.where(xs < 0, xs + 2, np.where(xs <= 2, xs**2, 4.0))
m1 = xs < 0; m2 = (xs >= 0) & (xs <= 2); m3 = xs > 2
axs[1].plot(xs[m1], pw[m1], "b", lw=2); axs[1].plot(xs[m2], pw[m2], "b", lw=2); axs[1].plot(xs[m3], pw[m3], "b", lw=2)
axs[1].plot(0, 2, "bo", mfc="white"); axs[1].plot(0, 0, "bo"); axs[1].plot(2, 4, "bo")
axes_style(axs[1], "F4: bo'lakli, x=0 da sakrash", (-4, 5), (-3, 6))
axs[2].plot(xs, relu(xs - 1), lw=1.5, ls="--", label="ReLU(x−1)")
axs[2].plot(xs, relu(1 - xs), lw=1.5, ls="--", label="ReLU(1−x)")
axs[2].plot(xs, relu(xs - 1) + relu(1 - xs), "k", lw=2.5, label="yig'indi = |x−1|")
axs[2].legend(fontsize=8); axes_style(axs[2], "G3: ikki ReLU → |x−1|", (-3, 5), (-1, 5))
save(fig, "06_kompozitsiya_bolakli.png")

print(f"\nTayyor: {OUT}\nQo'lda chizganing bilan solishtir. Farq bor joyni daftarga yoz.")
