#!/usr/bin/env python3
"""
Tenglamalar — yechimlarni tekshirish / Equations — verification

⚠️  Bu faylni FAQAT o'z yechimingni qog'ozga yozganingdan keyin ishga tushir.

Ishga tushirish:  python3 01_tenglamalar.py
Talab:            pip install sympy
"""

import sympy as sp

x, y, z, a, m, t = sp.symbols('x y z a m t')

LINE = "─" * 70


def show(tag, title, expected, got):
    """Bitta masalani chiroyli chiqarish."""
    print(f"\n[{tag}] {title}")
    print(f"    Kutilgan / Expected : {expected}")
    print(f"    SymPy               : {got}")


print(LINE)
print("A. CHIZIQLI TENGLAMALAR / LINEAR EQUATIONS")
print(LINE)

show("A1", "3x - 7 = 5x + 9", "{-8}",
     sp.solveset(sp.Eq(3*x - 7, 5*x + 9), x, domain=sp.S.Reals))

show("A2", "(2x-1)/3 - (x+2)/4 = 1", "{22/5}",
     sp.solveset(sp.Eq((2*x - 1)/3 - (x + 2)/4, 1), x, domain=sp.S.Reals))

show("A3", "5(x-3) - 2x = 3x - 15", "Reals (ayniyat / identity)",
     sp.solveset(sp.Eq(5*(x - 3) - 2*x, 3*x - 15), x, domain=sp.S.Reals))

show("A4", "4(x+1) - 3 = 4x + 2", "EmptySet (yechim yo'q)",
     sp.solveset(sp.Eq(4*(x + 1) - 3, 4*x + 2), x, domain=sp.S.Reals))

print("\n[A5] (a-2)x = a^2 - 4   — parametrli / with a parameter")
print("    Kutilgan: a != 2 -> x = a+2  |  a = 2 -> barcha x (Reals)")
print(f"    a != 2  (masalan a=5): x = {sp.solve(sp.Eq((5-2)*x, 5**2 - 4), x)}  (kutilgan 7 = a+2)")
print(f"    a == 2               : {sp.solveset(sp.Eq(0*x, 0), x, domain=sp.S.Reals)}")

print("\n[A6] (m^2-9)x = m-3     — parametrli / with a parameter")
print("    Kutilgan: m != ±3 -> x = 1/(m+3)  |  m = 3 -> Reals  |  m = -3 -> EmptySet")
for mv in (5, 3, -3):
    coef, rhs = mv**2 - 9, mv - 3
    sol = sp.solveset(sp.Eq(coef*x, rhs), x, domain=sp.S.Reals)
    note = f"1/(m+3) = {sp.Rational(1, mv+3)}" if mv not in (3, -3) else ""
    print(f"    m = {mv:>2} : {sol}   {note}")


print("\n" + LINE)
print("B. KVADRAT TENGLAMALAR / QUADRATIC EQUATIONS")
print(LINE)

show("B1", "x^2 - 5x + 6 = 0", "{2, 3}",
     sp.solveset(sp.Eq(x**2 - 5*x + 6, 0), x, domain=sp.S.Reals))

show("B2", "2x^2 + 3x - 2 = 0", "{-2, 1/2}",
     sp.solveset(sp.Eq(2*x**2 + 3*x - 2, 0), x, domain=sp.S.Reals))

sol_b3 = sp.solveset(sp.Eq(x**2 + 6*x + 2, 0), x, domain=sp.S.Reals)
show("B3", "x^2 + 6x + 2 = 0  (to'la kvadratga to'ldirish)", "{-3 - sqrt(7), -3 + sqrt(7)}", sol_b3)
print(f"    Son ko'rinishida    : {[sp.nsimplify(v).evalf(6) for v in sol_b3]}")
print(f"    (x+3)^2 - 7 ekanini tekshiramiz: {sp.expand((x + 3)**2 - 7)}  <- x^2+6x+2 bo'lishi kerak")

show("B4", "3x^2 - 12 = 0", "{-2, 2}",
     sp.solveset(sp.Eq(3*x**2 - 12, 0), x, domain=sp.S.Reals))

print("\n[B5] x^2 - 7x + 12 = 0  ->  x1^2 + x2^2 = ?")
r = sp.solve(sp.Eq(x**2 - 7*x + 12, 0), x)
print(f"    Ildizlar            : {r}")
print(f"    Viyet orqali        : (x1+x2)^2 - 2*x1*x2 = 7**2 - 2*12 = {7**2 - 2*12}")
print(f"    To'g'ridan-to'g'ri  : {sum(v**2 for v in r)}   (kutilgan 25)")

