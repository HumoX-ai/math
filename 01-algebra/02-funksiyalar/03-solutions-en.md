# Solutions — Functions

> ⛔ **If you haven't solved it yourself — close this.** Reading a solution gives the
> feeling of understanding, not understanding. Mistakes → `00-mindset/xatolar-daftari.md`.

---

## A. The concept, domain, range

### A1 — `f(x) = 2x² − 3x + 1`

```
f(0)  = 1
f(1)  = 2 − 3 + 1 = 0
f(−2) = 8 + 6 + 1 = 15

f(a+1) = 2(a+1)² − 3(a+1) + 1
       = 2a² + 4a + 2 − 3a − 3 + 1
       = 2a² + a
```

**Check:** `a = 0` → `f(1) = 0` ✓. `a = 1` → `f(2) = 3`; formula `2 + 1 = 3` ✓.

---

### A2 — `f(x) = √(x − 3) / (x − 5)`

```
Root:         x ≥ 3
Denominator:  x ≠ 5
```

**Answer:** `D = [3, 5) ∪ (5, +∞)`

---

### A3 — `g(x) = 1/(x² − 4) + √(6 − x)`

```
Denominator:  x ≠ ±2
Root:         x ≤ 6
```

**Answer:** `D = (−∞, −2) ∪ (−2, 2) ∪ (2, 6]`

---

### A4 — Which are functions?

| | Function? | Reason |
|---|---|---|
| (a) `y = x²` | ✅ | one `y` per `x` |
| (b) `x = y²` | ❌ | `x = 4` → `y = 2` **and** `y = −2` |
| (c) `y = \|x\|` | ✅ | one output |
| (d) `x² + y² = 1` | ❌ | `x = 0` → `y = ±1` (a circle fails the vertical line test) |
| (e) `y = 3` | ✅ | constant function — every `x` maps to `3` |

---

### A5 — Range

```
(a) x² ≥ 0  →  x² + 2 ≥ 2, reached at x = 0             E = [2, +∞)
(b) −|x| ≤ 0 → −|x| + 3 ≤ 3, reached at x = 0           E = (−∞, 3]
(c) √x ≥ 0  →  √x − 1 ≥ −1, reached at x = 0            E = [−1, +∞)
(d) 1 + x² ≥ 1  →  0 < 1/(1+x²) ≤ 1
    1 reached at x = 0; 0 never reached                  E = (0, 1]
```

---

### A6 — Formula from a table

```
y = kx + b
x = 0 → y = 3      →  b = 3
x = 1 → y = 5      →  k = 2
y = 2x + 3.   Check x=2: 7 ✓  x=3: 9 ✓  x=4: 11 ✓
```

> "Training" on 5 data points. A 2-parameter model (`k`, `b`) needed 2 points; the other
> 3 acted as **validation**.

---

## B. Linear functions

### B1
```
k = (7 − 3)/(3 − 1) = 2,   3 = 2 + b → b = 1.        y = 2x + 1
```

### B2 — `y = −3x + 6`
```
k = −3 (decreasing, steep),  b = 6
y-intercept (0, 6);  x-intercept: −3x + 6 = 0 → (2, 0)
```

### B3
```
(a) Parallel: k = 2, through (0, 4) → b = 4.            y = 2x + 4
(b) Perpendicular: k = −1/2, through (2, 1):
    1 = −1 + b → b = 2.                                  y = −x/2 + 2
```

### B4
```
k = (5 − (−4))/(2 − (−1)) = 3,   5 = 6 + b → b = −1.    f(x) = 3x − 1
Check f(−1) = −4 ✓
```

### B5
```
(a) F = 45 + 32 = 77°F
(b) 212 = 1.8C + 32 → C = 100°C
(c) C = 1.8C + 32 → −0.8C = 32 → C = −40.   −40°C = −40°F
```

### B6
```
(a) C(d) = 2000d + 5000
(b) C(7) = 19 000
(c) 2000d + 5000 ≤ 25 000 → d ≤ 10 km
(d) k = 2000: the EXTRA cost per km (rate of change)
    b = 5000: what you pay even at d = 0 (the fixed part)
```

