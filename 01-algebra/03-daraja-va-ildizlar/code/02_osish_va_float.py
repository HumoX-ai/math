#!/usr/bin/env python3
"""F bloki — o'sish va kompyuter sonlari. Talab: numpy."""
import numpy as np
LINE = "═" * 72

print(LINE + "\nF1–F2 — STANDART KO'RINISH\n" + LINE)
for v in (3_400_000, 0.00052, 6.02e23, 1.6e-19):
    print(f"  {v!s:>14}  =  {v:.2e}")
print(f"  (3e8)(2e-5) = {3e8*2e-5:.0e}   (8e12)/(4e7) = {8e12/4e7:.0e}   (2e3)² = {(2e3)**2:.0e}   √(4e6) = {np.sqrt(4e6):.0e}")

print("\n" + LINE + "\nF3 — QOG'OZ BUKLASH\n" + LINE)
thick_mm = 0.1 * 2**42
print(f"  2⁴² = {2**42:,}")
print(f"  0.1 mm × 2⁴² = {thick_mm:.3e} mm = {thick_mm/1e6:,.0f} km   (Oygacha 384 400 km → {'UZOQROQ ✓' if thick_mm/1e6 > 384400 else 'yaqinroq'})")
for k in (10, 20, 30, 42):
    print(f"    {k:>2} marta → {0.1*2**k/1e6:>16,.6f} km")

print("\n" + LINE + "\nF4a — n² vs 2ⁿ\n" + LINE)
print(f"  {'n':>3} {'n²':>8} {'2ⁿ':>14}  2ⁿ>n²?")
for k in list(range(1, 11)) + [20, 30, 64]:
    print(f"  {k:>3} {k**2:>8} {2**k:>14,}  {'✓' if 2**k > k**2 else ('=' if 2**k == k**2 else '✗')}")
print("  ➜ n ≥ 5 dan boshlab doim ✓. Polinomial vs eksponensial.")

print("\n" + LINE + "\nF4b — MODEL XOTIRASI\n" + LINE)
N = 175e9
for name, B in (("float32", 4), ("float16/bf16", 2), ("int8", 1), ("int4", 0.5)):
    print(f"  GPT-3 175B × {B:>3} bayt ({name:>12}) = {N*B:.1e} bayt = {N*B/1e9:>6,.0f} GB  →  80GB GPU: {N*B/80e9:.1f} ta")

print("\n" + LINE + "\nF4c — FLOAT CHEGARALARI (hammasi 2ⁿ)\n" + LINE)
for dt in (np.float32, np.float16):
    fi = np.finfo(dt)
    print(f"  {dt.__name__:>8}: bits={fi.bits}  mantissa={fi.nmant}  eps=2^−{fi.nmant}={fi.eps:.3e}  max={fi.max:.3e}  tiny={fi.tiny:.3e}")
print(f"  bfloat16: bits=16  mantissa=7   eps=2^−7={2**-7:.3e}  max≈3.39e38 (float32 kabi range, kam aniqlik)")

print("\n  2²⁴ = 16 777 216 dan keyin float32 butun sonlarni yo'qotadi:")
for v in (16_777_215, 16_777_216, 16_777_217, 16_777_218, 16_777_219):
    f = np.float32(v)
    print(f"    float32({v}) = {int(f):,}   {'✓' if int(f) == v else '✗ YO`QOLDI'}")

print("\n  0.1 + 0.2 == 0.3 ?")
s = 0.1 + 0.2
print(f"    0.1 + 0.2 = {s!r}   ==0.3 → {s == 0.3}   |   abs(diff) < 1e-9 → {abs(s - 0.3) < 1e-9}  ← shunday tekshir")
print(f"    0.1 ikkilikda: {0.1:.20f}  (cheksiz kasr, kesilgan)")

print("\n  float16 overflow (max 65504):")
with np.errstate(over="ignore"):                       # overflow — aynan ko'rsatmoqchi bo'lgan narsa
    for v in (60000, 65504, 65505, 70000):
        print(f"    float16({v}) = {np.float16(v)}")
print("  ➜ Shuning uchun fp16 training'da loss scaling; bf16 da bu muammo yo'q (8-bit eksponent).")

print("\n  Softmax overflow va yechimi (log-sum-exp):")
z = np.array([1000.0, 999.0, 998.0], dtype=np.float32)
with np.errstate(over="ignore", invalid="ignore"):
    naive = np.exp(z) / np.exp(z).sum()
stable = np.exp(z - z.max()) / np.exp(z - z.max()).sum()
print(f"    exp(1000) to'g'ridan-to'g'ri: {naive}   ← inf/nan")
print(f"    exp(z − max z):               {stable}   ← to'g'ri")
print("\n" + LINE)
