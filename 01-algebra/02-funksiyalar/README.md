# 02 — Funksiyalar / Functions

> **Bu mavzu nima uchun ⭐⭐⭐⭐⭐?**
> Chunki **neyron tarmoq — bu funksiya**. Model — funksiya. Loss — funksiya. Aktivatsiya —
> funksiya. Training — "ma'lumotga eng yaxshi mos keladigan funksiyani topish".
> Bu mavzuni tushunmasang, keyingi hamma narsa — formulalar yig'indisi bo'lib qoladi.

**Oldingi mavzu:** [01-tenglamalar-va-tengsizliklar](../01-tenglamalar-va-tengsizliklar/README.md)
**Keyingi mavzu:** [03-daraja-va-ildizlar](../03-daraja-va-ildizlar/README.md)

---

## 📄 Fayllar

| Fayl | Nima | Qachon |
|------|------|--------|
| [01-nazariya-uz.md](01-nazariya-uz.md) | Nazariya (o'zbekcha), 14 bo'lim | 1–8-kun |
| [01-theory-en.md](01-theory-en.md) | Theory (English) | O'zbekchadan keyin |
| [02-masalalar-uz.md](02-masalalar-uz.md) | 42 ta masala — **yechimsiz** | Har kuni |
| [02-problems-en.md](02-problems-en.md) | Same problems in English | Har kuni |
| [03-yechimlar-uz.md](03-yechimlar-uz.md) | To'liq yechimlar | ⚠️ Faqat o'zing yozgandan keyin |
| [03-solutions-en.md](03-solutions-en.md) | Full solutions | ⚠️ Same rule |
| [04-ai-bogliqlik.md](04-ai-bogliqlik.md) | Neyron tarmoq = funksiya kompozitsiyasi | 8-kun |
| [05-lugat-glossary.md](05-lugat-glossary.md) | O'zbekcha ↔ Inglizcha | Har kuni yonida |
| [06-checklist.md](06-checklist.md) | O'zingni tekshirish | 9–10-kun |
| [code/](code/) | Grafiklar + tekshiruvlar + mini neyron tarmoq | Har kun oxirida |

---

## 🗓 10 kunlik reja

| Kun | Nazariya | Masalalar | Kod |
|-----|----------|-----------|-----|
| **1** | §1–4 (funksiya nima, domain, range, grafik) | A1–A6 | `02_grafiklar.py` — galereya |
| **2** | §5–6 (asosiy funksiyalar, chiziqli funksiya) | B1–B7 | `01_funksiyalar.py` |
| **3** | §7 (kvadrat funksiya, cho'qqi, vertex form) | C1–C6 | `02_grafiklar.py` |
| **4** | §8 (juft/toq, monotonlik, nollar, ishora) | D1–D6 | `01_funksiyalar.py` |
| **5** | §9 (grafik almashtirishlar) | E1–E2 | `02_grafiklar.py` — transformations |
| **6** | §10 (**kompozitsiya** — eng muhim bo'lim) | E3–E7 | `03_ai_bogliqlik.py` |
| **7** | §11–12 (teskari funksiya, bo'lakli) | F1–F5 | `01_funksiyalar.py` |
| **8** | §13 (AI funksiyalari) + `04-ai-bogliqlik.md` | G1–G5 | `03_ai_bogliqlik.py` |
| **9** | Takrorlash — `06-checklist.md` | Xato qilganlar | — |
| **10** | **Nazorat:** 60 daqiqa, 10 masala | `02-masalalar` oxirida | — |

**Har kun boshida (5 daq):** bo'sh qog'ozga kechagi mavzuni yoz.
**Har kun oxirida (2 daq):** `00-mindset/03-progress-log.md`.

---

## ✅ Tugatish shartlari

- [ ] "Funksiya" ta'rifini va u nima uchun "har bir x ga **bitta** y" bo'lishi kerakligini tushuntira olaman.
- [ ] Istalgan formuladan domain'ni topa olaman.
- [ ] `y = kx + b` da `k` va `b` ning ma'nosini bilaman va ikki nuqtadan chiziq yoza olaman.
- [ ] Parabola cho'qqisini `−b/2a` orqali va vertex form orqali topa olaman.
- [ ] Juft/toq funksiyani **ta'rifdan** tekshira olaman.
- [ ] `f(g(x))` va `g(f(x))` farqini bilaman va ikkalasini hisoblay olaman.
- [ ] Teskari funksiyani topa olaman va qachon mavjud bo'lishini bilaman.
- [ ] `f(x−2)+3` grafigi qaysi tomonga siljishini **o'ylamay** ayta olaman.
- [ ] **Chiziqli funksiyalar kompozitsiyasi yana chiziqli** ekanini isbotlay olaman (va bu neyron tarmoqda nima uchun muhimligini).
- [ ] ReLU'lar yig'indisi bilan `|x − 1|` ni qura olaman.
- [ ] `L(w) = Σ(wxᵢ − yᵢ)²` ning parabola ekanini ko'rsata olaman.

---

## ⚠️ Eslatma

Bu mavzuda **grafik chizish majburiy**. Qog'ozda, qo'l bilan. Kompyuterda chizilgan
grafikni ko'rish — tanish. O'zing chizish — bilish. `code/02_grafiklar.py` — faqat
o'zing chizganingdan keyin tekshirish uchun.