### B7
```
(a) 2x + 1 = −x + 7 → x = 2, y = 5.      (2, 5)
(b) 2x + 1 = 2x − 3 → 1 = −3, false → no intersection.
    Same slope (parallel), different intercepts.
```

> The graphical face of D3 from the previous topic (an inconsistent system).

---

## C. Quadratic functions

### C1 — `f(x) = x² − 6x + 5`
```
Zeros:   (x − 1)(x − 5) = 0 → x = 1, 5
Vertex:  x₀ = 6/2 = 3,  f(3) = −4  →  (3, −4)     (also: midpoint of zeros = 3 ✓)
Axis:    x = 3.   y-intercept: 5.   a > 0 → ∪.   Range: [−4, +∞)
```

### C2 — `f(x) = −2x² + 8x − 3`
```
x₀ = −8/(−4) = 2,  f(2) = −8 + 16 − 3 = 5.   a < 0 → MAXIMUM 5.   Range (−∞, 5]
```

### C3
```
x² + 4x + 7 = (x + 2)² + 3.   Vertex (−2, 3).   Min 3 > 0 → NO zeros.   (D = −12 < 0 ✓)
```

### C4 — vertex `(1, −2)`, through `(0, 1)`
```
y = a(x − 1)² − 2;   1 = a − 2 → a = 3
y = 3(x − 1)² − 2 = 3x² − 6x + 1
Check: x₀ = 6/6 = 1 ✓, f(1) = −2 ✓, f(0) = 1 ✓
```

### C5
```
S(x) = x(20 − x) = −x² + 20x,  x₀ = 10  →  S = 100 m², a 10 × 10 square.
```

### C6 — `h(t) = −5t² + 20t`
```
(a) t₀ = 2 s,  h(2) = 20 m
(b) −5t(t − 4) = 0 → t = 0 (launch) or t = 4 s (landing)
(c) −5t² + 20t ≥ 15
    −5t² + 20t − 15 ≥ 0     | ÷(−5) → 🔴 sign flips
    t² − 4t + 3 ≤ 0
    (t − 1)(t − 3) ≤ 0  →  1 ≤ t ≤ 3
Check: h(1) = 15 ✓, h(3) = 15 ✓, h(0.5) = 8.75 < 15 ✓
```

---

## D. Properties

### D1
```
(a) f(−x) = x⁴ − 3x² = f(x)             EVEN
(b) g(−x) = −(x³ + x) = −g(x)           ODD
(c) h(−x) = x² − x ≠ ±h(x)              NEITHER
(d) |−x| = |x|                          EVEN
(e) 1/(−x) = −1/x                       ODD
(f) x² + 1                              EVEN
```

### D2 — `f(x) = x³ − 4x`
```
Zeros: x(x − 2)(x + 2) = 0 → −2, 0, 2
Test points: x=−3: −15 (−);  x=−1: 3 (+);  x=1: −3 (−);  x=3: 15 (+)

     −2       0       2
──────●───────●───────●──────
  −       +       −       +

f(x) > 0  ⟺  x ∈ (−2, 0) ∪ (2, +∞)
f(−x) = −x³ + 4x = −f(x)  →  ODD
```

### D3
```
(a) parabola, vertex x = 2:  decreasing (−∞, 2], increasing [2, +∞)
(b) k < 0: decreasing on ℝ
(c) 1/x: decreasing on (−∞, 0) AND on (0, +∞) separately.
    🔴 NOT "decreasing on the whole domain": −1 < 1 but f(−1) = −1 < f(1) = 1.
```

### D4 — Proof
```
Take any x₁ < x₂.
2x₁ < 2x₂          (multiply by 2 > 0)
2x₁ + 3 < 2x₂ + 3  (add 3)
f(x₁) < f(x₂)      ∎
```

### D5 — `f(x) = 1/(1 + x²)`
```
x² ≥ 0 → 1 + x² ≥ 1 → 0 < 1/(1 + x²) ≤ 1
Upper bound 1 reached at x = 0 → MAXIMUM 1 at x = 0
Lower bound 0 never reached (1/(1+x²) = 0 has no solution)
E = (0, 1].   Bounded.   Even: f(−x) = f(x) ✓
```

