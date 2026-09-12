#!/usr/bin/env python3
"""Daraja va ildizlar — A–E bloklarini tekshirish. Talab: sympy, numpy."""
import sympy as sp
import numpy as np
from fractions import Fraction as Fr

x, a, b, n = sp.symbols('x a b n', positive=True)
xr = sp.Symbol('x', real=True)
LINE = "─" * 70
head = lambda s: print("\n" + LINE + f"\n{s}\n" + LINE)

head("A. DARAJA HISOBLASH")
print(f"[A1] 2**5={2**5}  (-3)**3={(-3)**3}  (-2)**4={(-2)**4}  -2**4={-2**4}  ← Python'da ham har xil!")
print(f"     (1/2)**3={Fr(1,2)**3}  0.1**2={0.1**2:.4f}")
print(f"[A2] 5**0={5**0}  (-7)**0={(-7)**0}  0**5={0**5}  (2/3)**0={Fr(2,3)**0}  0**0 (Python)={0**0} ← kelishuv, matematikada aniqlanmagan")
print(f"[A3] 2**-3={Fr(2)**-3}  (1/3)**-2={Fr(1,3)**-2}  10**-4={10**-4}  (-2)**-3={Fr(-2)**-3}  (2/5)**-1={Fr(2,5)**-1}")
print(f"[A4] 3⁻²+3⁻¹={Fr(3)**-2 + Fr(3)**-1}   2⁻¹−4⁻¹={Fr(2)**-1 - Fr(4)**-1}   (2⁻¹)⁻¹={(Fr(2)**-1)**-1}")
print(f"[A5] 2¹⁰={2**10} vs 10³={10**3}  |  3⁴={3**4} vs 4³={4**3}  |  2⁻³={Fr(2)**-3}≈{float(Fr(2)**-3):.3f} vs 3⁻²={Fr(3)**-2}≈{float(Fr(3)**-2):.3f}")
xv = -2
print(f"[A6] x=-2:  x²={xv**2}  −x²={-xv**2}  (−x)²={(-xv)**2}  x³={xv**3}  x⁻²={Fr(xv)**-2}  −x⁻²={-Fr(xv)**-2}")
print(f"[A7] 2**100 = {2**100}  →  oxirgi raqam {2**100 % 10};  oxirgi raqamlar davri: {[2**k % 10 for k in range(1, 9)]}")

head("B. XOSSALAR")
print(f"[B1] a³a⁵={sp.simplify(a**3*a**5)}  a⁷/a²={sp.simplify(a**7/a**2)}  (a²)⁴={(a**2)**4}  (2a)³={sp.expand((2*a)**3)}  (a/b)²={(a/b)**2}  a⁵a⁻²={sp.simplify(a**5*a**-2)}")
print(f"[B2] 2³·2⁴={2**3*2**4} (=2⁷={2**7}, ≠4⁷={4**7})  3⁵/3³={3**5//3**3}  (5²)³={(5**2)**3}  2³·5³={2**3*5**3}")
y = sp.Symbol('y', positive=True)
print(f"[B3] (x²y³)²(xy)⁻¹ = {sp.simplify((x**2*y**3)**2*(x*y)**-1)}")
print(f"[B4] (a⁻²b³)⁻¹/(ab⁻²) = {sp.simplify((a**-2*b**3)**-1/(a*b**-2))}")
print(f"[B5] (2x³)²(3x)⁻¹ = {sp.simplify((2*x**3)**2*(3*x)**-1)}")
print(f"[B6] 4ⁿ8ⁿ/2ⁿ = {sp.simplify(4**n*8**n/2**n)} = {sp.powsimp(sp.simplify(4**n*8**n/2**n), force=True)}")
print(f"[B7] (2³)²={(2**3)**2}  2^(3²)={2**(3**2)}  |  (3²)^(1/2)={sp.sqrt(3**2)}")

head("C. ILDIZLAR")
print(f"[C1] √49={sp.sqrt(49)}  √0.25={np.sqrt(0.25)}  ³√(−8)={np.cbrt(-8):.0f}  ⁴√81={sp.root(81, 4)}  √(16/9)={sp.sqrt(sp.Rational(16, 9))}  ³√(1/27)={sp.root(sp.Rational(1, 27), 3)}  ⁵√(−32)={np.sign(-32)*abs(-32)**(1/5):.0f}")
print(f"     ⚠️ NumPy: (-8)**(1/3) = {(-8)**(1/3)}  ← nan/kompleks!  np.cbrt(-8) = {np.cbrt(-8)}")
print(f"[C2] √((−5)²)={sp.sqrt((-5)**2)}  √(x²) at x=−3: {sp.sqrt((-3)**2)}  ³√((−5)³)={np.cbrt((-5)**3):.0f}  |  umumiy: √(x²) = {sp.sqrt(xr**2)}")
for e in [sp.sqrt(50), sp.sqrt(72), sp.sqrt(200), sp.root(54, 3), sp.sqrt(12) + sp.sqrt(27)]:
    print(f"[C3] {e}")
print(f"[C4] √2√8={sp.sqrt(2)*sp.sqrt(8)}  √3√12={sp.sqrt(3)*sp.sqrt(12)}  √50/√2={sp.sqrt(50)/sp.sqrt(2)}  ³√4·³√16={sp.root(4,3)*sp.root(16,3)}")
for e in [1/sp.sqrt(2), 3/sp.sqrt(12), 1/(sp.sqrt(3) - 1), 2/(sp.sqrt(5) + sp.sqrt(3))]:
    print(f"[C5] {e}  =  {sp.radsimp(e)}")
