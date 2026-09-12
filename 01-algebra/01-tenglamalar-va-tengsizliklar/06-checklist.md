# ✅ O'zingni tekshirish / Self-Assessment Checklist

> **Qoida:** har bir savolga javobni **bo'sh qog'ozga** yoz. Hech narsaga qaramay.
> Faqat shundan keyin nazariyani ochib tekshir.
>
> Bu — 3-kun, 7-kun va 21-kunda takrorlanadigan fayl (spaced repetition).

---

## 1-daraja: Ta'riflar (bilaman / bilmayman)

Har birini **o'z so'zing bilan** tushuntir:

- [ ] Tenglama, ayniyat va yolg'on tenglik orasidagi farq nima?
- [ ] "Yechimlar to'plami" nima? Nega bu "javob" dan yaxshiroq so'z?
- [ ] ODZ (domain) nima? Uchta asosiy taqiqni ayt.
- [ ] "Ekvivalent almashtirish" nima?
- [ ] "Begona ildiz" (extraneous root) nima? Qanday paydo bo'ladi?
- [ ] Diskriminant nima va u nimani aytadi?
- [ ] `|x|` ning geometrik ma'nosi nima?
- [ ] Interval usuli qanday ishlaydi?

---

## 2-daraja: Formulalarni CHIQARISH (yodlash emas)

Bo'sh qog'ozga, formulalarga qaramay:

- [ ] `ax² + bx + c = 0` dan boshlab **kvadrat tenglama formulasini chiqar**
      (to'la kvadratga to'ldirish orqali, har bir qadam bilan)
- [ ] Viyet formulalarini chiqar (`x₁ + x₂` va `x₁x₂`)
- [ ] `x₁² + x₂²` ni Viyet orqali ifodala
- [ ] `(√a − √b)² ≥ 0` dan **AM–GM tengsizligini** chiqar
- [ ] `x + 1/x ≥ 2` (x > 0) ni isbotla
- [ ] `ReLU(z) = (z + |z|)/2` ekanini isbotla
- [ ] `f(x) = (a/2)x²` uchun gradient descent yaqinlashish shartini chiqar

---

## 3-daraja: Tezkor savollar (har biri 30 soniya)

- [ ] `−5x > 20` → javob? *(x < −4)*
- [ ] `x² = 7x` → nechta ildiz? *(2 ta: 0 va 7)*
- [ ] `√(x²)` nimaga teng? *(|x|)*
- [ ] `|x| < 5` → interval? *((−5, 5))*
- [ ] `|x| > 5` → interval? *((−∞,−5) ∪ (5,+∞))*
- [ ] `|x| > −3` → javob? *(ℝ — barcha sonlar)*
- [ ] `|x| < −3` → javob? *(∅)*
- [ ] `x² + 1 > 0` → javob? *(ℝ)*
- [ ] `x² + 1 < 0` → javob? *(∅)*
- [ ] `(x−1)/(x+2) ≥ 0` da `x = −2` kiradimi? *(YO'Q — maxraj noli hech qachon)*
- [ ] `D = 0` bo'lsa nechta ildiz? *(1 ta, ikki karrali)*
- [ ] `x² − 4x + 3 < 0` → ildizlar orasida yoki tashqarida? *(orasida: (1,3))*

---

## 4-daraja: Xato topish

Quyidagi yechimlarning **har birida bitta xato bor**. Top:

**Xato 1:**
```
−2x > 8
x > −4
```
<details><summary>Javob</summary>
Manfiy songa (−2) bo'lganda belgi almashishi kerak: <code>x < −4</code>
</details>

**Xato 2:**
```
x² = 9x
x = 9
```
<details><summary>Javob</summary>
x ga bo'lindi → <code>x = 0</code> ildizi yo'qoldi. To'g'risi: <code>x(x−9)=0 → {0, 9}</code>
</details>

**Xato 3:**
```
(x − 3)/(x + 1) < 2
x − 3 < 2(x + 1)
x − 3 < 2x + 2
−5 < x
Javob: x > −5
```
<details><summary>Javob</summary>
Maxrajga ko'paytirildi, lekin <code>x + 1</code> manfiy bo'lishi mumkin!
To'g'ri yo'l: hammasini chapga yig'ib, interval usuli.
To'g'ri javob: <code>(−∞, −5) ∪ (−1, +∞)</code>
</details>

**Xato 4:**
```
√(x + 3) = x − 3
x + 3 = x² − 6x + 9
x² − 7x + 6 = 0
x = 1  yoki  x = 6
Javob: {1, 6}
```
<details><summary>Javob</summary>
<code>x − 3 ≥ 0 → x ≥ 3</code> sharti tekshirilmadi. <code>x = 1</code> begona ildiz.
To'g'ri javob: <code>{6}</code>
</details>

**Xato 5:**
```
1/(x − 2) = 3/(x − 2)
1 = 3
Yechim yo'q, chunki 1 ≠ 3
```
<details><summary>Javob</summary>
Xulosa to'g'ri (∅), lekin sabab noto'g'ri yozilgan: avval ODZ (<code>x ≠ 2</code>)
yozilishi va yechim usuli ko'rsatilishi kerak. Bu yerda haqiqatan ham yechim yo'q,
lekin yechim yozuvi to'liq emas — ODZ yozmaslik odati keyinroq qimmatga tushadi.
</details>

---

## 5-daraja: Ulanishlar (AI bilan)

- [ ] Chiziqli sistemaning 3 holati (1/0/∞ yechim) neyron tarmoqlarda nimaga mos keladi?
- [ ] Nima uchun `cosine similarity` hech qachon 1 dan katta bo'lmaydi?
- [ ] Learning rate juda katta bo'lsa nima uchun loss "portlaydi"? Tengsizlik bilan tushuntir.
- [ ] Gradient clipping'dan keyin gradient normasi nimaga teng bo'ladi?
- [ ] "Dead ReLU" muammosini tengsizlik tilida ifodala.
- [ ] `|x|` va `x²` ning `x = 0` dagi farqi Lasso va Ridge farqini qanday tushuntiradi?

---

## 🎯 Yakuniy baho

| Bo'lim | To'g'ri / Jami |
|--------|----------------|
| 1-daraja (ta'riflar) | ___ / 8 |
| 2-daraja (chiqarish) | ___ / 7 |
| 3-daraja (tezkor) | ___ / 12 |
| 4-daraja (xato topish) | ___ / 5 |
| 5-daraja (AI ulanish) | ___ / 6 |
| **JAMI** | **___ / 38** |

| Ball | Xulosa |
|------|--------|
| 34–38 | ✅ Mavzu mustahkam. Keyingisiga o't. |
| 28–33 | 🟡 Yaxshi. Xato qilgan bo'limni 1 kun qayta ishla. |
| 20–27 | 🟠 Nazariyani qayta o'qi, masalalarni qaytadan yech. |
| 0–19 | 🔴 3–4 kun qo'shimcha kerak. Bu normal — **o'lchov, ayb emas**. |

---

## 📅 Takrorlash jadvali

Bu faylni quyidagi kunlarda qayta oching:

- [ ] Mavzu tugagan kuni
- [ ] +1 kun
- [ ] +3 kun
- [ ] +7 kun
- [ ] +21 kun
- [ ] Keyingi 2 mavzudan keyin (aralash takrorlash — eng samarali)

Har safar ballni yoz. O'sishni ko'rish — eng kuchli motivatsiya.