### D6 — `f(x) = x² − 2|x|`
```
Even: f(−x) = f(x) ✓ → draw x ≥ 0, then mirror.
x ≥ 0:  x² − 2x = (x − 1)² − 1,  vertex (1, −1),  zeros 0, 2
Mirror: vertex (−1, −1), zero −2
Zeros {−2, 0, 2}.   Min −1 at x = ±1.   Range [−1, +∞).   W-shape, corner at x = 0.
```

---

## E. Transformations and composition

### E1
```
(a) x² + 3        up 3,              vertex (0, 3)
(b) (x − 2)²      RIGHT 2,           vertex (2, 0)
(c) −x²           reflect,           ∩
(d) 2x²           stretch ×2,        narrower
(e) (x + 1)² − 4  left 1, down 4,    vertex (−1, −4)
```

### E2
```
(a) |x − 3| + 2:  vertex (3, 2), V opening up
(b) −|x + 1|:     vertex (−1, 0), Λ opening down
```

### E3
```
(a) f(g(x)) = 2x² + 1        (b) g(f(x)) = (2x + 1)² = 4x² + 4x + 1
(c) f(g(2)) = 9              (d) g(f(2)) = 25.        Not equal.
```

### E4
```
f(g(x)) = √(x − 4),  D = [4, +∞)
g(f(x)) = √x − 4,    D = [0, +∞)
```

### E5
```
(a) g = 3x − 1, f(u) = u⁵
(b) g = x² + 1, f(u) = √u
(c) g = x + 2, m(u) = u², f(v) = 1/v   →  f(m(g(x)))
```

### E6
```
(a) f(g(h(x))) = f(2x²) = 2x² + 1
(b) h(g(f(x))) = h(2x + 2) = 4x² + 8x + 4
(c) g(h(f(x))) = g((x+1)²) = 2x² + 4x + 2
```

### E7 — Mini neural network
```
(a) x=0: −1 → 0 → 3.   x=1: 1 → 1 → 2.   x=2: 3 → 3 → 0.   x=−1: −3 → 0 → 3.

(b) σ "off": 2x − 1 ≤ 0 ⟺ x ≤ 1/2 → y = 3
    σ "on":  x > 1/2 → y = −(2x − 1) + 3 = −2x + 4

        ⎧ 3,          x ≤ 1/2
y(x) =  ⎨
        ⎩ −2x + 4,    x > 1/2

(c) PIECEWISE LINEAR. A "kink" at x = 1/2. Continuous (both sides give 3).

(d) Without σ:  L₂(L₁(x)) = −2x + 4 — plain LINEAR. No kink.
    Two layers without activation = one linear function.
```

> 🔗 The central fact of deep learning, seen with your own hands: **linear∘linear is
> linear; the activation supplies the kink**. Many neurons = many kinks = any curve,
> approximately.

---

## F. Inverse and piecewise

### F1
```
y = 3x − 6 → x = (y + 6)/3 → f⁻¹(x) = (x + 6)/3
f(f⁻¹(x)) = 3·(x + 6)/3 − 6 = x ✓
```

### F2 — `f(x) = (2x + 1)/(x − 3)`
```
y(x − 3) = 2x + 1 → xy − 2x = 3y + 1 → x(y − 2) = 3y + 1 → x = (3y + 1)/(y − 2)
f⁻¹(x) = (3x + 1)/(x − 2),  D(f⁻¹) = ℝ \ {2}
Check: f(4) = 9,  f⁻¹(9) = 28/7 = 4 ✓
```

> `D(f⁻¹) = ℝ\{2} = E(f)` — `f` never equals 2 (horizontal asymptote).

### F3
```
No inverse: f(2) = f(−2) = 4 (fails the horizontal line test).
Restrict to x ≥ 0 → f⁻¹(x) = √x.   (Or x ≤ 0 → f⁻¹(x) = −√x.)
```

### F4
```
(a) f(−3) = −1,  f(0) = 0,  f(1.5) = 2.25,  f(2) = 4,  f(5) = 4
(c) x = 0: left → 2, right → 0 → JUMP, discontinuous
    x = 2: left → 4, right → 4 → continuous
```

