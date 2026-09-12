#!/usr/bin/env python3
"""
Tengsizliklar — yechimlarni tekshirish / Inequalities — verification

⚠️  Avval qog'ozda yech, keyin ishga tushir.

Ishga tushirish:  python3 02_tengsizliklar.py
Talab:            pip install sympy
"""

import sympy as sp

x = sp.Symbol('x', real=True)
LINE = "─" * 70


def check(tag, expr_str, expr, expected):
    """Tengsizlikni SymPy bilan yechib, kutilgan javob bilan solishtiradi."""
    sol = sp.solveset(expr, x, domain=sp.S.Reals)
    print(f"\n[{tag}] {expr_str}")
    print(f"    Kutilgan / Expected : {expected}")
    print(f"    SymPy               : {sp.pretty(sol, use_unicode=True)}")
    return sol


def sample_test(tag, f, points):
    """Sonli tekshiruv: bir nechta nuqtada tengsizlik bajariladimi?"""
    print(f"    Sonli tekshiruv     :", end=" ")
    parts = []
    for p in points:
        ok = bool(f(p))
        parts.append(f"x={p}: {'✓' if ok else '✗'}")
    print("   ".join(parts))


print(LINE)
print("E. TENGSIZLIKLAR / INEQUALITIES")
print(LINE)

check("E1", "-3x + 5 > 11", -3*x + 5 > 11, "(-oo, -2)")
sample_test("E1", lambda p: -3*p + 5 > 11, [-3, -2, 0])

# Qo'sh tengsizlik uchun reduce_inequalities ishlatiladi
sol_e2 = sp.reduce_inequalities([2 <= 3*x - 4, 3*x - 4 < 11], x)
print("\n[E2] 2 <= 3x - 4 < 11")
print("    Kutilgan / Expected : [2, 5)")
print(f"    SymPy               : {sol_e2}")
sample_test("E2", lambda p: 2 <= 3*p - 4 < 11, [1, 2, 4, 5])

check("E3", "x^2 - x - 6 <= 0", x**2 - x - 6 <= 0, "[-2, 3]")
sample_test("E3", lambda p: p**2 - p - 6 <= 0, [-3, -2, 0, 3, 4])

check("E4", "x^2 + 4x + 5 > 0", x**2 + 4*x + 5 > 0, "Reals (barcha x)")
print(f"    To'la kvadrat       : x^2+4x+5 = {sp.factor(sp.expand((x+2)**2 + 1))} = (x+2)^2 + 1 >= 1")
print(f"    Diskriminant        : D = {sp.discriminant(x**2 + 4*x + 5, x)}  (< 0 -> ildiz yo'q)")

check("E5", "-x^2 + 4x - 3 > 0", -x**2 + 4*x - 3 > 0, "(1, 3)")
sample_test("E5", lambda p: -p**2 + 4*p - 3 > 0, [0, 1, 2, 3, 4])

check("E6", "x^2 - 4x >= 0", x**2 - 4*x >= 0, "(-oo, 0] U [4, oo)")
sample_test("E6", lambda p: p**2 - 4*p >= 0, [-1, 0, 2, 4, 5])

check("E7", "(x-1)/(x+2) >= 0", (x - 1)/(x + 2) >= 0, "(-oo, -2) U [1, oo)")
print("    Ishoralar jadvali   :")
for a, b, tp in [("-oo", "-2", -3), ("-2", "1", 0), ("1", "+oo", 2)]:
    val = sp.Rational(tp - 1, tp + 2)
    print(f"       ({a:>3}, {b:>4})  sinov x={tp:>2}  ->  {val}  ->  {'+' if val > 0 else '-'}")
print("    ⚠️  x = -2 HECH QACHON kirmaydi (maxraj noli)")

check("E8", "(x+3)(x-1)/(x-2)^2 < 0", (x + 3)*(x - 1)/(x - 2)**2 < 0, "(-3, 1)")
print("    (x-2)^2 > 0 har doim -> ishoraga ta'sir qilmaydi")
sample_test("E8", lambda p: (p + 3)*(p - 1)/(p - 2)**2 < 0, [-4, -3, 0, 1, 3])

check("E9", "(x-2)/(x+1) < 1", (x - 2)/(x + 1) < 1, "(-1, oo)")
print(f"    Chapga yig'amiz     : (x-2)/(x+1) - 1 = {sp.simplify((x - 2)/(x + 1) - 1)}")
print("    -3/(x+1) < 0  <=>  x+1 > 0  <=>  x > -1")
print("    🔴 Krest-nakrest ko'paytirish 'x < 3' beradi — NOTO'G'RI:")
sample_test("E9", lambda p: (p - 2)/(p + 1) < 1, [-2, -1.5, 0, 2, 5])
print("       x=-2 va x=-1.5 da tengsizlik BAJARILMAYDI, lekin 'x<3' ularni kiritardi.")

check("E10", "|x - 4| < 3", sp.Abs(x - 4) < 3, "(1, 7)")
print("    Masofa talqini      : x, 4 dan 3 birlikdan yaqin")

check("E11", "|2x + 1| >= 5", sp.Abs(2*x + 1) >= 5, "(-oo, -3] U [2, oo)")
sample_test("E11", lambda p: abs(2*p + 1) >= 5, [-4, -3, 0, 2, 3])

print("\n[E12] Isbot: x + 1/x >= 2   (x > 0)")
expr = x + 1/x - 2
print(f"    x + 1/x - 2 = {sp.simplify(expr)} = {sp.factor(sp.together(expr))}")
print("    (x-1)^2 / x  >= 0   chunki  (x-1)^2 >= 0  va  x > 0     ∎")
print("    Sonli tekshiruv     :", end=" ")
for p in [sp.Rational(1, 4), sp.Rational(1, 2), 1, 2, 10]:
    v = p + sp.Rational(1, 1)/p
    print(f"x={p}: {v} ({'=' if v == 2 else '>'}2)", end="   ")
print()
print("    Tenglik faqat x = 1 da.")
print(f"    x < 0 bo'lsa: x=-2 -> {-2 + sp.Rational(1,-2)} <= -2  (tengsizlik TESKARI)")

print("\n" + LINE)
print("CHEGARA NUQTALARI TESTI / BOUNDARY TEST")
print(LINE)
print("Eng ko'p xato chegara nuqtalarida qilinadi. Har birini tekshir:\n")
boundary = [
    ("E3: x^2-x-6 <= 0", lambda p: p**2 - p - 6 <= 0, [-2, 3], "ikkalasi ham KIRADI (<=)"),
    ("E6: x^2-4x >= 0", lambda p: p**2 - 4*p >= 0, [0, 4], "ikkalasi ham KIRADI (>=)"),
    ("E7: (x-1)/(x+2) >= 0", lambda p: (p - 1)/(p + 2) >= 0 if p != -2 else None, [1], "x=1 KIRADI"),
    ("E11: |2x+1| >= 5", lambda p: abs(2*p + 1) >= 5, [-3, 2], "ikkalasi ham KIRADI (>=)"),
]
for name, f, pts, note in boundary:
    res = "  ".join(f"x={p}: {'✓' if f(p) else '✗'}" for p in pts)
    print(f"  {name:<28} {res:<24} {note}")

print("\n" + LINE)
print("Tugadi. Interval chegaralarini ( ) va [ ] to'g'ri yozdingmi?")
print("Bu — tengsizliklardagi 1-raqamli xato manbai.")
print(LINE)
