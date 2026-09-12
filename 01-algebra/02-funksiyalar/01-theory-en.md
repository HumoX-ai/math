# Functions — Theory

> **How to read:** after each section, close the file, draw the graph **by hand**, and
> write the definition in your own words. Learning this topic without drawing is like
> learning to swim from a book.

**Contents**

1. [What a function is](#1-what-a-function-is)
2. [Ways to define a function](#2-ways-to-define-a-function)
3. [Domain and range](#3-domain-and-range)
4. [The graph](#4-the-graph)
5. [Gallery of parent functions](#5-gallery-of-parent-functions)
6. [Linear functions](#6-linear-functions)
7. [Quadratic functions](#7-quadratic-functions)
8. [Properties of functions](#8-properties-of-functions)
9. [Graph transformations](#9-graph-transformations)
10. [Composition](#10-composition)
11. [Inverse functions](#11-inverse-functions)
12. [Piecewise functions](#12-piecewise-functions)
13. [Functions that matter for AI](#13-functions-that-matter-for-ai)
14. [Museum of mistakes](#14-museum-of-mistakes)

---

## 1. What a function is

### 1.1 Definition

A **function** is a **rule** that assigns to every input value (`x`) **exactly one**
output value (`y`).

```
        ┌─────────────┐
  x ──► │      f      │ ──► y = f(x)
        └─────────────┘
      input         output
      (argument)    (value)
```

**Notation:** `f(x)` means "the value of f at x" (`f` is **not multiplied** by x!).

```
f(x) = 2x + 1

f(3)  = 2·3 + 1 = 7          ← 3 went in, 7 came out
f(0)  = 1
f(−1) = −1
f(a)  = 2a + 1
f(a+1) = 2(a+1) + 1 = 2a + 3  ← the WHOLE expression replaces x
```

### 1.2 The "exactly one" rule — why it matters

```
✅ A FUNCTION                       ❌ NOT A FUNCTION
   x → x²                              x → ±√x
   1 → 1                               4 → 2  and  4 → −2
   2 → 4                               (one input, TWO outputs)
   −1 → 1
   (two inputs → same output is FINE)
```

- Every `x` gets one `y`: **mandatory**.
- Different `x`'s sharing a `y`: **allowed** (`f(1) = f(−1) = 1` for `x²`).

> 🔗 **AI:** a neural network is a function: `f(image) = "cat"`. One image, one answer.
> If a model gave a different answer to the same input each time, it wouldn't be a
> function — and you couldn't train or test it. (Randomness — `sampling` — is added
> *on top of* the function, separately.)

### 1.3 The vertical line test

On a graph: if **any vertical line** crosses the graph at **2 or more** points, it is
not a function.

```
   y = x²  (function)             x = y²  (NOT a function)
      │    ╱                          │      ╭──
      │   ╱                        ───┼─────●────  ← vertical line
   ───┼──╱───                         │      ╰──      crosses twice
      │╱                              │
```

---

## 2. Ways to define a function

| Method | Example | AI analogue |
|--------|---------|-------------|
| **Formula** | `f(x) = x² − 1` | Model architecture |
| **Table** | `x: 1,2,3 → y: 2,4,6` | **Dataset** (training data) |
| **Graph** | a parabola sketch | Loss curve, visualization |
| **Words** | "double the number and add 1" | Task description |
| **Algorithm** | `def f(x): return 2*x+1` | Code |

> 🔗 **The essence of machine learning:** we are given a **table** (data) and want to find
> a **formula** (model). In problem A6 you do exactly this by hand.

---

## 3. Domain and range

### 3.1 Domain — D(f)

**D(f)** is the set of all `x` for which the function **makes sense**. It is the same
thing as the domain from the previous topic.

```
1.  Denominator ≠ 0      f(x) = 1/(x−2)        D = ℝ \ {2}  or  (−∞,2) ∪ (2,+∞)
2.  Even root ≥ 0        f(x) = √(x+3)         D = [−3, +∞)
3.  Both together        f(x) = √(x−1)/(x−4)   D = [1, 4) ∪ (4, +∞)
4.  No restriction       f(x) = x² + 3x        D = ℝ
```

**Algorithm:** find every "danger spot" → write a condition → **intersect** the conditions (∩).

### 3.2 Range — E(f)

**E(f)** is the set of all `y` values the function **actually takes**.

```
f(x) = x²           E = [0, +∞)      since x² ≥ 0 always, and 0 is reached
f(x) = x² + 2       E = [2, +∞)      shifted up by 2
f(x) = −|x| + 3     E = (−∞, 3]      maximum 3, at x = 0
f(x) = √x − 1       E = [−1, +∞)
f(x) = 1/x          E = ℝ \ {0}      never equals 0
f(x) = 1/(1+x²)     E = (0, 1]       ← important: 0 is NOT reached, 1 IS
```

**Ways to find the range:**
1. Sketch the graph and ask "where are the upper/lower limits."
2. Start from the simplest piece: `x² ≥ 0` → `x² + 2 ≥ 2`.
3. Solve `y = f(x)` for `x` and see which `y` admit a solution.

> 🔗 **AI:** the range of `sigmoid` is `(0, 1)` — that's why it's used as a
> **probability**. `tanh` has range `(−1, 1)`. `ReLU` has range `[0, +∞)`. Choosing an
> activation = choosing a range.

---

## 4. The graph

The **graph** is the set of all points `(x, f(x))`.

```
f(x) = x² − 2

x:   −2   −1    0    1    2
y:    2   −1   −2   −1    2

      y
      │        ●(2,2)
   2 ─┼─●
      │  ╲     ╱
   ───┼───●───●─── x
      │    ╲ ╱
  −2 ─┼─────●(0,−2)
```

**What you can read off a graph:**

| Question | Where on the graph |
|----------|--------------------|
| `f(1) = ?` | go up from `x = 1` to the curve → read `y` |
| Zeros (`f(x) = 0`) | where the graph crosses the `x`-axis |
| Where `f(x) > 0` | where the graph is **above** the `x`-axis |
| Minimum/maximum | lowest/highest point |
| Increasing/decreasing | going up/down as you move left to right |
| Domain | the graph's "shadow" on the `x`-axis |
| Range | the graph's "shadow" on the `y`-axis |

> 🔗 **AI:** a `loss vs epoch` plot is **the graph of a function**. Reading it (is it
> decreasing? flattening? jumping?) is an ML engineer's daily work.

---

## 5. Gallery of parent functions

You must be able to draw these 7 **from memory**. Draw each three times on paper.

| Function | Graph | D | E | Property |
|----------|-------|---|---|----------|
| `f(x) = c` | horizontal line | ℝ | {c} | constant |
| `f(x) = x` | 45° line | ℝ | ℝ | identity, odd |
| `f(x) = x²` | parabola ∪ | ℝ | [0,∞) | even, min (0,0) |
| `f(x) = x³` | S-shape | ℝ | ℝ | odd, increasing |
| `f(x) = \|x\|` | V-shape | ℝ | [0,∞) | even, min (0,0), corner |
| `f(x) = √x` | half parabola (sideways) | [0,∞) | [0,∞) | increasing, slows down |
| `f(x) = 1/x` | hyperbola | ℝ\{0} | ℝ\{0} | odd, 2 branches |

```
   x²          x³           |x|          √x           1/x
   ╲  ╱         ╱          ╲   ╱          ╭──         ╲│
    ╲╱       ──┼──          ╲ ╱          ╱          ───┼───
              ╱              ╲          ╱             │╲
```

**Why exactly these:** every other function you'll meet is one of these **shifted,
stretched, added, or composed** (§9, §10).

---

## 6. Linear functions

### 6.1 Form

```
f(x) = kx + b
       │    └── b: the constant term, the y-intercept — where the graph crosses the y-axis
       └── k: the slope — the RATE of change
```

**Graph:** a straight line. Two points are enough.

### 6.2 The meaning of `k` — the key idea

```
k = (y₂ − y₁)/(x₂ − x₁) = Δy/Δx = "how much y changes when x grows by one unit"
```

| k | Graph | Meaning |
|---|-------|---------|
| k > 0 | ↗ | increasing |
| k < 0 | ↘ | decreasing |
| k = 0 | → | constant (horizontal) |
| \|k\| large | steep | changes fast |
| \|k\| small | flat | changes slowly |

**Example:** a taxi: 5000 base fare + 2000 per km.
`C(d) = 2000d + 5000`. `k = 2000` — price per km. `b = 5000` — the price at d = 0.

### 6.3 Line through two points

```
Points (1, 3) and (3, 7):

1. k = (7 − 3)/(3 − 1) = 4/2 = 2
2. b:  plug (1, 3) into y = 2x + b:  3 = 2·1 + b  →  b = 1
3. f(x) = 2x + 1

Check (3, 7):  2·3 + 1 = 7 ✓
```

### 6.4 Parallel and perpendicular

```
Parallel:         k₁ = k₂           (same rate, different start)
Perpendicular:    k₁ · k₂ = −1      (k₂ = −1/k₁)
```

### 6.5 Zeros and intercepts

```
f(x) = −3x + 6
y-intercept:  f(0) = 6                  → (0, 6)
x-intercept (zero):  −3x + 6 = 0 → x = 2 → (2, 0)
```

> 🔗🔗 **AI — this section IS machine learning:**
>
> ```
> School:       y = kx + b
> ML:           y = wx + b        w — weight, b — bias
> Many inputs:  y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b = w·x + b
> PyTorch:      nn.Linear(n, 1)
> ```
>
> `nn.Linear` is a **linear function**. Every layer of a neural network is a linear
> function followed by an activation. Training `w` = finding `k`.
> In 6.3 you found `k, b` from two points — that was **training on 2 data points**.

---

## 7. Quadratic functions

### 7.1 Form and vertex

```
f(x) = ax² + bx + c,   a ≠ 0

Vertex:             x₀ = −b/(2a),    y₀ = f(x₀)
Axis of symmetry:   x = x₀
a > 0  →  ∪  →  y₀ = MINIMUM,   E = [y₀, +∞)
a < 0  →  ∩  →  y₀ = MAXIMUM,   E = (−∞, y₀]
```

**Why `−b/2a`?** The zeros `x₁, x₂` are symmetric; their midpoint is
`(x₁+x₂)/2 = (−b/a)/2 = −b/2a` (Vieta!). The formula works even when there are no zeros.

### 7.2 Vertex form

```
f(x) = a(x − h)² + k          vertex (h, k)
```

From standard form to vertex form — **complete the square** (previous topic!):

```
x² + 4x + 7
= (x² + 4x + 4) + 3
= (x + 2)² + 3               →  vertex (−2, 3),  min = 3
```

**What vertex form gives you:**
- The vertex, immediately.
- `(x − h)² ≥ 0` → `f(x) ≥ k` (for a > 0) — the range, immediately.
- The graph = `x²` shifted `h` right, `k` up, stretched by `a` (§9).

### 7.3 Three forms

| Form | Formula | What it shows instantly |
|------|---------|-------------------------|
| Standard | `ax² + bx + c` | `c` = y-intercept |
| Vertex | `a(x − h)² + k` | vertex `(h, k)` |
| Factored | `a(x − x₁)(x − x₂)` | zeros `x₁, x₂` |

### 7.4 Optimization with quadratics

```
Largest area of a rectangle with perimeter 40 m?

Sides: x and 20 − x
S(x) = x(20 − x) = −x² + 20x
a = −1 < 0 → there is a maximum
x₀ = −20/(2·(−1)) = 10  →  S = 100 m²  →  a SQUARE
```

> 🔗 **AI:** this is **optimization** in its simplest form. Loss functions are often
> (locally) parabola-shaped. Gradient descent is "rolling down to the vertex." In problem
> G5 you'll show that `L(w)` is **literally a parabola**.

---

## 8. Properties of functions

### 8.1 Even and odd

```
EVEN:   f(−x) = f(x)      graph is SYMMETRIC about the y-axis (mirror)
ODD:    f(−x) = −f(x)     graph is symmetric about the origin (180° rotation)
```

**Check from the definition — only from the definition:**

```
f(x) = x⁴ − 3x²
f(−x) = (−x)⁴ − 3(−x)² = x⁴ − 3x² = f(x)         → EVEN

g(x) = x³ + x
g(−x) = −x³ − x = −(x³ + x) = −g(x)              → ODD

h(x) = x² + x
h(−x) = x² − x     ≠ h(x)  and  ≠ −h(x)          → NEITHER
```

**Shortcut (polynomials):** only even powers → even; only odd powers → odd; mixed →
neither. `|x|` is even. `1/x` is odd. A constant `c ≠ 0` is even.

> 🔗 **AI:** `tanh` is odd, `x²` (MSE) is even, `ReLU` is neither. Knowing the symmetry
> helps you reason about a model: e.g. `tanh(−x) = −tanh(x)` — a negative signal comes
> out exactly negated.

### 8.2 Monotonicity

```
INCREASING on an interval:   x₁ < x₂  ⟹  f(x₁) < f(x₂)     ↗
DECREASING on an interval:   x₁ < x₂  ⟹  f(x₁) > f(x₂)     ↘
```

**Sample proof:** `f(x) = 2x + 3` is increasing:

```
x₁ < x₂  →  2x₁ < 2x₂  →  2x₁ + 3 < 2x₂ + 3  →  f(x₁) < f(x₂)   ∎
```

⚠️ **Trap:** `1/x` is decreasing on `(−∞, 0)` **and** decreasing on `(0, +∞)`, but it is
**NOT decreasing on its whole domain**: `f(−1) = −1 < f(1) = 1`. State intervals separately.

> 🔗 **AI:** `sigmoid`, `softmax`, `log`, `exp` are **monotonically increasing**. This
> matters a lot: a monotone function **preserves order**. If `z₁ > z₂` then
> `softmax(z)₁ > softmax(z)₂`. That's why `argmax` is the same before and after softmax.

### 8.3 Zeros and sign

```
f(x) = x³ − 4x = x(x − 2)(x + 2)

Zeros:  x = −2, 0, 2

Signs (sign chart — previous topic):
     −2        0        2
──────●────────●────────●──────
  −        +        −        +

f(x) > 0  ⟺  x ∈ (−2, 0) ∪ (2, +∞)
```

### 8.4 Boundedness

```
f(x) = 1/(1 + x²)

1 + x² ≥ 1   →   0 < 1/(1+x²) ≤ 1
E = (0, 1]:  bounded above by 1 (reached at x = 0), bounded below by 0 (never reached)
```

### 8.5 Maximum and minimum

- **Global:** the largest/smallest value over the whole domain.
- **Local:** the largest/smallest in some neighbourhood.

> 🔗 **AI:** finding the minimum of the loss = training. The **local** minimum trap is a
> classic deep-learning problem. Those words come from this section.

---

## 9. Graph transformations

Get hundreds of graphs from one parent (`x²`, `|x|`, `√x`...). **Memorize:**

| Notation | Effect | Direction |
|----------|--------|-----------|
| `f(x) + c` | shift up | ↑ c |
| `f(x) − c` | shift down | ↓ c |
| `f(x − c)` | shift **right** | → c ⚠️ (minus = right!) |
| `f(x + c)` | shift **left** | ← c |
| `a·f(x)`, a > 1 | vertical stretch | steeper |
| `a·f(x)`, 0 < a < 1 | vertical compression | flatter |
| `−f(x)` | reflect over the x-axis | ∪ → ∩ |
| `f(−x)` | reflect over the y-axis | left↔right |
| `f(bx)`, b > 1 | horizontal compression | narrower |
| `\|f(x)\|` | fold the negative part up | |
| `f(\|x\|)` | mirror the right half onto the left | |

**Why does `f(x − 2)` go RIGHT?** Because `f(x − 2)` at `x = 2` gives `f(0)`. The value
the original had at `x = 0` now sits at `x = 2` — it moved right.

**Example — in order:**

```
y = −2(x − 3)² + 1        parent: x²

1. x²           → parabola, vertex (0,0)
2. (x − 3)²     → 3 right,               vertex (3, 0)
3. 2(x − 3)²    → stretch by 2,          vertex (3, 0), narrower
4. −2(x − 3)²   → reflect,               vertex (3, 0), ∩
5. −2(x−3)² + 1 → 1 up,                  vertex (3, 1)   ✓
```

> 🔗 **AI — normalization:** `z = (x − μ)/σ` is `x` shifted left by `μ` and compressed
> by `1/σ`. It's in **every** ML pipeline. Its inverse `x = σz + μ` is denormalization.
> This is §9, exactly.

---

## 10. Composition

> ⭐⭐⭐⭐⭐ **The most important section of the whole topic.** A neural network is a composition.

### 10.1 Definition

```
(f ∘ g)(x) = f(g(x))       "first g, then f"    ← read from the INSIDE out

  x ──► g ──► g(x) ──► f ──► f(g(x))
```

**Example:**

```
f(x) = 2x + 1,    g(x) = x²

f(g(x)) = f(x²) = 2x² + 1              ← g goes inside f
g(f(x)) = g(2x+1) = (2x + 1)²          ← f goes inside g

f(g(2)) = 2·4 + 1 = 9
g(f(2)) = (5)² = 25                    ← NOT EQUAL!
```

**Composition is NOT commutative:** `f∘g ≠ g∘f` in general. Order matters.

### 10.2 Domain

The domain of `f(g(x))`: `x` must be in the domain of `g` **and** `g(x)` must be in the
domain of `f`.

```
f(x) = √x,  g(x) = x − 4
f(g(x)) = √(x − 4)     D: x − 4 ≥ 0  →  x ≥ 4
g(f(x)) = √x − 4       D: x ≥ 0
```

### 10.3 Decomposition

```
h(x) = (3x − 1)⁵          →   g(x) = 3x − 1  (inner),   f(u) = u⁵  (outer)
h(x) = √(x² + 1)          →   g(x) = x² + 1,             f(u) = √u
h(x) = 1/(x + 2)²         →   g(x) = x + 2,   m(u) = u², f(v) = 1/v   (3 layers)
```

This skill is mandatory for the **chain rule** in calculus: to differentiate, you must
be able to separate the outer and inner functions.

### 10.4 🔗🔗 A neural network IS a composition

```
One layer:        h = σ(Wx + b)                σ — activation (ReLU, sigmoid...)
                       └──┬──┘
                    linear function

Two layers:       y = W₂ · σ(W₁x + b₁) + b₂
                      └───────┬───────────┘
                       f₂ ∘ σ ∘ f₁

n layers:         y = fₙ ∘ σ ∘ fₙ₋₁ ∘ σ ∘ ... ∘ σ ∘ f₁ (x)

"Deep" learning = "many-layer COMPOSITION"
```

**Why activations are needed — a proof (very important):**

```
Compose two linear functions:
f(x) = ax + b,   g(x) = cx + d

f(g(x)) = a(cx + d) + b = (ac)x + (ad + b)  →  STILL LINEAR!
                          └┬┘   └───┬───┘
                          k'        b'

So:  100 linear layers = 1 linear layer.
Depth buys nothing.

Put an activation (σ) — a NON-linear function — between them, and the composition
becomes genuinely more complex.
```

This proof is half of the answer to "why does deep learning work at all." You just
understood it, and it used only §6 and §10.

**Example (problem E7):**

```
L₁(x) = 2x − 1,   σ(z) = max(0, z),   L₂(z) = −z + 3

y(x) = L₂(σ(L₁(x)))

x = 0:  L₁ = −1  →  σ = 0   →  L₂ = 3
x = 1:  L₁ = 1   →  σ = 1   →  L₂ = 2
x = 2:  L₁ = 3   →  σ = 3   →  L₂ = 0

Graph:  for x ≤ 1/2, y = 3 (flat);   for x > 1/2, y = −2x + 4 (falling)
        → a PIECEWISE LINEAR function. A ReLU network always produces one.
```

---

## 11. Inverse functions

### 11.1 The idea

`f` takes `x` to `y`. `f⁻¹` takes `y` **back** to `x`.

```
f:    x ──► y            f(x) = 3x − 6:      2 ──► 0
f⁻¹:  y ──► x            f⁻¹(y) = (y+6)/3:   0 ──► 2

f⁻¹(f(x)) = x    and    f(f⁻¹(y)) = y      ← "undoing"
```

⚠️ `f⁻¹(x)` is **NOT** `1/f(x)`! Similar notation, different meaning.

### 11.2 When it exists

Only for **one-to-one** (injective) functions: different `x` → different `y`.

**Horizontal line test:** if some horizontal line crosses the graph at 2+ points, there is
**no** inverse.

```
f(x) = x²:   f(2) = f(−2) = 4  →  send 4 back to 2 or to −2?  →  NO inverse
Fix:  restrict the domain:  for x ≥ 0,  f⁻¹(x) = √x
```

### 11.3 Algorithm

```
1. Write y = f(x)
2. Solve for x in terms of y
3. Swap x ↔ y (by convention the argument is called x)

f(x) = (2x + 1)/(x − 3)

y(x − 3) = 2x + 1
xy − 3y = 2x + 1
xy − 2x = 3y + 1
x(y − 2) = 3y + 1
x = (3y + 1)/(y − 2)

f⁻¹(x) = (3x + 1)/(x − 2),   x ≠ 2

Check:  f(4) = 9/1 = 9,   f⁻¹(9) = 28/7 = 4  ✓
```

### 11.4 Graph

The graphs of `f` and `f⁻¹` are **symmetric** about the line `y = x`. `D(f⁻¹) = E(f)`,
`E(f⁻¹) = D(f)`.

> 🔗 **AI:**
> - `exp` ↔ `log` (upcoming topics)
> - `sigmoid` ↔ `logit`: `σ(x) = 1/(1+e⁻ˣ)`, `logit(p) = ln(p/(1−p))`
> - normalization ↔ denormalization
> - **Autoencoder:** `encoder` ↔ `decoder` — a pair of "approximately inverse" functions
> - Tokenizer `encode` ↔ `decode`

---

## 12. Piecewise functions

A different formula on each interval:

```
        ⎧ x + 2,   x < 0
f(x) =  ⎨ x²,      0 ≤ x ≤ 2
        ⎩ 4,       x > 2

f(−3) = −1     (row 1)
f(0)  = 0      (row 2, since 0 ≤ 0 ≤ 2)
f(2)  = 4      (row 2)
f(5)  = 4      (row 3)
```

**Continuity** — does the graph "break"? Check at the boundaries:
`x = 0`: from the left `0 + 2 = 2`, from the right `0² = 0` → a **jump**, discontinuous.
`x = 2`: from the left `4`, from the right `4` → continuous.

### Piecewise functions in AI

```
ReLU(z)       = max(0, z)            = ⎧ z,  z > 0
                                       ⎩ 0,  z ≤ 0

LeakyReLU(z)  = ⎧ z,      z > 0
                ⎩ 0.01z,  z ≤ 0

Heaviside(z)  = ⎧ 1,  z ≥ 0             ← the first "neuron" (1943, McCulloch–Pitts)
                ⎩ 0,  z < 0

clip(z,lo,hi) = max(lo, min(hi, z))   ← gradient clipping, pixel range [0,255]

Huber loss    = ⎧ ½z²,           |z| ≤ δ    ← a blend of MSE and MAE
                ⎩ δ(|z| − δ/2),  |z| > δ
```

---

## 13. Functions that matter for AI

This section is an **introduction**. The number `e` and `ln` come in later topics. For
now, know the **shapes** and **properties**.

### 13.1 Sigmoid

```
σ(x) = 1 / (1 + e⁻ˣ)          e ≈ 2.718

         1 ┤            ╭────────
           │          ╱
       0.5 ┤────────●
           │      ╱
         0 ┤─────╯
           └────┼────────── x
                0
```

| Property | Value | Why it matters |
|----------|-------|----------------|
| D | ℝ | any number goes in |
| E | (0, 1) | works as a **probability** |
| σ(0) | 0.5 | the "no idea" point |
| Monotone | increasing | preserves order |
| Symmetry | σ(−x) = 1 − σ(x) | P(yes) + P(no) = 1 |
| Limits | x→+∞: →1, x→−∞: →0 | saturation |

**Range proof:** `e⁻ˣ > 0` → `1 + e⁻ˣ > 1` → `0 < 1/(1+e⁻ˣ) < 1`. ∎

### 13.2 tanh

```
tanh(x) = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ) = 2σ(2x) − 1

E = (−1, 1),  odd,  tanh(0) = 0,  monotonically increasing
```

### 13.3 ReLU

```
ReLU(x) = max(0, x)         E = [0, +∞),   corner at x = 0 (no derivative there)
```

Why is it the most popular? Cheap to compute, gradient is 1 or 0 (no saturation for
x > 0), and its compositions are piecewise linear.

### 13.4 Softmax (a function of many inputs)

```
softmax(z)ᵢ = eᶻⁱ / Σⱼ eᶻʲ

Properties:  each output ∈ (0, 1),   they sum to 1,   order is preserved
```

It is "the function that turns n numbers into n probabilities." It sits at the end of
every LLM.

### 13.5 Loss functions

```
MSE(y, ŷ) = (y − ŷ)²                even, a parabola, minimum 0 at 0
MAE(y, ŷ) = |y − ŷ|                 even, V-shape
```

---

## 14. Museum of mistakes

| # | Mistake | Correct |
|---|---------|---------|
| 1 | `f(x + 1) = f(x) + 1` | 🔴 The **whole** `(x+1)` replaces `x`: `f(x+1) = 2(x+1)+1` |
| 2 | `f(x − 2)` shifts left | 🔴 **Right**. `x − 2 = 0` → `x = 2` |
| 3 | `f(g(x)) = g(f(x))` | 🔴 **Not equal** in general |
| 4 | `f⁻¹(x) = 1/f(x)` | 🔴 Inverse function ≠ reciprocal |
| 5 | `x²` has an inverse | 🔴 Only when restricted to `x ≥ 0` |
| 6 | `1/x` is decreasing on its whole domain | 🔴 Only on each interval separately |
| 7 | "Even — because there's an `x²`" | 🔴 Only from the **definition**: check `f(−x) = f(x)` |
| 8 | Range = Domain | 🔴 Different things. `√x`: D=[0,∞), E=[0,∞) coincide by accident |
| 9 | Vertex at `x = b/2a` | 🔴 `x = −b/(2a)` — the minus! |
| 10 | `E(1/(1+x²)) = [0, 1]` | 🔴 `(0, 1]` — 0 is **never reached** |
| 11 | "A deep network = many linear layers" | 🔴 Linear∘linear = linear. Activations are **required** |
| 12 | Stating properties without a sketch | 🔴 Draw it. Every time. |

---

## 📌 One-page summary

```
FUNCTION:    each x → EXACTLY ONE y.  Vertical line test.
D(f):        denominator≠0, √ inside≥0.   E(f): the graph's y-shadow.

LINEAR:      y = kx + b.   k = Δy/Δx = rate.   b = y-intercept.
             Parallel: k₁=k₂.  Perpendicular: k₁k₂=−1.         [ML: y = wx + b]

QUADRATIC:   vertex x₀ = −b/2a.   Vertex form a(x−h)²+k.   a>0 → min, a<0 → max.

PROPERTIES:  even f(−x)=f(x) | odd f(−x)=−f(x) | monotone | zeros | bounded

SHIFTS:      f(x)+c ↑ | f(x−c) → | a·f(x) stretch | −f(x) reflect | f(−x) reflect

COMPOSITION: f(g(x)) — inside out. f∘g ≠ g∘f.
             (ax+b)∘(cx+d) = linear  →  ACTIVATIONS NEEDED          [ML: deep = many ∘]

INVERSE:     y=f(x) → solve for x → swap.  Only for one-to-one f.  ≠ 1/f(x)

AI:          sigmoid (0,1) | tanh (−1,1) | ReLU [0,∞) | softmax → probabilities
```

---

**Next:** [02-problems-en.md](02-problems-en.md) — paper, pen, and a **ruler**.