### F5 — clip
```
(a) clip(z, −1, 1) = ⎧ −1,  z < −1
                     ⎨ z,   −1 ≤ z ≤ 1
                     ⎩ 1,   z > 1
(b) = 1  ⟺  2x − 3 ≥ 1  ⟺  x ≥ 2
(c) = 0  ⟺  2x − 3 = 0  ⟺  x = 3/2
(d) = 2: range is [−1, 1] → NO solution
```

---

## G. 🔗 AI

### G1 — House prices
```
(a) w = 60/40 = 1.5,  b = 70 − 60 = 10.     price = 1.5·area + 10
(b) price(60) = 100 (thousand $)
(c) w: each extra m² adds 1.5k;  b: the price at area 0 (land, paperwork — the "base")
(d) weight — how heavily the input influences the output; bias — an input-independent shift
```

### G2 — Sigmoid
```
(a) σ(0) = 0.500   σ(1) ≈ 0.731   σ(−1) ≈ 0.269   σ(2) ≈ 0.881   σ(−2) ≈ 0.119

(b) σ(1) + σ(−1) = 1.000
    Proof: 1 − σ(x) = e⁻ˣ/(1 + e⁻ˣ);  multiply top and bottom by eˣ:
           = 1/(eˣ + 1) = σ(−x)   ∎

(c) e⁻ˣ > 0 → 1 + e⁻ˣ > 1 → 0 < 1/(1 + e⁻ˣ) < 1   ∎

(d) σ(x) ≥ 1/2 ⟺ 1 + e⁻ˣ ≤ 2 ⟺ e⁻ˣ ≤ 1 ⟺ −x ≤ 0 ⟺ x ≥ 0
```

> 🔗 (d) is the basis of the rule "`z ≥ 0` → class 1" in binary classification.
> (b) is why `P(yes) + P(no) = 1`.

### G3 — `|x − 1|` from ReLUs
```
(a) y(0) = 0 + 1 = 1,  y(1) = 0,  y(3) = 2 + 0 = 2,  y(−2) = 0 + 3 = 3

(b) y(x) = |x − 1|:
    x ≥ 1: h₁ = x − 1, h₂ = 0 → y = x − 1 ✓
    x < 1: h₁ = 0, h₂ = 1 − x → y = 1 − x ✓

(c) max(x, 2) = 2 + ReLU(x − 2).   Check x=5: 5 ✓, x=0: 2 ✓, x=2: 2 ✓
    (In general: max(a, b) = b + ReLU(a − b))
```

> 🔗 Two neurons built `|x−1|`. Hundreds build any piecewise-linear function. Millions
> get arbitrarily close to any smooth one. That's the intuition behind **universal
> approximation**.

### G4 — Normalization
```
Data: 10, 20, 40, 50

(a) min 10, max 50, range 40:  x' = (x − 10)/40 → 0, 0.25, 0.75, 1.   Range [0, 1]
(b) μ = 30;  deviations −20, −10, 10, 20;  squares sum 1000; /4 = 250; σ = √250 ≈ 15.81
    z = (x − 30)/15.81 → −1.265, −0.632, 0.632, 1.265
(c) Min-max:  k = 1/40 = 0.025,  b = −0.25
    Z-score:  k = 1/σ ≈ 0.0632,  b = −μ/σ ≈ −1.897
(d) x = 40x' + 10;     x = σz + μ = 15.81z + 30
```

### G5 — The loss parabola
```
(a) L(w) = (w − 2)² + (2w − 4)² + (3w − 5)² = 14w² − 50w + 45
(b) A PARABOLA. a = 14 > 0 → opens up → a unique MINIMUM (the loss is convex).
(c) w* = 50/28 = 25/14 ≈ 1.786
    L(w*) = 625/14 − 1250/14 + 630/14 = 5/14 ≈ 0.357
    Cross-check: w* = Σxy/Σx² = 25/14 ✓
(d) L(1) = 9,  L(2) = 1 — both > 5/14 ✓
```

> 🔗 **You just drew a loss landscape by hand.** One parameter → a parabola. Two → a bowl.
> Millions → an unvisualizable landscape that is still **locally** a parabola. Gradient
> descent walks down to the vertex. Watch it in `code/03_ai_bogliqlik.py`.

---

## 🎓 Final note

Blank-page test: close this and redo **E7** and **G5**. If you can — you know it.
If not — tomorrow. Both are normal.
