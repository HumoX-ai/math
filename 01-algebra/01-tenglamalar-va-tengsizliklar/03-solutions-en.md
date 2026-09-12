# Solutions — Equations and Inequalities

> ⛔ **If you haven't solved the problem yourself yet, close this file.**
>
> Reading a solution gives you the feeling of understanding, not understanding itself.
> That feeling is a lie. Details: [`../../00-mindset/01-learning-with-ai-en.md`](../../00-mindset/01-learning-with-ai-en.md)
>
> **How to use this:** put your own solution side by side and compare. A correct answer
> reached by a different route is fine. A wrong answer goes into [`../../00-mindset/xatolar-daftari.md`](../../00-mindset/xatolar-daftari.md).

---

## A. Linear equations

### A1 — `3x − 7 = 5x + 9`

```
3x − 7 = 5x + 9
3x − 5x = 9 + 7
−2x = 16
x = −8
```

**Check:** LHS = 3(−8) − 7 = −31;  RHS = 5(−8) + 9 = −31 ✓

**Answer:** `S = {−8}`

---

### A2 — `(2x − 1)/3 − (x + 2)/4 = 1`

LCD = 12.

```
4(2x − 1) − 3(x + 2) = 12
8x − 4 − 3x − 6 = 12
5x − 10 = 12
5x = 22
x = 22/5
```

**Check:** (2·4.4 − 1)/3 − (4.4 + 2)/4 = 7.8/3 − 6.4/4 = 2.6 − 1.6 = 1 ✓

**Answer:** `S = {22/5}` (= 4.4)

---

### A3 — `5(x − 3) − 2x = 3x − 15`

```
5x − 15 − 2x = 3x − 15
3x − 15 = 3x − 15
0 = 0            ← IDENTITY
```

**Answer:** `S = ℝ` — **every** real number is a solution.

> This is the `a = 0, b = 0` case of `ax + b = 0`. In linear algebra it is called an
> **underdetermined** system (infinitely many solutions).

---

### A4 — `4(x + 1) − 3 = 4x + 2`

```
4x + 4 − 3 = 4x + 2
4x + 1 = 4x + 2
0 = 1            ← FALSE
```

**Answer:** `S = ∅` — no solution.

> This is the `a = 0, b ≠ 0` case. In systems it's called **inconsistent**.
> Put A3 and A4 side by side: they look identical, the outcomes are opposite.

---

### A5 — `(a − 2)x = a² − 4`

⚠️ Don't take the bait of dividing by `(a − 2)` — it might be zero. Split into cases.

Factor the right side: `a² − 4 = (a − 2)(a + 2)`

```
(a − 2)x = (a − 2)(a + 2)
```

**Case 1: a ≠ 2** → the coefficient is nonzero, so we may divide:

```
x = a + 2
```

**Case 2: a = 2** → the equation becomes:

```
0 · x = 0     →     every x works
```

**Answer:**

```
a ≠ 2   →   S = {a + 2}
a = 2   →   S = ℝ
```

---

### A6 — `(m² − 9)x = m − 3`

```
(m − 3)(m + 3) · x = m − 3
```

**Case 1: m ≠ 3 and m ≠ −3** → coefficient ≠ 0:

```
x = (m − 3) / [(m − 3)(m + 3)] = 1 / (m + 3)
```

**Case 2: m = 3** → `0 · x = 0` → `S = ℝ`

**Case 3: m = −3** → `0 · x = −6` → `0 = −6` is false → `S = ∅`

**Answer:**

```
m ≠ ±3   →   S = { 1/(m + 3) }
m = 3    →   S = ℝ
m = −3   →   S = ∅
```

> Three cases — exactly the three cases of `ax + b = 0`. Not a coincidence: **structure**.

---

## B. Quadratic equations

### B1 — `x² − 5x + 6 = 0`

**(a) Factoring.** Two numbers with sum 5 and product 6: 2 and 3.

```
(x − 2)(x − 3) = 0   →   x = 2  or  x = 3
```

**(b) Formula.**

```
D = 25 − 24 = 1
x = (5 ± 1)/2   →   x₁ = 3,  x₂ = 2
```

