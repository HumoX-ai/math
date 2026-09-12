# Problems — Functions

> ⛔ **DO NOT open `03-solutions-en.md`.** Yourself first. Every one. Where a graph is
> asked for — **draw it on paper**, then compare with `code/02_grafiklar.py`.
>
> The 15-minute rule applies. Stuck? Go back to the theory, not to the solutions.

**Legend:** ⭐ easy · ⭐⭐ medium · ⭐⭐⭐ hard · 🔗 AI-connected · 📈 draw the graph

---

## A. The concept, domain, range

**A1** ⭐  `f(x) = 2x² − 3x + 1`. Compute `f(0)`, `f(1)`, `f(−2)`, `f(a + 1)`.
> In `f(a+1)` the **whole** `(a+1)` replaces `x`. Simplify.

**A2** ⭐⭐  Domain: `f(x) = √(x − 3) / (x − 5)`

**A3** ⭐⭐  Domain: `g(x) = 1/(x² − 4) + √(6 − x)`

**A4** ⭐⭐  Which of these define `y` as a function of `x`? Justify.
> (a) `y = x²`  (b) `x = y²`  (c) `y = |x|`  (d) `x² + y² = 1`  (e) `y = 3`

**A5** ⭐⭐  Range: (a) `f(x) = x² + 2`  (b) `g(x) = −|x| + 3`  (c) `h(x) = √x − 1`  (d) `k(x) = 1/(1 + x²)`
> For each, say whether the bound is **reached** — `[` or `(` — precisely.

**A6** ⭐⭐ 🔗  A table is given. Find the formula:
```
x:  0   1   2   3   4
y:  3   5   7   9  11
```
> This is the simplest "model fitting." Assume `y = kx + b`.

---

## B. Linear functions

**B1** ⭐  Write the equation of the line through `(1, 3)` and `(3, 7)`.

**B2** ⭐ 📈  `y = −3x + 6`. Find `k`, `b`, the x-intercept, the y-intercept. Draw it.

**B3** ⭐⭐  (a) The line **parallel** to `y = 2x − 1` through `(0, 4)`.
(b) The line **perpendicular** to `y = 2x − 1` through `(2, 1)`.

**B4** ⭐⭐  `f(x) = kx + b`, `f(2) = 5`, `f(−1) = −4`. Find `k` and `b`.

**B5** ⭐⭐  Fahrenheit–Celsius: `F = (9/5)C + 32`.
(a) `C = 25` → `F = ?`  (b) `F = 212` → `C = ?`  (c) At what temperature is `F = C`?

**B6** ⭐⭐ 🔗  A taxi: 5000 base fare + 2000 per km.
(a) Write `C(d)`. (b) `C(7) = ?` (c) With 25 000, how many km at most?
(d) State the **meaning** of `k` and `b` in words.

**B7** ⭐⭐⭐  (a) Intersection of `y = 2x + 1` and `y = −x + 7`.
(b) Do `y = 2x + 1` and `y = 2x − 3` intersect? Why?

---

## C. Quadratic functions

**C1** ⭐⭐ 📈  `f(x) = x² − 6x + 5`. Zeros, vertex, axis of symmetry, y-intercept, range. Graph.

**C2** ⭐⭐  `f(x) = −2x² + 8x − 3`. Vertex; maximum or minimum?; range.

**C3** ⭐⭐  Put `f(x) = x² + 4x + 7` into vertex form. Vertex? Any zeros?

**C4** ⭐⭐⭐  The parabola with vertex `(1, −2)` passing through `(0, 1)`. Write it in standard form.

**C5** ⭐⭐  A rectangle has perimeter 40 m. Which side lengths maximize the area? What is the maximum?

