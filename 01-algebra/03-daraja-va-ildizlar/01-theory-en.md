# Powers and Roots — Theory

> **How to read:** in this topic, **prove** every rule, never memorize it. The person who
> memorized `aᵐ·aⁿ = aᵐ⁺ⁿ` will one day also write `aᵐ + aⁿ = aᵐ⁺ⁿ`. The person who proved
> it by counting factors never will.

**Contents**

1. [Natural powers](#1-natural-powers)
2. [The power rules — and WHY](#2-the-power-rules--and-why)
3. [Zero and negative exponents](#3-zero-and-negative-exponents)
4. [Roots](#4-roots)
5. [Root properties](#5-root-properties)
6. [Rational exponents — the unifying idea](#6-rational-exponents--the-unifying-idea)
7. [Simplifying and rationalizing](#7-simplifying-and-rationalizing)
8. [Graphs of power functions](#8-graphs-of-power-functions)
9. [Scientific notation](#9-scientific-notation)
10. [Growth: 2ⁿ, n², and computer numbers](#10-growth-2ⁿ-n-and-computer-numbers)
11. [Power equations and inequalities](#11-power-equations-and-inequalities)
12. [What matters for AI](#12-what-matters-for-ai)
13. [Museum of mistakes](#13-museum-of-mistakes)

---

## 1. Natural powers

```
aⁿ = a · a · a · ... · a        (n times)
     └──────┬──────┘
   a — BASE,  n — EXPONENT

2⁵ = 32,   (−3)³ = −27,   (1/2)³ = 1/8,   0.1² = 0.01
```

### Sign rules

```
Positive base:            always positive
Negative base, EVEN n:    positive      (−2)⁴ = 16
Negative base, ODD n:     negative      (−2)³ = −8
```

### ⚠️ `(−2)⁴` vs `−2⁴` — DIFFERENT

```
(−2)⁴ = (−2)(−2)(−2)(−2) = +16       ← parentheses: the NEGATIVE NUMBER is raised
−2⁴   = −(2⁴) = −16                   ← no parentheses: compute 2⁴, then negate
```

Same in Python: `(-2)**4 = 16`, `-2**4 = -16`. A source of bugs in code, too.

---

## 2. The power rules — and WHY

Five rules. Prove each by **counting factors**:

### 2.1 Product: `aᵐ · aⁿ = aᵐ⁺ⁿ`
```
a³ · a² = (a·a·a)(a·a) = a⁵        3 + 2 = 5 ✓
```
**Why:** `m` factors next to `n` factors = `m + n` factors.

### 2.2 Quotient: `aᵐ / aⁿ = aᵐ⁻ⁿ`
```
a⁵ / a² = (a·a·a·a·a)/(a·a) = a³   5 − 2 = 3 ✓
```
**Why:** `n` factors cancel.

### 2.3 Power of a power: `(aᵐ)ⁿ = aᵐⁿ`
```
(a²)³ = a² · a² · a² = a⁶          2 · 3 = 6 ✓
```
**Why:** `aᵐ` written `n` times → `m·n` factors.

### 2.4 Power of a product: `(ab)ⁿ = aⁿbⁿ`
```
(ab)³ = ab · ab · ab = a³b³
```

### 2.5 Power of a quotient: `(a/b)ⁿ = aⁿ/bⁿ`
```
(a/b)² = a²/b²
```

### Table

| Rule | Formula | Example |
|------|---------|---------|
| Product | `aᵐ·aⁿ = aᵐ⁺ⁿ` | `2³·2⁴ = 2⁷ = 128` |
| Quotient | `aᵐ/aⁿ = aᵐ⁻ⁿ` | `3⁵/3³ = 9` |
| Power of power | `(aᵐ)ⁿ = aᵐⁿ` | `(5²)³ = 5⁶` |
| Product | `(ab)ⁿ = aⁿbⁿ` | `(2·5)³ = 1000` |
| Quotient | `(a/b)ⁿ = aⁿ/bⁿ` | `(2/3)² = 4/9` |

### ⚠️ Rules that DON'T exist (everyone makes these)

```
aᵐ + aⁿ  ≠  aᵐ⁺ⁿ          2² + 2³ = 12,  2⁵ = 32
(a + b)ⁿ  ≠  aⁿ + bⁿ      (1 + 1)² = 4,  1² + 1² = 2
2³ · 2⁴  ≠  4⁷            bases are NOT multiplied; it's 2⁷
(aᵐ)ⁿ  ≠  a^(mⁿ)          (2³)² = 64,  2^(3²) = 512
```

---

## 3. Zero and negative exponents

### 3.1 Why `a⁰ = 1`

**Not a definition — a consequence.** Follow the pattern:

```
2⁴ = 16
2³ = 8      ← ÷2
2² = 4      ← ÷2
2¹ = 2      ← ÷2
2⁰ = ?      ← ÷2  →  1
```

Or from the quotient rule: `a³/a³ = a⁰`, but `a³/a³ = 1`. So `a⁰ = 1`.

```
5⁰ = 1,   (−7)⁰ = 1,   (2/3)⁰ = 1,   x⁰ = 1  (x ≠ 0)
0⁰ — UNDEFINED (often taken as 1 by convention, but be careful)
```

### 3.2 Why `a⁻ⁿ = 1/aⁿ`

Keep the pattern going:

```
2¹ = 2
2⁰ = 1       ← ÷2
2⁻¹ = 1/2    ← ÷2
2⁻² = 1/4    ← ÷2
```

Or: `a²/a⁵ = a⁻³`, but `a²/a⁵ = 1/a³`. So `a⁻³ = 1/a³`.

```
2⁻³ = 1/8              10⁻⁴ = 0.0001
(1/3)⁻² = 3² = 9       ← flip the fraction, make the exponent positive
(2/5)⁻¹ = 5/2
(−2)⁻³ = −1/8
```

**General rule:** `(a/b)⁻ⁿ = (b/a)ⁿ` — flip and change the sign.

### ⚠️ `a⁻¹ ≠ −a`

`2⁻¹ = 1/2`, not `−2`. A negative exponent means **reciprocal**, not negative.

> 🔗 **AI:** `x⁻¹ = 1/x`, `x⁻¹ᐟ² = 1/√x`. RMSNorm: `x · (mean(x²))⁻¹ᐟ²`. Adam:
> `m · (√v + ε)⁻¹`. Learning rate: `η₀ · t⁻⁰·⁵`. All negative exponents.

---

## 4. Roots

### 4.1 Definition

```
ⁿ√a = b   ⟺   bⁿ = a          "the n-th root of a"

√9 = 3     since 3² = 9        (√ means ²√; the index 2 is omitted)
³√8 = 2    since 2³ = 8
⁴√81 = 3   since 3⁴ = 81
```

### 4.2 Even vs odd roots — a crucial difference

| | Even `n` (√, ⁴√) | Odd `n` (³√, ⁵√) |
|---|---|---|
| Negative radicand | ❌ **undefined** (over ℝ) | ✅ allowed |
| Result | always **≥ 0** | takes the sign of the radicand |
| Example | `√16 = 4` (NOT −4) | `³√(−8) = −2` |
| Reason | `x² = 16` has 2 roots; √ **picks the positive** | `x³ = −8` has 1 real root |

**√16 = 4, NOT ±4.** The equation `x² = 16` has solutions `±4`, but `√16` is **one number**: 4.
This is a convention (the principal root), and it makes √ a **function** (previous topic:
one input → one output).

### 4.3 `√(a²) = |a|` — once more

```
√((−5)²) = √25 = 5 = |−5|       ← NOT −5
√(x²) = |x|                      ← NOT x

But for odd roots:
³√((−5)³) = ³√(−125) = −5        ← odd roots keep the sign
```

> 🔗 **AI:** `‖v‖ = √(v₁² + ... + vₙ²)` is always `≥ 0`. There is no negative length. That's 4.2.

---

## 5. Root properties

For `a, b ≥ 0` (with even roots):

| Property | Formula | Example |
|----------|---------|---------|
| Product | `ⁿ√(ab) = ⁿ√a · ⁿ√b` | `√(4·9) = 6` |
| Quotient | `ⁿ√(a/b) = ⁿ√a / ⁿ√b` | `√(16/9) = 4/3` |
| Power | `ⁿ√(aᵐ) = (ⁿ√a)ᵐ` | `√(4³) = 8` |
| Root of a root | `ᵐ√(ⁿ√a) = ᵐⁿ√a` | `√(³√64) = ⁶√64 = 2` |
| Undoing | `(ⁿ√a)ⁿ = a` | `(√7)² = 7` |

### ⚠️ THE BIGGEST MISTAKE: `√(a + b) ≠ √a + √b`

```
√(9 + 16) = √25 = 5
√9 + √16 = 3 + 4 = 7        ≠ 5

√(a + b) = √a + √b  only when  a = 0  or  b = 0
(proof: square both sides → a + b = a + 2√(ab) + b → √(ab) = 0)
```

Roots distribute over **products**, NOT over **sums**.

> 🔗 **AI:** `‖u + v‖ ≠ ‖u‖ + ‖v‖`. In fact `‖u + v‖ ≤ ‖u‖ + ‖v‖` (triangle inequality,
> topic 1), with equality only when they point the same way.

---

## 6. Rational exponents — the unifying idea

> ⭐⭐⭐ This section makes powers and roots **one thing**. AI formulas use only this
> notation: `x^0.5`, `d^(−0.5)`, `N^(−0.076)`.

### 6.1 Why `a^(1/2) = √a`

We **want** the power rules to keep working for `1/2`. Then:

```
(a^(1/2))² = a^(1/2 · 2) = a¹ = a         (rule 2.3)
```

So `a^(1/2)` is a number whose square is `a`. That is `√a` (taking the positive one). ∎

Likewise `(a^(1/n))ⁿ = a` → `a^(1/n) = ⁿ√a`.

### 6.2 General definition

```
a^(m/n) = ⁿ√(aᵐ) = (ⁿ√a)ᵐ          a > 0

8^(2/3) = (³√8)² = 2² = 4          ← root first (smaller numbers), then power
4^(3/2) = (√4)³ = 2³ = 8
27^(−1/3) = 1/(³√27) = 1/3
16^(−3/4) = 1/(⁴√16)³ = 1/8
```

**Working order:** negative sign → flip; denominator → root; numerator → power.

### 6.3 All the rules survive

```
x^(1/2) · x^(1/3) = x^(5/6)
(x^(2/3))^(3/2) = x¹ = x
x^(3/4) / x^(1/4) = x^(1/2) = √x
√x · ³√x = x^(1/2 + 1/3) = x^(5/6) = ⁶√(x⁵)
```

### 6.4 Notation dictionary

| Root notation | Power notation | Code (Python/NumPy) |
|---------------|----------------|---------------------|
| `√x` | `x^(1/2)` = `x^0.5` | `x**0.5`, `np.sqrt(x)` |
| `1/√x` | `x^(−1/2)` | `x**-0.5` |
| `³√x` | `x^(1/3)` | `x**(1/3)`, `np.cbrt(x)` |
| `ⁿ√(xᵐ)` | `x^(m/n)` | `x**(m/n)` |
| `1/x` | `x^(−1)` | `x**-1` |

> ⚠️ The condition `a > 0` matters: `(−8)^(1/3)` is `−2` in math, but in NumPy
> `(-8)**(1/3)` gives `nan` (or a complex number). Use `np.cbrt(-8) = -2`. A real bug source.

---

## 7. Simplifying and rationalizing

### 7.1 Pulling factors out of a root

```
√50 = √(25 · 2) = 5√2         ← extract the largest perfect square
√72 = √(36 · 2) = 6√2
√200 = 10√2
³√54 = ³√(27 · 2) = 3·³√2     ← perfect cube for a cube root
√12 + √27 = 2√3 + 3√3 = 5√3   ← like radicals add (like terms!)
```

### 7.2 Multiplying roots

```
√2 · √8 = √16 = 4
√3 · √12 = 6
³√4 · ³√16 = ³√64 = 4
(√5 + √3)² = 5 + 2√15 + 3 = 8 + 2√15       ← (a+b)², with √a·√b = √(ab)
(√7 − √2)(√7 + √2) = 7 − 2 = 5             ← (a−b)(a+b) = a² − b²
```

### 7.3 Rationalizing the denominator

**Why:** `1/√2` is awkward to compute; `√2/2` is easy. And it's the convention.

**One root** — multiply by that root:
```
1/√2 = √2/(√2·√2) = √2/2
3/√12 = 3/(2√3) = 3√3/6 = √3/2
```

**Two terms** — multiply by the **conjugate** (`a − b` ↔ `a + b`):
```
    1          1 · (√3 + 1)        √3 + 1
────────  =  ───────────────  =  ──────────
 √3 − 1      (√3 − 1)(√3 + 1)        2

    2          2(√5 − √3)
─────────  =  ────────────  =  √5 − √3
 √5 + √3        5 − 3
```

> 🔗 **AI:** writing `1/√d` as `d^(−0.5)` is also "changing the form." In code
> `x / np.sqrt(d)` and `x * d**-0.5` are equal; the second is faster (division is expensive).

---

## 8. Graphs of power functions

The family `f(x) = xᵃ` (connecting to the previous topic):

```
   a = 2 (x²)      a = 3 (x³)      a = 1/2 (√x)    a = −1 (1/x)     a = −2 (1/x²)
     ╲  ╱             ╱               ╭──            ╲│                ╲│╱
      ╲╱           ──┼──             ╱             ───┼───           ───┼───
                    ╱               ╱                 │╲               │
   even, ∪        odd, S          only x≥0         odd, hyperbola   even, ∪ (no 0)
```

| `a` | D | E | Property |
|-----|---|---|----------|
| even natural | ℝ | [0,∞) | even, ∪ |
| odd natural | ℝ | ℝ | odd, increasing |
| `1/n` (even n) | [0,∞) | [0,∞) | increasing, slowing |
| negative | ℝ\{0} | | vertical asymptote at 0 |

**For `x > 1`:** bigger exponent → faster growth. `x⁰·⁵ < x < x² < x³`.
**For `0 < x < 1`:** REVERSED. `x³ < x² < x < x⁰·⁵`. (`0.5³ = 0.125 < 0.25 < 0.5 < √0.5 ≈ 0.707`)

> 🔗 **AI:** the scaling law `L(N) ∝ N^(−0.076)` is `xᵃ` with a small negative `a`. The
> graph decreases slowly and never reaches 0. On a log-log plot it's a **straight line**
> (next topic — logarithms).

---

## 9. Scientific notation

`m × 10ⁿ` with `1 ≤ m < 10`.

```
3 400 000 = 3.4 × 10⁶
0.00052 = 5.2 × 10⁻⁴
6.02 × 10²³   (Avogadro)
1.6 × 10⁻¹⁹   (electron charge, C)
```

**Operations** — via the power rules:

```
(3 × 10⁸)(2 × 10⁻⁵) = 6 × 10³
(8 × 10¹²)/(4 × 10⁷) = 2 × 10⁵
(2 × 10³)² = 4 × 10⁶
√(4 × 10⁶) = 2 × 10³          ← root of 10⁶ is 10³ (exponent ÷ 2)
```

**In code:** `3.4e6`, `5.2e-4`, `1e-5` (learning rate!), `1e9` (parameters).

> 🔗 **Orders of magnitude in AI:**
> ```
> learning rate      1e-3 ... 1e-5
> weight decay       1e-2 ... 1e-4
> epsilon (Adam)     1e-8
> parameters         1e8 (BERT) ... 1e11 (GPT-3) ... 1e12
> training tokens    1e12 ... 1e13
> FLOPs              1e23 ... 1e25
> ```
> Reading these as `× 10ⁿ` fluently is the language of the field.

---

## 10. Growth: 2ⁿ, n², and computer numbers

### 10.1 Polynomial vs exponential

| n | n² | 2ⁿ |
|---|-----|-----|
| 1 | 1 | 2 |
| 2 | 4 | 4 |
| 3 | 9 | 8 |
| 4 | 16 | 16 |
| 5 | 25 | 32 |
| 10 | 100 | 1 024 |
| 20 | 400 | 1 048 576 |
| 30 | 900 | ~10⁹ |
| 64 | 4 096 | ~1.8 × 10¹⁹ |

From `n ≥ 5` on, `2ⁿ` is **always** ahead and the gap explodes. This is the
"polynomial vs exponential" divide — a central idea of computer science. Full treatment
in the **Exponentials** topic.

**Paper folding:** fold 0.1 mm paper 42 times: `0.1 mm × 2⁴² ≈ 4.4 × 10¹¹ mm = 440 000 km`
— **farther than the Moon** (384 000 km).

### 10.2 Computer numbers — floats

Computers store numbers as `± m × 2ᵉ` (binary scientific notation!):

| Format | Bits (sign/exp/mantissa) | Max | Precision (ε) |
|--------|--------------------------|-----|---------------|
| float32 | 1 / 8 / 23 | ≈ 3.4 × 10³⁸ (≈2¹²⁸) | 2⁻²³ ≈ 1.2 × 10⁻⁷ |
| float16 | 1 / 5 / 10 | 65 504 | 2⁻¹⁰ ≈ 9.8 × 10⁻⁴ |
| bfloat16 | 1 / 8 / 7 | ≈ 3.4 × 10³⁸ | 2⁻⁷ ≈ 7.8 × 10⁻³ |

**Consequences:**
- `float32` stores integers **exactly** only up to `2²⁴ = 16 777 216`. `16 777 217` cannot
  be stored — it rounds to `16 777 216`.
- `0.1 + 0.2 ≠ 0.3` — because `0.1` is an infinite fraction in binary (like `1/3` in decimal).
- In `float16`, `70 000` **overflows** to `inf`. That's why mixed-precision training needs
  loss scaling.
- `bfloat16` trades precision for range — the standard in LLM training.

> 🔗 This table is the doorway to **Numerical Mathematics**. For now just notice: every
> limit is a `2ⁿ`.

---

## 11. Power equations and inequalities

### 11.1 `xⁿ = a`

```
x³ = 27    →  x = 3                  (odd: one root)
x³ = −64   →  x = −4
x⁴ = 16    →  x = ±2                 (even: TWO, don't forget ±!)
x² = 5     →  x = ±√5
x⁴ = −16   →  ∅                      (an even power is never negative)
```

### 11.2 `aˣ = b` — matching bases (a preview of logarithms)

```
2ˣ = 32   →  2ˣ = 2⁵      →  x = 5
3ˣ = 1/9  →  3ˣ = 3⁻²     →  x = −2
5ˣ = 1    →  5ˣ = 5⁰      →  x = 0
(1/2)ˣ = 8  →  2⁻ˣ = 2³   →  x = −3
4ˣ = 8    →  2²ˣ = 2³     →  x = 3/2
```

**Rule:** `aˣ = aʸ ⟺ x = y` (a > 0, a ≠ 1) — because `aˣ` is one-to-one.
What about `2ˣ = 10`? Bases can't be matched → you need a **logarithm** (next topic).

### 11.3 Rational exponents

```
x^(3/2) = 8    →  x = 8^(2/3) = 4          (raise both sides to 2/3)
x^(−2) = 1/25  →  x² = 25  →  x = ±5
x^(1/3) = −2   →  x = (−2)³ = −8
```

### 11.4 Inequalities — via monotonicity

```
x² < 9     →  −3 < x < 3            (parabola, topic 1)
x² ≥ 16    →  x ≤ −4 or x ≥ 4
x³ > 8     →  x > 2                 (x³ increasing → sign kept, one interval)
√x < 3     →  0 ≤ x < 9             (don't forget the domain x ≥ 0!)
2ˣ > 16    →  x > 4                 (2ˣ increasing)
(1/2)ˣ > 1/8  →  x < 3              (base < 1 → DECREASING → sign FLIPS)
```

### 11.5 Comparing without a calculator

**Method 1 — square** (both positive):
```
√2 + √3  vs  √10
(√2 + √3)² = 5 + 2√6     vs   10
2√6  vs  5    →   24  vs  25    →   24 < 25
So  √2 + √3 < √10
```

**Method 2 — common exponent:**
```
2³⁰⁰  vs  3²⁰⁰
2³⁰⁰ = (2³)¹⁰⁰ = 8¹⁰⁰,    3²⁰⁰ = (3²)¹⁰⁰ = 9¹⁰⁰
8 < 9  →  2³⁰⁰ < 3²⁰⁰
```

---

## 12. What matters for AI

### 12.1 The L2 norm — a root

```
‖v‖₂ = √(v₁² + v₂² + ... + vₙ²)

‖(3, 4)‖ = 5,   ‖(1, 2, 2)‖ = 3
‖(1, 1, ..., 1)‖ (n ones) = √n              ← this is where 1/√d comes from
```

Unit vector: `v/‖v‖` has length 1. `(3,4)/5 = (0.6, 0.8)`.

### 12.2 Attention scaling: `1/√d_k`

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) V
```

**Why `√d`?** `q·k = Σqᵢkᵢ` is a sum of `d` terms. If each is ~1, the "size" (standard
deviation) of the sum grows like `√d` (proved in probability). Dividing by `√d` brings it
back to ~1. `d = 64` → `÷8`.

### 12.3 Weight initialization

```
He init:      std = √(2/n_in)       for ReLU
Xavier init:  std = √(1/n_in)  or  √(2/(n_in + n_out))

n_in = 512:  √(2/512) = √(1/256) = 1/16 = 0.0625
n_in = 128:  √(2/128) = 1/8
```

**Reason:** a sum of `n` terms grows ~`√n` times (as in 12.2). To keep the signal from
growing `√n` per layer, we shrink the weights by `1/√n`.

### 12.4 RMS and RMSNorm

```
RMS(x) = √( (x₁² + ... + xₙ²)/n )        "root mean square" — root and square in the name
RMSNorm(x) = x / RMS(x) · γ

x = (1, −2, 2, 4):  squares 1, 4, 4, 16 → sum 25 → /4 = 6.25 → √ = 2.5
x/RMS = (0.4, −0.8, 0.8, 1.6),  whose RMS is 1 ✓
```

LLaMA, Mistral, Gemma use RMSNorm.

### 12.5 Learning-rate schedules

```
η(t) = η₀ / √t = η₀ · t^(−1/2)

Transformer (Vaswani 2017):  η = d^(−0.5) · min(t^(−0.5), t · w^(−1.5))
d = 512, w = 4000, t = 4000:  (512 · 4000)^(−0.5) = 1/√2 048 000 ≈ 1/1431 ≈ 7 × 10⁻⁴
```

### 12.6 Scaling laws — power laws

```
L(N) = (N_c / N)^α         α ≈ 0.076   (Kaplan et al. 2020)
```

10× more parameters → loss multiplied by `10^(−0.076) ≈ 0.84` — a 16% drop.
This is `xᵃ` (§8) with a small negative `a`.

### 12.7 Compute scale

```
GPT-3: 175 × 10⁹ params × 4 bytes (float32) = 7 × 10¹¹ bytes = 700 GB
       in float16: 350 GB
Training FLOPs ≈ 6 · N · D = 6 · (1.75 × 10¹¹)(3 × 10¹¹) ≈ 3.15 × 10²³
```

### 12.8 Table

| This topic | Name in AI |
|------------|------------|
| `√(Σx²)` | L2 norm, Euclidean distance, RMSE |
| `√n` — norm of n ones | `1/√d_k` scaling, `1/√n` init |
| `x^(−1/2)` | RMSNorm, Adam denominator, lr decay |
| `x²` | MSE loss, variance, L2 regularization |
| `xᵃ`, small negative a | Scaling laws `N^(−α)` |
| `2ⁿ` | float range, bits, computational blow-up |
| `2⁻²³` | float32 machine epsilon |
| `m × 10ⁿ` | `1e-5`, `1e9` — hyperparameter language |
| `(a+b)² ≠ a²+b²` | `‖u+v‖² = ‖u‖² + 2u·v + ‖v‖²` — the law of cosines |

---

## 13. Museum of mistakes

| # | Mistake | Correct |
|---|---------|---------|
| 1 | `(a + b)² = a² + b²` | 🔴 `a² + 2ab + b²` |
| 2 | `√(a + b) = √a + √b` | 🔴 Only over products: `√(ab) = √a√b` |
| 3 | `−2⁴ = 16` | 🔴 `−16`. `(−2)⁴ = 16` |
| 4 | `a⁻¹ = −a` | 🔴 `1/a` |
| 5 | `2³ · 2⁴ = 4⁷` | 🔴 `2⁷`. Bases are not multiplied |
| 6 | `2³ · 2⁴ = 2¹²` | 🔴 `2⁷`. Exponents are **added**, not multiplied |
| 7 | `(a³)² = a⁹` | 🔴 `a⁶`. Multiply, don't exponentiate |
| 8 | `aᵐ + aⁿ = aᵐ⁺ⁿ` | 🔴 There is **no** rule for sums |
| 9 | `√16 = ±4` | 🔴 `√16 = 4`. `x² = 16` has solutions `±4` |
| 10 | `√(x²) = x` | 🔴 `\|x\|` |
| 11 | `x⁴ = 16 → x = 2` | 🔴 `x = ±2` |
| 12 | `(−8)^(1/3)` in NumPy is `−2` | 🔴 `nan`. Use `np.cbrt(−8)` |
| 13 | Confidently `0⁰ = 0` or `= 1` | 🔴 Undefined; context-dependent |
| 14 | `(1/2)ˣ > 1/8 → x > 3` | 🔴 `x < 3`. Base < 1 → decreasing → sign flips |
| 15 | Leaving `1/√2` as is | 🟡 `√2/2` — convention (not wrong, but habit) |
| 16 | `√x < 3 → x < 9` | 🔴 `0 ≤ x < 9`. Domain! |
| 17 | `x^(1/2) · x^(1/3) = x^(1/6)` | 🔴 `x^(5/6)`. Fractions are **added**: 1/2 + 1/3 |
| 18 | `0.1 + 0.2 == 0.3` in float32 | 🔴 `False`. 0.1 is infinite in binary |

---

## 📌 One-page summary

```
POWERS:     aᵐaⁿ = aᵐ⁺ⁿ | aᵐ/aⁿ = aᵐ⁻ⁿ | (aᵐ)ⁿ = aᵐⁿ | (ab)ⁿ = aⁿbⁿ | (a/b)ⁿ = aⁿ/bⁿ
            a⁰ = 1 | a⁻ⁿ = 1/aⁿ | (a/b)⁻ⁿ = (b/a)ⁿ
            (−2)⁴ = 16 ≠ −2⁴ = −16
NOT RULES:  aᵐ + aⁿ ≠ aᵐ⁺ⁿ | (a+b)ⁿ ≠ aⁿ + bⁿ | 2³·2⁴ ≠ 4⁷

ROOTS:      √a ≥ 0 (principal) | √(a²) = |a| | ³√(−8) = −2 (odd allowed)
            √(ab) = √a√b | √(a/b) = √a/√b | √(a+b) ≠ √a + √b
            a^(m/n) = ⁿ√(aᵐ) — powers and roots are ONE THING

SIMPLIFY:   √50 = 5√2 | 1/√2 = √2/2 | 1/(√3−1) = (√3+1)/2 (conjugate)

EQUATIONS:  xⁿ = a: odd → 1 root, even → ±, negative a → ∅
            aˣ = aʸ ⟺ x = y   (match bases; otherwise — log)
            base < 1 → decreasing → inequality sign FLIPS

SCI. NOT.:  m × 10ⁿ, 1 ≤ m < 10.  Code: 1e-5, 1e9

AI:         ‖v‖ = √(Σv²) | 1/√d_k | std = √(2/n) | RMS | η/√t | N^(−α) | 2⁻²³
```

---

**Next:** [02-problems-en.md](02-problems-en.md)