**Answer:** `S = {2, 3}`

---

### B2 — `2x² + 3x − 2 = 0`

```
a = 2,  b = 3,  c = −2
D = 9 − 4·2·(−2) = 9 + 16 = 25,   √D = 5

x = (−3 ± 5)/4

x₁ = 2/4  = 1/2
x₂ = −8/4 = −2
```

**Check (x = 1/2):** 2(1/4) + 3(1/2) − 2 = 0.5 + 1.5 − 2 = 0 ✓

**Answer:** `S = {−2, 1/2}`

---

### B3 — `x² + 6x + 2 = 0` (completing the square)

```
x² + 6x = −2                      | coefficient of x is 6; half is 3; square is 9
x² + 6x + 9 = −2 + 9              | add 9 to both sides
(x + 3)² = 7
x + 3 = ±√7                       | DON'T forget ±
x = −3 ± √7
```

**Cross-check with the formula:** `D = 36 − 8 = 28`, `√28 = 2√7`,
`x = (−6 ± 2√7)/2 = −3 ± √7` ✓

**Answer:** `S = {−3 − √7, −3 + √7} ≈ {−5.646, −0.354}`

> This technique returns later, in exactly this form, in the Gaussian distribution,
> ridge regression, and Kalman filters. It matters more than the formula.

---

### B4 — `3x² − 12 = 0`

```
x² = 4
x = ±2          ← DON'T forget ± (taking a root loses solutions)
```

**Answer:** `S = {−2, 2}`

---

### B5 — `x² − 7x + 12 = 0`, find `x₁² + x₂²`

Vieta:

```
x₁ + x₂ = 7,      x₁ · x₂ = 12
```

Identity:

```
x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂ = 49 − 24 = 25
```

**Check:** the roots are 3 and 4 → 9 + 16 = 25 ✓

**Answer:** `25`

---

### B6 — `x² − 2mx + (m + 2) = 0` with exactly one root

"Exactly one root" ⟺ `D = 0`.

```
D = (−2m)² − 4(m + 2) = 4m² − 4m − 8 = 0
m² − m − 2 = 0
(m − 2)(m + 1) = 0
m = 2   or   m = −1
```

**Check:**

```
m = 2:   x² − 4x + 4 = (x − 2)² = 0  →  x = 2   ✓
m = −1:  x² + 2x + 1 = (x + 1)² = 0  →  x = −1  ✓
```

**Answer:** `m ∈ {−1, 2}`

---

### B7 — `x⁴ − 5x² + 4 = 0`

Substitute `t = x²`, with the condition **`t ≥ 0`**.

```
t² − 5t + 4 = 0
(t − 1)(t − 4) = 0
t = 1  or  t = 4          ← both ≥ 0, both valid

t = 1  →  x = ±1
t = 4  →  x = ±2
```

**Answer:** `S = {−2, −1, 1, 2}`

> If a value of `t` came out negative, that branch would be **discarded** — `x² ≥ 0`.

---

## C. Rational, radical and absolute value equations

### C1 — `(x + 1)/(x − 2) = 3`

```
Domain:  x ≠ 2

x + 1 = 3(x − 2) = 3x − 6
7 = 2x
x = 7/2 = 3.5      ← in the domain ✓
```

**Check:** (3.5 + 1)/(3.5 − 2) = 4.5/1.5 = 3 ✓

**Answer:** `S = {7/2}`

---

### C2 — `1/(x − 1) + 1/(x + 1) = 2/(x² − 1)`

```
Domain:  x² − 1 = (x−1)(x+1) ≠ 0   →   x ≠ 1  and  x ≠ −1
```

Combine the left side:

```
   1        1       (x + 1) + (x − 1)        2x
───────  +  ─────  = ─────────────────  =  ───────
 x − 1      x + 1     (x − 1)(x + 1)        x² − 1
```

So:

```
2x/(x² − 1) = 2/(x² − 1)   →   2x = 2   →   x = 1
```

🔴 But `x = 1` is **not in the domain**.

**Answer:** `S = ∅`

> The best possible argument for writing the domain **first**. Anyone who skips it
> answers `{1}` — and is wrong.

