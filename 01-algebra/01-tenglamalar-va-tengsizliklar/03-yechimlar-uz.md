# Yechimlar — Tenglamalar va Tengsizliklar

> ⛔ **Agar sen masalani hali o'zing yechmagan bo'lsang — bu faylni yop.**
>
> Yechimni o'qish sizga "tushundim" hissini beradi, lekin bilim bermaydi. Bu his —
> aldov. Batafsil: [`../../00-mindset/01-ai-bilan-organish-uz.md`](../../00-mindset/01-ai-bilan-organish-uz.md)
>
> **Qanday ishlatish:** o'z yechimingni yonma-yon qo'yib solishtir. Javob to'g'ri, lekin
> yo'l boshqacha bo'lsa — bu normal. Javob noto'g'ri bo'lsa — `xatolar-daftari.md` ga yoz.

---

## A. Chiziqli tenglamalar

### A1 — `3x − 7 = 5x + 9`

```
3x − 7 = 5x + 9
3x − 5x = 9 + 7
−2x = 16
x = −8
```

**Tekshirish:** chap = 3(−8) − 7 = −31;  o'ng = 5(−8) + 9 = −31 ✓

**Javob:** `S = {−8}`

---

### A2 — `(2x − 1)/3 − (x + 2)/4 = 1`

Umumiy maxraj: 12.

```
12 · [(2x−1)/3] − 12 · [(x+2)/4] = 12 · 1
4(2x − 1) − 3(x + 2) = 12
8x − 4 − 3x − 6 = 12
5x − 10 = 12
5x = 22
x = 22/5
```

**Tekshirish:** (2·4.4 − 1)/3 − (4.4 + 2)/4 = 7.8/3 − 6.4/4 = 2.6 − 1.6 = 1 ✓

**Javob:** `S = {22/5}` (= 4.4)

---

### A3 — `5(x − 3) − 2x = 3x − 15`

```
5x − 15 − 2x = 3x − 15
3x − 15 = 3x − 15
3x − 3x = −15 + 15
0 = 0            ← AYNIYAT
```

**Javob:** `S = ℝ` — **barcha** haqiqiy sonlar yechim.

> Bu `ax + b = 0` ning `a = 0, b = 0` holati. Chiziqli algebrada bu
> **cheksiz ko'p yechim** (underdetermined system) deb ataladi.

---

### A4 — `4(x + 1) − 3 = 4x + 2`

```
4x + 4 − 3 = 4x + 2
4x + 1 = 4x + 2
4x − 4x = 2 − 1
0 = 1            ← YOLG'ON
```

**Javob:** `S = ∅` — yechim yo'q.

> Bu `a = 0, b ≠ 0` holati. Sistemalarda bu **inconsistent** (nomuvofiq) deb ataladi.
> A3 va A4 ni yonma-yon qo'y: tashqi ko'rinishi bir xil, natija tamoman boshqacha.

---

### A5 — `(a − 2)x = a² − 4`

⚠️ Vasvasaga tushma: `(a − 2)` ga bo'lmoqchi bo'lasan. Lekin u **nolga teng bo'lishi
mumkin**. Shuning uchun holatlarga ajratamiz.

Avval o'ng tomonni ajratamiz: `a² − 4 = (a − 2)(a + 2)`

```
(a − 2)x = (a − 2)(a + 2)
```

**1-holat: a ≠ 2** → `(a − 2) ≠ 0`, bo'lish mumkin:

```
x = a + 2
```

**2-holat: a = 2** → tenglama shunday bo'ladi:

```
0 · x = 0     →     har qanday x to'g'ri
```

**Javob:**

```
a ≠ 2   →   S = {a + 2}
a = 2   →   S = ℝ
```

---

### A6 — `(m² − 9)x = m − 3`

```
(m − 3)(m + 3) · x = m − 3
```

**1-holat: m ≠ 3 va m ≠ −3** → koeffitsient ≠ 0:

```
x = (m − 3) / [(m − 3)(m + 3)] = 1 / (m + 3)
```

**2-holat: m = 3** → `0 · x = 0` → `S = ℝ`

**3-holat: m = −3** → `0 · x = −3 − 3 = −6` → `0 = −6` yolg'on → `S = ∅`

**Javob:**

```
m ≠ ±3   →   S = { 1/(m + 3) }
m = 3    →   S = ℝ
m = −3   →   S = ∅
```

> Uchta holat — aynan `ax + b = 0` ning uchta holati. Bu tasodif emas, bu **struktura**.

---

## B. Kvadrat tenglamalar

### B1 — `x² − 5x + 6 = 0`

**(a) Ko'paytuvchilarga ajratish.** Yig'indisi 5, ko'paytmasi 6 bo'lgan sonlar: 2 va 3.

