# Equations and Inequalities — Theory

> **How to read this:** don't copy. After each section, close the file and rewrite it
> **in your own words** on paper. If you can derive a formula without looking, you know
> it. Otherwise you don't.

**Contents**

1. [What an equation is](#1-what-an-equation-is)
2. [Equivalent transformations — the heart of the topic](#2-equivalent-transformations--the-heart-of-the-topic)
3. [Linear equations](#3-linear-equations)
4. [Systems of linear equations](#4-systems-of-linear-equations)
5. [Quadratic equations](#5-quadratic-equations)
6. [Rational equations](#6-rational-equations)
7. [Radical equations](#7-radical-equations)
8. [Absolute value equations](#8-absolute-value-equations)
9. [Inequalities: core properties](#9-inequalities-core-properties)
10. [Linear and quadratic inequalities](#10-linear-and-quadratic-inequalities)
11. [The sign-chart method](#11-the-sign-chart-method-rational-inequalities)
12. [Absolute value inequalities](#12-absolute-value-inequalities)
13. [Inequalities that matter for AI](#13-inequalities-that-matter-for-ai)
14. [Museum of mistakes](#14-museum-of-mistakes)

---

## 1. What an equation is

### 1.1 Three kinds of equality

Distinguishing these three is where everything begins:

| Type | Example | Meaning |
|------|---------|---------|
| **Identity** | x + x = 2x | True for **all** x |
| **Equation** | 2x + 1 = 7 | True for **some** x (here x = 3) |
| **Contradiction** | x = x + 1 | True for **no** x |

An equation is a **question**: *"for which values of x is this equality true?"*

### 1.2 The solution set

The answer to an equation is not a number — it is a **set**.

```
2x + 1 = 7        →  S = {3}
x² = 4            →  S = {−2, 2}
x² = −1           →  S = ∅        (empty set, over the reals)
x + x = 2x        →  S = ℝ        (all real numbers)
```

This set-based view matters, because later:
- in linear systems the solution set becomes a **line or a plane**,
- in optimization it becomes the **feasible set**.

### 1.3 The domain

The **domain** answers: *"for which x does the equation even make sense?"*

Three main restrictions:

```
1.  Denominator ≠ 0        →   1/(x−2)      requires   x ≠ 2
2.  Even root ≥ 0          →   √(x−3)       requires   x ≥ 3
3.  Log argument > 0       →   log(x+1)     requires   x > −1
```

> ⚠️ **Write the domain BEFORE you solve, not after.** This is the #1 source of errors.
> The domain is the fence; you work inside it.

---

## 2. Equivalent transformations — the heart of the topic

Understand this section and the rest is technique. Miss it and you will keep making
mistakes forever.

**Question:** what are we actually doing when we "solve" an equation?

**Answer:** we simplify the equation in ways that **do not change its solution set**.

```
A = B          →          A' = B'          →          x = 5
(complicated)            (simpler)                  (the answer)

    ↑ every step must PRESERVE the solution set
```

### 2.1 Safe operations (solution set preserved)

| Operation | Example |
|-----------|---------|
| **Add/subtract** the same thing on both sides | x − 3 = 5 → x = 8 |
| Multiply/divide both sides by a **nonzero constant** | 2x = 6 → x = 3 |
| Simplify one side (identity rewriting) | 2(x+1) = 2x+2 |

### 2.2 DANGEROUS operations

This is the most important table in the topic. Memorize it:

| Operation | What happens | What to do |
|-----------|--------------|------------|
| **Multiply by an expression containing x** | **Extraneous roots** appear | **Check** at the end |
| **Divide by an expression containing x** | **Roots are lost** | Handle the divisor = 0 case separately |
| **Square both sides** | **Extraneous roots** appear | **Check** at the end |
| **Take a square root** | Roots are lost (± forgotten) | `√(a²) = \|a\|`, never forget `±` |

#### Example 1 — losing a root by dividing (extremely common)

```
x² = 5x
─────────────────────────────────
❌ WRONG:
   x² = 5x
   x = 5          ← divided both sides by x
   Answer: {5}    ← x = 0 WAS LOST!

✅ RIGHT:
   x² − 5x = 0
   x(x − 5) = 0
   x = 0  or  x = 5
   Answer: {0, 5}
```

**Rule:** *never divide by a variable. Always move everything to one side and factor.*

#### Example 2 — gaining an extraneous root by squaring

```
√x = −2
─────────────────────────────────
Square both sides:  x = 4
Check:  √4 = 2 ≠ −2   ❌
Answer: S = ∅
```

Why? Because `a = b  ⟹  a² = b²` is true, but **the converse is false**:
`a² = b²  ⟹  a = b  or  a = −b`. Squaring destroys the information "no, that one is
negative."

### 2.3 The golden rule

> **If you used a dangerous operation — substitute your answer back into the ORIGINAL
> equation. Every time.**

This is not "being careful." It is a **mandatory part of the solution**.

---

## 3. Linear equations

### 3.1 General form

```
ax + b = 0,     a, b — given numbers,  x — unknown
```

### 3.2 Complete case analysis (the basis of parametric equations)

```
ax + b = 0

├── a ≠ 0                  →  x = −b/a          (unique solution)
│
└── a = 0                  →  becomes  b = 0
    ├── b = 0  →  0 = 0    →  S = ℝ             (infinitely many solutions)
    └── b ≠ 0  →  b = 0    →  S = ∅             (no solution)
```

> These three cases are **not a coincidence**. You will meet exactly the same three in
> the matrix system `Ax = b`. Understand them now with one variable and linear algebra
> gets much easier.

### 3.3 Algorithm

```
1. Expand brackets
2. Clear denominators (multiply by the LCD)
3. Move x-terms LEFT, constants RIGHT
4. Simplify to  ax = c
5. Divide by a (check a ≠ 0!)
6. Verify
```

**Example:**

```
(2x − 1)/3 − (x + 2)/4 = 1

Multiply by 12 (the LCD):
    4(2x − 1) − 3(x + 2) = 12
    8x − 4 − 3x − 6 = 12
    5x − 10 = 12
    5x = 22
    x = 22/5 = 4.4

Check:  (2·4.4 − 1)/3 − (4.4 + 2)/4 = 7.8/3 − 6.4/4 = 2.6 − 1.6 = 1  ✓
```

---

## 4. Systems of linear equations

> ⭐ **This section is the direct door into linear algebra.** Read it carefully.

### 4.1 What a system is

```
⎧ 2x + y = 7
⎨
⎩ x − y = 2
```

**Meaning:** *"find the pair (x, y) that satisfies both equations simultaneously."*

### 4.2 Geometric meaning (the key idea)

Each linear equation is a **line** in the plane. Solving the system =
**finding where the lines intersect**.

```
1) Lines intersect            2) Parallel                3) Identical
      ╲   ╱                      ────────                  ══════════
       ╲ ╱                       ────────                  (same line)
        ╳
       ╱ ╲
   1 solution                  0 solutions              infinitely many
   (determined)                (inconsistent)           (underdetermined)
```

> 🔗 **AI connection:** in a neural network, "more parameters than data points" is case 3 —
> **infinitely many solutions**. That is exactly why regularization is needed: something
> must decide **which** of the infinitely many solutions to pick. It starts right here.

### 4.3 Method 1 — substitution

```
⎧ 2x + y = 7        →  y = 7 − 2x
⎩ x − y = 2

x − (7 − 2x) = 2
x − 7 + 2x = 2
3x = 9  →  x = 3
y = 7 − 2·3 = 1

Answer: (3, 1)
```

### 4.4 Method 2 — elimination ⭐

More important, because **Gaussian elimination** grows directly out of it.

```
⎧ 2x + y = 7
⎩ x − y = 2
─────────────  add (the y's cancel)
  3x     = 9   →  x = 3
              →  y = 1
```

### 4.5 Three unknowns

```
⎧ x + y + z = 6      ... (1)
⎨ 2x − y + z = 3     ... (2)
⎩ x + 2y − z = 2     ... (3)

(1)+(3):   2x + 3y = 8      ... (4)
(2)+(3):   3x + y  = 5      ... (5)

From (5): y = 5 − 3x
Into (4): 2x + 3(5 − 3x) = 8
          2x + 15 − 9x = 8
          −7x = −7  →  x = 1
          y = 5 − 3 = 2
From (1): z = 6 − 1 − 2 = 3

Answer: (1, 2, 3)
Check (2): 2 − 2 + 3 = 3 ✓   (3): 1 + 4 − 3 = 2 ✓
```

> 🔗 This process **is** Gaussian elimination. In linear algebra you write it with
> matrices and it leads to `A⁻¹b`, `rank`, and LU decomposition. What you're doing by
> hand right now is that same algorithm.

---

## 5. Quadratic equations

```
ax² + bx + c = 0,     a ≠ 0
```

### 5.1 DERIVE the formula (don't memorize it)

This is the single most important skill in the topic. **Completing the square** shows up
again and again later — in the Gaussian distribution, ridge regression, and Kalman filters.

```
ax² + bx + c = 0                          | divide by a (a ≠ 0)

x² + (b/a)x + c/a = 0

x² + (b/a)x = −c/a                        | half the coefficient of x
                                          | is b/(2a); square it
x² + (b/a)x + (b/2a)² = −c/a + (b/2a)²    | add to both sides

(x + b/2a)² = b²/4a² − c/a                | the left side is a perfect square

(x + b/2a)² = (b² − 4ac) / 4a²            | common denominator on the right

x + b/2a = ± √(b² − 4ac) / 2a             | take the root (DON'T forget ±)

x = (−b ± √(b² − 4ac)) / 2a               ✓
```

**Discriminant:** `D = b² − 4ac`

| D | Number of roots | Graph |
|---|-----------------|-------|
| D > 0 | 2 distinct real roots | Parabola crosses the x-axis twice |
| D = 0 | 1 root (double root) | Parabola touches the x-axis |
| D < 0 | No real roots | Parabola never reaches the x-axis |

### 5.2 Vieta's formulas

If `x₁, x₂` are the roots of `ax² + bx + c = 0`:

```
x₁ + x₂ = −b/a
x₁ · x₂ =  c/a
```

For `x² + px + q = 0` (a = 1): `x₁ + x₂ = −p`, `x₁·x₂ = q`

**Why it's useful:**
- Compute things like `x₁² + x₂²` without finding the roots:
  `x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂`
- Spot integer roots fast: `x² − 5x + 6 = 0` → sum 5, product 6 → 2 and 3.

### 5.3 Factoring

```
x² − 5x + 6 = 0
(x − 2)(x − 3) = 0
x = 2  or  x = 3
```

**The zero-product property:** `A · B = 0  ⟺  A = 0 or B = 0`
This works **only for zero**. From `A · B = 6` nothing follows!

### 5.4 Identities worth knowing cold

```
a² − b² = (a − b)(a + b)
a² ± 2ab + b² = (a ± b)²
a³ − b³ = (a − b)(a² + ab + b²)
a³ + b³ = (a + b)(a² − ab + b²)
ax² + bx + c = a(x − x₁)(x − x₂)      ← when D ≥ 0
```

---

## 6. Rational equations

x appears in a denominator. **Algorithm:**

```
1. Write the domain:  every denominator ≠ 0
2. Combine over a common denominator, or cross-multiply
3. Solve the resulting equation
4. DISCARD any root outside the domain
```

**Example (the classic trap):**

```
1/(x−1) + 1/(x+1) = 2/(x²−1)

Domain:  x ≠ 1,  x ≠ −1     (since x² − 1 = (x−1)(x+1))

Combine the left side:
    (x+1) + (x−1)         2x
    ───────────────  =  ───────
    (x−1)(x+1)           x² − 1

So:   2x/(x²−1) = 2/(x²−1)   →   2x = 2   →   x = 1

BUT x = 1 is not in the domain  ❌

Answer: S = ∅
```

> This is exactly why the domain must be written **first**.

---

## 7. Radical equations

x appears under a root.

### 7.1 The core scheme

```
√(f(x)) = g(x)

  ⟺   ⎧ g(x) ≥ 0            ← a square root is never negative!
      ⎩ f(x) = g(x)²         ← (this automatically gives f(x) ≥ 0)
```

> You don't need to write `f(x) ≥ 0` separately: if `f(x) = g(x)²`, it is already ≥ 0.
> But `g(x) ≥ 0` is **mandatory**.

**Example:**

```
√(x + 5) = x − 1

Condition:  x − 1 ≥ 0  →  x ≥ 1

Square:     x + 5 = (x − 1)²
            x + 5 = x² − 2x + 1
            x² − 3x − 4 = 0
            (x − 4)(x + 1) = 0
            x = 4  or  x = −1

x = −1:  violates x ≥ 1  ❌
x = 4:   √9 = 3 = 4 − 1  ✓

Answer: {4}
```

### 7.2 Two radicals

Isolate one radical, square, then isolate the remaining one and square again. Track the
conditions at every step.

---

## 8. Absolute value equations

### 8.1 Definition

```
        ⎧  x,   if x ≥ 0
|x| =   ⎨
        ⎩ −x,   if x < 0
```

**Geometric meaning:** `|x|` is the **distance** from x to 0.
More generally, `|a − b|` is the distance between a and b.

> 🔗 This "distance" reading later becomes the **norm**: `‖v‖` is the length of a vector.
> `|x|` is the 1-dimensional norm. L1 regularization (Lasso) comes directly from it.

### 8.2 Key properties

```
|x| ≥ 0                       always
|x| = 0  ⟺  x = 0
|−x| = |x|
|x·y| = |x|·|y|
|x/y| = |x|/|y|               (y ≠ 0)
√(x²) = |x|                   ⚠️ NOT x!
|x + y| ≤ |x| + |y|           ← triangle inequality
```

### 8.3 Solution methods

**Method A — `|f(x)| = a` (a is a number):**

```
a < 0  →  no solution
a = 0  →  f(x) = 0
a > 0  →  f(x) = a  or  f(x) = −a
```

**Example:** `|2x − 3| = 5` → `2x − 3 = 5` (x = 4) or `2x − 3 = −5` (x = −1)

**Method B — `|f(x)| = g(x)` (x on the right too):**

```
⎧ g(x) ≥ 0
⎩ f(x) = g(x)  or  f(x) = −g(x)
```

**Example:**

```
|x − 1| = 2x + 3

Condition:  2x + 3 ≥ 0  →  x ≥ −1.5

1)  x − 1 = 2x + 3   →  x = −4   ❌ (violates the condition)
2)  x − 1 = −(2x+3)  →  x − 1 = −2x − 3  →  3x = −2  →  x = −2/3  ✓

Check:  |−2/3 − 1| = 5/3;   2(−2/3) + 3 = 5/3  ✓

Answer: {−2/3}
```

**Method C — case analysis by intervals (several absolute values):**

Find the points where each expression inside an absolute value becomes zero, split the
number line at those points, and remove the absolute values on each piece.

---

## 9. Inequalities: core properties

### 9.1 Four symbols

```
a < b    strictly less
a ≤ b    less than or equal (non-strict)
a > b    strictly greater
a ≥ b    greater than or equal (non-strict)
```

### 9.2 Property table ⭐

| # | Property | Direction |
|---|----------|-----------|
| 1 | `a < b  ⟹  a + c < b + c` | **unchanged** |
| 2 | `a < b`, `c > 0  ⟹  ac < bc` | **unchanged** |
| 3 | `a < b`, `c < 0  ⟹  ac > bc` | 🔴 **FLIPS** |
| 4 | `a < b`, `b < c  ⟹  a < c` | transitivity |
| 5 | `a < b`, `c < d  ⟹  a + c < b + d` | addition is allowed |
| 6 | `0 < a < b  ⟹  1/a > 1/b` | 🔴 **FLIPS** |
| 7 | `0 ≤ a < b  ⟹  a² < b²` | only for non-negatives! |

> ⚠️ **Property 5 has no subtraction analogue:** inequalities **cannot be subtracted**.
> From `3 < 5` and `1 < 10` you may NOT conclude `3 − 1 < 5 − 10` (2 < −5 is false).

### 9.3 Why multiplying by a negative flips the sign

This is not a rule to memorize — it's something to **see**:

```
Number line:     −5 ────── −2 ────── 0 ────── 2 ────── 5
                 ←──────── smaller left, bigger right ────────→

2 < 5  is true.
Now multiply by (−1):  −2  and  −5

Multiplication by a negative REFLECTS every point about 0.
After reflection, "left" and "right" swap  →  −2 > −5
```

Draw the number line on paper and explain it to yourself once. After that you will
never forget it.

### 9.4 Interval notation

| Notation | Meaning | On the line |
|----------|---------|-------------|
| `(a, b)` | a < x < b | endpoints **open** ○ |
| `[a, b]` | a ≤ x ≤ b | endpoints **closed** ● |
| `[a, b)` | a ≤ x < b | mixed |
| `(−∞, a)` | x < a | ∞ is always open |
| `A ∪ B` | union ("or") | |
| `A ∩ B` | intersection ("and") | |

---

## 10. Linear and quadratic inequalities

### 10.1 Linear

```
−3x + 5 > 11
     −3x > 6
       x < −2        ← divided by (−3), sign FLIPPED

Answer:  x ∈ (−∞, −2)
```

**Verification habit:** pick a number from your answer (say x = −3) and plug it into the
original: `−3(−3) + 5 = 14 > 11` ✓. Then pick one outside (x = 0): `5 > 11` ❌ — correct.

### 10.2 Compound inequality

```
2 ≤ 3x − 4 < 11        | add 4 everywhere
6 ≤ 3x < 15            | divide everywhere by 3  (3 > 0, sign unchanged)
2 ≤ x < 5

Answer:  x ∈ [2, 5)
```

### 10.3 Quadratic inequalities — the parabola method ⭐

```
ax² + bx + c  >  0   (or <, ≥, ≤)
```

**Algorithm:**

```
1. Find the zeros:  ax² + bx + c = 0  →  x₁, x₂
2. Sketch the parabola:   a > 0 → opens UP    ∪
                          a < 0 → opens DOWN  ∩
3. Read off the graph: where is it above / below the x-axis
```

**Example:** `x² − x − 6 ≤ 0`

```
Zeros:  x² − x − 6 = 0  →  (x − 3)(x + 2) = 0  →  x = −2,  x = 3
a = 1 > 0  →  opens up

        ╲                    ╱
         ╲                  ╱
  ────────●────────────────●────────  x
         −2       ⌄        3
              (here it is ≤ 0)

Answer:  x ∈ [−2, 3]
```

**Memory rule (for a > 0):**

```
ax² + bx + c < 0   →   BETWEEN the roots     (−2, 3)
ax² + bx + c > 0   →   OUTSIDE the roots     (−∞,−2) ∪ (3,+∞)
```

### 10.4 When D < 0

```
x² + 4x + 5 > 0
D = 16 − 20 = −4 < 0   →  no roots, the parabola never crosses the x-axis
a = 1 > 0              →  the parabola is ENTIRELY above the x-axis

Answer:  x ∈ ℝ  (all real numbers)
```

If the same example asked for `< 0`, the answer would be `∅`.

> 🔗 **AI connection:** "`ax² + bx + c > 0` for every x" (D < 0, a > 0) becomes
> **positive definiteness** for matrices. That is what lets optimization conclude
> "this point is a minimum."

---

## 11. The sign-chart method (rational inequalities)

The most powerful technique here. **Always in this order:**

```
1. Move everything LEFT  →  P(x)/Q(x) ▽ 0   (zero must be on the right!)
2. Combine into a single fraction
3. Factor numerator and denominator
4. CRITICAL POINTS: numerator = 0 (● filled, if ≤/≥)
                    denominator = 0 (○ ALWAYS open!)
5. Place them on the line, determine the sign on each interval
6. Write down the intervals with the required sign
```

> 🔴 **THE BIGGEST MISTAKE:** cross-multiplying in `(x−1)/(x+2) ≥ 0`.
> You **don't know** whether `x + 2` is positive or negative! If negative, the sign flips.
> **Never** multiply by a denominator in a rational inequality.

### Example 1

```
(x − 1)/(x + 2) ≥ 0

Critical points:  x = 1  (numerator = 0; ● because of ≥)
                  x = −2 (denominator = 0; ALWAYS ○)

Test one number from each interval:

          −2              1
  ────────○───────────────●────────  x
     x=−3       x=0          x=2
   (−4)/(−1)   (−1)/(2)    (1)/(4)
     = +4        = −0.5      = +0.25
      +            −            +

Answer:  x ∈ (−∞, −2) ∪ [1, +∞)
```

### Example 2 — an even-power factor

```
(x − 1)(x + 3) / (x − 2)² < 0

(x − 2)² > 0 always (for x ≠ 2) → the denominator does NOT affect the sign

So we need:  (x − 1)(x + 3) < 0   →   −3 < x < 1
The condition x ≠ 2 is automatically satisfied (2 ∉ (−3, 1))

Answer:  x ∈ (−3, 1)
```

**General rule:** a factor of **odd** multiplicity **flips** the sign as you cross its
root; a factor of **even** multiplicity **does not**.

---

## 12. Absolute value inequalities

### 12.1 The two core forms (memorize)

```
|x| < a   (a > 0)   ⟺   −a < x < a          ⟺   x ∈ (−a, a)
|x| > a   (a > 0)   ⟺   x < −a  OR  x > a    ⟺   x ∈ (−∞,−a) ∪ (a,+∞)
```

**Why, geometrically:**

```
|x| < 3  →  "distance from 0 is less than 3"     →  inside
       ───────(───────0───────)───────
              −3              3

|x| > 3  →  "distance from 0 is greater than 3"  →  outside
       ◄──────)───────0───────(──────►
              −3              3
```

Remember it as: "<" → **inside** (one interval), ">" → **outside** (two intervals).

### 12.2 Examples

```
|x − 4| < 3
⟺  −3 < x − 4 < 3
⟺   1 < x < 7
Answer: (1, 7)

Meaning: "x is within 3 units of 4"  ← the distance reading!
```

```
|2x + 1| ≥ 5
⟺  2x + 1 ≥ 5   or   2x + 1 ≤ −5
⟺  2x ≥ 4       or   2x ≤ −6
⟺  x ≥ 2        or   x ≤ −3
Answer: (−∞, −3] ∪ [2, +∞)
```

> ⚠️ When `a < 0`: `|x| < −2` → no solution (∅).  `|x| > −2` → all x (ℝ).
> Don't forget to check these cases.

---

## 13. Inequalities that matter for AI

This section goes beyond the school syllabus, but **these exact inequalities** appear in
machine learning proofs. Meet them now so that later you say "I know this."

### 13.1 Triangle inequality

```
|a + b| ≤ |a| + |b|
```

**Meaning:** the straight path is the shortest path.

For vectors: `‖u + v‖ ≤ ‖u‖ + ‖v‖`

> 🔗 This is one of the three axioms defining a **metric** (a distance). Distances between
> embeddings, k-NN, clustering — all of them rest on it.

### 13.2 AM–GM inequality

```
For a, b ≥ 0:      (a + b)/2  ≥  √(ab)
```

**Proof (one line):**

```
(√a − √b)² ≥ 0
a − 2√(ab) + b ≥ 0
a + b ≥ 2√(ab)
(a + b)/2 ≥ √(ab)        ✓  (equality only when a = b)
```

**Most famous consequence:** for `x > 0`, `x + 1/x ≥ 2`

```
AM–GM:  (x + 1/x)/2 ≥ √(x · 1/x) = 1   →   x + 1/x ≥ 2
```

### 13.3 Cauchy–Schwarz ⭐⭐

```
(a₁b₁ + a₂b₂ + ... + aₙbₙ)²  ≤  (a₁² + ... + aₙ²)(b₁² + ... + bₙ²)
```

In vector form:  `|u · v| ≤ ‖u‖ · ‖v‖`

> 🔗🔗 **This inequality is exactly why `cosine similarity` always lies in [−1, 1]:**
>
> ```
> cos(θ) = (u · v) / (‖u‖ · ‖v‖)
>
> Cauchy–Schwarz:  |u · v| ≤ ‖u‖·‖v‖
>            so:   |cos(θ)| ≤ 1
>            so:   −1 ≤ cos(θ) ≤ 1     ✓
> ```
>
> Every time you compute embedding similarity, you are relying on this inequality. It is
> the **shortest bridge** from school algebra to LLMs.

### 13.4 Bernoulli's inequality

```
For x ≥ −1 and n ≥ 1:     (1 + x)ⁿ ≥ 1 + nx
```

Used in convergence analysis and learning-rate bounds.

### 13.5 Jensen's inequality — just an introduction

If `f` is a **convex** function:

```
f( E[X] )  ≤  E[ f(X) ]
```

> 🔗 This is the foundation of the **ELBO** (variational inference), of
> **KL divergence ≥ 0**, and of the **EM algorithm**. You don't have to prove it now —
> just remember the shape.

### 13.6 Summary table

| Inequality | Where it shows up in AI |
|------------|-------------------------|
| Triangle | Metrics, embedding distances, gradient-norm bounds |
| AM–GM | Optimization, bounding arguments |
| Cauchy–Schwarz | **Cosine similarity ∈ [−1,1]**, attention scores |
| Bernoulli | Convergence rates, learning rates |
| Jensen | KL divergence, ELBO, VAE, EM |

---

## 14. Museum of mistakes

**Everyone** makes these. Knowing them in advance means not making them.

| # | Mistake | Correct |
|---|---------|---------|
| 1 | `−3x > 6  →  x > −2` | 🔴 `x < −2` — dividing by a negative flips the sign |
| 2 | `x² = 5x  →  x = 5` | 🔴 Don't divide by x! `x(x−5)=0` → `{0, 5}` |
| 3 | `√(x²) = x` | 🔴 `√(x²) = \|x\|` |
| 4 | Multiplying by a denominator in a rational inequality | 🔴 Use the sign chart |
| 5 | Not writing the domain | 🔴 Write it **before** solving |
| 6 | Squaring without checking | 🔴 Extraneous roots appear |
| 7 | `(a + b)² = a² + b²` | 🔴 `= a² + 2ab + b²` |
| 8 | Filling in ● at a denominator zero | 🔴 Denominator zeros are **always** ○ |
| 9 | `\|x\| > −2` → "no solution" | 🔴 All x, since an absolute value is always ≥ 0 |
| 10 | Ignoring `a = 0` in a parametric equation | 🔴 Always split into cases |
| 11 | Deducing `1/a > 1/b` from `a < b` | 🔴 Only if a and b have the **same sign** |
| 12 | Subtracting inequalities | 🔴 Only **addition** is valid |

---

## 📌 One-page summary

```
EQUATIONS:
  write domain  →  simplify  →  solve  →  VERIFY
  Dangerous: ×variable, ÷variable, ()², √

LINEAR:        ax + b = 0    →  a≠0: x=−b/a | a=0,b=0: ℝ | a=0,b≠0: ∅
SYSTEM:        intersecting | parallel | identical  →  1 | 0 | ∞ solutions
QUADRATIC:     x = (−b ± √D)/2a,   D = b² − 4ac
VIETA:         x₁+x₂ = −b/a,   x₁x₂ = c/a
ABS VALUE:     √(x²) = |x|,   |x|<a ⟺ −a<x<a,   |x|>a ⟺ outside

INEQUALITIES:
  🔴 ×/÷ by a negative  →  SIGN FLIPS
  Quadratic: a>0 & <0  →  between the roots
             a>0 & >0  →  outside the roots
  Rational:  move all left → 0, sign chart, denominator ○

FOR AI:        |a+b| ≤ |a|+|b|  |  (a+b)/2 ≥ √(ab)  |  |u·v| ≤ ‖u‖‖v‖
```

---

**Next:** [02-problems-en.md](02-problems-en.md) — get paper and a pen.