print(f"[C6] (√5+√3)²={sp.expand((sp.sqrt(5)+sp.sqrt(3))**2)}  (√7−√2)(√7+√2)={sp.expand((sp.sqrt(7)-sp.sqrt(2))*(sp.sqrt(7)+sp.sqrt(2)))}  (2√3)²={sp.expand((2*sp.sqrt(3))**2)}")
print(f"[C7] √(9+16)={sp.sqrt(25)}  √9+√16={sp.sqrt(9)+sp.sqrt(16)}  →  teng emas.  (√(a+b))² − (√a+√b)² = {sp.expand(sp.sqrt(a+b)**2 - (sp.sqrt(a)+sp.sqrt(b))**2)} = 0 ⟺ ab = 0")
print(f"[C8] √(x²−6x+9) = {sp.sqrt(sp.factor(xr**2 - 6*xr + 9))}  →  x=1: {abs(1-3)},  x=5: {abs(5-3)}")

head("D. RATSIONAL KO'RSATKICH")
print(f"[D1] 8^(1/3)={sp.root(8,3)}  16^(1/4)={sp.root(16,4)}  27^(2/3)={sp.Integer(27)**sp.Rational(2,3)}  4^(3/2)={sp.Integer(4)**sp.Rational(3,2)}  32^(−1/5)={sp.Integer(32)**sp.Rational(-1,5)}  81^(−3/4)={sp.Integer(81)**sp.Rational(-3,4)}")
print(f"[D3] x^½·x^⅓={sp.simplify(x**sp.Rational(1,2)*x**sp.Rational(1,3))}  x^¾/x^¼={sp.simplify(x**sp.Rational(3,4)/x**sp.Rational(1,4))}  (x^⅔)^(3/2)={sp.simplify((x**sp.Rational(2,3))**sp.Rational(3,2))}  (x⁶)^⅓={sp.simplify((x**6)**sp.Rational(1,3))}")
print(f"[D4] √x·³√x={sp.simplify(sp.sqrt(x)*sp.root(x,3))}   √(x√x)={sp.simplify(sp.sqrt(x*sp.sqrt(x)))}")
print(f"[D5] 0.001^(1/3)={round(0.001**(1/3), 6)}  (1/16)^(−½)={sp.Rational(1,16)**sp.Rational(-1,2)}  0.25^(−½)={0.25**-0.5}  (8/27)^(⅔)={sp.Rational(8,27)**sp.Rational(2,3)}")
print(f"[D6] (a^(1/2))² = {sp.simplify((a**sp.Rational(1,2))**2)}  ← a chiqdi: a^(1/2) kvadrati a bo'lgan son = √a")

head("E. TENGLAMALAR VA TENGSIZLIKLAR")
X = sp.Symbol('x', real=True)
for eq, txt in [(sp.Eq(X**3, 27), "x³=27"), (sp.Eq(X**3, -64), "x³=−64"), (sp.Eq(X**4, 16), "x⁴=16"), (sp.Eq(X**2, 5), "x²=5"), (sp.Eq(X**4, -16), "x⁴=−16")]:
    print(f"[E1] {txt:>8}: {sp.solveset(eq, X, sp.S.Reals)}")
for eq, txt in [(sp.Eq(2**X, 32), "2ˣ=32"), (sp.Eq(3**X, sp.Rational(1, 9)), "3ˣ=1/9"), (sp.Eq(5**X, 1), "5ˣ=1"), (sp.Eq(sp.Rational(1, 2)**X, 8), "(½)ˣ=8"), (sp.Eq(4**X, 8), "4ˣ=8")]:
    sol = sp.solveset(eq, X, sp.S.Reals)
    print(f"[E2] {txt:>8}: {sp.FiniteSet(*[sp.nsimplify(sp.simplify(v)) for v in sol])}")
print(f"[E3] x^(3/2)=8: {sp.solveset(sp.Eq(x**sp.Rational(3,2), 8), x, sp.S.Reals)}   x⁻²=1/25: {sp.solveset(sp.Eq(X**-2, sp.Rational(1,25)), X, sp.S.Reals)}   x^(1/3)=−2: x = (−2)³ = {(-2)**3}")
print(f"[E4] √(x−1)=3: {sp.solveset(sp.Eq(sp.sqrt(X-1), 3), X, sp.S.Reals)}   ³√(2x+1)=3: {sp.solveset(sp.Eq(2*X+1, 27), X)}   √(x+2)=x: {sp.solveset(sp.Eq(sp.sqrt(X+2), X), X, sp.S.Reals)}")
for ineq, txt in [(X**2 < 9, "x²<9"), (X**2 >= 16, "x²≥16"), (X**3 > 8, "x³>8"), (sp.sqrt(X) < 3, "√x<3"), (2**X > 16, "2ˣ>16"), (sp.Rational(1, 2)**X > sp.Rational(1, 8), "(½)ˣ>1/8")]:
    print(f"[E5] {txt:>8}: {sp.pretty(sp.solveset(ineq, X, sp.S.Reals), use_unicode=True)}")
print(f"[E6] √2+√3 ≈ {float(sp.sqrt(2)+sp.sqrt(3)):.5f}  vs  √10 ≈ {float(sp.sqrt(10)):.5f}   →  {'<' if sp.sqrt(2)+sp.sqrt(3) < sp.sqrt(10) else '>'}")
print(f"     2³⁰⁰ raqamlar soni: {len(str(2**300))},  3²⁰⁰: {len(str(3**200))}   →  2³⁰⁰ {'<' if 2**300 < 3**200 else '>'} 3²⁰⁰")
print("\n" + LINE + "\nTugadi.\n" + LINE)
