#!/usr/bin/env python3
"""
Funksiyalar — A–F bloklarini tekshirish / Functions — verification
⚠️  Avval qog'ozda yech.
Talab: pip install sympy
"""
import sympy as sp

x, a, y, t = sp.symbols('x a y t', real=True)
LINE = "─" * 70


def head(s):
    print("\n" + LINE + f"\n{s}\n" + LINE)


def domain(expr):
    """SymPy bilan haqiqiy domain'ni topish."""
    return sp.calculus.util.continuous_domain(expr, x, sp.S.Reals)


def rng(expr, dom=sp.S.Reals):
    return sp.calculus.util.function_range(expr, x, dom)


def parity(f):
    fm = f.subs(x, -x)
    if sp.simplify(fm - f) == 0:
        return "JUFT (even)"
    if sp.simplify(fm + f) == 0:
        return "TOQ (odd)"
    return "hech qaysi (neither)"


head("A. FUNKSIYA TUSHUNCHASI")
f = 2*x**2 - 3*x + 1
print(f"[A1] f = {f}")
for v in (0, 1, -2):
    print(f"     f({v}) = {f.subs(x, v)}")
print(f"     f(a+1) = {sp.expand(f.subs(x, a + 1))}    (kutilgan 2a² + a)")

print(f"\n[A2] D( √(x−3)/(x−5) ) = {domain(sp.sqrt(x - 3)/(x - 5))}    (kutilgan [3,5) ∪ (5,∞))")
print(f"[A3] D( 1/(x²−4) + √(6−x) ) = {domain(1/(x**2 - 4) + sp.sqrt(6 - x))}")

print("\n[A5] Range:")
for name, e in [("x²+2", x**2 + 2), ("−|x|+3", -sp.Abs(x) + 3),
                ("√x − 1", sp.sqrt(x) - 1), ("1/(1+x²)", 1/(1 + x**2))]:
    d = domain(e)
    print(f"     E({name:>9}) = {rng(e, d)}")

print("\n[A6] Jadval → y = kx + b")
pts = [(0, 3), (1, 5), (2, 7), (3, 9), (4, 11)]
k_, b_ = sp.symbols('k b')
sol = sp.solve([sp.Eq(k_*px + b_, py) for px, py in pts[:2]], [k_, b_])
print(f"     {sol}  →  y = {sol[k_]}x + {sol[b_]}")
print(f"     Qolgan nuqtalar mos keladimi: {all(sol[k_]*px + sol[b_] == py for px, py in pts)}")


head("B. CHIZIQLI FUNKSIYA")


def line_through(p, q):
    k = sp.Rational(q[1] - p[1], q[0] - p[0])
    b = p[1] - k*p[0]
    return k*x + b


print(f"[B1] (1,3),(3,7):        y = {line_through((1, 3), (3, 7))}")
print(f"[B4] f(2)=5, f(−1)=−4:   f = {line_through((2, 5), (-1, -4))}")
L = -3*x + 6
print(f"[B2] y = {L}:  x-kesma {sp.solve(L, x)}, y-kesma {L.subs(x, 0)}")
print(f"[B3a] parallel 2x−1, (0,4):      y = {2*x + 4}")
kp = sp.Rational(-1, 2)
print(f"[B3b] perpendikulyar, (2,1):      y = {kp*x + (1 - kp*2)}")
C = sp.Symbol('C')
print(f"[B5c] F = C:  C = {sp.solve(sp.Eq(C, sp.Rational(9, 5)*C + 32), C)}")
print(f"[B6c] 2000d + 5000 ≤ 25000:  {sp.solve(2000*x + 5000 <= 25000, x)}")
print(f"[B7a] 2x+1 = −x+7:  x = {sp.solve(sp.Eq(2*x + 1, -x + 7), x)}, y = {(2*x+1).subs(x, 2)}")
print(f"[B7b] 2x+1 = 2x−3:  {sp.solve(sp.Eq(2*x + 1, 2*x - 3), x)}  (bo'sh — parallel)")


head("C. KVADRAT FUNKSIYA")


def vertex(q):
    p = sp.Poly(q, x)
    A, B, _ = p.all_coeffs()
    x0 = -B/(2*A)
    return x0, q.subs(x, x0)


for name, q in [("x²−6x+5", x**2 - 6*x + 5), ("−2x²+8x−3", -2*x**2 + 8*x - 3),
                ("x²+4x+7", x**2 + 4*x + 7)]:
    x0, y0 = vertex(q)
    print(f"[C] {name:>10}: nollar {sp.solve(q, x)}, cho'qqi ({x0}, {y0}), "
          f"vertex form: {sp.Poly(q, x).all_coeffs()[0]}(x − ({x0}))² + ({y0})")

print(f"[C4] cho'qqi (1,−2), (0,1):  y = {sp.expand(3*(x-1)**2 - 2)}")
print(f"[C5] S(x) = x(20−x): max at x = {vertex(x*(20 - x))[0]}, S = {vertex(x*(20 - x))[1]}")
h = -5*t**2 + 20*t
print(f"[C6] h(t) = {h}: max t = {-20/(2*-5)}, h = {h.subs(t, 2)}; yerga: {sp.solve(h, t)}; "
      f"h ≥ 15: {sp.solve(h >= 15, t)}")


