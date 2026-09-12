# Funksiyalar — Nazariya

> **O'qish usuli:** har bo'limdan keyin faylni yop, grafikni **qo'l bilan** chiz, ta'rifni
> o'z so'zing bilan yoz. Bu mavzuda grafik chizmasdan o'rganish — suzishni kitobdan o'rganish.

**Mundarija**

1. [Funksiya nima](#1-funksiya-nima)
2. [Funksiyani berish usullari](#2-funksiyani-berish-usullari)
3. [Aniqlanish sohasi va qiymatlar sohasi](#3-aniqlanish-sohasi-va-qiymatlar-sohasi)
4. [Grafik](#4-grafik)
5. [Asosiy funksiyalar galereyasi](#5-asosiy-funksiyalar-galereyasi)
6. [Chiziqli funksiya](#6-chiziqli-funksiya)
7. [Kvadrat funksiya](#7-kvadrat-funksiya)
8. [Funksiya xossalari](#8-funksiya-xossalari)
9. [Grafik almashtirishlar](#9-grafik-almashtirishlar)
10. [Murakkab funksiya (kompozitsiya)](#10-murakkab-funksiya-kompozitsiya)
11. [Teskari funksiya](#11-teskari-funksiya)
12. [Bo'lakli funksiyalar](#12-bolakli-funksiyalar)
13. [AI uchun muhim funksiyalar](#13-ai-uchun-muhim-funksiyalar)
14. [Xatolar muzeyi](#14-xatolar-muzeyi)

---

## 1. Funksiya nima

### 1.1 Ta'rif

**Funksiya** — bu **qoida**: har bir kirish qiymatiga (`x`) **aynan bitta** chiqish
qiymatini (`y`) mos qo'yadi.

```
        ┌─────────────┐
  x ──► │      f      │ ──► y = f(x)
        └─────────────┘
      kirish        chiqish
      (input)       (output)
      (argument)    (qiymat / value)
```

**Yozuv:** `f(x)` — "f funksiyasining x dagi qiymati" (`f` **ko'paytirilmaydi** x ga!).

```
f(x) = 2x + 1

f(3)  = 2·3 + 1 = 7          ← x = 3 kirdi, 7 chiqdi
f(0)  = 1
f(−1) = −1
f(a)  = 2a + 1
f(a+1) = 2(a+1) + 1 = 2a + 3  ← x o'rniga BUTUN ifoda qo'yiladi
```

### 1.2 "Aynan bitta" qoidasi — nima uchun muhim

```
✅ FUNKSIYA                         ❌ FUNKSIYA EMAS
   x → x²                              x → ±√x
   1 → 1                               4 → 2  va  4 → −2
   2 → 4                               (bitta kirishga IKKITA chiqish)
   −1 → 1
   (ikki kirish bir chiqishga — MUMKIN)
```

- Har bir `x` ga bitta `y`: **majburiy**.
- Har xil `x` lar bir xil `y` ga: **mumkin** (`f(1) = f(−1) = 1` uchun `x²`).

> 🔗 **AI:** neyron tarmoq — bu funksiya: `f(rasm) = "mushuk"`. Bitta rasmga bitta javob.
> Agar model bir xil kirishga har safar boshqa javob bersa — bu funksiya emas, va uni
> o'rgatish ham, tekshirish ham bo'lmaydi. (Tasodifiylik — `sampling` — funksiya *ustiga*
> alohida qo'shiladi.)

### 1.3 Vertikal chiziq testi

Grafikda: agar **biror vertikal chiziq** grafikni **2 yoki undan ko'p** nuqtada kessa —
bu funksiya emas.

```
   y = x²  (funksiya)            x = y²  (funksiya EMAS)
      │    ╱                          │      ╭──
      │   ╱                        ───┼─────●────  ← vertikal chiziq
   ───┼──╱───                         │      ╰──      2 nuqtada kesdi
      │╱                              │
```

---

## 2. Funksiyani berish usullari

| Usul | Misol | AI'dagi o'xshashi |
|------|-------|-------------------|
| **Formula** | `f(x) = x² − 1` | Model arxitekturasi |
| **Jadval** | `x: 1,2,3 → y: 2,4,6` | **Dataset** (train data) |
| **Grafik** | parabola chizmasi | Loss curve, vizualizatsiya |
| **So'z bilan** | "sonni ikkilantirib 1 qo'sh" | Task ta'rifi |
| **Algoritm** | `def f(x): return 2*x+1` | Kod |

> 🔗 **Machine learning ning asl mohiyati:** bizga **jadval** (ma'lumot) berilgan,
> biz **formula** (model) topmoqchimiz. Sen A6 masalasida shuni qo'lda qilasan.

---

## 3. Aniqlanish sohasi va qiymatlar sohasi

### 3.1 Aniqlanish sohasi — D(f) (domain)

**D(f)** — funksiya **ma'noga ega** bo'lgan barcha `x` lar to'plami. Bu oldingi
mavzudagi ODZ ning o'zi.

```
1.  Maxraj ≠ 0            f(x) = 1/(x−2)        D = ℝ \ {2}  yoki  (−∞,2) ∪ (2,+∞)
2.  Juft ildiz ostida ≥ 0 f(x) = √(x+3)         D = [−3, +∞)
3.  Ikkalasi birga        f(x) = √(x−1)/(x−4)   D = [1, 4) ∪ (4, +∞)
4.  Cheklov yo'q          f(x) = x² + 3x        D = ℝ
```

**Algoritm:** har bir "xavfli joy"ni top → shart yoz → shartlarni **kesishtir** (∩).

### 3.2 Qiymatlar sohasi — E(f) (range)

**E(f)** — funksiya **qabul qiladigan** barcha `y` lar to'plami.

```
f(x) = x²           E = [0, +∞)      chunki x² ≥ 0 har doim, 0 ga yetadi
f(x) = x² + 2       E = [2, +∞)      3 yuqoriga siljigan
f(x) = −|x| + 3     E = (−∞, 3]      maksimum 3, x = 0 da
f(x) = √x − 1       E = [−1, +∞)
f(x) = 1/x          E = ℝ \ {0}      hech qachon 0 ga teng bo'lmaydi
f(x) = 1/(1+x²)     E = (0, 1]       ← muhim: 0 ga YETMAYDI, 1 ga YETADI
```

**Range topish usullari:**
1. Grafik chizib "yuqori/past chegara qayerda" deb qarash.
2. Eng oddiy qismdan boshlash: `x² ≥ 0` → `x² + 2 ≥ 2`.
3. `y = f(x)` ni `x` ga nisbatan yechib, qaysi `y` larda yechim borligini ko'rish.

> 🔗 **AI:** `sigmoid` ning range'i `(0, 1)` — shuning uchun u **ehtimollik** sifatida
> ishlatiladi. `tanh` range'i `(−1, 1)`. `ReLU` range'i `[0, +∞)`. Aktivatsiya tanlash =
> range tanlash.

---

## 4. Grafik

**Grafik** — barcha `(x, f(x))` nuqtalar to'plami.

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

**Grafikdan o'qish mumkin bo'lgan narsalar:**

| Savol | Grafikda qayerda |
|-------|------------------|
| `f(1) = ?` | `x = 1` dan vertikal yuqoriga → grafikga tegish → `y` ni o'qish |
| Nollar (`f(x) = 0`) | Grafik `x` o'qini kesgan joylar |
| `f(x) > 0` qayerda | Grafik `x` o'qidan **yuqorida** |
| Minimum/maksimum | Eng past/yuqori nuqta |
| O'suvchi/kamayuvchi | Chapdan o'ngga yuqoriga/pastga |
| Domain | Grafikning `x` o'qiga "soyasi" |
| Range | Grafikning `y` o'qiga "soyasi" |

> 🔗 **AI:** `loss vs epoch` grafigi — bu **funksiya grafigi**. Uni o'qish (kamayadimi?
> tekislanadimi? sakraydimi?) — ML muhandisining kunlik ishi.

---

## 5. Asosiy funksiyalar galereyasi

Bu 7 tasini **yoddan chiza olishing** kerak. Har birini qog'ozga 3 marta chiz.

| Funksiya | Grafik | D | E | Xossa |
|----------|--------|---|---|-------|
| `f(x) = c` | gorizontal chiziq | ℝ | {c} | o'zgarmas |
| `f(x) = x` | 45° to'g'ri chiziq | ℝ | ℝ | ayniyat (identity), toq |
| `f(x) = x²` | parabola ∪ | ℝ | [0,∞) | juft, min (0,0) |
| `f(x) = x³` | S-shakl | ℝ | ℝ | toq, o'suvchi |
| `f(x) = \|x\|` | V-shakl | ℝ | [0,∞) | juft, min (0,0), burchak |
| `f(x) = √x` | yarim parabola (yotgan) | [0,∞) | [0,∞) | o'suvchi, sekinlashadi |
| `f(x) = 1/x` | giperbola | ℝ\{0} | ℝ\{0} | toq, 2 bo'lak |

```
   x²          x³           |x|          √x           1/x
   ╲  ╱         ╱          ╲   ╱          ╭──         ╲│
    ╲╱       ──┼──          ╲ ╱          ╱          ───┼───
              ╱              ╲          ╱             │╲
```

**Nima uchun aynan bular:** qolgan barcha funksiyalar shularning **siljitilgan,
cho'zilgan, qo'shilgan, kompozitsiya qilingan** shakllari (§9, §10).

---

## 6. Chiziqli funksiya

### 6.1 Ko'rinish

```
f(x) = kx + b
       │    └── b: ozod had, y-kesma (y-intercept) — grafik y o'qini qayerda kesadi
       └── k: burchak koeffitsienti (slope) — o'zgarish TEZLIGI
```

**Grafik:** to'g'ri chiziq. Ikki nuqta yetarli.

### 6.2 `k` ning ma'nosi — eng muhim g'oya

```
k = (y₂ − y₁)/(x₂ − x₁) = Δy/Δx = "x bir birlik o'sganda y qancha o'zgaradi"
```

| k | Grafik | Ma'no |
|---|--------|-------|
| k > 0 | ↗ | o'suvchi |
| k < 0 | ↘ | kamayuvchi |
| k = 0 | → | o'zgarmas (gorizontal) |
| \|k\| katta | tik | tez o'zgaradi |
| \|k\| kichik | yotiq | sekin o'zgaradi |

**Misol:** taksi: 5000 so'm o'tirish + 2000 so'm/km.
`C(d) = 2000d + 5000`. `k = 2000` — har km uchun narx. `b = 5000` — d = 0 dagi narx.

### 6.3 Ikki nuqtadan chiziq tenglamasi

```
(1, 3) va (3, 7) nuqtalar:

1. k = (7 − 3)/(3 − 1) = 4/2 = 2
2. b:  y = 2x + b  ga (1, 3) ni qo'y:  3 = 2·1 + b  →  b = 1
3. f(x) = 2x + 1

Tekshir (3, 7):  2·3 + 1 = 7 ✓
```

### 6.4 Parallel va perpendikulyar

```
Parallel:         k₁ = k₂           (bir xil tezlik, har xil boshlanish)
Perpendikulyar:   k₁ · k₂ = −1      (k₂ = −1/k₁)
```

### 6.5 Nollar va kesmalar

```
f(x) = −3x + 6
y-kesma:  f(0) = 6                 → (0, 6)
x-kesma (nol):  −3x + 6 = 0 → x = 2 → (2, 0)
```

> 🔗🔗 **AI — bu bo'lim to'g'ridan-to'g'ri ML:**
>
> ```
> Maktab:      y = kx + b
> ML:          y = wx + b        w — weight (og'irlik), b — bias
> Ko'p kirish: y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b = w·x + b
> PyTorch:     nn.Linear(n, 1)
> ```
>
> `nn.Linear` — bu **chiziqli funksiya**. Neyron tarmoqdagi har bir qatlam (layer) —
> chiziqli funksiya + aktivatsiya. `w` ni o'rgatish = `k` ni topish.
> Sen 6.3 da ikki nuqtadan `k, b` topding — bu **2 ta ma'lumotli training**.

---

## 7. Kvadrat funksiya

### 7.1 Ko'rinish va cho'qqi

```
f(x) = ax² + bx + c,   a ≠ 0

Cho'qqi (vertex):   x₀ = −b/(2a),    y₀ = f(x₀)
Simmetriya o'qi:    x = x₀
a > 0  →  ∪  →  y₀ = MINIMUM,   E = [y₀, +∞)
a < 0  →  ∩  →  y₀ = MAKSIMUM,  E = (−∞, y₀]
```

**Nima uchun `−b/2a`?** Nollar `x₁, x₂` simmetrik, o'rtasi `(x₁+x₂)/2 = (−b/a)/2 = −b/2a`
(Viyet!). Ildiz bo'lmasa ham formula ishlaydi.

### 7.2 Vertex form — cho'qqi ko'rinishi

```
f(x) = a(x − h)² + k          cho'qqi (h, k)
```

Standart ko'rinishdan vertex form'ga — **to'la kvadratga to'ldirish** (oldingi mavzu!):

```
x² + 4x + 7
= (x² + 4x + 4) + 3
= (x + 2)² + 3               →  cho'qqi (−2, 3),  min = 3
```

**Vertex form nima beradi:**
- Cho'qqini darrov ko'rasan.
- `(x − h)² ≥ 0` → `f(x) ≥ k` (a > 0 da) — range darrov.
- Grafik = `x²` ni `h` ga o'ngga, `k` ga yuqoriga siljitish, `a` marta cho'zish (§9).

### 7.3 Uch ko'rinish

| Ko'rinish | Formula | Nimani darrov ko'rsatadi |
|-----------|---------|--------------------------|
| Standart | `ax² + bx + c` | `c` = y-kesma |
| Vertex | `a(x − h)² + k` | cho'qqi `(h, k)` |
| Faktorli | `a(x − x₁)(x − x₂)` | nollar `x₁, x₂` |

### 7.4 Kvadrat funksiya bilan optimizatsiya

```
Perimetri 40 m to'rtburchakning eng katta yuzi?

Tomonlar: x va 20 − x
S(x) = x(20 − x) = −x² + 20x
a = −1 < 0 → maksimum bor
x₀ = −20/(2·(−1)) = 10  →  S = 100 m²  →  KVADRAT
```

> 🔗 **AI:** Bu — **optimizatsiya**ning eng oddiy ko'rinishi. Loss funksiyasi ko'pincha
> (lokal) parabola shaklida. Gradient descent — "parabolaning cho'qqisiga dumalab tushish".
> G5 masalasida sen `L(w)` ning **aynan parabola** ekanini ko'rsatasan.

---

## 8. Funksiya xossalari

### 8.1 Juft va toq

```
JUFT (even):   f(−x) = f(x)      grafik y o'qiga nisbatan SIMMETRIK (ko'zgu)
TOQ  (odd):    f(−x) = −f(x)     grafik koordinata boshiga nisbatan simmetrik (180° burish)
```

**Tekshirish — ta'rifdan, faqat ta'rifdan:**

```
f(x) = x⁴ − 3x²
f(−x) = (−x)⁴ − 3(−x)² = x⁴ − 3x² = f(x)         → JUFT

g(x) = x³ + x
g(−x) = −x³ − x = −(x³ + x) = −g(x)              → TOQ

h(x) = x² + x
h(−x) = x² − x     ≠ h(x)  va  ≠ −h(x)           → HECH QAYSI
```

**Tezkor qoida (polinomlar uchun):** faqat juft darajalar → juft; faqat toq darajalar → toq;
aralash → hech qaysi. `|x|` — juft. `1/x` — toq. Konstanta `c ≠ 0` — juft.

> 🔗 **AI:** `tanh` — toq, `x²` (MSE) — juft, `ReLU` — hech qaysi. Simmetriya bilishi
> model haqida fikrlashda yordam beradi: masalan, `tanh(−x) = −tanh(x)` — manfiy signal
> aynan teskari chiqadi.

### 8.2 Monotonlik

```
O'SUVCHI  (increasing) oraliqda:   x₁ < x₂  ⟹  f(x₁) < f(x₂)     ↗
KAMAYUVCHI (decreasing) oraliqda:  x₁ < x₂  ⟹  f(x₁) > f(x₂)     ↘
```

**Isbot namunasi:** `f(x) = 2x + 3` o'suvchi:

```
x₁ < x₂  →  2x₁ < 2x₂  →  2x₁ + 3 < 2x₂ + 3  →  f(x₁) < f(x₂)   ∎
```

⚠️ **Tuzoq:** `1/x` — `(−∞, 0)` da kamayuvchi **va** `(0, +∞)` da kamayuvchi, lekin
**butun domain'da kamayuvchi EMAS**: `f(−1) = −1 < f(1) = 1`. Oraliqlarni alohida yoz.

> 🔗 **AI:** `sigmoid`, `softmax`, `log`, `exp` — **monoton o'suvchi**. Bu juda muhim:
> monoton funksiya **tartibni saqlaydi**. Agar `z₁ > z₂` bo'lsa, `softmax(z)₁ > softmax(z)₂`.
> Shuning uchun `argmax` softmax'dan oldin va keyin bir xil.

### 8.3 Nollar va ishora

```
f(x) = x³ − 4x = x(x − 2)(x + 2)

Nollar:  x = −2, 0, 2

Ishoralar (interval usuli — oldingi mavzu):
     −2        0        2
──────●────────●────────●──────
  −        +        −        +

f(x) > 0  ⟺  x ∈ (−2, 0) ∪ (2, +∞)
```

### 8.4 Chegaralanganlik

```
f(x) = 1/(1 + x²)

1 + x² ≥ 1   →   0 < 1/(1+x²) ≤ 1
E = (0, 1]:  yuqoridan 1 bilan (x = 0 da yetadi), pastdan 0 bilan (yetmaydi) chegaralangan
```

### 8.5 Maksimum va minimum

- **Global:** butun domain'dagi eng katta/kichik qiymat.
- **Lokal:** biror atrofdagi eng katta/kichik.

> 🔗 **AI:** loss funksiyasi minimumini topish = training. **Lokal** minimum tuzog'i —
> deep learning'ning klassik muammosi. Bu so'zlar shu bo'limdan.

---

## 9. Grafik almashtirishlar

Bitta asosiy grafikdan (`x²`, `|x|`, `√x`...) yuzlab boshqasini olish. **Yod ol:**

| Yozuv | Nima bo'ladi | Yo'nalish |
|-------|--------------|-----------|
| `f(x) + c` | yuqoriga siljish | ↑ c |
| `f(x) − c` | pastga siljish | ↓ c |
| `f(x − c)` | **o'ngga** siljish | → c ⚠️ (minus = o'ng!) |
| `f(x + c)` | **chapga** siljish | ← c |
| `a·f(x)`, a > 1 | vertikal cho'zish | tikroq |
| `a·f(x)`, 0 < a < 1 | vertikal siqish | yotiqroq |
| `−f(x)` | x o'qiga nisbatan aks | ∪ → ∩ |
| `f(−x)` | y o'qiga nisbatan aks | chap↔o'ng |
| `f(bx)`, b > 1 | gorizontal siqish | torroq |
| `\|f(x)\|` | manfiy qismni yuqoriga buk | |
| `f(\|x\|)` | o'ng yarmini chapga ko'zguda ko'chir | |

**Nima uchun `f(x − 2)` O'NGGA?** Chunki `f(x − 2)` da `x = 2` bo'lganda `f(0)` chiqadi.
Ya'ni asl grafikning `x = 0` dagi qiymati endi `x = 2` da turadi — o'ngga ko'chdi.

**Misol — tartib bilan:**

```
y = −2(x − 3)² + 1        asos: x²

1. x²           → parabola, cho'qqi (0,0)
2. (x − 3)²     → 3 o'ngga,          cho'qqi (3, 0)
3. 2(x − 3)²    → 2 marta cho'zish,  cho'qqi (3, 0), torroq
4. −2(x − 3)²   → aks,               cho'qqi (3, 0), ∩
5. −2(x−3)² + 1 → 1 yuqoriga,        cho'qqi (3, 1)   ✓
```

> 🔗 **AI — normalizatsiya:** `z = (x − μ)/σ` — bu `x` ni `μ` ga chapga siljitish va
> `1/σ` ga siqish. **Har bir** ML pipeline'da bor. Teskarisi `x = σz + μ` —
> denormalizatsiya. Bu §9 ning o'zi.

---

## 10. Murakkab funksiya (kompozitsiya)

> ⭐⭐⭐⭐⭐ **Butun mavzuning eng muhim bo'limi.** Neyron tarmoq — bu kompozitsiya.

### 10.1 Ta'rif

```
(f ∘ g)(x) = f(g(x))       "avval g, keyin f"    ← o'qish tartibi: ICHKARIDAN tashqariga

  x ──► g ──► g(x) ──► f ──► f(g(x))
```

**Misol:**

```
f(x) = 2x + 1,    g(x) = x²

f(g(x)) = f(x²) = 2x² + 1              ← g ni f ning ichiga qo'ydik
g(f(x)) = g(2x+1) = (2x + 1)²          ← f ni g ning ichiga qo'ydik

f(g(2)) = 2·4 + 1 = 9
g(f(2)) = (5)² = 25                    ← TENG EMAS!
```

**Kompozitsiya kommutativ EMAS:** `f∘g ≠ g∘f` (umuman olganda). Tartib muhim.

### 10.2 Domain

`f(g(x))` ning domain'i: `x` — `g` ning domain'ida **va** `g(x)` — `f` ning domain'ida.

```
f(x) = √x,  g(x) = x − 4
f(g(x)) = √(x − 4)     D: x − 4 ≥ 0  →  x ≥ 4
g(f(x)) = √x − 4       D: x ≥ 0
```

### 10.3 Ajratish (decomposition)

```
h(x) = (3x − 1)⁵          →   g(x) = 3x − 1  (ichki),   f(u) = u⁵  (tashqi)
h(x) = √(x² + 1)          →   g(x) = x² + 1,             f(u) = √u
h(x) = 1/(x + 2)²         →   g(x) = x + 2,   m(u) = u², f(v) = 1/v   (3 qavat)
```

Bu ko'nikma calculus'da **zanjir qoidasi** (chain rule) uchun majburiy: hosila olishda
tashqi va ichki funksiyani ajrata bilish kerak.

### 10.4 🔗🔗 Neyron tarmoq = kompozitsiya

```
Bitta qatlam:     h = σ(Wx + b)                σ — aktivatsiya (ReLU, sigmoid...)
                       └──┬──┘
                    chiziqli funksiya

Ikki qatlam:      y = W₂ · σ(W₁x + b₁) + b₂
                      └───────┬───────────┘
                       f₂ ∘ σ ∘ f₁

n qatlam:         y = fₙ ∘ σ ∘ fₙ₋₁ ∘ σ ∘ ... ∘ σ ∘ f₁ (x)

"Deep" learning = "ko'p qavatli KOMPOZITSIYA"
```

**Nima uchun aktivatsiya kerak — isbot (juda muhim):**

```
Ikki chiziqli funksiya kompozitsiyasi:
f(x) = ax + b,   g(x) = cx + d

f(g(x)) = a(cx + d) + b = (ac)x + (ad + b)  →  BU HAM CHIZIQLI!
                          └┬┘   └───┬───┘
                          k'        b'

Demak:  100 ta chiziqli qatlam = 1 ta chiziqli qatlam.
Chuqurlik hech narsa bermaydi.

Aktivatsiya (σ) — chiziqli BO'LMAGAN funksiya — orasiga qo'yilganda
kompozitsiya haqiqatan murakkablashadi.
```

Bu isbot — deep learning'ning "nima uchun" degan savolining yarmi. Sen uni hozir
tushunding, va u faqat §6 va §10 dan iborat.

**Misol (E7 masalasi):**

```
L₁(x) = 2x − 1,   σ(z) = max(0, z),   L₂(z) = −z + 3

y(x) = L₂(σ(L₁(x)))

x = 0:  L₁ = −1  →  σ = 0   →  L₂ = 3
x = 1:  L₁ = 1   →  σ = 1   →  L₂ = 2
x = 2:  L₁ = 3   →  σ = 3   →  L₂ = 0

Grafik:  x ≤ 1/2 da  y = 3 (tekis),   x > 1/2 da  y = −2x + 4 (tushuvchi)
         → BO'LAKLI CHIZIQLI funksiya. ReLU-tarmoq har doim shunday chiqaradi.
```

---

## 11. Teskari funksiya

### 11.1 G'oya

`f` `x` ni `y` ga olib boradi. `f⁻¹` — `y` ni **qaytarib** `x` ga olib boradi.

```
f:    x ──► y            f(x) = 3x − 6:      2 ──► 0
f⁻¹:  y ──► x            f⁻¹(y) = (y+6)/3:   0 ──► 2

f⁻¹(f(x)) = x    va    f(f⁻¹(y)) = y      ← "bekor qilish"
```

⚠️ `f⁻¹(x)` — bu `1/f(x)` **EMAS**! Yozuv o'xshash, ma'no boshqa.

### 11.2 Qachon mavjud

Faqat **bir qiymatli** (one-to-one, injective) funksiyalar uchun: har xil `x` → har xil `y`.

**Gorizontal chiziq testi:** biror gorizontal chiziq grafikni 2+ nuqtada kessa —
teskari funksiya **yo'q**.

```
f(x) = x²:   f(2) = f(−2) = 4  →  4 ni qaytarsak 2 mi, −2 mi?  →  teskari YO'Q
Yechim:  domain'ni cheklash:  x ≥ 0 da  f⁻¹(x) = √x
```

### 11.3 Topish algoritmi

```
1. y = f(x) yoz
2. x ni y orqali ifodala (tenglamani x ga nisbatan yech)
3. x ↔ y ni almashtir (odat bo'yicha argument x deb yoziladi)

f(x) = (2x + 1)/(x − 3)

y(x − 3) = 2x + 1
xy − 3y = 2x + 1
xy − 2x = 3y + 1
x(y − 2) = 3y + 1
x = (3y + 1)/(y − 2)

f⁻¹(x) = (3x + 1)/(x − 2),   x ≠ 2

Tekshir:  f(4) = 9/1 = 9,   f⁻¹(9) = 28/7 = 4  ✓
```

### 11.4 Grafik

`f` va `f⁻¹` grafiklari `y = x` chizig'iga nisbatan **simmetrik**. `D(f⁻¹) = E(f)`,
`E(f⁻¹) = D(f)`.

> 🔗 **AI:**
> - `exp` ↔ `log` (keyingi mavzular)
> - `sigmoid` ↔ `logit`: `σ(x) = 1/(1+e⁻ˣ)`, `logit(p) = ln(p/(1−p))`
> - normalizatsiya ↔ denormalizatsiya
> - **Autoencoder:** `encoder` ↔ `decoder` — "taxminan teskari" funksiyalar juftligi
> - Tokenizer `encode` ↔ `decode`

---

## 12. Bo'lakli funksiyalar

Har xil oraliqda har xil formula:

```
        ⎧ x + 2,   x < 0
f(x) =  ⎨ x²,      0 ≤ x ≤ 2
        ⎩ 4,       x > 2

f(−3) = −1     (1-qator)
f(0)  = 0      (2-qator, 0 ≤ 0 ≤ 2)
f(2)  = 4      (2-qator)
f(5)  = 4      (3-qator)
```

**Uzluksizlik** (continuity) — grafik "uzilmaydi"mi? Bo'lak chegaralarida tekshir:
`x = 0`: chapdan `0 + 2 = 2`, o'ngdan `0² = 0` → **sakrash**, uzilish.
`x = 2`: chapdan `4`, o'ngdan `4` → uzluksiz.

### AI'dagi bo'lakli funksiyalar

```
ReLU(z)       = max(0, z)            = ⎧ z,  z > 0
                                       ⎩ 0,  z ≤ 0

LeakyReLU(z)  = ⎧ z,      z > 0
                ⎩ 0.01z,  z ≤ 0

Heaviside(z)  = ⎧ 1,  z ≥ 0             ← birinchi "neyron" (1943, McCulloch–Pitts)
                ⎩ 0,  z < 0

clip(z,lo,hi) = max(lo, min(hi, z))   ← gradient clipping, pixel [0,255]

Huber loss    = ⎧ ½z²,           |z| ≤ δ    ← MSE va MAE aralashmasi
                ⎩ δ(|z| − δ/2),  |z| > δ
```

---

## 13. AI uchun muhim funksiyalar

Bu bo'lim — **tanishuv**. `e` soni va `ln` keyingi mavzularda. Hozir **shakl** va
**xossalar**ni bil.

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

| Xossa | Qiymat | Nega muhim |
|-------|--------|------------|
| D | ℝ | istalgan son kiradi |
| E | (0, 1) | **ehtimollik** sifatida ishlaydi |
| σ(0) | 0.5 | "ishonchsizlik" nuqtasi |
| Monoton | o'suvchi | tartibni saqlaydi |
| Simmetriya | σ(−x) = 1 − σ(x) | "ha" va "yo'q" ehtimolliklari yig'indisi 1 |
| Chegaralar | x→+∞: →1, x→−∞: →0 | to'yinish (saturation) |

**Range isboti:** `e⁻ˣ > 0` → `1 + e⁻ˣ > 1` → `0 < 1/(1+e⁻ˣ) < 1`. ∎

### 13.2 tanh

```
tanh(x) = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ) = 2σ(2x) − 1

E = (−1, 1),  toq funksiya,  tanh(0) = 0,  monoton o'suvchi
```

### 13.3 ReLU

```
ReLU(x) = max(0, x)         E = [0, +∞),   x = 0 da burchak (hosilasi yo'q)
```

Nima uchun eng mashhur? Hisoblash arzon, gradient 1 yoki 0 (to'yinmaydi, x > 0 da),
kompozitsiyasi — bo'lakli chiziqli.

### 13.4 Softmax (ko'p kirishli funksiya)

```
softmax(z)ᵢ = eᶻⁱ / Σⱼ eᶻʲ

Xossalari:  har bir chiqish ∈ (0, 1),   yig'indisi = 1,   tartibni saqlaydi
```

Bu — "n ta sonni n ta ehtimollikka aylantiruvchi funksiya". Har bir LLM oxirida turadi.

### 13.5 Loss funksiyalari

```
MSE(y, ŷ) = (y − ŷ)²                juft, parabola, minimum 0 da
MAE(y, ŷ) = |y − ŷ|                 juft, V-shakl
```

---

## 14. Xatolar muzeyi

| # | Xato | To'g'risi |
|---|------|-----------|
| 1 | `f(x + 1) = f(x) + 1` | 🔴 `x` o'rniga **butun** `(x+1)` qo'yiladi: `f(x+1) = 2(x+1)+1` |
| 2 | `f(x − 2)` — chapga siljish | 🔴 **O'ngga**. `x − 2 = 0` → `x = 2` |
| 3 | `f(g(x)) = g(f(x))` | 🔴 Umuman olganda **teng emas** |
| 4 | `f⁻¹(x) = 1/f(x)` | 🔴 Teskari funksiya ≠ teskari son |
| 5 | `x²` teskari funksiyaga ega | 🔴 Faqat `x ≥ 0` ga cheklansa |
| 6 | `1/x` butun domain'da kamayuvchi | 🔴 Faqat har bir oraliqda alohida |
| 7 | "Juft — chunki `x²` bor" | 🔴 Faqat **ta'rifdan**: `f(−x) = f(x)` tekshir |
| 8 | Range = Domain | 🔴 Har xil narsa. `√x`: D=[0,∞), E=[0,∞) tasodifan bir xil |
| 9 | Cho'qqi `x = b/2a` | 🔴 `x = −b/(2a)` — minus! |
| 10 | `E(1/(1+x²)) = [0, 1]` | 🔴 `(0, 1]` — 0 ga **yetmaydi** |
| 11 | "Chuqur tarmoq = ko'p chiziqli qatlam" | 🔴 Chiziqlilar kompozitsiyasi = chiziqli. Aktivatsiya **kerak** |
| 12 | Grafikni chizmasdan xossa aytish | 🔴 Chiz. Har doim. |

---

## 📌 Bir sahifalik xulosa

```
FUNKSIYA:    har bir x → AYNAN BITTA y.  Vertikal chiziq testi.
D(f):        maxraj≠0, √ ichi≥0.   E(f): grafikning y-soyasi.

CHIZIQLI:    y = kx + b.   k = Δy/Δx = tezlik.   b = y-kesma.
             Parallel: k₁=k₂.  Perpendikulyar: k₁k₂=−1.       [ML: y = wx + b]

KVADRAT:     cho'qqi x₀ = −b/2a.   Vertex form a(x−h)²+k.   a>0 → min, a<0 → max.

XOSSALAR:    juft f(−x)=f(x) | toq f(−x)=−f(x) | monoton | nollar | chegaralangan

SILJITISH:   f(x)+c ↑ | f(x−c) → | a·f(x) cho'zish | −f(x) aks | f(−x) aks

KOMPOZITSIYA: f(g(x)) — ichkaridan tashqariga. f∘g ≠ g∘f.
             (ax+b)∘(cx+d) = chiziqli  →  AKTIVATSIYA KERAK       [ML: deep = ko'p ∘]

TESKARI:     y=f(x) → x ni yech → almashtir.  Faqat bir qiymatli f uchun.  ≠ 1/f(x)

AI:          sigmoid (0,1) | tanh (−1,1) | ReLU [0,∞) | softmax → ehtimollik
```

---

**Keyingi qadam:** [02-masalalar-uz.md](02-masalalar-uz.md) — qog'oz, qalam, va **chizg'ich**.
