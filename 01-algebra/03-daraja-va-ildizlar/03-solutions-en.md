# Solutions — Powers and Roots

> ⛔ **Haven't solved it yourself? Close this.** Mistakes → `00-mindset/xatolar-daftari.md`.

---

## A. Computing powers

### A1
```
2⁵ = 32          (−3)³ = −27        (−2)⁴ = 16
−2⁴ = −16        (1/2)³ = 1/8       0.1² = 0.01
```
`(−2)⁴`: a negative number multiplied 4 times → positive. `−2⁴ = −(2⁴)`: power first, then negate.

### A2
```
5⁰ = 1     (−7)⁰ = 1     0⁵ = 0     (2/3)⁰ = 1     0⁰ — UNDEFINED
```
`0⁵ = 0` (a power of zero); `0⁰` is where two rules collide (`a⁰ = 1` vs `0ⁿ = 0`).

### A3
```
2⁻³ = 1/8       (1/3)⁻² = 9       10⁻⁴ = 0.0001       (−2)⁻³ = −1/8       (2/5)⁻¹ = 5/2
```

### A4
```
3⁻² + 3⁻¹ = 1/9 + 3/9 = 4/9        2⁻¹ − 4⁻¹ = 1/2 − 1/4 = 1/4        (2⁻¹)⁻¹ = 2
```

### A5
```
2¹⁰ = 1024 > 1000 = 10³        3⁴ = 81 > 64 = 4³        2⁻³ = 0.125 > 0.111 ≈ 3⁻²
```

### A6 — `x = −2`
```
x² = 4     −x² = −4     (−x)² = 4     x³ = −8     x⁻² = 1/4     −x⁻² = −1/4
```

### A7 — last digit of `2¹⁰⁰`
```
Last digits of 2ⁿ:  2, 4, 8, 6,  2, 4, 8, 6, ...     period 4
100 = 4 · 25, remainder 0  →  4th position in the cycle  →  6
```
**Answer:** 6. (Check: `2⁴ = 16`, `2⁸ = 256`, `2¹² = 4096` — all end in 6 ✓)

---

## B. Power rules

### B1
```
a⁸     a⁵     a⁸     8a³     a²/b²     a³
```

### B2
```
2³·2⁴ = 2⁷ = 128  (NOT 4⁷!)      3⁵/3³ = 9      (5²)³ = 5⁶ = 15 625      2³·5³ = 10³ = 1000
```

### B3
```
x⁴y⁶ · x⁻¹y⁻¹ = x³y⁵
```

### B4
```
(a⁻²b³)⁻¹ = a²b⁻³;   a²b⁻³ / (a·b⁻²) = a^(2−1) b^(−3+2) = a b⁻¹ = a/b
```

### B5
```
4x⁶ · 1/(3x) = (4/3)x⁵
```

### B6
```
(2²)ⁿ(2³)ⁿ/2ⁿ = 2^(2n+3n−n) = 2^(4n) = 16ⁿ
```

### B7
```
(a) (aᵐ)ⁿ = aᵐ · aᵐ · ... · aᵐ (n times) = a^(m+m+...+m) = a^(mn)   ∎
(b) (2³)² = 64,   2^(3²) = 2⁹ = 512.   Different — parentheses matter.
(c) (3²)^(1/2) = 3^(2·1/2) = 3¹ = 3.   So 9^(1/2) = √9 = 3 ✓
```

---

## C. Roots

### C1
```
7     0.5     −2     3     4/3     1/3     −2
```

### C2
```
√((−5)²) = √25 = 5           (NOT −5: even roots are ≥ 0)
√(x²) at x = −3: √9 = 3 = |−3|
³√((−5)³) = ³√(−125) = −5    ← THE DIFFERENT ONE: odd roots keep the sign
```
In general `√(x²) = |x|` but `³√(x³) = x`.

### C3
```
√50 = 5√2     √72 = 6√2     √200 = 10√2     ³√54 = 3·³√2     √12 + √27 = 2√3 + 3√3 = 5√3
```

### C4
```
√16 = 4     √36 = 6     √25 = 5     ³√64 = 4
```

