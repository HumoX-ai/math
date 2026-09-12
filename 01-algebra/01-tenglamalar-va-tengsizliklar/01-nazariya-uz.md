# Tenglamalar va Tengsizliklar — Nazariya

> **O'qish usuli:** ko'chirma. Har bo'limni o'qigach, kitobni yop va **o'z so'zing bilan**
> qog'ozga qayta yoz. Formulani ko'rmasdan chiqara olsang — bilding. Aks holda — yo'q.

**Mundarija**

1. [Tenglama nima](#1-tenglama-nima)
2. [Ekvivalent almashtirishlar — mavzuning yuragi](#2-ekvivalent-almashtirishlar--mavzuning-yuragi)
3. [Chiziqli tenglamalar](#3-chiziqli-tenglamalar)
4. [Chiziqli tenglamalar sistemasi](#4-chiziqli-tenglamalar-sistemasi)
5. [Kvadrat tenglamalar](#5-kvadrat-tenglamalar)
6. [Ratsional tenglamalar](#6-ratsional-tenglamalar)
7. [Irratsional tenglamalar](#7-irratsional-tenglamalar)
8. [Modulli tenglamalar](#8-modulli-tenglamalar)
9. [Tengsizliklar: asosiy xossalar](#9-tengsizliklar-asosiy-xossalar)
10. [Chiziqli va kvadrat tengsizliklar](#10-chiziqli-va-kvadrat-tengsizliklar)
11. [Interval usuli](#11-interval-usuli-ratsional-tengsizliklar)
12. [Modulli tengsizliklar](#12-modulli-tengsizliklar)
13. [AI uchun muhim tengsizliklar](#13-ai-uchun-muhim-tengsizliklar)
14. [Xatolar muzeyi](#14-xatolar-muzeyi)

---

## 1. Tenglama nima

### 1.1 Uch xil tenglik

Bu uchtasini farqlash — hamma narsaning boshi:

| Turi | Misol | Ma'nosi |
|------|-------|---------|
| **Ayniyat** (identity) | x + x = 2x | **Barcha** x uchun to'g'ri |
| **Tenglama** (equation) | 2x + 1 = 7 | **Ba'zi** x uchun to'g'ri (bu yerda x = 3) |
| **Yolg'on tenglik** | x = x + 1 | **Hech qanday** x uchun to'g'ri emas |

Tenglama — bu **savol**: *"x ning qanday qiymatlarida bu tenglik to'g'ri bo'ladi?"*

### 1.2 Yechimlar to'plami (solution set)

Tenglamaning javobi — bitta son emas, **to'plam**.

```
2x + 1 = 7        →  S = {3}
x² = 4            →  S = {−2, 2}
x² = −1           →  S = ∅        (bo'sh to'plam, haqiqiy sonlarda)
x + x = 2x        →  S = ℝ        (barcha haqiqiy sonlar)
```

Bu "to'plam" nuqtai nazari muhim, chunki keyinchalik:
- chiziqli sistemalarda yechimlar to'plami **to'g'ri chiziq yoki tekislik** bo'ladi,
- optimizatsiyada **ruxsat etilgan soha** (feasible set) tushunchasi shundan chiqadi.

### 1.3 ODZ — Aniqlanish sohasi (domain)

**ODZ** = *"x ning qanday qiymatlarida tenglamaning o'zi ma'noga ega?"*

Uchta asosiy taqiq:

```
1.  Maxraj ≠ 0            →   1/(x−2)      uchun   x ≠ 2
2.  Juft ildiz ostida ≥ 0 →   √(x−3)       uchun   x ≥ 3
3.  Logarifm ichi > 0     →   log(x+1)     uchun   x > −1
```

> ⚠️ **ODZ ni yechishdan OLDIN yoz.** Keyin emas. Bu 1-raqamli xato manbai.
> ODZ — bu chegara, sen uning ichida ishlaysan.

---

## 2. Ekvivalent almashtirishlar — mavzuning yuragi

Bu bo'limni tushunsang, qolgan hamma narsa texnika. Tushunmasang — doim adashasan.

**Savol:** tenglamani "yechish" deganda biz nima qilamiz?

**Javob:** tenglamani **yechimlar to'plami o'zgarmaydigan** tarzda soddalashtiramiz.

```
A = B          →          A' = B'          →          x = 5
(murakkab)               (soddaroq)                  (javob)

    ↑ har bir qadam yechimlar to'plamini SAQLASHI kerak
```

### 2.1 Xavfsiz amallar (yechimlar to'plami saqlanadi)

| Amal | Misol |
|------|-------|
| Ikkala tomonga bir xil son/ifoda **qo'shish/ayirish** | x − 3 = 5 → x = 8 |
| Ikkala tomonni **nolmas songa** ko'paytirish/bo'lish | 2x = 6 → x = 3 |
| Bir tomonni soddalashtirish (ayniy almashtirish) | 2(x+1) = 2x+2 |

### 2.2 XAVFLI amallar

Bu jadval — mavzuning eng muhim jadvali. Yodla:

| Amal | Nima bo'ladi | Nima qilish kerak |
|------|--------------|-------------------|
| **O'zgaruvchili ifodaga ko'paytirish** | **Begona ildiz** paydo bo'ladi | Oxirida **tekshir** |
| **O'zgaruvchili ifodaga bo'lish** | **Ildiz yo'qoladi** | Bo'luvchi = 0 holatini alohida ko'r |
| **Kvadratga ko'tarish** | **Begona ildiz** paydo bo'ladi | Oxirida **tekshir** |
| **Kvadrat ildiz olish** | Ildiz yo'qoladi (± unutiladi) | `√(a²) = \|a\|`, `±` ni unutma |

#### Misol 1 — bo'lish orqali ildiz yo'qotish (juda keng tarqalgan xato)

```
x² = 5x
─────────────────────────────────
❌ NOTO'G'RI:
   x² = 5x
   x = 5          ← ikkala tomonni x ga bo'ldik
   Javob: {5}     ← x = 0 YO'QOLDI!

✅ TO'G'RI:
   x² − 5x = 0
   x(x − 5) = 0
   x = 0  yoki  x = 5
   Javob: {0, 5}
```

**Qoida:** *hech qachon o'zgaruvchiga bo'lma. Har doim bir tomonga yig'ib, ko'paytuvchilarga ajrat.*

#### Misol 2 — kvadratga ko'tarib begona ildiz olish

```
√x = −2
─────────────────────────────────
Kvadratga ko'taramiz:  x = 4
Tekshiramiz:  √4 = 2 ≠ −2   ❌
Javob: S = ∅
```

Nega shunday bo'ldi? Chunki `a = b  ⟹  a² = b²` to'g'ri, lekin **teskarisi noto'g'ri**:
`a² = b²  ⟹  a = b  yoki  a = −b`. Kvadratga ko'tarish "yo'q, bu manfiy" degan
ma'lumotni yo'qotadi.

### 2.3 Oltin qoida

> **Xavfli amal ishlatsang — javobni ASL tenglamaga qo'yib tekshir. Har doim.**

Bu "ehtiyotkorlik" emas — bu yechimning **majburiy qismi**.

---

## 3. Chiziqli tenglamalar

### 3.1 Umumiy ko'rinish

```
ax + b = 0,     a, b — berilgan sonlar,  x — noma'lum
```

### 3.2 To'liq tahlil (parametrli tenglamalarning asosi)

```
ax + b = 0

├── a ≠ 0                  →  x = −b/a          (bitta yechim)
│
└── a = 0                  →  b = 0 ga aylanadi
    ├── b = 0  →  0 = 0    →  S = ℝ             (cheksiz ko'p yechim)
    └── b ≠ 0  →  b = 0    →  S = ∅             (yechim yo'q)
```

> Bu uchta holat **tasodifiy emas**. Keyinchalik `Ax = b` matritsali sistemada aynan
> shu uchta holatni ko'rasan. Hozir bitta o'zgaruvchi bilan tushunib olsang —
> chiziqli algebra ancha oson bo'ladi.

### 3.3 Yechish algoritmi

```
1. Qavslarni och
2. Maxrajlardan qutul (umumiy maxrajga ko'paytir)
3. x li hadlarni CHAPGA, sonlarni O'NGGA yig'
4. Ixchamla:  ax = c
5. a ga bo'l (a ≠ 0 ni tekshir!)
6. Tekshir
```

**Misol:**

```
(2x − 1)/3 − (x + 2)/4 = 1

12 ga ko'paytiramiz (umumiy maxraj):
    4(2x − 1) − 3(x + 2) = 12
    8x − 4 − 3x − 6 = 12
    5x − 10 = 12
    5x = 22
    x = 22/5 = 4.4

Tekshirish:  (2·4.4 − 1)/3 − (4.4 + 2)/4 = 7.8/3 − 6.4/4 = 2.6 − 1.6 = 1  ✓
```

---

## 4. Chiziqli tenglamalar sistemasi

> ⭐ **Bu bo'lim linear algebra'ning to'g'ridan-to'g'ri kirish eshigi.** Diqqat bilan o'qi.

### 4.1 Sistema nima

```
⎧ 2x + y = 7
⎨
⎩ x − y = 2
```

**Ma'nosi:** *"ikkala tenglamani bir vaqtda qanoatlantiruvchi (x, y) juftlikni top."*

### 4.2 Geometrik ma'no (eng muhim g'oya)

Har bir chiziqli tenglama tekislikda **to'g'ri chiziq**. Sistemani yechish =
**chiziqlarning kesishish nuqtasini topish**.

```
1) Chiziqlar kesishadi        2) Parallel                3) Ustma-ust
      ╲   ╱                      ────────                  ══════════
       ╲ ╱                       ────────                  (bir xil chiziq)
        ╳
       ╱ ╲
   1 ta yechim                 0 ta yechim              Cheksiz ko'p yechim
   (determined)                (inconsistent)           (underdetermined)
```

> 🔗 **AI bilan bog'liqlik:** neyron tarmoqda "parametrlar soni > ma'lumot soni" holati —
> bu 3-holat, ya'ni **cheksiz ko'p yechim**. Shuning uchun regularizatsiya kerak:
> cheksiz yechimdan **qaysi birini** tanlashni aytish kerak. Bu shu yerdan boshlanadi.

### 4.3 Usul 1 — o'rniga qo'yish (substitution)

```
⎧ 2x + y = 7        →  y = 7 − 2x
⎩ x − y = 2

x − (7 − 2x) = 2
x − 7 + 2x = 2
3x = 9  →  x = 3
y = 7 − 2·3 = 1

Javob: (3, 1)
```

### 4.4 Usul 2 — qo'shish/ayirish (elimination) ⭐

Bu usul muhimroq, chunki **Gauss usuli** aynan shundan o'sib chiqadi.

```
⎧ 2x + y = 7
⎩ x − y = 2
─────────────  qo'shamiz (y lar yo'qoladi)
  3x     = 9   →  x = 3
              →  y = 1
```

### 4.5 Uch noma'lumli sistema

```
⎧ x + y + z = 6      ... (1)
⎨ 2x − y + z = 3     ... (2)
⎩ x + 2y − z = 2     ... (3)

(1)+(3):   2x + 3y = 8      ... (4)
(2)+(3):   3x + y  = 5      ... (5)

(5) dan:   y = 5 − 3x
(4) ga:    2x + 3(5 − 3x) = 8
           2x + 15 − 9x = 8
           −7x = −7  →  x = 1
           y = 5 − 3 = 2
(1) dan:   z = 6 − 1 − 2 = 3

Javob: (1, 2, 3)
Tekshir (2): 2 − 2 + 3 = 3 ✓   (3): 1 + 4 − 3 = 2 ✓
```

> 🔗 Bu jarayon **Gaussian elimination**. Linear algebra'da buni matritsa bilan
> yozasan va u `A⁻¹b`, `rank`, `LU decomposition` ga olib boradi. Hozir qo'lda
> qilayotganing — o'sha algoritmning o'zi.

---

## 5. Kvadrat tenglamalar

```
ax² + bx + c = 0,     a ≠ 0
```

### 5.1 Formulani CHIQARISH (yodlama — chiqar!)

Bu — butun mavzudagi eng muhim ko'nikma. **To'liq kvadratga to'ldirish** (completing
the square) usuli keyinchalik Gaussian taqsimotda, ridge regression'da, Kalman filterda
qayta-qayta uchraydi.

```
ax² + bx + c = 0                          | a ga bo'lamiz (a ≠ 0)

x² + (b/a)x + c/a = 0

x² + (b/a)x = −c/a                        | x ning koeffitsientining
                                          | yarmi = b/(2a), uni kvadratlaymiz
x² + (b/a)x + (b/2a)² = −c/a + (b/2a)²    | ikkala tomonga qo'shamiz

(x + b/2a)² = b²/4a² − c/a                | chap tomon — to'la kvadrat

(x + b/2a)² = (b² − 4ac) / 4a²            | o'ng tomonni umumiy maxrajga

x + b/2a = ± √(b² − 4ac) / 2a             | ildiz olamiz (± ni UNUTMA)

x = (−b ± √(b² − 4ac)) / 2a               ✓
```

**Diskriminant:** `D = b² − 4ac`

| D | Ildizlar soni | Grafik |
|---|---------------|--------|
| D > 0 | 2 ta har xil ildiz | Parabola x o'qini 2 nuqtada kesadi |
| D = 0 | 1 ta (ikki karrali) ildiz | Parabola x o'qiga urinadi |
| D < 0 | Haqiqiy ildiz yo'q | Parabola x o'qini kesmaydi |

### 5.2 Viyet teoremasi

Agar `x₁, x₂` — `ax² + bx + c = 0` ning ildizlari bo'lsa:

```
x₁ + x₂ = −b/a
x₁ · x₂ =  c/a
```

`x² + px + q = 0` uchun (a = 1): `x₁ + x₂ = −p`, `x₁·x₂ = q`

**Nima uchun foydali:**
- Ildizlarni topmasdan `x₁² + x₂²` kabi ifodalarni hisoblash:
  `x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂`
- Butun ildizlarni tez topish: `x² − 5x + 6 = 0` → yig'indisi 5, ko'paytmasi 6 → 2 va 3.

### 5.3 Ko'paytuvchilarga ajratish

```
x² − 5x + 6 = 0
(x − 2)(x − 3) = 0
x = 2  yoki  x = 3
```

**Nol haqidagi asosiy fakt:** `A · B = 0  ⟺  A = 0 yoki B = 0`
Bu faqat **nol** uchun ishlaydi. `A · B = 6` dan hech narsa kelib chiqmaydi!

### 5.4 Cho'ntak formulalari

```
a² − b² = (a − b)(a + b)
a² ± 2ab + b² = (a ± b)²
a³ − b³ = (a − b)(a² + ab + b²)
a³ + b³ = (a + b)(a² − ab + b²)
ax² + bx + c = a(x − x₁)(x − x₂)      ← D ≥ 0 bo'lganda
```

---

## 6. Ratsional tenglamalar

Maxrajda x bor. **Algoritm:**

```
1. ODZ yoz:  har bir maxraj ≠ 0
2. Umumiy maxrajga keltir yoki krest-nakrest ko'paytir
3. Hosil bo'lgan tenglamani yech
4. ODZ ga tushmaydigan ildizlarni TASHLAB YUBOR
```

**Misol (klassik tuzoq):**

```
1/(x−1) + 1/(x+1) = 2/(x²−1)

ODZ:  x ≠ 1,  x ≠ −1     (chunki x² − 1 = (x−1)(x+1))

Chap tomonni yig'amiz:
    (x+1) + (x−1)         2x
    ───────────────  =  ───────
    (x−1)(x+1)           x² − 1

Demak:   2x/(x²−1) = 2/(x²−1)   →   2x = 2   →   x = 1

LEKIN x = 1 ∉ ODZ  ❌

Javob: S = ∅
```

> Bu misol nima uchun ODZ ni **boshida** yozish kerakligini ko'rsatadi.

---

## 7. Irratsional tenglamalar

Ildiz ostida x bor.

### 7.1 Asosiy sxema

```
√(f(x)) = g(x)

  ⟺   ⎧ g(x) ≥ 0            ← ildiz manfiy bo'la olmaydi!
      ⎩ f(x) = g(x)²         ← (bu avtomatik f(x) ≥ 0 ni beradi)
```

> `f(x) ≥ 0` ni alohida yozish shart emas: agar `f(x) = g(x)²` bo'lsa, u allaqachon ≥ 0.
> Lekin `g(x) ≥ 0` **majburiy**.

**Misol:**

```
√(x + 5) = x − 1

Shart:  x − 1 ≥ 0  →  x ≥ 1

Kvadratga:  x + 5 = (x − 1)²
            x + 5 = x² − 2x + 1
            x² − 3x − 4 = 0
            (x − 4)(x + 1) = 0
            x = 4  yoki  x = −1

x = −1:  shart x ≥ 1 buzilgan  ❌
x = 4:   √9 = 3 = 4 − 1  ✓

Javob: {4}
```

### 7.2 Ikkita ildiz bo'lsa

Bittasini bir tomonga ajrat, kvadratga ko'tar, keyin qolganini ajratib yana kvadratga
ko'tar. Har qadamda shartlarni yozib bor.

---

## 8. Modulli tenglamalar

### 8.1 Modul nima

```
        ⎧  x,   agar x ≥ 0
|x| =   ⎨
        ⎩ −x,   agar x < 0
```

**Geometrik ma'no:** `|x|` — bu x dan 0 gacha bo'lgan **masofa**.
Umumiy holda: `|a − b|` — a va b orasidagi masofa.

> 🔗 Bu "masofa" talqini keyinchalik **norm** tushunchasiga aylanadi:
> `‖v‖` — vektorning uzunligi. `|x|` — bu 1 o'lchovli norm. L1 regularizatsiya
> (`Lasso`) to'g'ridan-to'g'ri shundan.

### 8.2 Muhim xossalar

```
|x| ≥ 0                       har doim
|x| = 0  ⟺  x = 0
|−x| = |x|
|x·y| = |x|·|y|
|x/y| = |x|/|y|               (y ≠ 0)
√(x²) = |x|                   ⚠️ x EMAS!
|x + y| ≤ |x| + |y|           ← uchburchak tengsizligi
```

### 8.3 Yechish usullari

**Usul A — `|f(x)| = a` (a — son):**

```
a < 0  →  yechim yo'q
a = 0  →  f(x) = 0
a > 0  →  f(x) = a  yoki  f(x) = −a
```

**Misol:** `|2x − 3| = 5` → `2x − 3 = 5` (x = 4) yoki `2x − 3 = −5` (x = −1)

**Usul B — `|f(x)| = g(x)` (o'ng tomonda ham x bor):**

```
⎧ g(x) ≥ 0
⎩ f(x) = g(x)  yoki  f(x) = −g(x)
```

**Misol:**

```
|x − 1| = 2x + 3

Shart:  2x + 3 ≥ 0  →  x ≥ −1.5

1)  x − 1 = 2x + 3   →  −4 = x   →  x = −4  ❌ (shartni buzadi)
2)  x − 1 = −(2x+3)  →  x − 1 = −2x − 3  →  3x = −2  →  x = −2/3  ✓

Tekshir:  |−2/3 − 1| = 5/3;   2(−2/3) + 3 = 5/3  ✓

Javob: {−2/3}
```

**Usul C — intervallar bo'yicha (bir nechta modul bo'lganda):**

Modul ichidagi ifodalar nolga aylanadigan nuqtalarni top, son o'qini bo'laklarga ajrat,
har bo'lakda modullarni och.

---

## 9. Tengsizliklar: asosiy xossalar

### 9.1 To'rtta belgi

```
a < b    a kichik b dan            (qat'iy)
a ≤ b    a kichik yoki teng        (qat'iy emas)
a > b    a katta b dan             (qat'iy)
a ≥ b    a katta yoki teng         (qat'iy emas)
```

### 9.2 Xossalar jadvali ⭐

| # | Xossa | Belgi |
|---|-------|-------|
| 1 | `a < b  ⟹  a + c < b + c` | **o'zgarmaydi** |
| 2 | `a < b`, `c > 0  ⟹  ac < bc` | **o'zgarmaydi** |
| 3 | `a < b`, `c < 0  ⟹  ac > bc` | 🔴 **ALMASHADI** |
| 4 | `a < b`, `b < c  ⟹  a < c` | tranzitivlik |
| 5 | `a < b`, `c < d  ⟹  a + c < b + d` | qo'shish mumkin |
| 6 | `0 < a < b  ⟹  1/a > 1/b` | 🔴 **ALMASHADI** |
| 7 | `0 ≤ a < b  ⟹  a² < b²` | faqat manfiy bo'lmaganda! |

> ⚠️ **5-xossaning teskarisi YO'Q:** tengsizliklarni **ayirib bo'lmaydi**.
> `3 < 5` va `1 < 10` dan `3 − 1 < 5 − 10` kelib chiqmaydi (2 < −5 — yolg'on).

### 9.3 Nima uchun manfiy songa ko'paytirganda belgi almashadi

Bu "qoida" emas, buni **tushunish** kerak:

```
Son o'qida:      −5 ────── −2 ────── 0 ────── 2 ────── 5
                 ←──────── chapga kichik, o'ngga katta ────────→

2 < 5  to'g'ri.
Endi (−1) ga ko'paytiramiz:  −2  va  −5

Ko'paytirish barcha nuqtalarni 0 ga nisbatan AKS ETTIRADI (aynadi).
Aks etgandan keyin "chap/o'ng" almashadi  →  −2 > −5
```

Bo'sh qog'ozga son o'qini chizib, o'zingga bir marta tushuntir. Shundan keyin
hech qachon unutmaysan.

### 9.4 Interval yozuvi

| Yozuv | Ma'nosi | Son o'qida |
|-------|---------|------------|
| `(a, b)` | a < x < b | uchlari **ochiq** ○ |
| `[a, b]` | a ≤ x ≤ b | uchlari **yopiq** ● |
| `[a, b)` | a ≤ x < b | aralash |
| `(−∞, a)` | x < a | ∞ doim ochiq |
| `A ∪ B` | birlashma ("yoki") | |
| `A ∩ B` | kesishma ("va") | |

---

## 10. Chiziqli va kvadrat tengsizliklar

### 10.1 Chiziqli

```
−3x + 5 > 11
     −3x > 6
       x < −2        ← (−3) ga bo'ldik, belgi ALMASHDI

Javob:  x ∈ (−∞, −2)
```

**Tekshirish odati:** javobdan bitta son ol (masalan x = −3) va asl tengsizlikka qo'y:
`−3(−3) + 5 = 14 > 11` ✓. Chegaradan tashqaridan ham ol (x = 0): `5 > 11` ❌ — to'g'ri.

### 10.2 Qo'sh tengsizlik

```
2 ≤ 3x − 4 < 11        | hamma tomonga +4
6 ≤ 3x < 15            | hamma tomonni :3  (3 > 0, belgi o'zgarmaydi)
2 ≤ x < 5

Javob:  x ∈ [2, 5)
```

### 10.3 Kvadrat tengsizliklar — parabola usuli ⭐

```
ax² + bx + c  >  0   (yoki <, ≥, ≤)
```

**Algoritm:**

```
1. Nollarni top:  ax² + bx + c = 0  →  x₁, x₂
2. Parabolani chiz:   a > 0 → shoxlari YUQORIGA  ∪
                      a < 0 → shoxlari PASTGA    ∩
3. Grafikdan o'qi:  qayerda grafik x o'qidan yuqorida / pastda
```

**Misol:** `x² − x − 6 ≤ 0`

```
Nollar:  x² − x − 6 = 0  →  (x − 3)(x + 2) = 0  →  x = −2,  x = 3
a = 1 > 0  →  shoxlari yuqoriga

        ╲                    ╱
         ╲                  ╱
  ────────●────────────────●────────  x
         −2       ⌄        3
              (bu yerda ≤ 0)

Javob:  x ∈ [−2, 3]
```

**Yod olish uchun qoida (a > 0 bo'lganda):**

```
ax² + bx + c < 0   →   ildizlar ORASIDA        (−2, 3)
ax² + bx + c > 0   →   ildizlardan TASHQARIDA  (−∞,−2) ∪ (3,+∞)
```

### 10.4 D < 0 bo'lgan holat

```
x² + 4x + 5 > 0
D = 16 − 20 = −4 < 0   →  ildiz yo'q, parabola x o'qini kesmaydi
a = 1 > 0              →  parabola BUTUNLAY x o'qidan yuqorida

Javob:  x ∈ ℝ  (barcha haqiqiy sonlar)
```

Agar shu misolda `< 0` so'ralsa — javob `∅`.

> 🔗 **AI bog'liqlik:** `ax² + bx + c > 0` barcha x uchun bajarilishi (D < 0, a > 0)
> matritsalarda **musbat aniqlik** (positive definite) tushunchasiga aylanadi.
> Bu esa optimizatsiyada "bu nuqta minimum" degan xulosani beradi.

---

## 11. Interval usuli (ratsional tengsizliklar)

Bu — eng kuchli texnika. **Har doim shu tartibda:**

```
1. Hammasini CHAP tomonga yig'  →  P(x)/Q(x) ▽ 0   (o'ng tomonda 0 bo'lsin!)
2. Bitta kasr qilib yig'
3. Surat va maxrajni ko'paytuvchilarga ajrat
4. KRITIK NUQTALAR: surat = 0 (● to'ldirilgan, agar ≤/≥) 
                    maxraj = 0 (○ doim ochiq!)
5. Nuqtalarni son o'qiga qo'y, oraliqlarda ishorani aniqla
6. Kerakli ishorali oraliqlarni yoz
```

> 🔴 **ENG KATTA XATO:** `(x−1)/(x+2) ≥ 0` da krest-nakrest ko'paytirish.
> `x + 2` musbatmi yoki manfiymi — **bilmaysan**! Agar manfiy bo'lsa, belgi almashadi.
> Ratsional tengsizlikda **hech qachon** maxrajga ko'paytirma.

### Misol 1

```
(x − 1)/(x + 2) ≥ 0

Kritik nuqtalar:  x = 1  (surat = 0, ≥ bo'lgani uchun ●)
                  x = −2 (maxraj = 0, DOIM ○)

Ishoralarni tekshiramiz (har oraliqdan bitta son olib):

          −2              1
  ────────○───────────────●────────  x
     x=−3       x=0          x=2
   (−4)/(−1)   (−1)/(2)    (1)/(4)
     = +4        = −0.5      = +0.25
      +            −            +

Javob:  x ∈ (−∞, −2) ∪ [1, +∞)
```

### Misol 2 — juft karrali ko'paytuvchi

```
(x − 1)(x + 3) / (x − 2)² < 0

(x − 2)² > 0  har doim (x ≠ 2 bo'lsa) → maxraj ishoraga TA'SIR QILMAYDI

Demak kerak:  (x − 1)(x + 3) < 0   →   −3 < x < 1
x ≠ 2 sharti avtomatik bajariladi (2 ∉ (−3, 1))

Javob:  x ∈ (−3, 1)
```

**Umumiy qoida:** ko'paytuvchi **toq** darajada bo'lsa — nuqtadan o'tganda ishora
**almashadi**; **juft** darajada bo'lsa — **almashmaydi**.

---

## 12. Modulli tengsizliklar

### 12.1 Ikkita asosiy shakl (yodla)

```
|x| < a   (a > 0)   ⟺   −a < x < a          ⟺   x ∈ (−a, a)
|x| > a   (a > 0)   ⟺   x < −a  YOKI  x > a  ⟺   x ∈ (−∞,−a) ∪ (a,+∞)
```

**Geometrik ravshanlik:**

```
|x| < 3  →  "0 dan masofa 3 dan kichik"  →  ichkarida
       ───────(───────0───────)───────
              −3              3

|x| > 3  →  "0 dan masofa 3 dan katta"   →  tashqarida
       ◄──────)───────0───────(──────►
              −3              3
```

Buni "<" → **ichkarida** (bitta interval), ">" → **tashqarida** (ikkita interval) deb
eslab qol.

### 12.2 Misollar

```
|x − 4| < 3
⟺  −3 < x − 4 < 3
⟺   1 < x < 7
Javob: (1, 7)

Ma'nosi: "x, 4 dan 3 birlikdan yaqin"  ← masofa talqini!
```

```
|2x + 1| ≥ 5
⟺  2x + 1 ≥ 5   yoki   2x + 1 ≤ −5
⟺  2x ≥ 4       yoki   2x ≤ −6
⟺  x ≥ 2        yoki   x ≤ −3
Javob: (−∞, −3] ∪ [2, +∞)
```

> ⚠️ `a < 0` bo'lganda: `|x| < −2` → yechim yo'q (∅).  `|x| > −2` → barcha x (ℝ).
> Bu holatlarni tekshirishni unutma.

---

## 13. AI uchun muhim tengsizliklar

Bu bo'lim maktab dasturidan tashqarida, lekin **aynan shular** machine learning
isbotlarida uchraydi. Hozir tanishib qo'y — keyin uchratganda "bilaman" deysan.

### 13.1 Uchburchak tengsizligi (triangle inequality)

```
|a + b| ≤ |a| + |b|
```

**Ma'nosi:** to'g'ri yo'l — eng qisqa yo'l.

Vektorlar uchun: `‖u + v‖ ≤ ‖u‖ + ‖v‖`

> 🔗 Bu **metrika** (distance) ta'rifining 3 ta shartidan biri. Embedding'lar orasidagi
> masofa, k-NN, clustering — hammasi shu shartga tayanadi.

### 13.2 O'rta arifmetik–o'rta geometrik (AM–GM)

```
a, b ≥ 0  uchun:      (a + b)/2  ≥  √(ab)
```

**Isbot (bir qatorda):**

```
(√a − √b)² ≥ 0
a − 2√(ab) + b ≥ 0
a + b ≥ 2√(ab)
(a + b)/2 ≥ √(ab)        ✓  (tenglik faqat a = b da)
```

**Eng mashhur natija:**  `x > 0` uchun  `x + 1/x ≥ 2`

```
AM–GM:  (x + 1/x)/2 ≥ √(x · 1/x) = 1   →   x + 1/x ≥ 2
```

### 13.3 Koshi–Bunyakovskiy–Shvarts (Cauchy–Schwarz) ⭐⭐

```
(a₁b₁ + a₂b₂ + ... + aₙbₙ)²  ≤  (a₁² + ... + aₙ²)(b₁² + ... + bₙ²)
```

Vektor tilida:  `|u · v| ≤ ‖u‖ · ‖v‖`

> 🔗🔗 **Bu tengsizlik nima uchun `cosine similarity` doim [−1, 1] oralig'ida
> bo'lishini tushuntiradi:**
>
> ```
> cos(θ) = (u · v) / (‖u‖ · ‖v‖)
>
> Cauchy–Schwarz:  |u · v| ≤ ‖u‖·‖v‖
>          demak:  |cos(θ)| ≤ 1
>          demak:  −1 ≤ cos(θ) ≤ 1     ✓
> ```
>
> Har safar embedding'lar o'xshashligini hisoblaganingda — sen shu tengsizlikdan
> foydalanyapsan. Bu o'zbek maktab algebrasidan LLM'gacha bo'lgan **eng qisqa ko'prik**.

### 13.4 Bernulli tengsizligi

```
x ≥ −1,  n ≥ 1  uchun:     (1 + x)ⁿ ≥ 1 + nx
```

Yaqinlashish tahlillarida, learning rate baholarida ishlatiladi.

### 13.5 Yensen tengsizligi (Jensen) — tanishuv uchun

Agar `f` **qavariq** (convex) funksiya bo'lsa:

```
f( E[X] )  ≤  E[ f(X) ]
```

> 🔗 Bu tengsizlik **ELBO** (variational inference), **KL divergence ≥ 0**,
> **EM algoritmi** ning asosi. Hozir isbotlash shart emas — shaklini eslab qol.

### 13.6 Xulosa jadval

| Tengsizlik | AI'dagi joyi |
|------------|--------------|
| Uchburchak | Metrika, embedding masofalari, gradient norm chegaralari |
| AM–GM | Optimizatsiya, chegaralarni baholash |
| Cauchy–Schwarz | **Cosine similarity ∈ [−1,1]**, attention scorelari |
| Bernulli | Yaqinlashish tezligi, learning rate |
| Jensen | KL divergence, ELBO, VAE, EM |

---

## 14. Xatolar muzeyi

Bu xatolarni **hamma** qiladi. Oldindan bilsang — qilmaysan.

| # | Xato | To'g'risi |
|---|------|-----------|
| 1 | `−3x > 6  →  x > −2` | 🔴 `x < −2` — manfiyga bo'lganda belgi almashadi |
| 2 | `x² = 5x  →  x = 5` | 🔴 x ga bo'lma! `x(x−5)=0` → `{0, 5}` |
| 3 | `√(x²) = x` | 🔴 `√(x²) = \|x\|` |
| 4 | Ratsional tengsizlikda maxrajga ko'paytirish | 🔴 Interval usulini ishlat |
| 5 | ODZ ni yozmaslik | 🔴 Yechishdan **oldin** yoz |
| 6 | Kvadratga ko'tarib tekshirmaslik | 🔴 Begona ildiz paydo bo'ladi |
| 7 | `(a + b)² = a² + b²` | 🔴 `= a² + 2ab + b²` |
| 8 | Maxrajda ● (to'ldirilgan nuqta) qo'yish | 🔴 Maxraj noli **doim** ○ ochiq |
| 9 | `\|x\| > −2` → "yechim yo'q" | 🔴 Barcha x, chunki modul doim ≥ 0 |
| 10 | Parametrli tenglamada `a = 0` ni ko'rmaslik | 🔴 Har doim holatlarga bo'l |
| 11 | `1/a > 1/b` ni `a < b` dan chiqarish | 🔴 Faqat a, b **bir xil ishorali** bo'lsa |
| 12 | Tengsizliklarni ayirish | 🔴 Faqat **qo'shish** mumkin |

---

## 📌 Bir sahifalik xulosa

```
TENGLAMA:
  ODZ yoz  →  soddalashtir  →  yech  →  TEKSHIR
  Xavfli: ×o'zgaruvchi, ÷o'zgaruvchi, ()², √

CHIZIQLI:      ax + b = 0    →  a≠0: x=−b/a | a=0,b=0: ℝ | a=0,b≠0: ∅
SISTEMA:       kesishish | parallel | ustma-ust  →  1 | 0 | ∞ yechim
KVADRAT:       x = (−b ± √D)/2a,   D = b² − 4ac
VIYET:         x₁+x₂ = −b/a,   x₁x₂ = c/a
MODUL:         √(x²) = |x|,   |x|<a ⟺ −a<x<a,   |x|>a ⟺ tashqarida

TENGSIZLIK:
  🔴 Manfiyga ×/÷  →  BELGI ALMASHADI
  Kvadrat:   a>0 & <0  →  ildizlar orasida
             a>0 & >0  →  ildizlardan tashqarida
  Ratsional: hammasini chapga → 0, interval usuli, maxraj ○

AI UCHUN:      |a+b| ≤ |a|+|b|  |  (a+b)/2 ≥ √(ab)  |  |u·v| ≤ ‖u‖‖v‖
```

---

**Keyingi qadam:** [02-masalalar-uz.md](02-masalalar-uz.md) — qog'oz va qalam ol.
