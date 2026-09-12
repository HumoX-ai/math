# 03 — Daraja va Ildizlar / Powers and Roots

> **Bu mavzu nima uchun kerak?**
> `‖x‖ = √(Σxᵢ²)` — norm. `1/√d_k` — attention. `√(2/n)` — init. `x^(−1/2)` — RMSNorm, Adam.
> `10⁹` parametr, `2⁻²³` float aniqligi, `N^(−0.07)` scaling law. Deep learning'ning
> yarmi — darajalar va ildizlar bilan yozilgan. Bu mavzusiz **eksponenta va logarifm**
> (keyingi ikkitasi) bo'lmaydi, ular esa softmax va cross-entropy'ning asosi.

**Oldingi:** [02-funksiyalar](../02-funksiyalar/README.md) · **Keyingi:** `04-logarifmlar`

---

## 📄 Fayllar

| Fayl | Nima | Qachon |
|------|------|--------|
| [01-nazariya-uz.md](01-nazariya-uz.md) | Nazariya (o'zbekcha), 13 bo'lim | 1–7-kun |
| [01-theory-en.md](01-theory-en.md) | Theory (English) | O'zbekchadan keyin |
| [02-masalalar-uz.md](02-masalalar-uz.md) | 43 ta masala — **yechimsiz** | Har kuni |
| [02-problems-en.md](02-problems-en.md) | Same in English | Har kuni |
| [03-yechimlar-uz.md](03-yechimlar-uz.md) | To'liq yechimlar | ⚠️ Faqat o'zing yozgandan keyin |
| [03-solutions-en.md](03-solutions-en.md) | Full solutions | ⚠️ Same rule |
| [04-ai-bogliqlik.md](04-ai-bogliqlik.md) | Norm, √d, init, float32, scaling laws | 8-kun |
| [05-lugat-glossary.md](05-lugat-glossary.md) | O'zbekcha ↔ Inglizcha | Har kuni yonida |
| [06-checklist.md](06-checklist.md) | O'zingni tekshirish | 9–10-kun |
| [code/](code/) | Tekshiruvlar + float tajribalari + √d eksperimenti | Har kun oxirida |

---

## 🗓 10 kunlik reja

| Kun | Nazariya | Masalalar | Kod |
|-----|----------|-----------|-----|
| **1** | §1–3 (natural, nol, manfiy daraja) | A1–A7 | `01_daraja_ildiz.py` |
| **2** | §2 chuqur (xossalar **isboti**) | B1–B7 | — |
| **3** | §4–5 (ildizlar, xossalari) | C1–C4 | `01_daraja_ildiz.py` |
| **4** | §7 (soddalashtirish, ratsionallashtirish) | C5–C8 | — |
| **5** | §6 (**ratsional ko'rsatkich** — birlashtiruvchi g'oya) | D1–D6 | `01_daraja_ildiz.py` |
| **6** | §8–9 (grafiklar, standart ko'rinish) + §11 tenglamalar | E1–E6 | `02_osish_va_float.py` |
| **7** | §10 (o'sish: 2ⁿ vs n², float32) | F1–F4 | `02_osish_va_float.py` |
| **8** | §12 + `04-ai-bogliqlik.md` | G1–G5 | `03_ai_bogliqlik.py` |
| **9** | Takrorlash — `06-checklist.md` | Xato qilganlar | — |
| **10** | **Nazorat:** 60 daqiqa, 10 masala | `02-masalalar` oxirida | — |

---

## ✅ Tugatish shartlari

- [ ] 5 ta daraja xossasini **nima uchun** ishlashini (ko'paytuvchilarni sanab) tushuntira olaman.
- [ ] `a⁰ = 1` va `a⁻ⁿ = 1/aⁿ` **nima uchun** shunday aniqlanganini ayta olaman (pattern orqali).
- [ ] `(−2)⁴` va `−2⁴` farqini hech o'ylamay ayta olaman.
- [ ] `√(x²) = |x|` — va bu nega `x` emas.
- [ ] `√(a + b) ≠ √a + √b` — va misol bilan ko'rsata olaman.
- [ ] `a^(m/n) = ⁿ√(aᵐ)` ekanini **isbotlay** olaman.
- [ ] `√50`, `1/(√3 − 1)` kabi ifodalarni soddalashtira olaman.
- [ ] `2ˣ = 32`, `x^(3/2) = 8` kabi tenglamalarni yecha olaman.
- [ ] `√2 + √3` va `√10` ni kalkulyatorsiz solishtira olaman.
- [ ] `2³⁰⁰` va `3²⁰⁰` ni solishtira olaman.
- [ ] `‖(3,4)‖ = 5`, `1/√64 = 1/8`, `√(2/512) = 1/16` — sekundlarda.
- [ ] `float32` nima uchun `16 777 217` ni saqlay olmasligini tushuntira olaman.

---

## ⚠️ Bu mavzuning o'ziga xos xavfi

Daraja xossalari **oson ko'rinadi** — va aynan shuning uchun eng ko'p xato qilinadi.
`(a+b)² = a² + b²` xatosini universitet talabalari ham qiladi. Har bir xossani
**isbotlab** o'rgan, yodlab emas. Xatolar muzeyi (§13) — bu mavzuda eng uzun.
