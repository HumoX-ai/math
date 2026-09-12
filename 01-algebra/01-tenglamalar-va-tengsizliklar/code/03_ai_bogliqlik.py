#!/usr/bin/env python3
"""
F bloki — Algebra va AI orasidagi ko'prik / The bridge between algebra and AI

Bu skript sen qo'lda yechgan F1-F5 masalalarini tekshiradi VA ularning
machine learning'dagi to'g'ridan-to'g'ri ma'nosini ko'rsatadi.

Ishga tushirish:  python3 03_ai_bogliqlik.py
Talab:            pip install numpy
"""

import numpy as np

LINE = "═" * 72


print(LINE)
print("F1 — CHIZIQLI REGRESSIYA = CHIZIQLI TENGLAMALAR SISTEMASI")
print(LINE)

X = np.array([1.0, 2.0, 3.0])
Y = np.array([2.0, 3.0, 5.0])
n = len(X)

Sx, Sy, Sxx, Sxy = X.sum(), Y.sum(), (X * X).sum(), (X * Y).sum()
print("\nNuqtalar: " + ", ".join(f"({xi:g}, {yi:g})" for xi, yi in zip(X, Y)))
print(f"\n  n   = {n}")
print(f"  Sx  = {Sx:g}        (kutilgan 6)")
print(f"  Sxx = {Sxx:g}       (kutilgan 14)")
print(f"  Sy  = {Sy:g}       (kutilgan 10)")
print(f"  Sxy = {Sxy:g}       (kutilgan 23)")

print("\nNormal tenglamalar (sen qo'lda yechgan sistema):")
print(f"    {Sxx:g}w + {Sx:g}b = {Sxy:g}")
print(f"     {Sx:g}w + {n:g}b = {Sy:g}")

A = np.array([[Sxx, Sx], [Sx, n]])
b_vec = np.array([Sxy, Sy])
w, b = np.linalg.solve(A, b_vec)
print(f"\n  Yechim: w = {w:.6f}  (kutilgan 1.5)")
print(f"          b = {b:.6f}  (kutilgan 1/3 = {1/3:.6f})")
print(f"\n  Model:  y = {w:.4f}·x + {b:.4f}")

pred = w * X + b
res = Y - pred
print("\n  Qoldiqlar (residuals):")
for xi, yi, pi, ri in zip(X, Y, pred, res):
    print(f"    x={xi:g}:  y={yi:g}   bashorat={pi:.4f}   qoldiq={ri:+.4f}")
print(f"\n  Σ(qoldiq)      = {res.sum():.10f}   <- NOL bo'lishi kerak (∂S/∂b = 0)")
print(f"  Σ(qoldiq · x)  = {(res * X).sum():.10f}   <- NOL bo'lishi kerak (∂S/∂w = 0)")

print("\n  Xuddi shu narsa MATRITSA ko'rinishida (linear algebra tili):")
Xd = np.column_stack([X, np.ones(n)])          # design matrix
normal_lhs = Xd.T @ Xd
normal_rhs = Xd.T @ Y
print(f"    XᵀX = \n{normal_lhs}")
print(f"    Xᵀy = {normal_rhs}")
print(f"    (XᵀX)⁻¹Xᵀy = {np.linalg.solve(normal_lhs, normal_rhs)}")
print(f"    np.polyfit   = {np.polyfit(X, Y, 1)}")
print("\n  ➜ Uchala usul bir xil javob berdi. Sen qo'lda yechgan 2x2 sistema —")
print("    bu aynan sklearn.LinearRegression ichida yechiladigan sistema.")


print("\n" + LINE)
print("F2 — LEARNING RATE = TENGSIZLIK")
print(LINE)

print("\n  f(x) = 3x²,  f'(x) = 6x,  x_{k+1} = x_k(1 − 6η)")
print("  Yaqinlashish sharti:  |1 − 6η| < 1   ⟺   0 < η < 1/3\n")


def gd(eta, x0=1.0, steps=8):
    xs, xk = [x0], x0
    for _ in range(steps):
        xk = xk - eta * 6 * xk
        xs.append(xk)
    return xs


