# 01 — Tenglamalar va Tengsizliklar / Equations and Inequalities

> **Bu mavzu nima uchun birinchi?**
> Chunki AI'dagi deyarli hamma narsa oxir-oqibat **tenglama yechish** yoki **tengsizlikni
> qanoatlantirish**ga qaytadi. Gradient descent — tenglama. Optimizatsiya cheklovlari —
> tengsizlik. Linear regression — chiziqli sistema. Bu mavzusiz keyingisi bo'lmaydi.

---

## 📄 Fayllar

| Fayl | Nima | Qachon ochiladi |
|------|------|-----------------|
| [01-nazariya-uz.md](01-nazariya-uz.md) | Nazariya (o'zbekcha) | 1-kun |
| [01-theory-en.md](01-theory-en.md) | Theory (English) | O'zbekchani o'qigach |
| [02-masalalar-uz.md](02-masalalar-uz.md) | 42 ta masala — **yechimsiz** | Har kuni |
| [02-problems-en.md](02-problems-en.md) | Same problems in English | Har kuni |
| [03-yechimlar-uz.md](03-yechimlar-uz.md) | To'liq yechimlar | ⚠️ **Faqat o'zing yozgandan keyin** |
| [03-solutions-en.md](03-solutions-en.md) | Full solutions | ⚠️ Same rule |
| [04-ai-bogliqlik.md](04-ai-bogliqlik.md) | Bu mavzu AI'da qayerda | 8-kun |
| [05-lugat-glossary.md](05-lugat-glossary.md) | O'zbekcha ↔ Inglizcha atamalar | Har kuni yonida |
| [06-checklist.md](06-checklist.md) | O'zingni tekshirish | 9–10-kun |
| [code/](code/) | Python tekshiruvlari | Har kuni oxirida |

---

## 🗓 10 kunlik reja

Har kun: **45–90 daqiqa**. Qog'oz va qalam majburiy. Telefon boshqa xonada.

| Kun | Nazariya | Masalalar | Kod |
|-----|----------|-----------|-----|
| **1** | §1–3 (tenglama nima, ekvivalent almashtirishlar, chiziqli) | A1–A6 | — |
| **2** | §4 (chiziqli sistemalar) | D1–D5 | `01_tenglamalar.py` |
| **3** | §5 (kvadrat tenglamalar + formulani **chiqarish**) | B1–B4 | — |
| **4** | §5 davomi (Viyet, parametr) | B5–B7 | `01_tenglamalar.py` |
| **5** | §6–8 (ratsional, irratsional, modul) | C1–C7 | — |
| **6** | §9–10 (tengsizlik xossalari, chiziqli, kvadrat) | E1–E6 | `02_tengsizliklar.py` |
| **7** | §11–12 (interval usuli, modulli tengsizliklar) | E7–E12 | `02_tengsizliklar.py` |
| **8** | §13 (AI uchun muhim tengsizliklar) + `04-ai-bogliqlik.md` | F1–F5 | `03_ai_bogliqlik.py` |
| **9** | Takrorlash — `06-checklist.md` | Xato qilgan hammasi | — |
| **10** | **Nazorat:** bo'sh qog'oz testi | Tasodifiy 10 ta masala, 60 daqiqa | Hammasi |

**10-kundan keyin:** `02-funksiyalar` papkasiga o'tasan. Lekin bu mavzuni
+1 kun, +3 kun, +7 kun, +21 kunda qayta ko'rasan (spaced repetition jadvali).

---

## ✅ Bu mavzuni tugatdim deyish uchun shartlar

Hammasiga **ha** deyolmasang — tugamagan:

- [ ] Kvadrat tenglama formulasini bo'sh qog'ozga **chiqara olaman** (yodlab emas).
- [ ] Nima uchun tengsizlikni manfiy songa bo'lganda belgi almashishini **tushuntira olaman**.
- [ ] Ratsional tengsizlikni interval usuli bilan 3 daqiqada yecha olaman.
- [ ] "Begona ildiz" (extraneous root) nima ekanini va qachon paydo bo'lishini bilaman.
- [ ] 3 noma'lumli chiziqli sistemani qo'lda yecha olaman.
- [ ] Chiziqli sistemaning 3 xil holatini (1 ta / 0 ta / cheksiz yechim) **geometrik**
      tushuntira olaman.
- [ ] `|x| < a` va `|x| > a` ni hech o'ylamay yoza olaman.
- [ ] AM–GM tengsizligini isbotlay olaman.
- [ ] Gradient descent'ning `0 < η < 2/a` shartini chiqara olaman.
- [ ] Bu mavzudagi 20 ta inglizcha atamani bilaman.

---

## 🧠 Har kun boshlanishida (5 daqiqa)

Bo'sh qog'ozga, **hech narsaga qaramay**, kechagi mavzudan eslaganingni yoz.
Yomon chiqsa — yaxshi. Demak, bugun nimani takrorlash kerakligi aniq.

## 🧠 Har kun oxirida (2 daqiqa)

`../../00-mindset/03-progress-log.md` ni to'ldir. 4 qator.
Xato qilgan bo'lsang — `../../00-mindset/xatolar-daftari.md` ga yoz.

---

## ⚠️ Eslatma

Yechimlar faylini erta ochish — o'zingni aldash. Hech kim bilmaydi, faqat sen bilasan.
Va 6 oydan keyin natijani ham faqat sen ko'rasan.
