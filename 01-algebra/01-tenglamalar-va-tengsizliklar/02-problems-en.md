# Problems — Equations and Inequalities

> ⛔ **DO NOT open `03-solutions-en.md`.** Write your own first. Every single one.
>
> **Rule:** spend at least 15 minutes on each problem yourself. If you're stuck, go back
> to the theory, not to the solutions. If it's still not working after 15 minutes, ask AI
> for a **hint** (not an answer), then continue on your own.

**Legend:** ⭐ easy · ⭐⭐ medium · ⭐⭐⭐ hard · 🔗 connected to AI

**Required format for every solution:**

```
1. Domain (when relevant)
2. Solution steps
3. Verification
4. Answer (as a set)
```

---

## A. Linear equations

**A1** ⭐  `3x − 7 = 5x + 9`

**A2** ⭐  `(2x − 1)/3 − (x + 2)/4 = 1`

**A3** ⭐⭐  `5(x − 3) − 2x = 3x − 15`
> Careful: the answer may not be "a single number."

**A4** ⭐⭐  `4(x + 1) − 3 = 4x + 2`

**A5** ⭐⭐⭐  `(a − 2)x = a² − 4`
> `a` is a parameter. Give the answer for **all** values of `a`.

**A6** ⭐⭐⭐  `(m² − 9)x = m − 3`
> `m` is a parameter. There are three cases. Find all of them.

---

## B. Quadratic equations

**B1** ⭐  `x² − 5x + 6 = 0`
> Solve it twice: (a) by factoring, (b) with the formula.

**B2** ⭐  `2x² + 3x − 2 = 0`

**B3** ⭐⭐  `x² + 6x + 2 = 0`
> **Do not use the formula.** Solve it by completing the square.

**B4** ⭐  `3x² − 12 = 0`

**B5** ⭐⭐  `x₁` and `x₂` are the roots of `x² − 7x + 12 = 0`.
> Compute `x₁² + x₂²` **without finding the roots**.

**B6** ⭐⭐⭐  For which values of `m` does `x² − 2mx + (m + 2) = 0` have
**exactly one** root?

**B7** ⭐⭐  `x⁴ − 5x² + 4 = 0`
> Hint: substitute `t = x²`.

---

## C. Rational, radical and absolute value equations

**C1** ⭐  `(x + 1)/(x − 2) = 3`

**C2** ⭐⭐  `1/(x − 1) + 1/(x + 1) = 2/(x² − 1)`
> Write the domain **first**.

**C3** ⭐⭐  `x/(x − 3) − 2 = 3/(x − 3)`

**C4** ⭐⭐  `√(x + 5) = x − 1`

**C5** ⭐⭐  `√(2x + 3) = x`

**C6** ⭐  `|2x − 3| = 5`

**C7** ⭐⭐⭐  `|x − 1| = 2x + 3`

---

## D. Systems of linear equations

**D1** ⭐
```
⎧ 2x + y = 7
⎩ x − y = 2
```
> Solve it both ways: substitution and elimination.

**D2** ⭐
```
⎧ 3x + 2y = 16
⎩ 5x − 2y = 0
```

**D3** ⭐⭐
```
⎧ x + 2y = 4
⎩ 2x + 4y = 9
```
> Explain the answer **geometrically** too (how are the lines positioned?).

**D4** ⭐⭐
```
⎧ x + 2y = 4
⎩ 2x + 4y = 8
```
> Write the answer with a parameter: `x = ?, y = t`.

**D5** ⭐⭐⭐
```
⎧ x + y + z = 6
⎨ 2x − y + z = 3
⎩ x + 2y − z = 2
```

---

## E. Inequalities

**E1** ⭐  `−3x + 5 > 11`

**E2** ⭐  `2 ≤ 3x − 4 < 11`

**E3** ⭐⭐  `x² − x − 6 ≤ 0`

**E4** ⭐⭐  `x² + 4x + 5 > 0`
> The answer may surprise you. Sketch the parabola.

**E5** ⭐⭐  `−x² + 4x − 3 > 0`
> Careful: `a < 0`.

**E6** ⭐⭐  `x² − 4x ≥ 0`

**E7** ⭐⭐  `(x − 1)/(x + 2) ≥ 0`
> ⛔ Do **not** multiply by the denominator. Use the sign chart.

**E8** ⭐⭐⭐  `(x + 3)(x − 1)/(x − 2)² < 0`

**E9** ⭐⭐⭐  `(x − 2)/(x + 1) < 1`
> ⛔ Cross-multiplying is the biggest mistake here. Move everything to the left first.

**E10** ⭐  `|x − 4| < 3`
> State the answer in the language of "distance" as well.