---

### C3 — `x/(x − 3) − 2 = 3/(x − 3)`

```
Domain:  x ≠ 3

Multiply by (x − 3):
x − 2(x − 3) = 3
x − 2x + 6 = 3
−x = −3
x = 3
```

🔴 `x = 3` is not in the domain.

**Answer:** `S = ∅`

---

### C4 — `√(x + 5) = x − 1`

```
Condition:  x − 1 ≥ 0   →   x ≥ 1

Square:
x + 5 = x² − 2x + 1
x² − 3x − 4 = 0
(x − 4)(x + 1) = 0
x = 4   or   x = −1

x = −1:  violates x ≥ 1  ❌  (extraneous root, created by squaring)
x = 4:   ✓
```

**Check:** `√9 = 3 = 4 − 1` ✓

**Answer:** `S = {4}`

---

### C5 — `√(2x + 3) = x`

```
Condition:  x ≥ 0     (the left side is a root; it can't be negative)

2x + 3 = x²
x² − 2x − 3 = 0
(x − 3)(x + 1) = 0
x = 3   or   x = −1

x = −1:  violates x ≥ 0  ❌
x = 3:   ✓
```

**Check:** `√9 = 3` ✓

**Answer:** `S = {3}`

---

### C6 — `|2x − 3| = 5`

The right side `5 > 0` → two cases:

```
1)  2x − 3 = 5    →  x = 4
2)  2x − 3 = −5   →  x = −1
```

**Check:** `|8 − 3| = 5` ✓;  `|−2 − 3| = 5` ✓

**Answer:** `S = {−1, 4}`

---

### C7 — `|x − 1| = 2x + 3`

x appears on the right → a **condition is mandatory**:

```
Condition:  2x + 3 ≥ 0   →   x ≥ −3/2
```

Two cases:

```
1)  x − 1 = 2x + 3     →  x = −4      ❌ (−4 < −3/2, violates the condition)
2)  x − 1 = −(2x + 3)  →  3x = −2  →  x = −2/3   ✓
```

**Check:** LHS = `|−2/3 − 1| = 5/3`;  RHS = `2(−2/3) + 3 = 5/3` ✓

**Answer:** `S = {−2/3}`

---

## D. Systems of linear equations

### D1
```
⎧ 2x + y = 7
⎩ x − y = 2
```

**Substitution:**

```
x = y + 2
2(y + 2) + y = 7  →  3y = 3  →  y = 1,  x = 3
```

**Elimination:**

```
  2x + y = 7
+ x − y = 2
──────────────
  3x     = 9   →  x = 3,  y = 1
```

**Check:** `2(3) + 1 = 7` ✓;  `3 − 1 = 2` ✓

**Answer:** `(3, 1)` — the lines cross at a single point.

---

### D2
```
⎧ 3x + 2y = 16
⎩ 5x − 2y = 0
```

The `y` coefficients are opposite → add directly:

```
8x = 16   →   x = 2
5(2) − 2y = 0  →  y = 5
```

**Check:** `3(2) + 2(5) = 16` ✓

**Answer:** `(2, 5)`

---

### D3
```
⎧ x + 2y = 4
⎩ 2x + 4y = 9
```

Multiply the first by 2:

```
2x + 4y = 8
2x + 4y = 9
```

Same left sides, different right sides → we would need `8 = 9`, which is false.

**Answer:** `S = ∅`

**Geometrically:** both lines have the same slope (`y = −x/2 + 2` and `y = −x/2 + 9/4`)
but different intercepts → **parallel lines**, never intersecting.

```
 ────────────  (y = −x/2 + 9/4)
 ────────────  (y = −x/2 + 2)
```

---

### D4
```
⎧ x + 2y = 4
⎩ 2x + 4y = 8
```

The second equation is the first times 2 — the **same line**. No new information.

Parametrize with `y = t` (any real t):

```
x = 4 − 2t
```

**Answer:** `S = {(4 − 2t, t) : t ∈ ℝ}` — infinitely many solutions.

**Check (t = 0):** (4, 0) ✓  **Check (t = 1):** (2, 1) ✓