head("D. XOSSALAR")
for name, e in [("x⁴−3x²", x**4 - 3*x**2), ("x³+x", x**3 + x), ("x²+x", x**2 + x),
                ("|x|", sp.Abs(x)), ("1/x", 1/x), ("x²+1", x**2 + 1),
                ("x³−4x", x**3 - 4*x), ("x²−2|x|", x**2 - 2*sp.Abs(x)), ("1/(1+x²)", 1/(1+x**2))]:
    print(f"[D1] {name:>9}: {parity(e)}")

g = x**3 - 4*x
print(f"\n[D2] x³−4x nollar: {sp.solve(g, x)};  f > 0: {sp.solve(g > 0, x)}")
print(f"[D5] E(1/(1+x²)) = {rng(1/(1+x**2))};  maksimum x=0: {(1/(1+x**2)).subs(x, 0)}")
w = x**2 - 2*sp.Abs(x)
print(f"[D6] x²−2|x| nollar: {sp.solve(w, x)};  E = {rng(w)}")
print(f"     x ≥ 0 da: {sp.expand(x**2 - 2*x)} = (x−1)² − 1  →  min −1, x = ±1")


head("E. ALMASHTIRISHLAR VA KOMPOZITSIYA")
f1 = 2*x + 1
g1 = x**2
print(f"[E3] f∘g = {sp.expand(f1.subs(x, g1))},  g∘f = {sp.expand(g1.subs(x, f1))}")
print(f"     f(g(2)) = {f1.subs(x, g1.subs(x, 2))},  g(f(2)) = {g1.subs(x, f1.subs(x, 2))}")
print(f"[E4] D(√(x−4)) = {domain(sp.sqrt(x - 4))},  D(√x − 4) = {domain(sp.sqrt(x) - 4)}")
F, G, H = x + 1, 2*x, x**2
comp = lambda *fs: (lambda e: [e := fn.subs(x, e) for fn in reversed(fs)][-1])(x)
print(f"[E6] f(g(h)) = {sp.expand(comp(F, G, H))},  h(g(f)) = {sp.expand(comp(H, G, F))},  "
      f"g(h(f)) = {sp.expand(comp(G, H, F))}")

L1 = 2*x - 1
relu = lambda z: sp.Max(0, z)
L2 = lambda z: -z + 3
net = L2(relu(L1))
print(f"\n[E7] y(x) = L₂(σ(L₁(x))) = {net}")
for v in (0, 1, 2, -1):
    print(f"     y({v:>2}) = {net.subs(x, v)}")
print(f"     bo'lakli: {sp.piecewise_fold(net.rewrite(sp.Piecewise))}")
print(f"     σ siz:   L₂(L₁(x)) = {sp.expand(L2(L1))}   ← chiziqli, bukilish yo'q")


head("F. TESKARI VA BO'LAKLI")


def inverse(expr):
    sol = sp.solve(sp.Eq(y, expr), x)
    return [s.subs(y, x) for s in sol]


print(f"[F1] f = 3x − 6,  f⁻¹ = {inverse(3*x - 6)}")
f2 = (2*x + 1)/(x - 3)
inv2 = inverse(f2)[0]
print(f"[F2] f = {f2},  f⁻¹ = {sp.simplify(inv2)}")
print(f"     f(4) = {f2.subs(x, 4)},  f⁻¹(f(4)) = {inv2.subs(x, f2.subs(x, 4))}")
print(f"     f(f⁻¹(x)) = {sp.simplify(f2.subs(x, inv2))}   ← x chiqishi kerak")
print(f"[F3] x² teskarisi (x ≥ 0): {sp.solve(sp.Eq(y, x**2), x)}  ← ikkita yechim = bir qiymatli emas; x≥0 da √x")

pw = sp.Piecewise((x + 2, x < 0), (x**2, x <= 2), (4, True))
print(f"[F4] f = {pw}")
for v in (-3, 0, 1.5, 2, 5):
    print(f"     f({v}) = {pw.subs(x, v)}")
left0, right0 = (x + 2).subs(x, 0), (x**2).subs(x, 0)      # chap bo'lak va o'ng bo'lak x=0 da
left2, right2 = (x**2).subs(x, 2), 4
print(f"     x=0: chapdan {left0}, o'ngdan {right0} → {'uzluksiz' if left0 == right0 else 'UZILISH (sakrash)'}")
print(f"     x=2: chapdan {left2}, o'ngdan {right2} → {'uzluksiz' if left2 == right2 else 'UZILISH'}")

# clip(z) = 1 ⟺ z ≥ 1 (yuqori tekis qism); = 0 ⟺ z = 0 (o'rta qism); = 2 — range tashqarisi
print(f"[F5] clip(2x−3) = 1  ⟺  2x−3 ≥ 1  ⟺  {sp.solve(2*x - 3 >= 1, x)}")
print(f"     clip(2x−3) = 0  ⟺  2x−3 = 0  ⟺  x = {sp.solve(sp.Eq(2*x - 3, 0), x)}")
print(f"     clip(2x−3) = 2:  range [−1, 1], 2 ∉ range → yechim yo'q")
import numpy as _np
_c = lambda z: _np.maximum(-1, _np.minimum(1, z))
print(f"     sonli: clip(2·2−3)={_c(1)}, clip(2·1.5−3)={_c(0)}, max clip = {_c(_np.linspace(-9, 9, 999)).max()}")

print("\n" + LINE + "\nTugadi. Farq bo'lsa — avval o'zingni, keyin kodni tekshir.\n" + LINE)