```
x² − 5x + 6 = (x − 2)(x − 3) = 0
x = 2   yoki   x = 3
```

**(b) Formula bilan.**

```
D = b² − 4ac = 25 − 24 = 1
x = (5 ± √1) / 2 = (5 ± 1)/2
x₁ = 3,   x₂ = 2
```

**Javob:** `S = {2, 3}`

---

### B2 — `2x² + 3x − 2 = 0`

```
a = 2,  b = 3,  c = −2
D = 3² − 4·2·(−2) = 9 + 16 = 25
√D = 5

x = (−3 ± 5) / (2·2) = (−3 ± 5)/4

x₁ = 2/4  = 1/2
x₂ = −8/4 = −2
```

**Tekshirish (x = 1/2):** 2(1/4) + 3(1/2) − 2 = 0.5 + 1.5 − 2 = 0 ✓

**Javob:** `S = {−2, 1/2}`

---

### B3 — `x² + 6x + 2 = 0` (to'la kvadratga to'ldirish)

```
x² + 6x + 2 = 0
x² + 6x = −2                      | x ning koeffitsienti 6, yarmi 3, kvadrati 9
x² + 6x + 9 = −2 + 9              | ikkala tomonga 9 qo'shamiz
(x + 3)² = 7                      | chap tomon to'la kvadrat
x + 3 = ±√7                       | ± ni UNUTMA
x = −3 ± √7
```

**Tekshirish (formula bilan):** `D = 36 − 8 = 28`, `√28 = 2√7`,
`x = (−6 ± 2√7)/2 = −3 ± √7` ✓

**Javob:** `S = {−3 − √7, −3 + √7} ≈ {−5.646, −0.354}`

> Bu usul keyinchalik Gauss taqsimoti, ridge regression va Kalman filterda
> aynan shu ko'rinishda qaytadi. Formuladan muhimroq.

---

### B4 — `3x² − 12 = 0`

```
3x² = 12
x² = 4
x = ±2          ← ± ni UNUTMA (√ olishda ildiz yo'qoladi)
```

**Javob:** `S = {−2, 2}`

---

### B5 — `x² − 7x + 12 = 0`, `x₁² + x₂²` ni top

Viyet teoremasi:

```
x₁ + x₂ = −b/a = 7
x₁ · x₂ =  c/a = 12
```

Ayniyat:

```
(x₁ + x₂)² = x₁² + 2x₁x₂ + x₂²
      ⟹    x₁² + x₂² = (x₁ + x₂)² − 2x₁x₂
```

Qo'yamiz:

```
x₁² + x₂² = 7² − 2·12 = 49 − 24 = 25
```

**Tekshirish:** ildizlar 3 va 4 → 9 + 16 = 25 ✓

**Javob:** `25`

---

### B6 — `x² − 2mx + (m + 2) = 0` aynan bitta ildizga ega

"Aynan bitta ildiz" ⟺ `D = 0`.

```
a = 1,  b = −2m,  c = m + 2

D = (−2m)² − 4·1·(m + 2)
  = 4m² − 4m − 8
  = 0

4(m² − m − 2) = 0
m² − m − 2 = 0
(m − 2)(m + 1) = 0
m = 2   yoki   m = −1
```

**Tekshirish:**

```
m = 2:   x² − 4x + 4 = (x − 2)² = 0  →  x = 2   ✓ bitta ildiz
m = −1:  x² + 2x + 1 = (x + 1)² = 0  →  x = −1  ✓ bitta ildiz
```

**Javob:** `m ∈ {−1, 2}`

---

### B7 — `x⁴ − 5x² + 4 = 0`

Almashtirish: `t = x²`, bunda **`t ≥ 0`** (bu shartni unutma!).

```
t² − 5t + 4 = 0
(t − 1)(t − 4) = 0
t = 1   yoki   t = 4        ← ikkalasi ham ≥ 0, ikkalasi ham yaroqli

t = 1  →  x² = 1  →  x = ±1
t = 4  →  x² = 4  →  x = ±2
```

**Javob:** `S = {−2, −1, 1, 2}`

> Agar `t` manfiy chiqsa, o'sha yechim **tashlab yuboriladi** — chunki `x² ≥ 0`.

---

## C. Ratsional, irratsional va modulli tenglamalar

### C1 — `(x + 1)/(x − 2) = 3`

```
ODZ:  x − 2 ≠ 0   →   x ≠ 2

x + 1 = 3(x − 2)
x + 1 = 3x − 6
1 + 6 = 3x − x
7 = 2x
x = 7/2 = 3.5      ← ODZ ga tushadi ✓
```

**Tekshirish:** (3.5 + 1)/(3.5 − 2) = 4.5/1.5 = 3 ✓

