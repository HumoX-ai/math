# AI uchun Matematika — O'quv Repozitoriysi

> **Maqsad:** Algebra → Linear Algebra → Calculus → Probability → ... → AI Research Mathematics
> **Uslub:** har mavzuni (1) o'zbekcha tushunaman, (2) inglizcha terminini bilaman, (3) qo'lda yechaman, (4) Python'da tekshiraman, (5) AI'dagi joyini bilaman.

---

## 📁 Papkalar xaritasi

```
math/
├── README.md                    ← shu fayl (boshlanish nuqtasi)
├── requirements.md              ← to'liq roadmap (ChatGPT bergan)
├── 00-mindset/                  ← ⭐ AVVAL SHUNI O'QI
│   ├── 01-ai-bilan-organish-uz.md
│   ├── 01-learning-with-ai-en.md
│   ├── 02-motivatsiya-va-psixologiya-uz.md
│   ├── 02-motivation-and-psychology-en.md
│   ├── 03-progress-log.md       ← kunlik jurnal (o'zing to'ldirasan)
│   └── xatolar-daftari.md     ← xatolar daftari (eng qimmatli fayl)
└── 01-algebra/
    ├── 01-tenglamalar-va-tengsizliklar/   ← ⭐ BOSHLA SHU YERDAN
    ├── 02-funksiyalar/                    ← neyron tarmoq = funksiya
    └── 03-daraja-va-ildizlar/             ← norm, √d, float32, scaling laws
```

---

## 🚀 Qayerdan boshlash

**1-kun (bugun):**

1. `00-mindset/01-ai-bilan-organish-uz.md` — o'qi (~15 daqiqa).
   Bu AI'ga haddan tashqari ishonish muammosi haqida. Sen aytgan muammo aynan shu.
2. `00-mindset/02-motivatsiya-va-psixologiya-uz.md` — o'qi (~15 daqiqa).
3. `01-algebra/01-tenglamalar-va-tengsizliklar/README.md` — 10 kunlik rejani ko'r.
4. Boshla.

**Har kuni:** 45–90 daqiqa. Har kuni. Haftada 6 kun. Bitta dam olish kuni.

---

## 🧭 To'liq roadmap va papka nomlari

Har mavzu tugagach, keyingisi uchun shu nomda papka ochiladi:

| # | Papka | Mavzu | AI uchun muhimlik |
|---|-------|-------|-------------------|
| 01 | [`01-algebra/01-tenglamalar-va-tengsizliklar`](01-algebra/01-tenglamalar-va-tengsizliklar/README.md) | Tenglamalar va tengsizliklar ✅ | ⭐⭐⭐⭐ |
| 02 | [`01-algebra/02-funksiyalar`](01-algebra/02-funksiyalar/README.md) | Funksiyalar ✅ | ⭐⭐⭐⭐⭐ |
| 03 | [`01-algebra/03-daraja-va-ildizlar`](01-algebra/03-daraja-va-ildizlar/README.md) | Daraja va ildizlar ✅ | ⭐⭐⭐⭐ |
| 04 | `01-algebra/04-logarifmlar` | Logarifmlar | ⭐⭐⭐⭐⭐ |
| 05 | `01-algebra/05-eksponentalar` | Eksponentalar | ⭐⭐⭐⭐⭐ |
| 06 | `01-algebra/06-polinomlar` | Polinomlar | ⭐⭐⭐ |
| 07 | `01-algebra/07-absolyut-qiymat` | Absolyut qiymat | ⭐⭐⭐⭐ |
| 08 | `01-algebra/08-ketma-ketliklar` | Ketma-ketliklar | ⭐⭐⭐⭐ |
| 09 | `02-trigonometriya/` | Trigonometriya | ⭐⭐⭐ |
| 10 | `03-linear-algebra/` | Chiziqli algebra | ⭐⭐⭐⭐⭐ |
| 11 | `04-calculus/` | Calculus | ⭐⭐⭐⭐⭐ |
| 12 | `05-probability/` | Ehtimollar nazariyasi | ⭐⭐⭐⭐⭐ |
| 13 | `06-statistics/` | Statistika | ⭐⭐⭐⭐ |
| 14 | `07-optimization/` | Optimizatsiya | ⭐⭐⭐⭐⭐ |
| 15 | `08-information-theory/` | Axborot nazariyasi | ⭐⭐⭐⭐⭐ |
| 16 | `09-discrete-math/` | Diskret matematika | ⭐⭐⭐⭐ |
| 17 | `10-numerical-math/` | Sonli usullar | ⭐⭐⭐ |
| 18 | `11-graph-theory/` | Graflar nazariyasi | ⭐⭐⭐ |

---

## 📐 Har bir mavzu papkasining standart tuzilishi

```
NN-mavzu-nomi/
├── README.md              ← mavzuga kirish + kunlik reja
├── 01-nazariya-uz.md      ← nazariya (o'zbekcha)
├── 01-theory-en.md        ← theory (English)
├── 02-masalalar-uz.md     ← masalalar (yechimsiz!)
├── 02-problems-en.md      ← problems (no solutions!)
├── 03-yechimlar-uz.md     ← to'liq yechimlar
├── 03-solutions-en.md     ← full solutions
├── 04-ai-bogliqlik.md     ← bu mavzu AI'da qayerda ishlatiladi
├── 05-lugat-glossary.md   ← o'zbekcha ↔ inglizcha atamalar
├── 06-checklist.md        ← o'zingni tekshirish ro'yxati
└── code/                  ← Python tekshiruvlari
```

**Muhim qoida:** `02-masalalar` va `03-yechimlar` alohida fayl — chunki yechimni ko'rish
osonlashtiradi, oson narsa esa o'rgatmaydi. Yechimlar faylini **faqat o'z javobingni
yozib bo'lganingdan keyin** och.

---

## 🛠 Texnik talablar

```bash
# Python muhitini bir marta sozla
python3 -m venv .venv
source .venv/bin/activate
pip install numpy sympy matplotlib   # matplotlib — 02-funksiyalar grafiklari uchun
```

Har mavzuda `code/` papkasi bor — u yerdagi skriptlar sening qo'lda yechganingni tekshiradi.

---

## 📊 Progress

Kunlik jurnalni `00-mindset/03-progress-log.md` da yurit. Bu eng arzon va eng kuchli vosita.

---

## ⚖️ Bitta eslatma

Bu repozitoriyni AI yozdi. Ichidagi matematika tekshirilgan, lekin **sen ham tekshir**.
Agar biror joyda xato topsang — bu muvaffaqiyatsizlik emas, bu **sening o'sganing**.
Xato topgan kuningni jurnalga yoz. Bu eng qimmatli kun bo'ladi.