> 🔗 This is the case `rank(A) < number of unknowns`. In neural networks it is almost
> **always** the situation: more parameters than data. Hence the question "which of the
> infinitely many solutions do we pick?" → **regularization** is the answer to it.

---

### D5
```
⎧ x + y + z = 6      (1)
⎨ 2x − y + z = 3     (2)
⎩ x + 2y − z = 2     (3)
```

Eliminate `z` (its coefficients are +1, +1, −1):

```
(1) + (3):   2x + 3y = 8      (4)
(2) + (3):   3x + y  = 5      (5)
```

Now a 2×2 system:

```
From (5):  y = 5 − 3x
Into (4):  2x + 15 − 9x = 8
           −7x = −7   →   x = 1
           y = 2
From (1):  z = 6 − 1 − 2 = 3
```

**Check:**

```
(1):  1 + 2 + 3 = 6   ✓
(2):  2 − 2 + 3 = 3   ✓
(3):  1 + 4 − 3 = 2   ✓
```

**Answer:** `(x, y, z) = (1, 2, 3)`

> You just performed **Gaussian elimination**. In linear algebra you write the same
> thing with matrix rows.

---

## E. Inequalities

### E1 — `−3x + 5 > 11`

```
−3x > 6
x < −2              🔴 (−3) is NEGATIVE → the sign FLIPPED
```

**Check:** `x = −3` (inside): `14 > 11` ✓;  `x = 0` (outside): `5 > 11` ❌ — correct.

**Answer:** `x ∈ (−∞, −2)`

---

### E2 — `2 ≤ 3x − 4 < 11`

```
2 ≤ 3x − 4 < 11         | add 4 everywhere
6 ≤ 3x < 15             | divide everywhere by 3  (3 > 0 → sign unchanged)
2 ≤ x < 5
```

**Answer:** `x ∈ [2, 5)`

---

### E3 — `x² − x − 6 ≤ 0`

```
Zeros:  (x − 3)(x + 2) = 0  →  x = −2, 3
a = 1 > 0  →  opens up  ∪
"≤ 0" → below or on the x-axis → BETWEEN the roots
```

```
        ╲                    ╱
         ╲                  ╱
  ────────●────────────────●────────  x
         −2       ⌄        3
```

Endpoints are **filled** (●) because of `≤`.

**Answer:** `x ∈ [−2, 3]`

---

### E4 — `x² + 4x + 5 > 0`

```
D = 16 − 20 = −4 < 0   →  NO real roots
a = 1 > 0              →  opens up
```

No roots + opening up = the parabola is **entirely above** the x-axis.

Another way (completing the square): `x² + 4x + 5 = (x + 2)² + 1 ≥ 1 > 0` always.

**Answer:** `x ∈ ℝ`

> If the problem had asked for `< 0`, the answer would be `∅`.

---

### E5 — `−x² + 4x − 3 > 0`

**Route 1 — multiply by (−1) (the sign flips!):**

```
x² − 4x + 3 < 0
(x − 1)(x − 3) < 0
a > 0, "< 0" → BETWEEN the roots
1 < x < 3
```

**Route 2 — directly:**

```
Zeros: x = 1, x = 3
a = −1 < 0  →  opens DOWN  ∩
"> 0" → above the x-axis → BETWEEN the roots
```

```
              ╭────╮
             ╱      ╲
  ──────────○────────○──────────  x
            1        3
```

**Check:** `x = 2`: `−4 + 8 − 3 = 1 > 0` ✓

**Answer:** `x ∈ (1, 3)`

---

### E6 — `x² − 4x ≥ 0`

```
x(x − 4) ≥ 0
Zeros: x = 0, 4
a > 0, "≥ 0" → OUTSIDE the roots (endpoints included)
```

**Check:** `x = −1`: `5 ≥ 0` ✓;  `x = 2`: `−4 ≥ 0` ❌ (correctly excluded)

**Answer:** `x ∈ (−∞, 0] ∪ [4, +∞)`

---

### E7 — `(x − 1)/(x + 2) ≥ 0`

⛔ Multiplying by the denominator is **forbidden** — the sign of `x + 2` is unknown.

**Sign chart:**

