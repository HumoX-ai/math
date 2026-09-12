# Yechimlar — Funksiyalar

> ⛔ **Masalani o'zing yechmagan bo'lsang — yop.** Yechimni o'qish "tushundim" hissini
> beradi, bilim bermaydi. Xato bo'lsa → `00-mindset/xatolar-daftari.md`.

---

## A. Funksiya tushunchasi, domain, range

### A1 — `f(x) = 2x² − 3x + 1`

```
f(0)  = 0 − 0 + 1 = 1
f(1)  = 2 − 3 + 1 = 0
f(−2) = 2·4 − 3·(−2) + 1 = 8 + 6 + 1 = 15

f(a+1) = 2(a+1)² − 3(a+1) + 1
       = 2(a² + 2a + 1) − 3a − 3 + 1
       = 2a² + 4a + 2 − 3a − 2
       = 2a² + a
```

**Tekshirish:** `a = 0` → `f(1) = 0`; formula: `0 + 0 = 0` ✓. `a = 1` → `f(2) = 8 − 6 + 1 = 3`; formula: `2 + 1 = 3` ✓.

---

### A2 — `f(x) = √(x − 3) / (x − 5)`

```
Ildiz:   x − 3 ≥ 0  →  x ≥ 3
Maxraj:  x − 5 ≠ 0  →  x ≠ 5
Kesishma:  x ≥ 3  va  x ≠ 5
```

**Javob:** `D = [3, 5) ∪ (5, +∞)`

---

### A3 — `g(x) = 1/(x² − 4) + √(6 − x)`

```
Maxraj:  x² − 4 ≠ 0  →  x ≠ ±2
Ildiz:   6 − x ≥ 0   →  x ≤ 6
```

**Javob:** `D = (−∞, −2) ∪ (−2, 2) ∪ (2, 6]`

---

### A4 — Qaysilari funksiya?