### C5
```
1/√2 = √2/2
3/√12 = 3/(2√3) = √3/2
1/(√3 − 1) = (√3 + 1)/((√3 − 1)(√3 + 1)) = (√3 + 1)/2
2/(√5 + √3) = 2(√5 − √3)/(5 − 3) = √5 − √3
```

### C6
```
(√5 + √3)² = 8 + 2√15        (√7 − √2)(√7 + √2) = 5        (2√3)² = 12
```

### C7
```
√25 = 5  vs  3 + 4 = 7.   Not equal.
When equal?  Square: a + b = a + 2√(ab) + b  →  √(ab) = 0  →  a = 0 or b = 0. Only then.
```

### C8
```
x² − 6x + 9 = (x − 3)²  →  √((x − 3)²) = |x − 3|
x = 1: 2      x = 5: 2
|x − 3| = { x − 3 for x ≥ 3;  3 − x for x < 3 }
```
🔴 Writing `x − 3` would give `−2` at `x = 1` — a root can't be negative.

---

## D. Rational exponents

### D1
```
8^(1/3) = 2     16^(1/4) = 2     27^(2/3) = 3² = 9     4^(3/2) = 2³ = 8
32^(−1/5) = 1/2     81^(−3/4) = 1/3³ = 1/27
```

### D2
```
x^(1/2)     x^(2/3)     x^(−1/2)     x^(5/4)     x^(3/2)
```

### D3
```
x^(1/2 + 1/3) = x^(5/6)     x^(2/4) = √x     x^(2/3 · 3/2) = x     x^(6/3) = x²
```

### D4
```
√x · ³√x = x^(5/6) = ⁶√(x⁵)
√(x√x) = √(x^(3/2)) = x^(3/4)
```

### D5
```
0.1     16^(1/2) = 4     4^(1/2) = 2     (2/3)² = 4/9
```

### D6 — Proof
```
Assume (aᵖ)^q = a^(pq) holds for p = 1/2, q = 2.
Then (a^(1/2))² = a¹ = a, so a^(1/2) is a number whose square is a: √a or −√a.
By convention a^(1/2) > 0 (the power function stays positive) → a^(1/2) = √a.   ∎
Likewise (a^(1/n))ⁿ = a → a^(1/n) = ⁿ√a,  and  a^(m/n) = (a^(1/n))ᵐ = (ⁿ√a)ᵐ.   ∎
```

> The definition of rational exponents is not arbitrary — it is the **only** one that
> keeps the rules intact.

---

## E. Equations and inequalities

### E1
```
x = 3      x = −4      x = ±2      x = ±√5      ∅
```

### E2
```
2ˣ = 2⁵ → x = 5      3ˣ = 3⁻² → x = −2      5ˣ = 5⁰ → x = 0
2⁻ˣ = 2³ → x = −3    2²ˣ = 2³ → x = 3/2
```

### E3
```
x^(3/2) = 8 → x = 8^(2/3) = 4   (check: 4^(3/2) = 8 ✓)
x^(−2) = 1/25 → x² = 25 → x = ±5
x^(1/3) = −2 → x = (−2)³ = −8
```

### E4
```
√(x − 1) = 3 → x = 10
³√(2x + 1) = 3 → 2x + 1 = 27 → x = 13
√(x + 2) = x → x ≥ 0;  x² − x − 2 = 0 → (x − 2)(x + 1) = 0 → x = 2  (−1 rejected)
```

### E5
```
x² < 9 → (−3, 3)                    x² ≥ 16 → (−∞, −4] ∪ [4, ∞)
x³ > 8 → x > 2                      √x < 3 → 0 ≤ x < 9  (domain!)
2ˣ > 2⁴ → x > 4                     (1/2)ˣ > (1/2)³ → x < 3  (base < 1 → decreasing → FLIP)
```
Check the last: `x = 0`: `1 > 1/8` ✓. `x = 4`: `1/16 > 1/8`? No ✓.

### E6
```
(a) (√2 + √3)² = 5 + 2√6  vs  10  →  2√6 vs 5  →  24 vs 25  →  √2 + √3 < √10
(b) 2³⁰⁰ = 8¹⁰⁰,  3²⁰⁰ = 9¹⁰⁰,  8 < 9  →  2³⁰⁰ < 3²⁰⁰
```