**Javob:** `S = {7/2}`

---

### C2 — `1/(x − 1) + 1/(x + 1) = 2/(x² − 1)`

```
ODZ:  x² − 1 = (x−1)(x+1) ≠ 0   →   x ≠ 1  va  x ≠ −1
```

Chap tomonni umumiy maxrajga keltiramiz:

```
   1        1       (x + 1) + (x − 1)        2x
───────  +  ─────  = ─────────────────  =  ───────
 x − 1      x + 1     (x − 1)(x + 1)        x² − 1
```

Demak:

```
  2x        2
───────  = ───────        | maxrajlar bir xil, suratlarni tenglaymiz
x² − 1     x² − 1

2x = 2
x = 1
```

🔴 Lekin `x = 1` **ODZ ga tushmaydi**!

**Javob:** `S = ∅`

> Bu masala ODZ ni nima uchun **boshida** yozish kerakligining eng yaxshi dalili.
> ODZ yozmagan odam `{1}` deb javob beradi — va noto'g'ri bo'ladi.

---

### C3 — `x/(x − 3) − 2 = 3/(x − 3)`

```
ODZ:  x ≠ 3

Ikkala tomonni (x − 3) ga ko'paytiramiz:
x − 2(x − 3) = 3
x − 2x + 6 = 3
−x = −3
x = 3
```

🔴 `x = 3` ∉ ODZ.

**Javob:** `S = ∅`

---

### C4 — `√(x + 5) = x − 1`

```
Shart:  o'ng tomon ≥ 0   →   x − 1 ≥ 0   →   x ≥ 1

Kvadratga ko'taramiz:
x + 5 = (x − 1)²
x + 5 = x² − 2x + 1
0 = x² − 3x − 4
(x − 4)(x + 1) = 0
x = 4   yoki   x = −1
```

Shartni tekshiramiz:

```
x = −1:  x ≥ 1 buzildi  ❌  (begona ildiz — kvadratga ko'tarish tufayli)
x = 4:   4 ≥ 1  ✓
```

**Tekshirish:** `√(4 + 5) = √9 = 3`;  `4 − 1 = 3` ✓

**Javob:** `S = {4}`

---

### C5 — `√(2x + 3) = x`

```
Shart:  x ≥ 0        (chap tomon — ildiz, u manfiy bo'la olmaydi)

2x + 3 = x²
x² − 2x − 3 = 0
(x − 3)(x + 1) = 0
x = 3   yoki   x = −1

x = −1:  x ≥ 0 buzildi  ❌
x = 3:   ✓
```

**Tekshirish:** `√(2·3 + 3) = √9 = 3` ✓

**Javob:** `S = {3}`

---

### C6 — `|2x − 3| = 5`

O'ng tomon `5 > 0` → ikkita holat:

```
1)  2x − 3 = 5    →  2x = 8   →  x = 4
2)  2x − 3 = −5   →  2x = −2  →  x = −1
```

**Tekshirish:** `|2·4 − 3| = |5| = 5` ✓;  `|2·(−1) − 3| = |−5| = 5` ✓

**Javob:** `S = {−1, 4}`

---

### C7 — `|x − 1| = 2x + 3`

O'ng tomonda x bor → **shart yozish majburiy**:

```
Shart:  2x + 3 ≥ 0   →   x ≥ −3/2
```

Ikkita holat:

```
1)  x − 1 = 2x + 3
    −1 − 3 = 2x − x
    x = −4          ❌  (−4 < −3/2, shartni buzadi)

2)  x − 1 = −(2x + 3)
    x − 1 = −2x − 3
    3x = −2
    x = −2/3        ✓  (−2/3 ≥ −3/2)
```

**Tekshirish:** chap = `|−2/3 − 1| = |−5/3| = 5/3`;
o'ng = `2(−2/3) + 3 = −4/3 + 9/3 = 5/3` ✓

**Javob:** `S = {−2/3}`

---

## D. Chiziqli tenglamalar sistemasi

### D1
```
⎧ 2x + y = 7
⎩ x − y = 2
```

**Usul 1 — o'rniga qo'yish:**

```
2-tenglamadan:  x = y + 2
1-ga qo'yamiz:  2(y + 2) + y = 7
                2y + 4 + y = 7
                3y = 3  →  y = 1
                x = 1 + 2 = 3
```

**Usul 2 — qo'shish:**

```
  2x + y = 7
+ x − y = 2
──────────────
  3x     = 9   →  x = 3
                  y = 7 − 2·3 = 1
```

**Tekshirish:** `2(3) + 1 = 7` ✓;  `3 − 1 = 2` ✓

**Javob:** `(x, y) = (3, 1)` — chiziqlar bitta nuqtada kesishadi.