**E11** ⭐⭐  `|2x + 1| ≥ 5`

**E12** ⭐⭐⭐  Prove that `x + 1/x ≥ 2` for every `x > 0`.
> When does equality hold? What changes if `x < 0`?

---

## F. 🔗 AI-connected problems

> This block is the bridge between today's algebra and machine learning.
> No new knowledge is required — only what's in this topic.

### F1 ⭐⭐⭐ — Linear regression (normal equations)

You are given three points: `(1, 2)`, `(2, 3)`, `(3, 5)`.
We want to fit the "best" line `y = wx + b`. "Best" means the sum of squared errors is
minimal:

```
S(w, b) = Σ (w·xᵢ + b − yᵢ)²
```

Calculus shows that the minimum is found by solving this system (**the normal equations**):

```
⎧ w·Σx² + b·Σx = Σxy
⎩ w·Σx  + b·n  = Σy
```

**(a)** Compute `Σx`, `Σx²`, `Σy`, `Σxy`, `n`.
**(b)** Write the system and solve it by hand → find `w` and `b`.
**(c)** Compute the residual `yᵢ − (w·xᵢ + b)` for each point. What is their sum?
**(d)** Check your answer with `code/03_ai_bogliqlik.py`.

> You have just **trained a linear regression model by hand**. Inside `sklearn` exactly
> this system is solved (in matrix form: `XᵀX w = Xᵀy`).

### F2 ⭐⭐⭐ — When does gradient descent converge (learning rate)

We want to minimize `f(x) = 3x²`. The gradient descent step is:

```
x_{k+1} = x_k − η · f'(x_k),      f'(x) = 6x
```

**(a)** Write `x_{k+1}` in terms of `x_k` and `η` only. (Form: `x_{k+1} = c · x_k`)
**(b)** For the sequence to converge to zero we need `|c| < 1`.
Write that as an **inequality** in `η` and solve it.
**(c)** What happens if `η = 0.5`? Compute 4 steps starting from `x₀ = 1`.
**(d)** Derive the condition for the general case `f(x) = (a/2)x²`.

> This is the complete mathematical answer to **why a model "explodes" when the learning
> rate is too large**. The whole proof is one inequality.

### F3 ⭐⭐ — The bound on cosine similarity

You are given `u = (3, 4)` and `v = (4, 3)`.

**(a)** Compute the dot product `u · v`.
**(b)** Compute `‖u‖ = √(3² + 4²)` and `‖v‖`.
**(c)** Compute `cos(θ) = (u·v)/(‖u‖·‖v‖)`.
**(d)** Verify the Cauchy–Schwarz inequality for these numbers: `(u·v)² ≤ ‖u‖²·‖v‖²`
**(e)** For which `u`, `v` is `cos(θ) = 1`? Connect this to the **equality case** of the
inequality.

### F4 ⭐⭐ — The ReLU equation

`ReLU(z) = max(0, z)`. Like the absolute value, it is a **piecewise** function:

```
              ⎧ z,  if z > 0
ReLU(z)  =    ⎨
              ⎩ 0,  if z ≤ 0
```

**(a)** Solve `ReLU(2x − 6) = 4`.
**(b)** Find **all** x satisfying `ReLU(2x − 6) = 0` (this is an inequality!).
**(c)** Does `ReLU(2x − 6) = −1` have a solution? Why?
**(d)** Express `ReLU(z)` using `|z|`.
> Hint: compare `max(0, z)` with `(z + |z|)/2` for several values of z.

### F5 ⭐⭐⭐ — Gradient clipping

During training, if the gradient gets too large it is "clipped":

```
if ‖g‖ > c:      g  ←  c · g / ‖g‖
otherwise:       g  ←  g
```

You are given `g = (6, 8)` and `c = 4`.

**(a)** Compute `‖g‖ = √(6² + 8²)`.
**(b)** Does clipping trigger? (Check the inequality.)
**(c)** Compute the clipped gradient `g'`.
**(d)** Compute `‖g'‖`. What did you get?
**(e)** Prove in general that after clipping `‖g'‖ ≤ c` **always** holds.

---

## 🎯 Day 10 test

Time: **60 minutes**. No reference material. Solve these ten:

```
A2 · A5 · B3 · B6 · C2 · C7 · D5 · E7 · E9 · F2
```

**Scoring:**

| Correct | Verdict |
|---------|---------|
| 9–10 | Topic complete. Move on. |
| 7–8 | Rework the ones you missed, retest in 2 days. |
| 5–6 | Reread the theory, redo blocks C and E. |
| 0–4 | Three more days. This is not failure — it's a **measurement**. |