---

## F. Large and small numbers

### F1
```
3.4 × 10⁶        5.2 × 10⁻⁴
6.02 × 10²³ = 602 000 000 000 000 000 000 000   (602 followed by 21 zeros)
1.6 × 10⁻¹⁹ = 0.000 000 000 000 000 000 16      (18 zeros after the point, then 16)
```

### F2
```
6 × 10³        2 × 10⁵        4 × 10⁶        2 × 10³
```

### F3
```
0.1 mm × 4.4 × 10¹² = 4.4 × 10¹¹ mm = 4.4 × 10⁵ km = 440 000 km > 384 400 km → YES, past the Moon.
```

### F4
```
(a) n:  1  2  3  4  5   6   7   8   9   10
    n²: 1  4  9 16 25  36  49  64  81  100
    2ⁿ: 2  4  8 16 32  64 128 256 512 1024
    2ⁿ > n²: true at n = 1, equal at n = 2 and 4, false at n = 3, ALWAYS true for n ≥ 5.

(b) 175 × 10⁹ × 4 B = 7 × 10¹¹ B = 700 GB;  float16: 350 GB.
    (Why a single 80 GB GPU can't hold it — model parallelism is needed.)

(c) 2²⁴ = 16 777 216. Integers above this are not all exactly representable in float32:
    16 777 217 rounds to 16 777 216. Use int32/int64 for large indices, token IDs, counters.
```

---

## G. 🔗 AI

### G1 — L2 norm
```
(a) 5,  3,  2
(b) (0.6, 0.8);  √(0.36 + 0.64) = 1 ✓
(c) √n.   n = 64 → 8.   n = 512 → 16√2 ≈ 22.6
```

### G2 — `1/√d_k`
```
(a) d:     64     128     256     512    4096
    √d:     8    11.31     16    22.63     64
    1/√d: 0.125  0.0884  0.0625  0.0442  0.0156
(b) [64, 16, 0]/8 = [8, 2, 0]
(c) q·k is a sum of d terms, each ~±1 with random signs. Most cancel; the leftover
    imbalance is ~√d, not d (variances add → d, std = √d — proved in probability).
    Dividing by √d brings typical scores to ~1 so softmax doesn't saturate.
    Dividing by d would make them tiny and flatten softmax.
```

### G3 — He init
```
(a) √(2/512) = 1/16 = 0.0625    √(2/128) = 1/8 = 0.125    √(2/2048) = 1/32 = 0.03125    √(2/8) = 0.5
(b) A neuron sums n inputs: Σwᵢxᵢ ~ w·√n (as in G2-c). To keep the sum ~1: w ~ 1/√n.
    More inputs → each must contribute less.
(c) 2/n = 0.0025 → n = 800
```

### G4 — RMS
```
(a) squares (1, 4, 4, 16), sum 25, /4 = 6.25, √ = 2.5
(b) x' = (0.4, −0.8, 0.8, 1.6)
(c) RMS(x') = √((0.16 + 0.64 + 0.64 + 2.56)/4) = √1 = 1.
    That's the point: every layer's output has the same "size" — no explosion, no vanishing.
    In general RMS(x/RMS(x)) = 1 always (norm property ‖cv‖ = |c|‖v‖).
```

### G5 — LR schedule
```
(a) 0.1,  0.05,  0.01,  0.001
(b) 0.1/√t < 0.001 → √t > 100 → t > 10 000
(c) At t = w both arguments of min equal w^(−0.5):
    η = (d·w)^(−0.5) = 1/√2 048 000 ≈ 1/1431 ≈ 7.0 × 10⁻⁴
(d) t < w: min = t·w^(−1.5), linear in t → INCREASES (warmup)
    t > w: min = t^(−0.5) → DECREASES (inverse-sqrt decay)
    Shape: linear ramp up, peak at t = w, then 1/√t decay.
```

> 🔗 This is the actual formula from "Attention Is All You Need" (§5.3). You just analyzed
> it completely using nothing but power rules.

---

## 🎓 Final note

Blank page: redo **D6** (the proof) and **E6** (the comparisons). If you can — you know it.