---

### D2
```
⎧ 3x + 2y = 16
⎩ 5x − 2y = 0
```

`y` koeffitsientlari qarama-qarshi → to'g'ridan-to'g'ri qo'shamiz:

```
  3x + 2y = 16
+ 5x − 2y = 0
──────────────
  8x      = 16   →   x = 2

5(2) − 2y = 0  →  10 = 2y  →  y = 5
```

**Tekshirish:** `3(2) + 2(5) = 6 + 10 = 16` ✓

**Javob:** `(2, 5)`

---

### D3
```
⎧ x + 2y = 4
⎩ 2x + 4y = 9
```

1-tenglamani 2 ga ko'paytiramiz:

```
2x + 4y = 8
2x + 4y = 9
```

Chap tomonlar bir xil, o'ng tomonlar har xil → `8 = 9` kerak bo'ladi, bu yolg'on.

**Javob:** `S = ∅`

**Geometrik tushuntirish:** ikkala chiziqning burchak koeffitsienti bir xil
(`y = −x/2 + 2` va `y = −x/2 + 9/4`), lekin kesmalari har xil → **parallel chiziqlar**,
hech qachon kesishmaydi.

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

2-tenglama = 1-tenglama × 2. Ya'ni ular **bir xil chiziq**. Yangi ma'lumot yo'q.

Parametrlashtiramiz: `y = t` (t — istalgan haqiqiy son)

```
x + 2t = 4   →   x = 4 − 2t
```

**Javob:** `S = {(4 − 2t, t) : t ∈ ℝ}` — cheksiz ko'p yechim.

**Tekshirish (t = 0):** (4, 0) → `4 + 0 = 4` ✓, `8 + 0 = 8` ✓
**Tekshirish (t = 1):** (2, 1) → `2 + 2 = 4` ✓, `4 + 4 = 8` ✓

> 🔗 Bu holat — `rank(A) < noma'lumlar soni`. Neyron tarmoqlarda deyarli **har doim**
> shunday: parametrlar ma'lumotdan ko'p. Shuning uchun "qaysi yechimni tanlaymiz?"
> degan savol tug'iladi → **regularizatsiya** shu savolning javobi.

---

### D5
```
⎧ x + y + z = 6      (1)
⎨ 2x − y + z = 3     (2)
⎩ x + 2y − z = 2     (3)
```

`z` ni yo'qotamiz (uning koeffitsientlari +1, +1, −1):

```
(1) + (3):   (x + y + z) + (x + 2y − z) = 6 + 2
             2x + 3y = 8                              (4)

(2) + (3):   (2x − y + z) + (x + 2y − z) = 3 + 2
             3x + y = 5                               (5)
```

Endi 2 ta noma'lumli sistema:

```
(5) dan:  y = 5 − 3x
(4) ga:   2x + 3(5 − 3x) = 8
          2x + 15 − 9x = 8
          −7x = −7
          x = 1

y = 5 − 3(1) = 2
(1) dan:  z = 6 − x − y = 6 − 1 − 2 = 3
```

**Tekshirish:**

```
(1):  1 + 2 + 3 = 6   ✓
(2):  2 − 2 + 3 = 3   ✓
(3):  1 + 4 − 3 = 2   ✓
```

**Javob:** `(x, y, z) = (1, 2, 3)`

> Sen hozir **Gaussian elimination** qilding. Linear algebra'da xuddi shu narsani
> matritsa satrlari bilan yozasan.

---

## E. Tengsizliklar

### E1 — `−3x + 5 > 11`

```
−3x + 5 > 11
−3x > 6
x < −2              🔴 (−3) MANFIY → belgi ALMASHDI
```

**Tekshirish:** `x = −3` (javob ichidan): `−3(−3) + 5 = 14 > 11` ✓
`x = 0` (javobdan tashqari): `5 > 11` ❌ — to'g'ri, tashqarida.

**Javob:** `x ∈ (−∞, −2)`

---

### E2 — `2 ≤ 3x − 4 < 11`

```
2 ≤ 3x − 4 < 11         | hamma tomonga + 4
6 ≤ 3x < 15             | hamma tomonni : 3   (3 > 0 → belgi o'zgarmaydi)
2 ≤ x < 5
```

**Javob:** `x ∈ [2, 5)`

---

### E3 — `x² − x − 6 ≤ 0`

```
Nollar:  x² − x − 6 = 0
         (x − 3)(x + 2) = 0
         x = −2,  x = 3

a = 1 > 0  →  parabola shoxlari yuqoriga  ∪
"≤ 0" so'ralyapti → parabola x o'qidan PASTDA yoki unda
→ ildizlar ORASIDA
```