**C6** ⭐⭐⭐  A stone is thrown upward: `h(t) = −5t² + 20t` (metres, seconds).
(a) Maximum height and when. (b) When does it hit the ground?
(c) When is `h ≥ 15`? (That's an inequality from the previous topic.)

---

## D. Properties

**D1** ⭐⭐  Even, odd, or neither? Check **from the definition** (compute `f(−x)`):
> (a) `x⁴ − 3x²`  (b) `x³ + x`  (c) `x² + x`  (d) `|x|`  (e) `1/x`  (f) `x² + 1`

**D2** ⭐⭐ 📈  `f(x) = x³ − 4x`. Find the zeros, build a sign chart, where is `f(x) > 0`?
Even or odd? Sketch.

**D3** ⭐⭐  Intervals of monotonicity:
> (a) `f(x) = (x − 2)² + 1`  (b) `g(x) = −3x + 1`  (c) `h(x) = 1/x`
> There's a trap in (c).

**D4** ⭐⭐  **Prove** (from the definition): `f(x) = 2x + 3` is increasing.

**D5** ⭐⭐⭐ 🔗  `f(x) = 1/(1 + x²)`. Find the range **with proof**. Where is the maximum?
Bounded? Even or odd?

**D6** ⭐⭐⭐ 📈  `f(x) = x² − 2|x|`. Even or odd? Zeros? Minimum value and where?
Range? Graph (hint: draw for `x ≥ 0`, then mirror).

---

## E. Transformations and composition

**E1** ⭐ 📈  `f(x) = x²`. Write each and describe how the graph changes:
> (a) `f(x) + 3`  (b) `f(x − 2)`  (c) `−f(x)`  (d) `2f(x)`  (e) `f(x + 1) − 4`

**E2** ⭐⭐ 📈  Draw: (a) `y = |x − 3| + 2`  (b) `y = −|x + 1|`. Mark the vertices.

**E3** ⭐⭐  `f(x) = 2x + 1`, `g(x) = x²`.
(a) `f(g(x))`  (b) `g(f(x))`  (c) `f(g(2))`  (d) `g(f(2))`. Are they equal?

**E4** ⭐⭐  `f(x) = √x`, `g(x) = x − 4`. Write `f(g(x))` and `g(f(x))` and find their **domains**.

**E5** ⭐⭐  Express as `f(g(x))` (name the inner and outer functions):
> (a) `h(x) = (3x − 1)⁵`  (b) `h(x) = √(x² + 1)`  (c) `h(x) = 1/(x + 2)²` (3 layers)

**E6** ⭐⭐⭐  `f(x) = x + 1`, `g(x) = 2x`, `h(x) = x²`.
(a) `f(g(h(x)))`  (b) `h(g(f(x)))`  (c) `g(h(f(x)))`. All three should differ.

**E7** ⭐⭐⭐ 🔗 📈  **A mini neural network.**
`L₁(x) = 2x − 1`, `σ(z) = max(0, z)`, `L₂(z) = −z + 3`. `y(x) = L₂(σ(L₁(x)))`.
(a) `y(0)`, `y(1)`, `y(2)`, `y(−1)`.
(b) Write `y(x)` as a piecewise function.
(c) Draw it. What kind of function is this (name it)?
(d) What would you get without `σ` (`y = L₂(L₁(x))`)?

---

## F. Inverse and piecewise functions

**F1** ⭐  `f(x) = 3x − 6`. Find `f⁻¹(x)`. Verify `f(f⁻¹(x)) = x`.

**F2** ⭐⭐⭐  `f(x) = (2x + 1)/(x − 3)`. Find `f⁻¹(x)` and its domain. Check with `f(4)` and `f⁻¹(f(4))`.

**F3** ⭐⭐  Does `f(x) = x²` have an inverse? Why? With what restriction does it, and what
is `f⁻¹` then?

**F4** ⭐⭐ 📈  ```
        ⎧ x + 2,   x < 0
f(x) =  ⎨ x²,      0 ≤ x ≤ 2
        ⎩ 4,       x > 2
```
(a) `f(−3)`, `f(0)`, `f(1.5)`, `f(2)`, `f(5)`. (b) Graph. (c) Continuous at `x = 0` and `x = 2`?

**F5** ⭐⭐⭐ 🔗  `clip(z, −1, 1) = max(−1, min(1, z))`.
(a) Write it piecewise. (b) Solve `clip(2x − 3, −1, 1) = 1`.
(c) Solve `clip(2x − 3, −1, 1) = 0`. (d) Does `clip(2x − 3, −1, 1) = 2` have a solution?

---

## G. 🔗 AI-connected problems

### G1 ⭐⭐ — A linear model is a linear function

House price (thousand $) depends on area (m²). Two data points: `(40, 70)`, `(80, 130)`.
(a) Find the model `price = w · area + b`.
(b) Predict the price of a 60 m² house.
(c) The **economic meaning** of `w` and `b`?
(d) Why does ML call `k` a `weight` and `b` a `bias` — your own thoughts.

### G2 ⭐⭐⭐ — Sigmoid properties

`σ(x) = 1/(1 + e⁻ˣ)`. Given: `e⁰ = 1`, `e¹ ≈ 2.718`, `e⁻¹ ≈ 0.368`, `e² ≈ 7.389`, `e⁻² ≈ 0.135`.
(a) Compute `σ(0)`, `σ(1)`, `σ(−1)`, `σ(2)`, `σ(−2)` (3 decimals).
(b) `σ(1) + σ(−1) = ?` **Prove** that in general `σ(−x) = 1 − σ(x)`.
(c) Prove `0 < σ(x) < 1`.
(d) When is `σ(x) ≥ 0.5`? (That's the "classification threshold.")

### G3 ⭐⭐⭐ — Building functions out of ReLUs

`h₁(x) = ReLU(x − 1)`, `h₂(x) = ReLU(1 − x)`, `y(x) = h₁(x) + h₂(x)`.
(a) `y(0)`, `y(1)`, `y(3)`, `y(−2)`.
(b) Which famous function equals `y(x)`? Prove it (split into cases).
(c) Build `g(x) = max(x, 2)` using only ReLU and linear functions.
> This is the beginning of the idea "a ReLU network can build any piecewise linear function."

### G4 ⭐⭐ — Normalization is a linear transformation

Data: `[10, 20, 40, 50]`.
(a) **Min-max:** `x' = (x − min)/(max − min)`. Compute all. Range?
(b) **Z-score:** `z = (x − μ)/σ`. Compute `μ` (mean) and `σ = √(Σ(x−μ)²/n)`, then the `z`'s.
(c) Both are of the form `f(x) = kx + b` — write `k` and `b` for each.
(d) Write the inverse (denormalization) `x = ?`.

### G5 ⭐⭐⭐ — The loss is a function of the parameter

Data: `(1, 2)`, `(2, 4)`, `(3, 5)`. Model: `ŷ = wx` (no bias).
Loss: `L(w) = Σ(w·xᵢ − yᵢ)²`.
(a) **Expand** `L(w)` into the form `aw² + bw + c`.
(b) What kind of function is it? What does the sign of `a` tell you?
(c) Find the vertex: the best `w*` and `L(w*)`.
(d) Compute `L(1)` and `L(2)` — larger than `L(w*)`?
(e) In `code/03_ai_bogliqlik.py`, watch gradient descent roll to exactly that vertex.

---

## 🎯 Day 10 test

**60 minutes**, no reference material:

```
A3 · B4 · C4 · C6 · D5 · E4 · E7 · F2 · G3 · G5
```

| Correct | Verdict |
|---------|---------|
| 9–10 | Done. Next: `03-daraja-va-ildizlar`. |
| 7–8 | Rework the misses, retest in 2 days. |
| 5–6 | Redo blocks E and G. |
| 0–4 | +3 days. A measurement, not a verdict. |