```
Critical points:
   numerator = 0:    x = 1     →  ● (filled, because of ≥)
   denominator = 0:  x = −2    →  ○ (ALWAYS open)
```

Test one number per interval:

```
interval      test point      value              sign
(−∞, −2)      x = −3          (−4)/(−1) = 4        +
(−2, 1)       x = 0           (−1)/(2) = −0.5      −
(1, +∞)       x = 2           (1)/(4) = 0.25       +
```

```
          −2              1
  ────────○───────────────●────────  x
     +          −              +
```

We need "≥ 0" → the `+` intervals.

**Answer:** `x ∈ (−∞, −2) ∪ [1, +∞)`

> ⚠️ `x = −2` is **never** included, even with `≥` — the expression is undefined there.

---

### E8 — `(x + 3)(x − 1)/(x − 2)² < 0`

**Key observation:** `(x − 2)² > 0` always (for `x ≠ 2`), so the denominator **cannot
change the sign** — it is always positive.

Therefore the sign of the fraction = the sign of the numerator:

```
(x + 3)(x − 1) < 0
Zeros: x = −3, 1
a > 0, "< 0" → between the roots
−3 < x < 1
```

The condition `x ≠ 2` is automatic (`2 ∉ (−3, 1)`).

**Check:** `x = 0`: `(3)(−1)/4 = −0.75 < 0` ✓

**Answer:** `x ∈ (−3, 1)`

> **General rule:** an **even**-multiplicity factor does **not** flip the sign at its
> root; an **odd**-multiplicity one does.

---

### E9 — `(x − 2)/(x + 1) < 1`

🔴 **THE BIGGEST MISTAKE:** cross-multiplying to get `x − 2 < x + 1`. That is **wrong**,
because `x + 1` may be negative, in which case the sign flips.

**The right way — move everything left:**

```
(x − 2)/(x + 1) − 1 < 0

 (x − 2) − (x + 1)        x − 2 − x − 1          −3
─────────────────── =   ─────────────────  =  ───────  < 0
      x + 1                   x + 1             x + 1
```

The numerator `−3` is **always negative**. For the fraction to be negative, the
denominator must be **positive**:

```
x + 1 > 0
x > −1
```

**Check:**

```
x = 0  (inside):   (0−2)/(0+1) = −2 < 1  ✓
x = −2 (outside):  (−4)/(−1) = 4 < 1?  NO  ✓ correctly excluded
```

**Answer:** `x ∈ (−1, +∞)`

> Cross-multiplying would have produced `x < 3` — **completely wrong**. Make this mistake
> once deliberately, then write it in your error notebook.

---

### E10 — `|x − 4| < 3`

```
−3 < x − 4 < 3
1 < x < 7
```

**In the language of distance:** "x is less than 3 units away from 4."

```
       ───────(───────●───────)───────
               1      4       7
```

**Answer:** `x ∈ (1, 7)`

---

### E11 — `|2x + 1| ≥ 5`

`|...| ≥ a` → **outside** → two cases joined by "or":

```
1)  2x + 1 ≥ 5    →  x ≥ 2
2)  2x + 1 ≤ −5   →  x ≤ −3
```

**Check:** `x = 2`: `|5| = 5 ≥ 5` ✓;  `x = 0`: `1 ≥ 5` ❌ (correctly excluded)

**Answer:** `x ∈ (−∞, −3] ∪ [2, +∞)`

---

### E12 — Prove `x + 1/x ≥ 2` for `x > 0`

**Proof 1 — direct (the prettiest):**

```
x + 1/x − 2 = (x² − 2x + 1)/x = (x − 1)² / x
```

`x > 0` → the denominator is positive;  `(x − 1)² ≥ 0` → the numerator is non-negative.

```
⟹  (x − 1)²/x ≥ 0   ⟹   x + 1/x ≥ 2        ∎
```

**Proof 2 — via AM–GM:**

```
(a + b)/2 ≥ √(ab)   with  a = x,  b = 1/x:

(x + 1/x)/2 ≥ √(x · 1/x) = 1     ⟹   x + 1/x ≥ 2        ∎
```