```
        ╲                    ╱
         ╲                  ╱
  ────────●────────────────●────────  x
         −2       ⌄        3
```

Uchlari **to'ldirilgan** (●), chunki `≤` (tenglik ruxsat).

**Javob:** `x ∈ [−2, 3]`

---

### E4 — `x² + 4x + 5 > 0`

```
D = 4² − 4·1·5 = 16 − 20 = −4 < 0   →  haqiqiy ildiz YO'Q
a = 1 > 0                            →  parabola shoxlari yuqoriga
```

Ildiz yo'q + shoxlari yuqoriga = parabola **butunlay x o'qidan yuqorida**.

Boshqacha ko'rish (to'la kvadrat): `x² + 4x + 5 = (x + 2)² + 1 ≥ 1 > 0` har doim.

**Javob:** `x ∈ ℝ`

> Agar `< 0` so'ralsa edi — javob `∅` bo'lardi.

---

### E5 — `−x² + 4x − 3 > 0`

Ikki yo'l bor. Ikkinchisi xavfsizroq:

**Yo'l 1 — (−1) ga ko'paytirish (belgi almashadi!):**

```
−x² + 4x − 3 > 0        | × (−1)  →  🔴 belgi ALMASHADI
x² − 4x + 3 < 0
(x − 1)(x − 3) < 0
a = 1 > 0, "< 0" → ildizlar ORASIDA
1 < x < 3
```

**Yo'l 2 — to'g'ridan-to'g'ri:**

```
Nollar: −x² + 4x − 3 = 0  →  x = 1, x = 3
a = −1 < 0  →  parabola shoxlari PASTGA  ∩
"> 0" → parabola x o'qidan yuqorida → ildizlar ORASIDA
```

```
              ╭────╮
             ╱      ╲
  ──────────○────────○──────────  x
            1        3
```

**Tekshirish:** `x = 2`: `−4 + 8 − 3 = 1 > 0` ✓

**Javob:** `x ∈ (1, 3)`

---

### E6 — `x² − 4x ≥ 0`

```
x(x − 4) ≥ 0
Nollar: x = 0,  x = 4
a = 1 > 0, "≥ 0" → ildizlardan TASHQARIDA (uchlari kiradi)
```

**Tekshirish:** `x = −1`: `1 + 4 = 5 ≥ 0` ✓;  `x = 2`: `4 − 8 = −4 ≥ 0` ❌ (to'g'ri, chiqarilgan)

**Javob:** `x ∈ (−∞, 0] ∪ [4, +∞)`

---

### E7 — `(x − 1)/(x + 2) ≥ 0`

⛔ Maxrajga ko'paytirish **taqiqlanadi** — `x + 2` ning ishorasi noma'lum.

**Interval usuli:**

```
Kritik nuqtalar:
   surat = 0:    x = 1     →  ● (to'ldirilgan, chunki ≥)
   maxraj = 0:   x = −2    →  ○ (DOIM ochiq)
```

Har oraliqdan bitta son olib ishorani tekshiramiz:

```
oraliq        sinov nuqta     qiymat             ishora
(−∞, −2)      x = −3          (−4)/(−1) = 4        +
(−2, 1)       x = 0           (−1)/(2) = −0.5      −
(1, +∞)       x = 2           (1)/(4) = 0.25       +
```

```
          −2              1
  ────────○───────────────●────────  x
     +          −              +
```

"≥ 0" kerak → `+` bo'lgan oraliqlar.

**Javob:** `x ∈ (−∞, −2) ∪ [1, +∞)`

> ⚠️ `x = −2` **hech qachon** kirmaydi, hatto `≥` bo'lsa ham — u yerda ifoda aniqlanmagan.

---

### E8 — `(x + 3)(x − 1)/(x − 2)² < 0`

