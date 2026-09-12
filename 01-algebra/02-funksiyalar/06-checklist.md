# ✅ O'zingni tekshirish — Funksiyalar

> Bo'sh qog'ozga. Hech narsaga qaramay. 3-, 7-, 21-kunlarda qaytadan.

---

## 1-daraja: Ta'riflar (8)

- [ ] Funksiya nima? "Har bir x ga aynan bitta y" — nega **aynan bitta**?
- [ ] Domain va range farqi? Har biriga misol.
- [ ] Vertikal chiziq testi nima uchun ishlaydi?
- [ ] `k` (slope) ning ma'nosi bir jumlada?
- [ ] Juft va toq funksiya ta'rifi (formula bilan)?
- [ ] Kompozitsiya `f(g(x))` — qaysi funksiya birinchi qo'llanadi?
- [ ] Teskari funksiya qachon mavjud?
- [ ] Bo'lakli funksiya nima? AI'dan misol.

## 2-daraja: Chiqarish va isbot (7)

- [ ] `−b/2a` cho'qqi formulasini Viyet yoki to'la kvadrat orqali chiqar.
- [ ] `x² + 6x + 2` ni vertex form'ga keltir.
- [ ] `f(x) = 3x − 1` o'suvchi ekanini **ta'rifdan** isbotla.
- [ ] `(ax + b) ∘ (cx + d)` chiziqli ekanini isbotla. Bu neyron tarmoqda nima degani?
- [ ] `f(x) = (x + 1)/(x − 2)` ning teskarisini top.
- [ ] `σ(−x) = 1 − σ(x)` ni isbotla.
- [ ] `ReLU(x − 1) + ReLU(1 − x) = |x − 1|` ni isbotla.

## 3-daraja: Tezkor (12, har biri 30 soniya)

- [ ] `f(x) = x² − 1`, `f(−3) = ?` *(8)*
- [ ] `D(√(x − 4))` *([4, ∞))*
- [ ] `E(x² + 5)` *([5, ∞))*
- [ ] `E(1/(1 + x²))` *((0, 1])*
- [ ] `f(x − 3)` — qaysi tomonga? *(o'ngga 3)*
- [ ] `(1, 2)` va `(3, 8)` dan `k = ?` *(3)*
- [ ] `y = 2x + 1` ga perpendikulyar `k = ?` *(−1/2)*
- [ ] `x² − 4x + 1` cho'qqisining `x` i? *(2)*
- [ ] `x³ − x` juft, toq yoki hech qaysi? *(toq)*
- [ ] `f = x + 1`, `g = x²`: `f(g(3)) = ?` *(10)*; `g(f(3)) = ?` *(16)*
- [ ] `f(x) = 5x` ning teskarisi? *(x/5)*
- [ ] `ReLU(−7) = ?` *(0)*; `clip(5, −1, 1) = ?` *(1)*

## 4-daraja: Xato topish (5)

**Xato 1:**
```
f(x) = x² + 1,  f(x + 2) = x² + 1 + 2 = x² + 3
```
<details><summary>Javob</summary>
<code>x</code> o'rniga butun <code>(x+2)</code>: <code>f(x+2) = (x+2)² + 1 = x² + 4x + 5</code>
</details>

**Xato 2:**
```
y = (x + 3)² — bu x² ning 3 ga o'ngga siljigani
```
<details><summary>Javob</summary>
<b>Chapga</b> 3. <code>(x + 3)² = 0</code> → <code>x = −3</code>. Cho'qqi <code>(−3, 0)</code>.
</details>

**Xato 3:**
```
f(x) = 1/(x − 1),  f⁻¹(x) = x − 1
```
<details><summary>Javob</summary>
<code>f⁻¹ ≠ 1/f</code>. To'g'ri: <code>y = 1/(x−1)</code> → <code>x − 1 = 1/y</code> → <code>x = 1 + 1/y</code> → <code>f⁻¹(x) = 1 + 1/x</code>.
Tekshir: <code>f(2) = 1</code>, <code>f⁻¹(1) = 2</code> ✓
</details>

**Xato 4:**
```
f(x) = x² + x  juft, chunki x² juft
```
<details><summary>Javob</summary>
Ta'rifdan: <code>f(−x) = x² − x ≠ f(x)</code> va <code>≠ −f(x)</code>. <b>Hech qaysi.</b>
Bitta had juft bo'lishi yetarli emas — hammasi bo'lishi kerak.
</details>

**Xato 5:**
```
E(f) for f(x) = 1/(1 + x²) is [0, 1]
```
<details><summary>Javob</summary>
<code>(0, 1]</code>. <code>1/(1+x²) = 0</code> yechimsiz — 0 ga yetmaydi.
</details>

## 5-daraja: AI ulanishlar (6)

- [ ] Nima uchun aktivatsiyasiz chuqur tarmoq = bitta chiziqli funksiya?
- [ ] Sigmoid range (0,1) nima uchun ehtimollik uchun kerak?
- [ ] ReLU-tarmoq har doim qanday funksiya chiqaradi? Nega?
- [ ] `L(w) = Σ(wxᵢ − yᵢ)²` nima uchun parabola? Bu gradient descent uchun nima degani?
- [ ] Normalizatsiya `(x − μ)/σ` — §9 dagi qaysi almashtirishlar?
- [ ] Encoder/decoder — teskari funksiyalarmi? Aniq yoki taxminan?

---

## 🎯 Baho

| Bo'lim | Ball |
|--------|------|
| 1-daraja | ___ / 8 |
| 2-daraja | ___ / 7 |
| 3-daraja | ___ / 12 |
| 4-daraja | ___ / 5 |
| 5-daraja | ___ / 6 |
| **JAMI** | **___ / 38** |

34–38 ✅ keyingisiga · 28–33 🟡 1 kun · 20–27 🟠 nazariyani qayta · 0–19 🔴 +3 kun

## 📅 Takrorlash

- [ ] Tugagan kun  - [ ] +1  - [ ] +3  - [ ] +7  - [ ] +21  - [ ] 2 mavzudan keyin