**When is it an equality?** `(x − 1)² = 0` ⟺ `x = 1`. Check: `1 + 1 = 2` ✓

**What if `x < 0`?** Substitute `x = −y` with `y > 0`:

```
x + 1/x = −(y + 1/y) ≤ −2
```

So for negative x the inequality **reverses**: `x + 1/x ≤ −2`.
That is why the hypothesis `x > 0` is mandatory.

---

## F. 🔗 AI-connected problems

### F1 — Linear regression

**(a) Sums.** Points: (1,2), (2,3), (3,5)

```
n   = 3
Σx  = 6
Σx² = 1 + 4 + 9 = 14
Σy  = 10
Σxy = 2 + 6 + 15 = 23
```

**(b) The system and its solution.**

```
⎧ 14w + 6b = 23        (1)
⎩  6w + 3b = 10        (2)

(2) × 2:   12w + 6b = 20        (3)
(1) − (3): 2w = 3     →   w = 3/2 = 1.5

Into (2): 9 + 3b = 10   →   b = 1/3
```

**Answer:** `y = 1.5x + 1/3`

**(c) Residuals.**

```
x = 1:  predicted = 11/6 ≈ 1.8333    residual = 2 − 11/6 = +1/6
x = 2:  predicted = 10/3 ≈ 3.3333    residual = 3 − 10/3 = −1/3
x = 3:  predicted = 29/6 ≈ 4.8333    residual = 5 − 29/6 = +1/6

Sum:  1/6 − 2/6 + 1/6 = 0
```

**The residuals sum to zero.** Not a coincidence — it is exactly what setting the
derivative with respect to `b` to zero gives you:

```
∂S/∂b = 0   ⟺   Σ(residuals) = 0
∂S/∂w = 0   ⟺   Σ(residual · xᵢ) = 0
```

Check the second one too: `(1/6)(1) + (−1/3)(2) + (1/6)(3) = 0` ✓

> **You just trained a model by hand.** `sklearn.LinearRegression` solves exactly these
> two equations, in matrix form: `XᵀX w = Xᵀy` — the **normal equations**. It is the same
> object as block D.

---

### F2 — Gradient descent and the learning rate

**(a) The recursion.**

```
f(x) = 3x²   →   f'(x) = 6x

x_{k+1} = x_k − η·6x_k = x_k (1 − 6η)      →   c = 1 − 6η
```

So `x_k = (1 − 6η)^k · x₀` — a **geometric sequence**.

**(b) The convergence condition is an INEQUALITY.**

```
|1 − 6η| < 1
−1 < 1 − 6η < 1          | subtract 1 everywhere
−2 < −6η < 0             | divide by (−6)  →  🔴 SIGNS FLIP
 1/3 > η > 0

Answer:  0 < η < 1/3
```

**(c) If η = 0.5:**

```
c = 1 − 3 = −2      →  |c| = 2 > 1  →  DIVERGES

x₀ = 1
x₁ = −2
x₂ = 4
x₃ = −8
x₄ = 16
```

The values **grow and alternate in sign** — this is exactly why training produces
`loss = NaN`. The model "explodes."

**(d) General case.**

```
f(x) = (a/2)x²   →   x_{k+1} = x_k(1 − ηa)

|1 − ηa| < 1
−2 < −ηa < 0
0 < ηa < 2

For a > 0:      0 < η < 2/a        ✓
```

**Check:** here `f = 3x² = (6/2)x²` → `a = 6` → `0 < η < 1/3` ✓ — matches part (b).

> `a` is the **curvature** (the second derivative). In many dimensions it becomes the
> largest eigenvalue of the Hessian (`λ_max`) and the condition reads `0 < η < 2/λ_max`.
> That is **one of the most important inequalities in deep learning** — and it is proved
> entirely inside this topic.

---

### F3 — The bound on cosine similarity

```
u = (3, 4),   v = (4, 3)
```

**(a)** `u · v = 12 + 12 = 24`

**(b)** `‖u‖ = √25 = 5`;  `‖v‖ = 5`

**(c)** `cos(θ) = 24/25 = 0.96`

**(d) Cauchy–Schwarz:**