print(f"  {'η':>7} │ {'c = 1−6η':>9} │ {'|c|<1?':>7} │ qadamlar (x₀ = 1)")
print("  " + "─" * 68)
for eta in [0.05, 0.1, 1/6, 0.3, 1/3, 0.5]:
    c = 1 - 6 * eta
    xs = gd(eta, steps=5)
    tail = "  ".join(f"{v:>9.4f}" for v in xs[1:])
    flag = "✓ ha" if abs(c) < 1 else "✗ YO'Q"
    print(f"  {eta:>7.4f} │ {c:>9.4f} │ {flag:>7} │ {tail}")

print("\n  ➜ η = 1/3 da c = −1: qiymatlar ±1 orasida sakraydi, yaqinlashmaydi (chegara holat).")
print("  ➜ η = 0.5 da c = −2: 1 → −2 → 4 → −8 → 16 ... PORTLASH.")
print("    Training log'da bu 'loss: nan' bo'lib ko'rinadi.")

print("\n  Umumiy holat: f(x) = (a/2)x²  →  0 < η < 2/a")
for a_val in [2, 6, 10, 100]:
    print(f"    a = {a_val:>3}  →  0 < η < {2/a_val:.4f}")
print("  Ko'p o'lchovda:  0 < η < 2/λ_max(Hessian)")


print("\n" + LINE)
print("F3 — KOSHI–SHVARTS = COSINE SIMILARITY CHEGARASI")
print(LINE)

u = np.array([3.0, 4.0])
v = np.array([4.0, 3.0])
dot = u @ v
nu, nv = np.linalg.norm(u), np.linalg.norm(v)

print(f"\n  u = {u},  v = {v}")
print(f"  u · v  = {dot:g}          (kutilgan 24)")
print(f"  ‖u‖    = {nu:g}          (kutilgan 5)")
print(f"  ‖v‖    = {nv:g}          (kutilgan 5)")
print(f"  cos θ  = {dot/(nu*nv):.6f}   (kutilgan 0.96)")
cs_ok = "✓ TO'G'RI" if dot**2 <= (nu*nv)**2 else "✗ BUZILDI"
print(f"\n  Koshi–Shvarts:  (u·v)² = {dot**2:g}  ≤  ‖u‖²‖v‖² = {(nu*nv)**2:g}   → {cs_ok}")

print("\n  Tasodifiy 100000 ta vektor juftligida tengsizlik buziladimi?")
rng = np.random.default_rng(0)
U = rng.normal(size=(100000, 8))
V = rng.normal(size=(100000, 8))
dots = np.einsum('ij,ij->i', U, V)
cosines = dots / (np.linalg.norm(U, axis=1) * np.linalg.norm(V, axis=1))
print(f"    min(cos θ) = {cosines.min():.10f}")
print(f"    max(cos θ) = {cosines.max():.10f}")
all_ok = "✓ HA" if np.all(np.abs(cosines) <= 1 + 1e-12) else "✗ YO'Q"
print(f"    Hammasi [-1, 1] ichidami? {all_ok}")
print("\n  ➜ Bu tasodif emas — Koshi–Shvarts tengsizligi buni KAFOLATLAYDI.")
print("    RAG, embedding qidiruvi, attention — hammasi shu kafolatga tayanadi.")

print("\n  Tenglik holati (kollinear vektorlar):")
for k in [2.0, 0.5, -1.0, -3.0]:
    vk = k * u
    c = (u @ vk) / (np.linalg.norm(u) * np.linalg.norm(vk))
    print(f"    v = {k:>5}·u  →  cos θ = {c:+.1f}")


print("\n" + LINE)
print("F4 — ReLU = BO'LAKLI FUNKSIYA = TENGSIZLIK")
print(LINE)

relu = lambda z: np.maximum(0.0, z)
relu_abs = lambda z: (z + np.abs(z)) / 2

print("\n  (a) ReLU(2x − 6) = 4  →  x = ?")
xs = np.linspace(-2, 10, 1201)
hit = xs[np.isclose(relu(2*xs - 6), 4.0, atol=1e-9)]
print(f"      Sonli qidiruv: x ≈ {hit[0]:g}   (kutilgan 5)")

print("\n  (b) ReLU(2x − 6) = 0  →  barcha x ≤ 3")
zeros = xs[relu(2*xs - 6) == 0]
print(f"      Eng katta yechim: x = {zeros.max():g}   (kutilgan 3)")
print("      Yechimlar soni:   cheksiz ko'p (bu aslida tengsizlik: 2x − 6 ≤ 0)")