**Asosiy kuzatish:** `(x − 2)² > 0` har doim (`x ≠ 2` bo'lganda). Ya'ni maxraj
**ishoraga ta'sir qilmaydi** — u har doim musbat.

Demak kasrning ishorasi = suratning ishorasi:

```
(x + 3)(x − 1) < 0
Nollar: x = −3,  x = 1
a > 0, "< 0" → ildizlar orasida
−3 < x < 1
```

`x ≠ 2` shartini tekshiramiz: `2 ∉ (−3, 1)` → shart avtomatik bajarilgan.

**Tekshirish:** `x = 0`: `(3)(−1)/4 = −0.75 < 0` ✓

**Javob:** `x ∈ (−3, 1)`

> **Umumiy qoida:** ko'paytuvchi **juft** darajada bo'lsa, u nuqtadan o'tganda ishora
> **almashmaydi**; **toq** darajada bo'lsa — almashadi.

---

### E9 — `(x − 2)/(x + 1) < 1`

🔴 **ENG KATTA XATO:** `x − 2 < x + 1` deb krest-nakrest ko'paytirish. Bu **noto'g'ri**,
chunki `x + 1` manfiy bo'lishi mumkin — u holda belgi almashadi.

**To'g'ri yo'l — hammasini chapga:**

```
(x − 2)/(x + 1) − 1 < 0

 (x − 2) − (x + 1)
─────────────────── < 0
      x + 1

 x − 2 − x − 1
───────────────  < 0
     x + 1

    −3
─────────  < 0
  x + 1
```

Surat `−3` — **doim manfiy**. Kasr manfiy bo'lishi uchun maxraj **musbat** bo'lishi kerak:

```
x + 1 > 0
x > −1
```

**Tekshirish:**

```
x = 0  (javob ichida):    (0−2)/(0+1) = −2 < 1  ✓
x = −2 (javobdan tashqari): (−2−2)/(−2+1) = (−4)/(−1) = 4 < 1?  YO'Q  ✓ to'g'ri chiqarilgan
```

**Javob:** `x ∈ (−1, +∞)`

> Agar krest-nakrest ko'paytirganingda `x < 3` degan **butunlay noto'g'ri** javob
> chiqardi. Bu xatoni bir marta qilib ko'r va daftaringga yoz.

---

### E10 — `|x − 4| < 3`

```
|x − 4| < 3
⟺  −3 < x − 4 < 3
⟺   1 < x < 7
```

**Masofa tilida:** "x son o'qida 4 dan 3 birlikdan kamroq uzoqlikda".

```
       ───────(───────●───────)───────
               1      4       7
```

**Javob:** `x ∈ (1, 7)`

---

### E11 — `|2x + 1| ≥ 5`

`|...| ≥ a` → **tashqarida** → ikkita holat, "yoki":

```
1)  2x + 1 ≥ 5    →  2x ≥ 4    →  x ≥ 2
2)  2x + 1 ≤ −5   →  2x ≤ −6   →  x ≤ −3
```

**Tekshirish:** `x = 2`: `|5| = 5 ≥ 5` ✓;  `x = 0`: `|1| = 1 ≥ 5` ❌ (to'g'ri, chiqarilgan)

**Javob:** `x ∈ (−∞, −3] ∪ [2, +∞)`

---

### E12 — Isbot: `x > 0` uchun `x + 1/x ≥ 2`

**Isbot 1 — to'g'ridan-to'g'ri (eng chiroyli):**

```
x + 1/x − 2 = (x² − 2x + 1)/x = (x − 1)² / x
```

`x > 0` → maxraj musbat;  `(x − 1)² ≥ 0` → surat manfiy emas.

```
⟹  (x − 1)²/x ≥ 0
⟹  x + 1/x − 2 ≥ 0
⟹  x + 1/x ≥ 2        ∎
```

**Isbot 2 — AM–GM orqali:**

```
a, b ≥ 0 uchun  (a + b)/2 ≥ √(ab)

a = x,  b = 1/x  olamiz:
(x + 1/x)/2 ≥ √(x · 1/x) = √1 = 1
x + 1/x ≥ 2            ∎
```

**Tenglik qachon?** `(x − 1)² = 0` ⟺ `x = 1`.
Tekshir: `1 + 1/1 = 2` ✓

**`x < 0` bo'lsa nima bo'ladi?** `x = −y` qo'yamiz (`y > 0`):

```
x + 1/x = −y − 1/y = −(y + 1/y) ≤ −2
```

Ya'ni manfiy x lar uchun tengsizlik **teskari**: `x + 1/x ≤ −2`.
Shuning uchun `x > 0` sharti majburiy.

---

## F. 🔗 AI bilan bog'liq masalalar

### F1 — Chiziqli regressiya

**(a) Yig'indilar.** Nuqtalar: (1,2), (2,3), (3,5)

```
n   = 3
Σx  = 1 + 2 + 3 = 6
Σx² = 1 + 4 + 9 = 14
Σy  = 2 + 3 + 5 = 10
Σxy = 1·2 + 2·3 + 3·5 = 2 + 6 + 15 = 23
```

**(b) Sistema va yechim.**

```
⎧ 14w + 6b = 23        (1)
⎩  6w + 3b = 10        (2)

(2) × 2:   12w + 6b = 20        (3)

(1) − (3): (14w − 12w) + (6b − 6b) = 23 − 20
           2w = 3
           w = 3/2 = 1.5

(2) ga:    6(1.5) + 3b = 10
           9 + 3b = 10
           3b = 1
           b = 1/3
```

**Javob:** `y = 1.5x + 1/3`

**(c) Qoldiqlar (residuals).**

```
x = 1:  bashorat = 1.5 + 1/3 = 11/6 ≈ 1.8333   qoldiq = 2 − 11/6 = +1/6
x = 2:  bashorat = 3.0 + 1/3 = 10/3 ≈ 3.3333   qoldiq = 3 − 10/3 = −1/3
x = 3:  bashorat = 4.5 + 1/3 = 29/6 ≈ 4.8333   qoldiq = 5 − 29/6 = +1/6

Yig'indi:  1/6 − 2/6 + 1/6 = 0
```

**Qoldiqlar yig'indisi = 0.** Bu tasodif emas! `b` bo'yicha hosila nolga tenglanganda
aynan shu shart chiqadi. Ya'ni:

```
∂S/∂b = 0   ⟺   Σ(qoldiqlar) = 0
∂S/∂w = 0   ⟺   Σ(qoldiq · xᵢ) = 0
```

Ikkinchisini ham tekshir: `(1/6)(1) + (−1/3)(2) + (1/6)(3) = 1/6 − 4/6 + 3/6 = 0` ✓

> **Sen hozir qo'lda model o'rgatding.** `sklearn.LinearRegression` xuddi shu ikkita
> tenglamani yechadi — faqat matritsa ko'rinishida: `XᵀX w = Xᵀy`.
> Bu "normal tenglamalar" deb ataladi va u **D bloki bilan bir xil narsa**.

---

### F2 — Gradient descent va learning rate

**(a) Rekursiya.**

```
f(x) = 3x²   →   f'(x) = 6x

x_{k+1} = x_k − η · 6x_k
        = x_k (1 − 6η)

Demak:  c = 1 − 6η
```

Ya'ni `x_k = (1 − 6η)^k · x₀` — **geometrik progressiya**.

**(b) Yaqinlashish sharti — TENGSIZLIK.**

```
|c| < 1
|1 − 6η| < 1
−1 < 1 − 6η < 1          | hamma tomondan 1 ayiramiz
−2 < −6η < 0             | (−6) ga bo'lamiz  →  🔴 BELGILAR ALMASHADI
 1/3 > η > 0

Javob:  0 < η < 1/3
```

**(c) η = 0.5 bo'lsa:**

```
c = 1 − 6(0.5) = 1 − 3 = −2      →  |c| = 2 > 1  →  UZOQLASHADI

x₀ = 1
x₁ = −2 · 1  = −2
x₂ = −2 · (−2) = 4
x₃ = −2 · 4  = −8
x₄ = −2 · (−8) = 16
```

Qiymatlar **o'sib boradi va ishorasi almashadi** — bu aynan training paytida
`loss = NaN` bo'lishining sababi. Model "portlaydi".

**(d) Umumiy holat.**

```
f(x) = (a/2)x²   →   f'(x) = ax
x_{k+1} = x_k(1 − ηa)

|1 − ηa| < 1
−1 < 1 − ηa < 1
−2 < −ηa < 0
0 < ηa < 2

Agar a > 0:      0 < η < 2/a        ✓
```

**Tekshirish:** bizda `f = 3x² = (6/2)x²` → `a = 6` → `0 < η < 2/6 = 1/3` ✓
(b) bandidagi javob bilan mos.

> `a` — bu funksiyaning **egriligi** (ikkinchi hosila). Ko'p o'lchovli holatda u
> Hessian matritsasining eng katta xos qiymati (`λ_max`) bo'ladi va shart
> `0 < η < 2/λ_max` ko'rinishini oladi. Bu — **deep learning'dagi eng muhim
> tengsizliklardan biri** va u to'liq shu mavzu doirasida isbotlanadi.

---

### F3 — Cosine similarity chegarasi

```
u = (3, 4),   v = (4, 3)
```

**(a)** `u · v = 3·4 + 4·3 = 12 + 12 = 24`

**(b)** `‖u‖ = √(9 + 16) = √25 = 5`;  `‖v‖ = √(16 + 9) = 5`

**(c)** `cos(θ) = 24 / (5 · 5) = 24/25 = 0.96`

**(d) Koshi–Shvarts:**

```
(u·v)²        = 24²      = 576
‖u‖² · ‖v‖²   = 25 · 25  = 625

576 ≤ 625   ✓
```

**(e) `cos(θ) = 1` qachon?**

Koshi–Shvartsda **tenglik** faqat vektorlar **kollinear** (bir chiziqda) bo'lganda:
`v = k·u`.

```
k > 0  →  bir yo'nalishda  →  cos θ = +1   (θ = 0°)
k < 0  →  qarama-qarshi    →  cos θ = −1   (θ = 180°)
```

Bizning misolda `v ≠ k·u` (chunki 4/3 ≠ 3/4), shuning uchun `cos θ = 0.96 < 1`.

> 🔗 **Shu sabab `cosine similarity` doim [−1, 1] oralig'ida bo'ladi.** Har safar
> embedding'lar o'xshashligini o'lchaganingda — Koshi–Shvarts tengsizligi kafolat beradi.

---

### F4 — ReLU tenglamasi

**(a)** `ReLU(2x − 6) = 4`

```
Natija 4 > 0  →  demak ReLU "o'chmagan", ya'ni 2x − 6 > 0 va ReLU(2x−6) = 2x − 6

2x − 6 = 4
2x = 10
x = 5

Tekshir:  2(5) − 6 = 4 > 0  ✓,  ReLU(4) = 4  ✓
```

**Javob:** `x = 5`

**(b)** `ReLU(2x − 6) = 0`

```
ReLU(z) = 0  ⟺  z ≤ 0

2x − 6 ≤ 0
2x ≤ 6
x ≤ 3
```

**Javob:** `x ∈ (−∞, 3]` — bu **cheksiz ko'p** yechim, chunki bu aslida tengsizlik.

> 🔗 Bu — "**dead ReLU**" muammosining matematikasi: neyron kirishi doim manfiy bo'lsa,
> chiqishi doim 0 bo'ladi, gradient ham 0 — neyron **o'lgan**.

**(c)** `ReLU(2x − 6) = −1` — **yechim yo'q**.
Sabab: `ReLU(z) = max(0, z) ≥ 0` har doim. Manfiy qiymat chiqmaydi.

**(d)** `ReLU(z) = (z + |z|)/2`

**Tekshirish:**

```
z = 5:    (5 + 5)/2 = 5      = max(0, 5)   ✓
z = −5:   (−5 + 5)/2 = 0     = max(0, −5)  ✓
z = 0:    (0 + 0)/2 = 0      = max(0, 0)   ✓
```

**Umumiy isbot:**

```
z ≥ 0  →  |z| = z   →  (z + z)/2 = z    = ReLU(z)  ✓
z < 0  →  |z| = −z  →  (z − z)/2 = 0    = ReLU(z)  ✓
```

> Shunga o'xshash: `max(a,b) = (a + b + |a − b|)/2`. Modul — bo'lakli funksiyalarni
> bitta formulaga yig'ish vositasi.

---

### F5 — Gradient clipping

```
g = (6, 8),   c = 4
```

**(a)** `‖g‖ = √(6² + 8²) = √(36 + 64) = √100 = 10`

**(b)** Clipping sharti: `‖g‖ > c` → `10 > 4` → **ha, ishga tushadi** ✓

**(c)** Kesilgan gradient:

```
g' = c · g / ‖g‖ = 4 · (6, 8) / 10 = (24/10, 32/10) = (2.4, 3.2)
```

**(d)** `‖g'‖ = √(2.4² + 3.2²) = √(5.76 + 10.24) = √16 = 4`

**Natija: `‖g'‖ = c` aynan.** Ya'ni clipping vektorning **uzunligini** `c` ga tenglaydi,
lekin **yo'nalishini saqlaydi**:

```
g'/‖g'‖ = (2.4, 3.2)/4 = (0.6, 0.8)
g /‖g‖  = (6, 8)/10    = (0.6, 0.8)      ← bir xil ✓
```

**(e) Umumiy isbot.**

```
1-holat: ‖g‖ ≤ c
   g' = g  →  ‖g'‖ = ‖g‖ ≤ c     ✓

2-holat: ‖g‖ > c
   g' = c·g/‖g‖

   Norm xossasi:  ‖k·v‖ = |k| · ‖v‖

   ‖g'‖ = ‖ (c/‖g‖) · g ‖ = |c/‖g‖| · ‖g‖

   c > 0 va ‖g‖ > 0  →  |c/‖g‖| = c/‖g‖

   ‖g'‖ = (c/‖g‖) · ‖g‖ = c      ✓

Har ikki holatda ham:  ‖g'‖ ≤ c    ∎
```

> 🔗 Nima uchun bu kerak? RNN va Transformer'larda gradient ba'zan portlaydi
> (`exploding gradients`). Clipping — bu **tengsizlik yordamida qo'yilgan qattiq chegara**.
> Butun mexanizm — shu bir necha qatorlik algebra.

---

## 🎓 Yakuniy eslatma

Agar bu fayldagi yechimlarni o'qib chiqding va "hammasi tushunarli" deb his qilsang —
**bu his aldov bo'lishi mumkin**.

Tekshirish usuli oddiy: faylni yop, bo'sh qog'oz ol va **E9** bilan **F2** ni
qaytadan yech. Agar qila olsang — bilasan. Qila olmasang — hali bilmaysan, va bu
mutlaqo normal. Ertaga qayta urin.