```
(u·v)²      = 576
‖u‖²·‖v‖²   = 625

576 ≤ 625   ✓
```

**(e) When is `cos(θ) = 1`?**

Equality in Cauchy–Schwarz holds exactly when the vectors are **collinear**: `v = k·u`.

```
k > 0  →  same direction      →  cos θ = +1   (θ = 0°)
k < 0  →  opposite direction  →  cos θ = −1   (θ = 180°)
```

Here `v ≠ k·u` (since 4/3 ≠ 3/4), so `cos θ = 0.96 < 1`.

> 🔗 **This is precisely why `cosine similarity` always lies in [−1, 1].** Every time you
> measure embedding similarity, Cauchy–Schwarz is what guarantees the range.

---

### F4 — The ReLU equation

**(a)** `ReLU(2x − 6) = 4`

```
The output 4 > 0 → the ReLU is "on", so ReLU(2x−6) = 2x − 6

2x − 6 = 4   →   x = 5

Check: 2(5) − 6 = 4 > 0 ✓,  ReLU(4) = 4 ✓
```

**Answer:** `x = 5`

**(b)** `ReLU(2x − 6) = 0`

```
ReLU(z) = 0  ⟺  z ≤ 0

2x − 6 ≤ 0   →   x ≤ 3
```

**Answer:** `x ∈ (−∞, 3]` — **infinitely many** solutions, because this is really an
inequality.

> 🔗 This is the mathematics of the "**dead ReLU**" problem: if a neuron's input is always
> negative, its output is always 0 and so is its gradient — the neuron is **dead**.

**(c)** `ReLU(2x − 6) = −1` — **no solution**, since `ReLU(z) = max(0, z) ≥ 0` always.

**(d)** `ReLU(z) = (z + |z|)/2`

**Check:**

```
z = 5:    (5 + 5)/2 = 5      = max(0, 5)   ✓
z = −5:   (−5 + 5)/2 = 0     = max(0, −5)  ✓
z = 0:    0                  = max(0, 0)   ✓
```

**Proof:**

```
z ≥ 0  →  |z| = z   →  (z + z)/2 = z    = ReLU(z)  ✓
z < 0  →  |z| = −z  →  (z − z)/2 = 0    = ReLU(z)  ✓
```

> Similarly: `max(a,b) = (a + b + |a − b|)/2`. The absolute value is the tool for
> collapsing a piecewise definition into one formula.

---

### F5 — Gradient clipping

```
g = (6, 8),   c = 4
```

**(a)** `‖g‖ = √(36 + 64) = √100 = 10`

**(b)** Clipping condition: `‖g‖ > c` → `10 > 4` → **yes, it triggers** ✓

**(c)** `g' = 4 · (6, 8)/10 = (2.4, 3.2)`

**(d)** `‖g'‖ = √(5.76 + 10.24) = √16 = 4`

**So `‖g'‖ = c` exactly.** Clipping fixes the vector's **length** at `c` while preserving
its **direction**:

```
g'/‖g'‖ = (2.4, 3.2)/4 = (0.6, 0.8)
g /‖g‖  = (6, 8)/10    = (0.6, 0.8)      ← identical ✓
```

**(e) General proof.**

```
Case 1: ‖g‖ ≤ c
   g' = g   →   ‖g'‖ = ‖g‖ ≤ c     ✓

Case 2: ‖g‖ > c
   g' = c·g/‖g‖

   Norm property:  ‖k·v‖ = |k| · ‖v‖

   ‖g'‖ = |c/‖g‖| · ‖g‖ = (c/‖g‖) · ‖g‖ = c      (c > 0, ‖g‖ > 0)

In both cases:  ‖g'‖ ≤ c    ∎
```

> 🔗 Why does this matter? In RNNs and Transformers gradients sometimes explode.
> Clipping is a **hard bound imposed by an inequality**. The whole mechanism is these
> few lines of algebra.

---

## 🎓 Final note

If you read through these solutions and felt "that all made sense" — **that feeling may
be an illusion**.

The test is simple: close the file, take a blank sheet, and redo **E9** and **F2**.
If you can, you know it. If you can't, you don't yet — and that is completely normal.
Try again tomorrow.