print("\n  (c) ReLU(2x − 6) = −1  →  yechim yo'q")
print(f"      min ReLU qiymati: {relu(2*xs - 6).min():g}  ≥ 0 har doim  →  −1 chiqmaydi ✓")

print("\n  (d) ReLU(z) = (z + |z|)/2  ekanini tekshiramiz:")
test_z = np.array([-5.0, -1.0, 0.0, 0.5, 3.0, 7.0])
print(f"      z            : {test_z}")
print(f"      max(0, z)    : {relu(test_z)}")
print(f"      (z + |z|)/2  : {relu_abs(test_z)}")
match_txt = "✓ HA" if np.allclose(relu(test_z), relu_abs(test_z)) else "✗ YO'Q"
print(f"      Mos keladimi : {match_txt}")

print("\n  ➜ 'Dead ReLU': agar neyron kirishi doim z ≤ 0 bo'lsa,")
print("    chiqish = 0 va gradient = 0 → neyron hech qachon o'rganmaydi.")


print("\n" + LINE)
print("F5 — GRADIENT CLIPPING = TENGSIZLIK BILAN QO'YILGAN CHEGARA")
print(LINE)


def clip_by_norm(g, c):
    ng = np.linalg.norm(g)
    return (c * g / ng, True) if ng > c else (g.copy(), False)


g = np.array([6.0, 8.0])
c = 4.0
gp, fired = clip_by_norm(g, c)

print(f"\n  g = {g},  c = {c:g}")
print(f"  ‖g‖   = {np.linalg.norm(g):g}          (kutilgan 10)")
fired_txt = "✓ clipping ISHGA TUSHADI" if fired else "yo'q, o'zgarmaydi"
print(f"  ‖g‖ > c ?  {np.linalg.norm(g):g} > {c:g}  →  {fired_txt}")
print(f"  g'    = {gp}    (kutilgan [2.4, 3.2])")
print(f"  ‖g'‖  = {np.linalg.norm(gp):g}          (kutilgan aynan 4)")

print("\n  Yo'nalish saqlanadimi?")
print(f"    g /‖g‖  = {g/np.linalg.norm(g)}")
print(f"    g'/‖g'‖ = {gp/np.linalg.norm(gp)}")
dir_txt = ("✓ HA — clipping faqat UZUNLIKNI o'zgartiradi"
           if np.allclose(g/np.linalg.norm(g), gp/np.linalg.norm(gp)) else "✗ YO'Q")
print(f"    Bir xilmi: {dir_txt}")

print("\n  (e) Isbot tekshiruvi: 100000 ta tasodifiy gradientda ‖g'‖ ≤ c bajariladimi?")
G = rng.normal(scale=5.0, size=(100000, 16))
norms = np.linalg.norm(G, axis=1, keepdims=True)
C = 20.0
Gc = np.where(norms > C, C * G / norms, G)
new_norms = np.linalg.norm(Gc, axis=1)
print(f"    max ‖g'‖ = {new_norms.max():.12f}   (c = {C:g} dan oshmasligi kerak)")
print(f"    Clipping'siz max ‖g‖ = {norms.max():.4f}  (chegaralanmagan)")
bound_txt = "✓ HECH BIRI c dan oshmadi" if new_norms.max() <= C + 1e-9 else "✗ BUZILDI"
print(f"    Natija: {bound_txt}")
print(f"    Clipping necha marta ishga tushdi: {(norms > C).sum()} / {len(G)}")

print("\n" + LINE)
print("XULOSA / SUMMARY")
print(LINE)
print("""
  Bugungi maktab algebrasi                →  Machine Learning
  ────────────────────────────────────────────────────────────────────
  2x2 chiziqli sistema                    →  Linear regression (normal eq.)
  |1 − 6η| < 1  tengsizligi               →  Learning rate chegarasi
  (u·v)² ≤ ‖u‖²‖v‖²                       →  cosine similarity ∈ [−1, 1]
  max(0, z) = (z + |z|)/2                 →  ReLU aktivatsiyasi
  ‖c·v‖ = |c|·‖v‖                         →  Gradient clipping kafolati

  Hech qanday sehr yo'q. Faqat algebra — lekin to'g'ri joyda qo'llangan.
""")
print(LINE)
