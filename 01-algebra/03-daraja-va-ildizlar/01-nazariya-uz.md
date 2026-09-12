# Daraja va Ildizlar — Nazariya

> **O'qish usuli:** bu mavzuda har bir qoidani **isbotla**, yodlama. `aᵐ·aⁿ = aᵐ⁺ⁿ` ni
> yodlagan odam `aᵐ + aⁿ = aᵐ⁺ⁿ` deb ham yozib qo'yadi. Ko'paytuvchilarni sanab
> isbotlagan odam — hech qachon.

**Mundarija**

1. [Natural daraja](#1-natural-daraja)
2. [Daraja xossalari — va NIMA UCHUN](#2-daraja-xossalari--va-nima-uchun)
3. [Nol va manfiy ko'rsatkich](#3-nol-va-manfiy-korsatkich)
4. [Ildizlar](#4-ildizlar)
5. [Ildiz xossalari](#5-ildiz-xossalari)
6. [Ratsional ko'rsatkich — birlashtiruvchi g'oya](#6-ratsional-korsatkich--birlashtiruvchi-goya)
7. [Soddalashtirish va ratsionallashtirish](#7-soddalashtirish-va-ratsionallashtirish)
8. [Darajali funksiyalar grafiklari](#8-darajali-funksiyalar-grafiklari)
9. [Standart ko'rinish](#9-standart-korinish)
10. [O'sish: 2ⁿ, n² va kompyuter sonlari](#10-osish-2ⁿ-n-va-kompyuter-sonlari)
11. [Daraja tenglamalari va tengsizliklari](#11-daraja-tenglamalari-va-tengsizliklari)
12. [AI uchun muhim](#12-ai-uchun-muhim)
13. [Xatolar muzeyi](#13-xatolar-muzeyi)

---

## 1. Natural daraja

```
aⁿ = a · a · a · ... · a        (n marta)
     └──────┬──────┘
   a — ASOS (base),  n — KO'RSATKICH (exponent)

2⁵ = 2·2·2·2·2 = 32
(−3)³ = (−3)(−3)(−3) = −27
(1/2)³ = 1/8
0.1² = 0.01
```

### Ishora qoidalari

```
Musbat asos:           har doim musbat
Manfiy asos, JUFT n:   musbat      (−2)⁴ = 16
Manfiy asos, TOQ n:    manfiy      (−2)³ = −8
```

### ⚠️ `(−2)⁴` va `−2⁴` — HAR XIL

```
(−2)⁴ = (−2)(−2)(−2)(−2) = +16       ← qavs: MANFIY SON darajaga ko'tarildi
−2⁴   = −(2⁴) = −16                   ← qavs yo'q: 2⁴ hisoblanib, keyin minus
```

Bu farq — Python'da ham: `(-2)**4 = 16`, `-2**4 = -16`. Kodda ham xato manbai.

---

## 2. Daraja xossalari — va NIMA UCHUN

Beshta qoida. Har birini **ko'paytuvchilarni sanab** isbotla:

### 2.1 Ko'paytirish: `aᵐ · aⁿ = aᵐ⁺ⁿ`

```
a³ · a² = (a·a·a)(a·a) = a·a·a·a·a = a⁵        3 + 2 = 5 ✓
```
**Sabab:** `m` ta va `n` ta ko'paytuvchi yonma-yon = `m + n` ta.

### 2.2 Bo'lish: `aᵐ / aⁿ = aᵐ⁻ⁿ`

```
a⁵ / a² = (a·a·a·a·a)/(a·a) = a·a·a = a³       5 − 2 = 3 ✓
```
**Sabab:** `n` ta ko'paytuvchi qisqaradi.

### 2.3 Darajaning darajasi: `(aᵐ)ⁿ = aᵐⁿ`

```
(a²)³ = a² · a² · a² = a⁶                      2 · 3 = 6 ✓
```
**Sabab:** `aᵐ` `n` marta yoziladi → `m·n` ta ko'paytuvchi.

### 2.4 Ko'paytmaning darajasi: `(ab)ⁿ = aⁿbⁿ`

```
(ab)³ = ab · ab · ab = (a·a·a)(b·b·b) = a³b³
```

### 2.5 Kasrning darajasi: `(a/b)ⁿ = aⁿ/bⁿ`

```
(a/b)² = (a/b)(a/b) = a²/b²
```

### Jadval

| Qoida | Formula | Misol |
|-------|---------|-------|
| Ko'paytirish | `aᵐ·aⁿ = aᵐ⁺ⁿ` | `2³·2⁴ = 2⁷ = 128` |
| Bo'lish | `aᵐ/aⁿ = aᵐ⁻ⁿ` | `3⁵/3³ = 3² = 9` |
| Darajaning darajasi | `(aᵐ)ⁿ = aᵐⁿ` | `(5²)³ = 5⁶` |
| Ko'paytma | `(ab)ⁿ = aⁿbⁿ` | `(2·5)³ = 8·125 = 1000` |
| Kasr | `(a/b)ⁿ = aⁿ/bⁿ` | `(2/3)² = 4/9` |

### ⚠️ Yo'q qoidalar (hamma qiladigan xatolar)

```
aᵐ + aⁿ  ≠  aᵐ⁺ⁿ          2² + 2³ = 4 + 8 = 12,  2⁵ = 32
(a + b)ⁿ  ≠  aⁿ + bⁿ      (1 + 1)² = 4,  1² + 1² = 2
aᵐ · bⁿ  ≠  (ab)ᵐ⁺ⁿ       asoslar har xil — hech narsa qilib bo'lmaydi
2³ · 2⁴  ≠  4⁷            asos ko'paytirilmaydi! = 2⁷
(aᵐ)ⁿ  ≠  a^(mⁿ)          (2³)² = 64,  2^(3²) = 2⁹ = 512
```

---

## 3. Nol va manfiy ko'rsatkich

### 3.1 Nima uchun `a⁰ = 1`

**Ta'rif emas — natija.** Pattern'ga qara:

```
2⁴ = 16
2³ = 8      ← ÷2
2² = 4      ← ÷2
2¹ = 2      ← ÷2
2⁰ = ?      ← ÷2  →  1
```

Yoki bo'lish qoidasidan: `a³/a³ = a³⁻³ = a⁰`. Lekin `a³/a³ = 1`. Demak `a⁰ = 1`.

```
5⁰ = 1,   (−7)⁰ = 1,   (2/3)⁰ = 1,   x⁰ = 1  (x ≠ 0)
0⁰ — ANIQLANMAGAN (kontekstga qarab 1 deb olinadi, lekin ehtiyot bo'l)
```

### 3.2 Nima uchun `a⁻ⁿ = 1/aⁿ`

Pattern'ni davom ettir:

```
2¹ = 2
2⁰ = 1       ← ÷2
2⁻¹ = 1/2    ← ÷2
2⁻² = 1/4    ← ÷2
2⁻³ = 1/8
```

Yoki: `a²/a⁵ = a²⁻⁵ = a⁻³`. Lekin `a²/a⁵ = 1/a³`. Demak `a⁻³ = 1/a³`.

```
2⁻³ = 1/8              10⁻⁴ = 0.0001
(1/3)⁻² = 3² = 9       ← kasrni teskari ag'darib, darajani musbat qil
(2/5)⁻¹ = 5/2
(−2)⁻³ = 1/(−8) = −1/8
```

**Umumiy qoida:** `(a/b)⁻ⁿ = (b/a)ⁿ` — ag'dar va ishorani o'zgartir.

### ⚠️ `a⁻¹ ≠ −a`

`2⁻¹ = 1/2`, `−2` emas. Manfiy ko'rsatkich = **teskari son**, manfiy son emas.

> 🔗 **AI:** `x⁻¹ = 1/x`, `x⁻¹ᐟ² = 1/√x`. RMSNorm: `x · (mean(x²))⁻¹ᐟ²`. Adam:
> `m/(√v + ε) = m · (√v + ε)⁻¹`. Learning rate: `η₀ · t⁻⁰·⁵`. Hammasi manfiy ko'rsatkich.

---

## 4. Ildizlar

### 4.1 Ta'rif

```
ⁿ√a = b   ⟺   bⁿ = a          "a ning n-darajali ildizi"

√9 = 3     chunki 3² = 9        (√ = ²√, indeks yozilmaydi)
³√8 = 2    chunki 2³ = 8
⁴√81 = 3   chunki 3⁴ = 81
```

### 4.2 Juft va toq ildiz — muhim farq

| | Juft `n` (√, ⁴√) | Toq `n` (³√, ⁵√) |
|---|---|---|
| Ildiz ostida manfiy | ❌ **aniqlanmagan** (ℝ da) | ✅ mumkin |
| Natija | doim **≥ 0** | asos ishorasi bilan |
| Misol | `√16 = 4` (−4 EMAS) | `³√(−8) = −2` |
| Sabab | `x² = 16` ning 2 ildizi bor, √ **musbatini** tanlaydi | `x³ = −8` ning 1 ta haqiqiy ildizi |

**√16 = 4, ±4 EMAS.** `x² = 16` tenglamaning ildizlari `±4`, lekin `√16` — bu **bitta son**, 4.
Bu kelishuv (arifmetik ildiz), va u √ ni **funksiya** qiladi (oldingi mavzu: bir kirish → bir chiqish).

### 4.3 `√(a²) = |a|` — yana bir marta

```
√((−5)²) = √25 = 5 = |−5|       ← −5 EMAS
√(x²) = |x|                      ← x EMAS

Lekin toq ildizda:
³√((−5)³) = ³√(−125) = −5        ← toq ildiz ishorani saqlaydi
```

> 🔗 **AI:** `‖v‖ = √(v₁² + ... + vₙ²)` — har doim `≥ 0`. Manfiy uzunlik yo'q. Bu 4.2 dan.

---

## 5. Ildiz xossalari

`a, b ≥ 0` uchun (juft ildizlarda):

| Xossa | Formula | Misol |
|-------|---------|-------|
| Ko'paytma | `ⁿ√(ab) = ⁿ√a · ⁿ√b` | `√(4·9) = 2·3 = 6` |
| Kasr | `ⁿ√(a/b) = ⁿ√a / ⁿ√b` | `√(16/9) = 4/3` |
| Daraja | `ⁿ√(aᵐ) = (ⁿ√a)ᵐ` | `√(4³) = 2³ = 8` |
| Ildizning ildizi | `ᵐ√(ⁿ√a) = ᵐⁿ√a` | `√(³√64) = ⁶√64 = 2` |
| Bekor qilish | `(ⁿ√a)ⁿ = a` | `(√7)² = 7` |

### ⚠️ ENG KATTA XATO: `√(a + b) ≠ √a + √b`

```
√(9 + 16) = √25 = 5
√9 + √16 = 3 + 4 = 7        ≠ 5

√(a + b) = √a + √b  faqat  a = 0  yoki  b = 0  bo'lganda
(isbot: kvadratga ko'tar → a + b = a + 2√(ab) + b → √(ab) = 0)
```

Ildiz **ko'paytma** ustida tarqaladi, **yig'indi** ustida — YO'Q.

> 🔗 **AI:** `‖u + v‖ ≠ ‖u‖ + ‖v‖`. Aslida `‖u + v‖ ≤ ‖u‖ + ‖v‖` (uchburchak tengsizligi,
> 1-mavzu). Tenglik faqat bir yo'nalishda bo'lganda.

---

## 6. Ratsional ko'rsatkich — birlashtiruvchi g'oya

> ⭐⭐⭐ Bu bo'lim daraja va ildizni **bitta narsa** qiladi. AI formulalarida faqat shu
> yozuv ishlatiladi: `x^0.5`, `d^(−0.5)`, `N^(−0.076)`.

### 6.1 Nima uchun `a^(1/2) = √a`

Daraja qoidalari `1/2` uchun ham ishlashini **xohlaymiz**. Unda:

```
(a^(1/2))² = a^(1/2 · 2) = a¹ = a         (2.3 qoida)
```

Demak `a^(1/2)` — kvadrati `a` bo'lgan son. Ya'ni `√a` (musbatini olamiz). ∎

Xuddi shunday: `(a^(1/n))ⁿ = a` → `a^(1/n) = ⁿ√a`.

### 6.2 Umumiy ta'rif

```
a^(m/n) = ⁿ√(aᵐ) = (ⁿ√a)ᵐ          a > 0

8^(2/3) = (³√8)² = 2² = 4          ← avval ildiz (kichik sonlar), keyin daraja
4^(3/2) = (√4)³ = 2³ = 8
27^(−1/3) = 1/(³√27) = 1/3
16^(−3/4) = 1/(⁴√16)³ = 1/2³ = 1/8
```

**Amaliy tartib:** manfiy ishora → ag'dar; maxraj → ildiz; surat → daraja.

### 6.3 Barcha qoidalar saqlanadi

```
x^(1/2) · x^(1/3) = x^(1/2 + 1/3) = x^(5/6)
(x^(2/3))^(3/2) = x^(2/3 · 3/2) = x¹ = x
x^(3/4) / x^(1/4) = x^(1/2) = √x
√x · ³√x = x^(1/2) · x^(1/3) = x^(5/6) = ⁶√(x⁵)
```

### 6.4 Yozuvlar lug'ati

| Ildiz yozuvi | Daraja yozuvi | Kod (Python/NumPy) |
|--------------|---------------|-------------------|
| `√x` | `x^(1/2)` = `x^0.5` | `x**0.5`, `np.sqrt(x)` |
| `1/√x` | `x^(−1/2)` | `x**-0.5`, `1/np.sqrt(x)` |
| `³√x` | `x^(1/3)` | `x**(1/3)`, `np.cbrt(x)` |
| `ⁿ√(xᵐ)` | `x^(m/n)` | `x**(m/n)` |
| `1/x` | `x^(−1)` | `x**-1`, `1/x` |

> ⚠️ `a > 0` sharti muhim: `(−8)^(1/3)` matematikda `−2`, lekin NumPy'da `(-8)**(1/3)` →
> `nan` (yoki kompleks son). `np.cbrt(-8) = -2`. Bu — real dasturlash xatosi manbai.

---

## 7. Soddalashtirish va ratsionallashtirish

### 7.1 Ildizdan ko'paytuvchi chiqarish

```
√50 = √(25 · 2) = √25 · √2 = 5√2       ← eng katta to'la kvadratni ajrat
√72 = √(36 · 2) = 6√2
√200 = √(100 · 2) = 10√2
³√54 = ³√(27 · 2) = 3·³√2              ← kub uchun to'la kub
√12 + √27 = 2√3 + 3√3 = 5√3            ← bir xil ildizlar qo'shiladi (o'xshash hadlar!)
```

### 7.2 Ildizlarni ko'paytirish

```
√2 · √8 = √16 = 4
√3 · √12 = √36 = 6
³√4 · ³√16 = ³√64 = 4
(√5 + √3)² = 5 + 2√15 + 3 = 8 + 2√15       ← (a+b)² formulasi, √a·√b = √(ab)
(√7 − √2)(√7 + √2) = 7 − 2 = 5             ← (a−b)(a+b) = a² − b²
```

### 7.3 Maxrajdagi irratsionallikdan qutulish

**Nima uchun:** `1/√2` ni hisoblash qiyin, `√2/2` oson. Va kelishuv shunday.

**Bitta ildiz** — o'sha ildizga ko'paytir:

```
1/√2 = (1·√2)/(√2·√2) = √2/2
3/√12 = 3/(2√3) = (3√3)/(2·3) = √3/2
```

**Ikki had** — **qo'shma** (conjugate) ifodaga ko'paytir (`a − b` ↔ `a + b`):

```
    1          1 · (√3 + 1)        √3 + 1        √3 + 1
────────  =  ───────────────  =  ──────────  =  ────────
 √3 − 1      (√3 − 1)(√3 + 1)      3 − 1           2

    2          2(√5 − √3)       2(√5 − √3)
─────────  =  ────────────  =  ──────────  =  √5 − √3
 √5 + √3        5 − 3               2
```

> 🔗 **AI:** `1/√d` ni `d^(−0.5)` deb yozish — bu ham "ko'rinishni o'zgartirish".
> Kodda `x / np.sqrt(d)` va `x * d**-0.5` bir xil, ikkinchisi tezroq (bo'lish qimmat).

---

## 8. Darajali funksiyalar grafiklari

`f(x) = xᵃ` oilasi (oldingi mavzu bilan bog'lanish):

```
   a = 2 (x²)      a = 3 (x³)      a = 1/2 (√x)    a = −1 (1/x)     a = −2 (1/x²)
     ╲  ╱             ╱               ╭──            ╲│                ╲│╱
      ╲╱           ──┼──             ╱             ───┼───           ───┼───
                    ╱               ╱                 │╲               │
   juft, ∪        toq, S          faqat x≥0        toq, giperbola   juft, ∪ (0 da yo'q)
```

| `a` | D | E | Xossa |
|-----|---|---|-------|
| juft natural | ℝ | [0,∞) | juft, ∪ |
| toq natural | ℝ | ℝ | toq, o'suvchi |
| `1/n` (juft n) | [0,∞) | [0,∞) | o'suvchi, sekinlashuvchi |
| manfiy | ℝ\{0} | | 0 da vertikal asimptota |

**`x > 1` da:** ko'rsatkich katta → tezroq o'sadi. `x⁰·⁵ < x < x² < x³`.
**`0 < x < 1` da:** TESKARI. `x³ < x² < x < x⁰·⁵`. (Masalan `0.5³ = 0.125 < 0.5² = 0.25 < 0.5 < √0.5 ≈ 0.707`)

> 🔗 **AI:** Scaling law `L(N) ∝ N^(−0.076)` — bu `xᵃ`, `a` kichik manfiy. Grafik:
> sekin-sekin kamayadi, hech qachon 0 ga yetmaydi. Log-log grafikda — **to'g'ri chiziq**
> (keyingi mavzu — logarifmlar).

---

## 9. Standart ko'rinish

**Scientific notation:** `m × 10ⁿ`, bunda `1 ≤ m < 10`.

```
3 400 000 = 3.4 × 10⁶
0.00052 = 5.2 × 10⁻⁴
6.02 × 10²³ = 602 000 000 000 000 000 000 000   (Avogadro)
1.6 × 10⁻¹⁹ = 0.00000000000000000016             (elektron zaryadi, C)
```

**Amallar** — daraja qoidalari bilan:

```
(3 × 10⁸)(2 × 10⁻⁵) = 6 × 10³
(8 × 10¹²)/(4 × 10⁷) = 2 × 10⁵
(2 × 10³)² = 4 × 10⁶
√(4 × 10⁶) = 2 × 10³          ← 10⁶ ning ildizi 10³ (ko'rsatkich ÷ 2)
```

**Kodda:** `3.4e6`, `5.2e-4`, `1e-5` (learning rate!), `1e9` (parametrlar).

> 🔗 **AI'dagi tartiblar (orders of magnitude):**
> ```
> learning rate      1e-3 ... 1e-5
> weight decay       1e-2 ... 1e-4
> epsilon (Adam)     1e-8
> parametrlar        1e8 (BERT) ... 1e11 (GPT-3) ... 1e12
> training tokenlar  1e12 ... 1e13
> FLOPs              1e23 ... 1e25
> ```
> Bu sonlarni `× 10ⁿ` ko'rinishida o'qiy olish — sohada gaplashish tili.

---

## 10. O'sish: 2ⁿ, n² va kompyuter sonlari

### 10.1 Darajali vs eksponensial

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

`n ≥ 5` dan boshlab `2ⁿ` **har doim** oldinda va farq portlab ketadi. Bu — "polinomial vs
eksponensial" farqi, informatikaning markaziy g'oyasi. To'liq — **Eksponentalar** mavzusida.

**Qog'oz buklash:** 0.1 mm qog'ozni 42 marta buklasang: `0.1 mm × 2⁴² ≈ 4.4 × 10¹¹ mm =
440 000 km` — **Oygacha masofadan** (384 000 km) ko'p.

### 10.2 Kompyuter sonlari — float

Kompyuter sonlarni `± m × 2ᵉ` ko'rinishida saqlaydi (ikkilik standart ko'rinish!):

| Format | Bitlar (ishora/eksp/mantissa) | Eng katta | Aniqlik (ε) |
|--------|-------------------------------|-----------|-------------|
| float32 | 1 / 8 / 23 | ≈ 3.4 × 10³⁸ (≈2¹²⁸) | 2⁻²³ ≈ 1.2 × 10⁻⁷ |
| float16 | 1 / 5 / 10 | 65 504 | 2⁻¹⁰ ≈ 9.8 × 10⁻⁴ |
| bfloat16 | 1 / 8 / 7 | ≈ 3.4 × 10³⁸ | 2⁻⁷ ≈ 7.8 × 10⁻³ |

**Natijalar:**
- `float32` butun sonlarni faqat `2²⁴ = 16 777 216` gacha **aniq** saqlaydi.
  `16 777 217` saqlanmaydi — `16 777 216` ga yaxlitlanadi.
- `0.1 + 0.2 ≠ 0.3` — chunki `0.1` ikkilikda cheksiz kasr (`1/3` o'nlikda kabi).
- `float16` da `70 000` — **overflow** (`inf`). Shuning uchun **mixed precision** training'da
  loss scaling kerak.
- `bfloat16` aniqlikni qurbon qilib range'ni saqlaydi — LLM training'da standart.

> 🔗 Bu jadval — **Numerical Mathematics** mavzusining kirish eshigi. Hozir faqat
> "ikkilik daraja" ekanini ko'r: hamma chegara — `2ⁿ`.

---

## 11. Daraja tenglamalari va tengsizliklari

### 11.1 `xⁿ = a`

```
x³ = 27    →  x = 3                  (toq: bitta ildiz)
x³ = −64   →  x = −4
x⁴ = 16    →  x = ±2                 (juft: IKKITA, ± unutma!)
x² = 5     →  x = ±√5
x⁴ = −16   →  ∅                      (juft daraja manfiy bo'lmaydi)
```

### 11.2 `aˣ = b` — asoslarni tenglashtirish (logarifm oldi-ko'rinishi)

```
2ˣ = 32   →  2ˣ = 2⁵      →  x = 5
3ˣ = 1/9  →  3ˣ = 3⁻²     →  x = −2
5ˣ = 1    →  5ˣ = 5⁰      →  x = 0
(1/2)ˣ = 8  →  2⁻ˣ = 2³   →  x = −3
4ˣ = 8    →  2²ˣ = 2³     →  2x = 3  →  x = 3/2
```

**Qoida:** `aˣ = aʸ ⟺ x = y` (a > 0, a ≠ 1) — chunki `aˣ` bir qiymatli funksiya.
`2ˣ = 10` bo'lsa? Asosni tenglashtirib bo'lmaydi → **logarifm** kerak (keyingi mavzu).

### 11.3 Ratsional ko'rsatkichli

```
x^(3/2) = 8    →  x = 8^(2/3) = 4          (ikkala tomonni 2/3 darajaga)
x^(−2) = 1/25  →  x² = 25  →  x = ±5
x^(1/3) = −2   →  x = (−2)³ = −8
```

### 11.4 Tengsizliklar — monotonlik orqali

```
x² < 9     →  −3 < x < 3            (parabola, 1-mavzu)
x² ≥ 16    →  x ≤ −4 yoki x ≥ 4
x³ > 8     →  x > 2                 (x³ o'suvchi → belgi saqlanadi, bitta oraliq)
√x < 3     →  0 ≤ x < 9             (D: x ≥ 0 ni unutma!)
2ˣ > 16    →  x > 4                 (2ˣ o'suvchi)
(1/2)ˣ > 1/8  →  x < 3              (asos < 1 → KAMAYUVCHI → belgi ALMASHADI)
```

### 11.5 Kalkulyatorsiz solishtirish

**Usul 1 — kvadratga ko'tarish** (ikkalasi musbat bo'lsa):
```
√2 + √3  vs  √10
(√2 + √3)² = 5 + 2√6     vs   10
2√6  vs  5    →   24  vs  25    →   24 < 25
Demak  √2 + √3 < √10
```

**Usul 2 — umumiy ko'rsatkichga keltirish:**
```
2³⁰⁰  vs  3²⁰⁰
2³⁰⁰ = (2³)¹⁰⁰ = 8¹⁰⁰,    3²⁰⁰ = (3²)¹⁰⁰ = 9¹⁰⁰
8 < 9  →  2³⁰⁰ < 3²⁰⁰
```

---

## 12. AI uchun muhim

### 12.1 L2 norm — ildiz

```
‖v‖₂ = √(v₁² + v₂² + ... + vₙ²)

‖(3, 4)‖ = √(9 + 16) = 5
‖(1, 2, 2)‖ = √9 = 3
‖(1, 1, ..., 1)‖ (n ta) = √n              ← 1/√d ning kelib chiqishi shu yerda
```

Birlik vektor: `v/‖v‖` — uzunligi 1. `(3,4)/5 = (0.6, 0.8)`.

### 12.2 Attention scaling: `1/√d_k`

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k) V
```

**Nima uchun `√d`?** `q·k = Σqᵢkᵢ` — `d` ta hadning yig'indisi. Har had ~1 bo'lsa,
yig'indining "o'lchami" (standart og'ishi) `√d` ga proporsional (ehtimollar mavzusida
isbotlanadi). `√d` ga bo'lish — o'lchamni ~1 ga qaytarish. `d = 64` → `÷8`.

### 12.3 Og'irliklarni boshlang'ich qiymatlash (initialization)

```
He init:      std = √(2/n_in)       ReLU uchun
Xavier init:  std = √(1/n_in)  yoki  √(2/(n_in + n_out))

n_in = 512:  √(2/512) = √(1/256) = 1/16 = 0.0625
n_in = 128:  √(2/128) = 1/8
```

**Sabab:** `n` ta hadning yig'indisi ~`√n` marta o'sadi (12.2 kabi). Har qatlamda signal
`√n` marta o'smasligi uchun og'irliklarni `1/√n` ga kichraytiramiz.

### 12.4 RMS va RMSNorm

```
RMS(x) = √( (x₁² + ... + xₙ²)/n )        "root mean square" — nomida ildiz va kvadrat
RMSNorm(x) = x / RMS(x) · γ

x = (1, −2, 2, 4):  kvadratlar 1, 4, 4, 16 → yig'indi 25 → /4 = 6.25 → √ = 2.5
x/RMS = (0.4, −0.8, 0.8, 1.6),  uning RMS'i = 1 ✓
```

LLaMA, Mistral, Gemma — RMSNorm ishlatadi.

### 12.5 Learning rate schedule

```
η(t) = η₀ / √t = η₀ · t^(−1/2)

Transformer (Vaswani 2017):  η = d^(−0.5) · min(t^(−0.5), t · w^(−1.5))
d = 512, w = 4000, t = 4000:  (512 · 4000)^(−0.5) = 1/√2 048 000 ≈ 1/1431 ≈ 7 × 10⁻⁴
```

### 12.6 Scaling laws — darajali qonunlar

```
L(N) = (N_c / N)^α         α ≈ 0.076   (Kaplan et al. 2020)
```

Parametrlar 10 marta oshsa loss `10^(−0.076) ≈ 0.84` marta — 16% kamayadi.
Bu `xᵃ` funksiyasi (§8), `a` kichik manfiy.

### 12.7 Hisob hajmi

```
GPT-3: 175 × 10⁹ parametr × 4 bayt (float32) = 7 × 10¹¹ bayt = 700 GB
       float16 da: 350 GB
Training FLOPs ≈ 6 · N · D = 6 · (1.75 × 10¹¹)(3 × 10¹¹) ≈ 3.15 × 10²³
```

### 12.8 Jadval

| Bugungi mavzu | AI'dagi nomi |
|---------------|--------------|
| `√(Σx²)` | L2 norm, Euclidean distance, RMSE |
| `√n` — n ta 1 ning normasi | `1/√d_k` scaling, `1/√n` init |
| `x^(−1/2)` | RMSNorm, Adam denominator, lr decay |
| `x²` | MSE loss, variance, L2 regularization |
| `xᵃ`, a < 0 kichik | Scaling laws `N^(−α)` |
| `2ⁿ` | float range, bit'lar, hisoblash portlashi |
| `2⁻²³` | float32 machine epsilon |
| `m × 10ⁿ` | `1e-5`, `1e9` — hyperparametr tili |
| `(a+b)² ≠ a²+b²` | `‖u+v‖² = ‖u‖² + 2u·v + ‖v‖²` — kosinus teoremasi |

---

## 13. Xatolar muzeyi

| # | Xato | To'g'risi |
|---|------|-----------|
| 1 | `(a + b)² = a² + b²` | 🔴 `a² + 2ab + b²` |
| 2 | `√(a + b) = √a + √b` | 🔴 Faqat ko'paytma ustida: `√(ab) = √a√b` |
| 3 | `−2⁴ = 16` | 🔴 `−16`. `(−2)⁴ = 16` |
| 4 | `a⁻¹ = −a` | 🔴 `1/a` |
| 5 | `2³ · 2⁴ = 4⁷` | 🔴 `2⁷`. Asos ko'paytirilmaydi |
| 6 | `2³ · 2⁴ = 2¹²` | 🔴 `2⁷`. Ko'rsatkichlar **qo'shiladi**, ko'paytirilmaydi |
| 7 | `(a³)² = a⁹` | 🔴 `a⁶`. Ko'paytiriladi, darajaga ko'tarilmaydi |
| 8 | `aᵐ + aⁿ = aᵐ⁺ⁿ` | 🔴 Yig'indi uchun qoida **yo'q** |
| 9 | `√16 = ±4` | 🔴 `√16 = 4`. `x² = 16` ning yechimi `±4` |
| 10 | `√(x²) = x` | 🔴 `\|x\|` |
| 11 | `x⁴ = 16 → x = 2` | 🔴 `x = ±2` |
| 12 | `(−8)^(1/3)` NumPy'da `−2` | 🔴 `nan`. `np.cbrt(−8)` ishlat |
| 13 | `0⁰ = 0` yoki `= 1` deb ishonch bilan | 🔴 Aniqlanmagan; kontekstga bog'liq |
| 14 | `(1/2)ˣ > 1/8 → x > 3` | 🔴 `x < 3`. Asos < 1 → kamayuvchi → belgi almashadi |
| 15 | `1/√2` ni shunday qoldirish | 🟡 `√2/2` — kelishuv (xato emas, lekin odat) |
| 16 | `√x < 3 → x < 9` | 🔴 `0 ≤ x < 9`. Domain! |
| 17 | `x^(1/2) · x^(1/3) = x^(1/6)` | 🔴 `x^(5/6)`. Kasrlar **qo'shiladi**: 1/2 + 1/3 |
| 18 | `float32` da `0.1 + 0.2 == 0.3` | 🔴 `False`. Ikkilikda 0.1 cheksiz |

---

## 📌 Bir sahifalik xulosa

```
DARAJA:     aᵐaⁿ = aᵐ⁺ⁿ | aᵐ/aⁿ = aᵐ⁻ⁿ | (aᵐ)ⁿ = aᵐⁿ | (ab)ⁿ = aⁿbⁿ | (a/b)ⁿ = aⁿ/bⁿ
            a⁰ = 1 | a⁻ⁿ = 1/aⁿ | (a/b)⁻ⁿ = (b/a)ⁿ
            (−2)⁴ = 16 ≠ −2⁴ = −16
YO'Q:       aᵐ + aⁿ ≠ aᵐ⁺ⁿ | (a+b)ⁿ ≠ aⁿ + bⁿ | 2³·2⁴ ≠ 4⁷

ILDIZ:      √a ≥ 0 (arifmetik) | √(a²) = |a| | ³√(−8) = −2 (toq mumkin)
            √(ab) = √a√b | √(a/b) = √a/√b | √(a+b) ≠ √a + √b
            a^(m/n) = ⁿ√(aᵐ) — daraja va ildiz BIR NARSA

SODDALASH:  √50 = 5√2 | 1/√2 = √2/2 | 1/(√3−1) = (√3+1)/2 (qo'shma)

TENGLAMA:   xⁿ = a: toq → 1 ildiz, juft → ±, manfiy a → ∅
            aˣ = aʸ ⟺ x = y   (asosni tenglashtir; bo'lmasa — log)
            asos < 1 → kamayuvchi → tengsizlik belgisi ALMASHADI

STANDART:   m × 10ⁿ, 1 ≤ m < 10.  Kod: 1e-5, 1e9

AI:         ‖v‖ = √(Σv²) | 1/√d_k | std = √(2/n) | RMS | η/√t | N^(−α) | 2⁻²³
```

---

**Keyingi qadam:** [02-masalalar-uz.md](02-masalalar-uz.md)