| | Funksiya? | Sabab |
|---|---|---|
| (a) `y = x²` | ✅ | har `x` ga bitta `y` |
| (b) `x = y²` | ❌ | `x = 4` → `y = 2` **va** `y = −2` |
| (c) `y = \|x\|` | ✅ | bitta chiqish |
| (d) `x² + y² = 1` | ❌ | `x = 0` → `y = ±1` (aylana vertikal chiziq testidan o'tmaydi) |
| (e) `y = 3` | ✅ | o'zgarmas funksiya — har `x` ga `3` |

---

### A5 — Range

```
(a) x² ≥ 0  →  x² + 2 ≥ 2,  x = 0 da yetadi          E = [2, +∞)
(b) |x| ≥ 0 → −|x| ≤ 0 → −|x| + 3 ≤ 3,  x = 0 da     E = (−∞, 3]
(c) √x ≥ 0  →  √x − 1 ≥ −1,  x = 0 da                E = [−1, +∞)
(d) 1 + x² ≥ 1  →  0 < 1/(1+x²) ≤ 1
    1 ga x = 0 da yetadi; 0 ga hech qachon yetmaydi   E = (0, 1]
```

---

### A6 — Jadvaldan formula

```
y = kx + b
x = 0 → y = 3      →  b = 3
x = 1 → y = 5      →  k + 3 = 5  →  k = 2
Formula:  y = 2x + 3
Tekshir: x=2: 7 ✓  x=3: 9 ✓  x=4: 11 ✓
```

> Bu — 5 ta ma'lumotli "training". Model 2 parametrli (`k`, `b`), 2 ta nuqta yetdi,
> qolgan 3 tasi **validation** vazifasini bajardi.

---

## B. Chiziqli funksiya

### B1 — `(1, 3)` va `(3, 7)`

```
k = (7 − 3)/(3 − 1) = 2
3 = 2·1 + b  →  b = 1
```

**Javob:** `y = 2x + 1`

---

### B2 — `y = −3x + 6`

```
k = −3 (kamayuvchi, tik),  b = 6
y-kesma: (0, 6)
x-kesma: −3x + 6 = 0  →  x = 2  →  (2, 0)
```

Grafik: `(0, 6)` va `(2, 0)` nuqtalarni tutashtir.

---

### B3

```
(a) Parallel: k = 2.  (0, 4) dan:  b = 4.      y = 2x + 4
(b) Perpendikulyar: k = −1/2.  (2, 1) dan:
    1 = (−1/2)·2 + b  →  1 = −1 + b  →  b = 2.  y = −x/2 + 2
```

---

### B4 — `f(2) = 5`, `f(−1) = −4`

```
k = (5 − (−4))/(2 − (−1)) = 9/3 = 3
5 = 3·2 + b  →  b = −1
f(x) = 3x − 1
Tekshir: f(−1) = −3 − 1 = −4 ✓
```

---

### B5 — `F = (9/5)C + 32`

```
(a) C = 25:   F = 45 + 32 = 77°F
(b) F = 212:  212 = 1.8C + 32  →  1.8C = 180  →  C = 100°C  (suv qaynashi)
(c) F = C:    C = 1.8C + 32  →  −0.8C = 32  →  C = −40
    −40°C = −40°F  ← mashhur fakt
```

---

### B6 — Taksi

```
(a) C(d) = 2000d + 5000
(b) C(7) = 14 000 + 5000 = 19 000 so'm
(c) 2000d + 5000 ≤ 25 000  →  2000d ≤ 20 000  →  d ≤ 10 km
(d) k = 2000: har 1 km uchun QO'SHIMCHA narx (o'zgarish tezligi)
    b = 5000: yo'l bosmasang ham to'lanadigan narx (d = 0 dagi qiymat)
```

---

### B7

```
(a) 2x + 1 = −x + 7  →  3x = 6  →  x = 2,  y = 5.       Nuqta: (2, 5)
(b) 2x + 1 = 2x − 3  →  1 = −3  yolg'on  →  kesishmaydi.
    Sabab: k₁ = k₂ = 2 (parallel), b₁ ≠ b₂ (har xil chiziq).
```

> Bu — oldingi mavzudagi D3 (sistema yechimsiz) ning grafik ko'rinishi.

---

## C. Kvadrat funksiya

### C1 — `f(x) = x² − 6x + 5`

```
Nollar:   x² − 6x + 5 = (x − 1)(x − 5) = 0  →  x = 1, 5
Cho'qqi:  x₀ = −(−6)/(2·1) = 3,   f(3) = 9 − 18 + 5 = −4   →  (3, −4)
          (yoki: nollar o'rtasi (1+5)/2 = 3 ✓)
Simmetriya o'qi:  x = 3
y-kesma:  f(0) = 5
a = 1 > 0  →  ∪, minimum −4
Range:    [−4, +∞)
```

---

### C2 — `f(x) = −2x² + 8x − 3`

```
x₀ = −8/(2·(−2)) = 2
f(2) = −8 + 16 − 3 = 5
a = −2 < 0  →  ∩  →  MAKSIMUM = 5,  cho'qqi (2, 5)
Range: (−∞, 5]
```

---

### C3 — `x² + 4x + 7` vertex form

```
x² + 4x + 7 = (x² + 4x + 4) + 3 = (x + 2)² + 3
Cho'qqi: (−2, 3).  Minimum 3 > 0  →  grafik x o'qidan yuqorida  →  NOLLARI YO'Q
Tekshir: D = 16 − 28 = −12 < 0 ✓
```

---

### C4 — cho'qqi `(1, −2)`, `(0, 1)` dan o'tadi

```
y = a(x − 1)² − 2
(0, 1):  1 = a(−1)² − 2  →  a = 3
y = 3(x − 1)² − 2 = 3(x² − 2x + 1) − 2 = 3x² − 6x + 1
Tekshir: x₀ = 6/6 = 1 ✓,  f(1) = 3 − 6 + 1 = −2 ✓,  f(0) = 1 ✓
```

---

### C5 — perimetr 40

```
Tomonlar x va 20 − x.  S(x) = x(20 − x) = −x² + 20x
x₀ = −20/(−2) = 10  →  S = 100 m².  Tomonlar 10 × 10 (kvadrat).
```

---

### C6 — `h(t) = −5t² + 20t`

```
(a) t₀ = −20/(2·(−5)) = 2 s,   h(2) = −20 + 40 = 20 m
(b) −5t² + 20t = 0  →  −5t(t − 4) = 0  →  t = 0 (otilgan) yoki t = 4 s (tushdi)
(c) −5t² + 20t ≥ 15
    −5t² + 20t − 15 ≥ 0        | ÷(−5) → 🔴 belgi almashadi
    t² − 4t + 3 ≤ 0
    (t − 1)(t − 3) ≤ 0
    1 ≤ t ≤ 3                  →  t ∈ [1, 3] sekund
Tekshir: h(1) = 15 ✓, h(2) = 20 ≥ 15 ✓, h(3) = −45 + 60 = 15 ✓, h(0.5) = −1.25 + 10 = 8.75 < 15 ✓
```

---

## D. Funksiya xossalari

### D1 — Juft/toq

```
(a) f(−x) = x⁴ − 3x² = f(x)                      JUFT
(b) g(−x) = −x³ − x = −(x³ + x) = −g(x)           TOQ
(c) h(−x) = x² − x  ≠ h(x),  ≠ −h(x)              HECH QAYSI
(d) |−x| = |x|                                    JUFT
(e) 1/(−x) = −1/x                                 TOQ
(f) (−x)² + 1 = x² + 1                            JUFT
```

---

### D2 — `f(x) = x³ − 4x`

```
Nollar: x(x² − 4) = x(x − 2)(x + 2) = 0  →  x = −2, 0, 2

Ishoralar (sinov nuqtalar):
  x = −3: −27 + 12 = −15  →  −
  x = −1: −1 + 4 = 3      →  +
  x = 1:  1 − 4 = −3      →  −
  x = 3:  27 − 12 = 15    →  +

     −2       0       2
──────●───────●───────●──────
  −       +       −       +

f(x) > 0  ⟺  x ∈ (−2, 0) ∪ (2, +∞)

Juft/toq: f(−x) = −x³ + 4x = −(x³ − 4x) = −f(x)  →  TOQ (grafik markaziy simmetrik)
```

---

### D3 — Monotonlik

```
(a) (x − 2)² + 1 — parabola, cho'qqi x = 2:
    kamayuvchi (−∞, 2],  o'suvchi [2, +∞)
(b) −3x + 1 — k < 0:  kamayuvchi butun ℝ da
(c) 1/x:  kamayuvchi (−∞, 0) da  VA  kamayuvchi (0, +∞) da.
    🔴 Lekin "butun domain'da kamayuvchi" DEB BO'LMAYDI:
    −1 < 1, lekin f(−1) = −1 < f(1) = 1 — kamaymagan, oshgan.
```

---

### D4 — Isbot: `f(x) = 2x + 3` o'suvchi

```
Ixtiyoriy x₁ < x₂ olamiz.
x₁ < x₂
2x₁ < 2x₂            (2 > 0 ga ko'paytirdik, belgi saqlanadi)
2x₁ + 3 < 2x₂ + 3    (3 qo'shdik)
f(x₁) < f(x₂)        ∎
```

---

### D5 — `f(x) = 1/(1 + x²)`

```
Range isboti:
  x² ≥ 0  →  1 + x² ≥ 1  →  0 < 1/(1 + x²) ≤ 1
  Yuqori chegara 1: x = 0 da yetadi (f(0) = 1)   →  MAKSIMUM = 1, x = 0 da
  Pastki chegara 0: 1/(1+x²) = 0 yechimsiz → yetmaydi
  E = (0, 1]

Chegaralangan: ha (0 < f ≤ 1)
Juft: f(−x) = 1/(1 + (−x)²) = f(x)  ✓
```

> 🔗 Bu funksiya sigmoid'ga o'xshash "qo'ng'iroq" shakl. Gauss taqsimoti `e^(−x²)` ham shu oilaviy shakl.

---

### D6 — `f(x) = x² − 2|x|`

```
Juft: f(−x) = x² − 2|−x| = x² − 2|x| = f(x)  ✓  →  faqat x ≥ 0 ni chizib, ko'zgu qilamiz.

x ≥ 0 da:  f(x) = x² − 2x = (x − 1)² − 1
  cho'qqi (1, −1),  nollar x = 0, x = 2
Ko'zgu:  cho'qqi (−1, −1),  nol x = −2

Nollar: {−2, 0, 2}
Minimum: −1,  x = ±1 da
Range: [−1, +∞)

Grafik: W-shakl (ikki parabola bo'lagi, x = 0 da burchak)
```

---

## E. Almashtirishlar va kompozitsiya

### E1 — `f(x) = x²`

```
(a) x² + 3          3 yuqoriga,            cho'qqi (0, 3)
(b) (x − 2)²        2 O'NGGA,              cho'qqi (2, 0)
(c) −x²             x o'qiga aks,          ∩, cho'qqi (0, 0)
(d) 2x²             2 marta cho'zish,      torroq, cho'qqi (0, 0)
(e) (x + 1)² − 4    1 chapga, 4 pastga,    cho'qqi (−1, −4)
```

---

### E2

```
(a) y = |x − 3| + 2:  |x| ni 3 o'ngga, 2 yuqoriga.  Cho'qqi (3, 2), V yuqoriga.
(b) y = −|x + 1|:     |x| ni 1 chapga, aks.          Cho'qqi (−1, 0), Λ pastga.
```

---

### E3 — `f(x) = 2x + 1`, `g(x) = x²`

```
(a) f(g(x)) = 2x² + 1
(b) g(f(x)) = (2x + 1)² = 4x² + 4x + 1
(c) f(g(2)) = 2·4 + 1 = 9
(d) g(f(2)) = 5² = 25
Teng emas. Kompozitsiya kommutativ emas.
```

---

### E4 — `f(x) = √x`, `g(x) = x − 4`

```
f(g(x)) = √(x − 4)      D: x − 4 ≥ 0  →  [4, +∞)
g(f(x)) = √x − 4        D: x ≥ 0       →  [0, +∞)
```

---

### E5 — Ajratish

```
(a) (3x − 1)⁵:     g(x) = 3x − 1,   f(u) = u⁵
(b) √(x² + 1):     g(x) = x² + 1,   f(u) = √u
(c) 1/(x + 2)²:    g(x) = x + 2,    m(u) = u²,   f(v) = 1/v     →  f(m(g(x)))
```

---

### E6 — `f = x + 1`, `g = 2x`, `h = x²`

```
(a) f(g(h(x))) = f(g(x²)) = f(2x²) = 2x² + 1
(b) h(g(f(x))) = h(g(x + 1)) = h(2x + 2) = (2x + 2)² = 4x² + 8x + 4
(c) g(h(f(x))) = g(h(x + 1)) = g((x + 1)²) = 2(x + 1)² = 2x² + 4x + 2
Uchtasi har xil ✓
```

---

### E7 — Mini neyron tarmoq

```
L₁(x) = 2x − 1,  σ(z) = max(0, z),  L₂(z) = −z + 3

(a)
x = 0:   L₁ = −1  →  σ = 0  →  L₂ = 3
x = 1:   L₁ = 1   →  σ = 1  →  L₂ = 2
x = 2:   L₁ = 3   →  σ = 3  →  L₂ = 0
x = −1:  L₁ = −3  →  σ = 0  →  L₂ = 3

(b) σ "o'chgan" qism: 2x − 1 ≤ 0  →  x ≤ 1/2  →  y = L₂(0) = 3
    σ "yongan" qism:  x > 1/2  →  y = −(2x − 1) + 3 = −2x + 4

        ⎧ 3,          x ≤ 1/2
y(x) =  ⎨
        ⎩ −2x + 4,    x > 1/2

(c) BO'LAKLI CHIZIQLI funksiya. x = 1/2 da "bukilish" (burchak). Uzluksiz (ikkala tomondan 3).

(d) σ siz:  L₂(L₁(x)) = −(2x − 1) + 3 = −2x + 4  — oddiy CHIZIQLI funksiya.
    Bukilish yo'q. Ya'ni aktivatsiya bo'lmasa, ikki qatlam = bitta chiziqli funksiya.
```

> 🔗 Bu — deep learning'ning asosiy faktini o'z qo'ling bilan ko'rish: **chiziqlilar
> kompozitsiyasi chiziqli; aktivatsiya "bukilish" beradi**. Ko'p neyron = ko'p bukilish
> = istalgan egri chiziqni taxminlash.

---

## F. Teskari funksiya va bo'lakli funksiyalar

### F1 — `f(x) = 3x − 6`

```
y = 3x − 6  →  x = (y + 6)/3  →  f⁻¹(x) = (x + 6)/3
Tekshir: f(f⁻¹(x)) = 3·(x + 6)/3 − 6 = x + 6 − 6 = x ✓
```

---

### F2 — `f(x) = (2x + 1)/(x − 3)`

```
y(x − 3) = 2x + 1
xy − 3y = 2x + 1
xy − 2x = 3y + 1
x(y − 2) = 3y + 1
x = (3y + 1)/(y − 2)

f⁻¹(x) = (3x + 1)/(x − 2),   D(f⁻¹) = ℝ \ {2}

Tekshir: f(4) = (8 + 1)/(4 − 3) = 9.   f⁻¹(9) = (27 + 1)/(9 − 2) = 28/7 = 4 ✓
```

> `D(f⁻¹) = ℝ\{2}` = `E(f)` — `f` hech qachon 2 ga teng bo'lmaydi (gorizontal asimptota).

---

### F3 — `f(x) = x²`

```
Teskari YO'Q: f(2) = f(−2) = 4 — bir qiymatli emas (gorizontal chiziq testi buziladi).
Cheklov: x ≥ 0 da f bir qiymatli  →  f⁻¹(x) = √x  (D = [0, ∞))
(Yoki x ≤ 0 da:  f⁻¹(x) = −√x)
```

---

### F4 — Bo'lakli funksiya

```
(a) f(−3) = −3 + 2 = −1       (x < 0)
    f(0) = 0² = 0             (0 ≤ 0 ≤ 2)
    f(1.5) = 2.25
    f(2) = 4                  (0 ≤ 2 ≤ 2)
    f(5) = 4                  (x > 2)

(c) x = 0:  chapdan → 0 + 2 = 2;  o'ngdan → 0² = 0.   2 ≠ 0  →  UZILISH (sakrash)
    x = 2:  chapdan → 4;          o'ngdan → 4.        →  UZLUKSIZ
```

---

### F5 — Clip

```
(a)                  ⎧ −1,   z < −1
    clip(z, −1, 1) = ⎨ z,    −1 ≤ z ≤ 1
                     ⎩ 1,    z > 1

(b) = 1  ⟺  2x − 3 ≥ 1  ⟺  x ≥ 2         (yuqori "tekis" qism)
(c) = 0  ⟺  2x − 3 = 0  ⟺  x = 3/2       (0 ∈ [−1,1], o'rta qism)
(d) = 2:  range [−1, 1], 2 ∉ range  →  YECHIM YO'Q
```

---

## G. 🔗 AI

### G1 — Uy narxi

```
(a) w = (130 − 70)/(80 − 40) = 60/40 = 1.5
    70 = 1.5·40 + b  →  b = 10
    narx = 1.5·maydon + 10
(b) narx(60) = 90 + 10 = 100 ming $
(c) w = 1.5: har qo'shimcha 1 m² narxni 1.5 ming $ oshiradi
    b = 10: maydon 0 bo'lganda ham 10 ming $ (yer, hujjat, "asos" narx)
(d) weight — kirish (maydon) natijaga qanchalik "og'irlik" bilan ta'sir qiladi;
    bias — kirishdan mustaqil siljish ("kirish nol bo'lsa ham natija shuncha")
```

---

### G2 — Sigmoid

```
(a) σ(0)  = 1/(1 + 1) = 0.500
    σ(1)  = 1/(1 + 0.368) = 1/1.368 ≈ 0.731
    σ(−1) = 1/(1 + 2.718) = 1/3.718 ≈ 0.269
    σ(2)  = 1/(1 + 0.135) = 1/1.135 ≈ 0.881
    σ(−2) = 1/(1 + 7.389) = 1/8.389 ≈ 0.119

(b) σ(1) + σ(−1) = 0.731 + 0.269 = 1.000

    Isbot:  1 − σ(x) = 1 − 1/(1 + e⁻ˣ) = (1 + e⁻ˣ − 1)/(1 + e⁻ˣ) = e⁻ˣ/(1 + e⁻ˣ)
            Surat va maxrajni eˣ ga ko'paytiramiz (e⁻ˣ · eˣ = 1):
            = 1/(eˣ + 1) = 1/(1 + e^(−(−x))) = σ(−x)   ∎

(c) e⁻ˣ > 0 har doim  →  1 + e⁻ˣ > 1  →  0 < 1/(1 + e⁻ˣ) < 1   ∎

(d) σ(x) ≥ 1/2  ⟺  1 + e⁻ˣ ≤ 2  ⟺  e⁻ˣ ≤ 1  ⟺  −x ≤ 0  ⟺  x ≥ 0
    (e^t ≤ 1 = e⁰ ⟺ t ≤ 0, chunki eˣ o'suvchi)
```

> 🔗 (d) — binary klassifikatsiyada "`z ≥ 0` → 1-sinf" qoidasining asosi.
> (b) — `P(ha) + P(yo'q) = 1` ning matematik sababi.

---

### G3 — ReLU'lardan `|x − 1|`

```
(a) y(0)  = ReLU(−1) + ReLU(1) = 0 + 1 = 1
    y(1)  = 0 + 0 = 0
    y(3)  = ReLU(2) + ReLU(−2) = 2 + 0 = 2
    y(−2) = ReLU(−3) + ReLU(3) = 0 + 3 = 3

(b) y(x) = |x − 1|.  Isbot:
    x ≥ 1:  h₁ = x − 1,  h₂ = 0       →  y = x − 1 = |x − 1| ✓
    x < 1:  h₁ = 0,      h₂ = 1 − x   →  y = 1 − x = |x − 1| ✓

(c) max(x, 2) = 2 + ReLU(x − 2)
    Tekshir: x = 5: 2 + 3 = 5 ✓;  x = 0: 2 + 0 = 2 ✓;  x = 2: 2 + 0 = 2 ✓
    (Umumiy: max(a, b) = b + ReLU(a − b))
```

> 🔗 Ikki neyron `|x−1|` ni qurdi. Yuzlab neyron — istalgan bo'lakli chiziqli funksiya.
> Millionlab — istalgan silliq funksiyaga xohlagancha yaqin. Bu **universal
> approximation** g'oyasining intuitsiyasi.

---

### G4 — Normalizatsiya

```
Ma'lumot: 10, 20, 40, 50

(a) min = 10, max = 50, max − min = 40
    x' = (x − 10)/40:   0,  0.25,  0.75,  1        Range: [0, 1]

(b) μ = (10 + 20 + 40 + 50)/4 = 30
    x − μ:  −20, −10, 10, 20
    (x − μ)²: 400, 100, 100, 400   →  Σ = 1000  →  /4 = 250
    σ = √250 = 5√10 ≈ 15.81
    z = (x − 30)/15.81:  −1.265,  −0.632,  0.632,  1.265

(c) Min-max:  x' = (1/40)x − 10/40        →  k = 0.025,   b = −0.25
    Z-score:  z = (1/σ)x − μ/σ            →  k ≈ 0.0632,  b ≈ −1.897

(d) Min-max teskari:  x = 40x' + 10
    Z-score teskari:  x = σz + μ = 15.81z + 30
```

> 🔗 Model normalizatsiya qilingan `z` ustida ishlaydi; javobni odamga ko'rsatishda (d)
> orqali qaytariladi. Bu **har bir** regressiya pipeline'ida bor.

---

### G5 — Loss parabola

```
Ma'lumot: (1,2), (2,4), (3,5).  ŷ = wx.

(a) L(w) = (w·1 − 2)² + (w·2 − 4)² + (w·3 − 5)²
         = (w − 2)² + (2w − 4)² + (3w − 5)²
         = (w² − 4w + 4) + (4w² − 16w + 16) + (9w² − 30w + 25)
         = 14w² − 50w + 45

(b) Kvadrat funksiya — PARABOLA. a = 14 > 0 → shoxlari yuqoriga → MINIMUM mavjud va yagona.
    (Bu "loss convex" degani. Gradient descent bunday holda kafolatlangan topadi.)

(c) w* = −b/(2a) = 50/28 = 25/14 ≈ 1.786
    L(w*) = 14(25/14)² − 50(25/14) + 45
          = 625/14 − 1250/14 + 630/14
          = 5/14 ≈ 0.357

    Tekshir formula bilan: w* = Σxᵢyᵢ/Σxᵢ² = (2 + 8 + 15)/(1 + 4 + 9) = 25/14 ✓

(d) L(1) = 14 − 50 + 45 = 9
    L(2) = 56 − 100 + 45 = 1
    Ikkalasi ham 5/14 ≈ 0.357 dan katta ✓ (w* — minimum)
```

> 🔗 **Sen hozir loss landscape'ni qo'lda chizding.** Bitta parametr — parabola.
> Ikki parametr — "piyola" (paraboloid). Millionlab parametr — ko'rib bo'lmaydigan
> landshaft, lekin **lokal ravishda** hali ham parabola. Gradient descent — shu
> parabolaning cho'qqisiga qadam-baqadam tushish. `code/03_ai_bogliqlik.py` da ko'r.

---

## 🎓 Yakuniy eslatma

Bo'sh qog'oz testi: faylni yop va **E7** bilan **G5** ni qaytadan yech. Bo'ldimi — bilasan.
Bo'lmadimi — ertaga. Ikkalasi ham normal.
