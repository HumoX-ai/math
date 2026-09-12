# ✅ O'zingni tekshirish — Daraja va Ildizlar

> Bo'sh qog'ozga. Kalkulyatorsiz. 3-, 7-, 21-kunlarda qaytadan.

---

## 1-daraja: Ta'riflar (8)

- [ ] `aⁿ` da asos va ko'rsatkich qaysi? `aⁿ` nima degani?
- [ ] `a⁰ = 1` **nima uchun**? (Pattern yoki bo'lish qoidasi orqali.)
- [ ] `a⁻ⁿ` nima? `a⁻¹` bilan `−a` farqi?
- [ ] `√16` nechchi? `x² = 16` ning yechimi nechchi? Farqi?
- [ ] Juft va toq ildiz farqi — 2 jumlada.
- [ ] `a^(m/n)` ta'rifi?
- [ ] Standart ko'rinish nima? `1 ≤ m < 10` sharti nega?
- [ ] `float32` da `2⁻²³` va `2²⁴` nima ma'noni anglatadi?

## 2-daraja: Isbot va chiqarish (7)

- [ ] `aᵐ·aⁿ = aᵐ⁺ⁿ` ni ko'paytuvchilarni sanab isbotla.
- [ ] `(aᵐ)ⁿ = aᵐⁿ` ni isbotla.
- [ ] `a⁰ = 1` ni bo'lish qoidasidan chiqar.
- [ ] `a^(1/2) = √a` ni isbotla (D6).
- [ ] `√(a + b) = √a + √b` faqat `ab = 0` da — isbotla.
- [ ] `1/(√5 − 2)` ni ratsionallashtir. *(√5 + 2)*
- [ ] `√2 + √3 < √10` ni isbotla.

## 3-daraja: Tezkor (14, har biri 20 soniya)

- [ ] `(−3)⁴ = ?` *(81)*   `−3⁴ = ?` *(−81)*
- [ ] `2⁻⁴ = ?` *(1/16)*
- [ ] `(2/3)⁻² = ?` *(9/4)*
- [ ] `2⁵·2³ = ?` *(2⁸ = 256)*
- [ ] `(3²)⁴ = ?` *(3⁸)*
- [ ] `√(49·4) = ?` *(14)*
- [ ] `√98 = ?` *(7√2)*
- [ ] `³√(−27) = ?` *(−3)*
- [ ] `16^(3/4) = ?` *(8)*
- [ ] `8^(−2/3) = ?` *(1/4)*
- [ ] `x^(1/3)·x^(1/6) = ?` *(x^(1/2))*
- [ ] `2ˣ = 1/16 → x = ?` *(−4)*
- [ ] `(1/3)ˣ > 1/27 → x ?` *(x < 3)*
- [ ] `5 × 10⁻³ · 4 × 10⁷ = ?` *(2 × 10⁵)*

## 4-daraja: Xato topish (6)

**Xato 1:** `(2x + 3)² = 4x² + 9`
<details><summary>Javob</summary><code>4x² + 12x + 9</code>. O'rta had unutilgan.</details>

**Xato 2:** `√(x² + 16) = x + 4`
<details><summary>Javob</summary>Ildiz yig'indi ustida tarqalmaydi. <code>x = 0</code>: <code>√16 = 4</code>, lekin <code>0 + 4 = 4</code> — tasodifan teng; <code>x = 3</code>: <code>√25 = 5 ≠ 7</code>.</details>

**Xato 3:** `3² · 3³ = 9⁵`
<details><summary>Javob</summary><code>3⁵ = 243</code>. Asos o'zgarmaydi.</details>

**Xato 4:** `x⁴ = 81 → x = 3`
<details><summary>Javob</summary><code>x = ±3</code>. Juft daraja — ikkita ildiz.</details>

**Xato 5:** `√x > 4 → x > 16`
<details><summary>Javob</summary>Bu yerda to'g'ri (D: x ≥ 0 avtomatik bajariladi, chunki x > 16). Lekin <code>√x < 4 → x < 16</code> XATO bo'lardi: <code>0 ≤ x < 16</code> kerak. Farqni tushun.</details>

**Xato 6:** `(−8)^(1/3)` ni NumPy'da `(-8)**(1/3)` deb hisoblash
<details><summary>Javob</summary><code>nan</code> chiqadi (yoki kompleks). <code>np.cbrt(-8) = -2.0</code> ishlat. Manfiy asosda kasr daraja — real analizda ham nozik.</details>

## 5-daraja: AI ulanishlar (6)

- [ ] `‖(3,4)‖` nechchi va bu `√` ning qaysi xossasi bilan `≥ 0`?
- [ ] `1/√d_k` nima uchun `√`, `d` emas? Bir jumla.
- [ ] `√(2/512)` nechchi va bu qayerda ishlatiladi?
- [ ] `x · (mean(x²))^(−1/2)` — bu nima va RMS'i nechchi bo'ladi?
- [ ] `float16` da `70 000` nima bo'ladi va nega?
- [ ] `L(N) = N^(−0.076)`: `N` 10 marta oshsa `L` nechchi marta kamayadi?

---

## 🎯 Baho

| Bo'lim | Ball |
|--------|------|
| 1-daraja | ___ / 8 |
| 2-daraja | ___ / 7 |
| 3-daraja | ___ / 14 |
| 4-daraja | ___ / 6 |
| 5-daraja | ___ / 6 |
| **JAMI** | **___ / 41** |

37–41 ✅ keyingisiga (`04-logarifmlar`) · 30–36 🟡 1 kun · 22–29 🟠 nazariyani qayta · 0–21 🔴 +3 kun

## 📅 Takrorlash

- [ ] Tugagan kun  - [ ] +1  - [ ] +3  - [ ] +7  - [ ] +21  - [ ] 2 mavzudan keyin