print("\n[B6] x^2 - 2mx + (m+2) = 0  aynan bitta ildizga ega  ->  D = 0")
D = sp.discriminant(x**2 - 2*m*x + (m + 2), x)
print(f"    D                   : {sp.simplify(D)}")
print(f"    D = 0 yechimi       : {sp.solve(sp.Eq(D, 0), m)}   (kutilgan [-1, 2])")
for mv in (2, -1):
    print(f"    m = {mv:>2}  ->  ildiz: {sp.solveset(sp.Eq(x**2 - 2*mv*x + (mv + 2), 0), x, domain=sp.S.Reals)}")

show("B7", "x^4 - 5x^2 + 4 = 0", "{-2, -1, 1, 2}",
     sp.solveset(sp.Eq(x**4 - 5*x**2 + 4, 0), x, domain=sp.S.Reals))


print("\n" + LINE)
print("C. RATSIONAL / IRRATSIONAL / MODULLI")
print(LINE)

show("C1", "(x+1)/(x-2) = 3", "{7/2}",
     sp.solveset(sp.Eq((x + 1)/(x - 2), 3), x, domain=sp.S.Reals))

print("\n[C2] 1/(x-1) + 1/(x+1) = 2/(x^2-1)")
print("    ODZ                 : x != 1, x != -1")
raw = sp.solve(sp.Eq(1/(x - 1) + 1/(x + 1), 2/(x**2 - 1)), x)
print(f"    solve() natijasi    : {raw}   <- SymPy ODZ ni hisobga oladi")
print("    Kutilgan            : [] (EmptySet) — x=1 begona ildiz")

print("\n[C3] x/(x-3) - 2 = 3/(x-3)")
print("    ODZ                 : x != 3")
print(f"    solve() natijasi    : {sp.solve(sp.Eq(x/(x - 3) - 2, 3/(x - 3)), x)}   (kutilgan [])")

show("C4", "sqrt(x+5) = x - 1", "{4}",
     sp.solveset(sp.Eq(sp.sqrt(x + 5), x - 1), x, domain=sp.S.Reals))

show("C5", "sqrt(2x+3) = x", "{3}",
     sp.solveset(sp.Eq(sp.sqrt(2*x + 3), x), x, domain=sp.S.Reals))

show("C6", "|2x - 3| = 5", "{-1, 4}",
     sp.solveset(sp.Eq(sp.Abs(2*x - 3), 5), x, domain=sp.S.Reals))

show("C7", "|x - 1| = 2x + 3", "{-2/3}",
     sp.solveset(sp.Eq(sp.Abs(x - 1), 2*x + 3), x, domain=sp.S.Reals))


print("\n" + LINE)
print("D. SISTEMALAR / SYSTEMS")
print(LINE)

print("\n[D1] 2x + y = 7 ;  x - y = 2")
print(f"    {sp.solve([sp.Eq(2*x + y, 7), sp.Eq(x - y, 2)], [x, y])}   (kutilgan x=3, y=1)")

print("\n[D2] 3x + 2y = 16 ;  5x - 2y = 0")
print(f"    {sp.solve([sp.Eq(3*x + 2*y, 16), sp.Eq(5*x - 2*y, 0)], [x, y])}   (kutilgan x=2, y=5)")

print("\n[D3] x + 2y = 4 ;  2x + 4y = 9      <- parallel chiziqlar")
print(f"    {sp.solve([sp.Eq(x + 2*y, 4), sp.Eq(2*x + 4*y, 9)], [x, y])}   (kutilgan [] — yechim yo'q)")

print("\n[D4] x + 2y = 4 ;  2x + 4y = 8      <- ustma-ust chiziqlar")
sol_d4 = sp.solve([sp.Eq(x + 2*y, 4), sp.Eq(2*x + 4*y, 8)], [x, y])
print(f"    {sol_d4}   (kutilgan: x = 4 - 2y, y istalgan -> cheksiz ko'p yechim)")
print("    Parametr bilan      : (x, y) = (4 - 2t, t),  t in R")

print("\n[D5] x+y+z=6 ;  2x-y+z=3 ;  x+2y-z=2")
sol_d5 = sp.solve([sp.Eq(x + y + z, 6), sp.Eq(2*x - y + z, 3), sp.Eq(x + 2*y - z, 2)], [x, y, z])
print(f"    {sol_d5}   (kutilgan x=1, y=2, z=3)")

print("\n    Xuddi shu narsa matritsa ko'rinishida (linear algebra oldi ko'rinishi):")
A = sp.Matrix([[1, 1, 1], [2, -1, 1], [1, 2, -1]])
b = sp.Matrix([6, 3, 2])
print(f"    A = {A.tolist()}")
print(f"    b = {b.T.tolist()[0]}")
print(f"    A^-1 * b = {(A.inv() * b).T.tolist()[0]}")
print(f"    rank(A) = {A.rank()}  (3 ta noma'lum, rank 3 -> yagona yechim)")

print("\n" + LINE)
print("Tugadi. Javoblaring mos keldimi? Mos kelmasa — avval O'ZINGNI qayta tekshir,")
print("keyin kodni. Xatoni 00-mindset/xatolar-daftari.md ga yoz.")
print(LINE)
