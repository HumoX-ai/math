# AI bilan o'rganish: eng katta xavf va undan chiqish yo'li

> Sen yozding: *"Hozir negadir AI chiqqanidan beri AI ga juda ishonib qolganman."*
> Bu fayl aynan shu haqida. Motivatsion gaplar emas — mexanizm va qoidalar.

---

## 1. Muammoning haqiqiy nomi: **ravonlik illyuziyasi**

AI biror mavzuni tushuntirganda, matn **aniq, tartibli, ravon** bo'ladi. Sen o'qiysan va
miyangda quyidagi his paydo bo'ladi:

> "Ha, tushundim."

Bu his — **aldov**. Psixologiyada buni *fluency illusion* (ravonlik illyuziyasi) yoki
*illusion of explanatory depth* (tushuntirish chuqurligi illyuziyasi) deyishadi.

Sabab oddiy:

| Sen his qilayotgan narsa | Aslida sodir bo'lgan narsa |
|--------------------------|----------------------------|
| "Bu mantiqli ko'rinyapti" | Sen **tanidim** (recognition) |
| "Men buni bilaman"        | Sen **eslay olaman** degani emas (recall) |
| "Oson ekan"               | Sen **qiyinchilikni boshqa odam bosib o'tdi** |

**Tanish (recognition)** va **eslash (recall)** — miyada butunlay boshqa ikki jarayon.
Kitobni o'qib chiqib "bildim" deyish — birinchisi. Bo'sh qog'ozga o'zing yozib chiqish —
ikkinchisi. Imtihon, ish, real muammo — doim ikkinchisini so'raydi.

**Test:** Hozir, hech narsaga qaramay, bo'sh qog'ozga kvadrat tenglama formulasini
**chiqarib ko'r** (yodlab emas — `ax² + bx + c = 0` dan boshlab). Agar qila olmasang —
sen uni bilmaysan, faqat tanigansan.

---

## 2. Nima uchun AI o'rganishni buzadi: **foydali qiyinchilik**

Robert Bjork'ning "desirable difficulties" (foydali qiyinchiliklar) tadqiqotlari:

> **O'rganish jarayonida qiyinchilik — nuqson emas, mexanizm.**

Miya faqat **qarshilikka uchraganda** qayta quradi. Sen bir masala ustida 20 daqiqa
qiynalganingda, miyang:

1. mavjud bilimlarni qidiradi,
2. ularni bir-biriga bog'laydi,
3. muvaffaqiyatsiz urinishlarni belgilaydi,
4. to'g'ri yechim kelganda uni **kuchli** yozib qo'yadi.

AI'dan darrov javob olsang — bu 4 bosqichning **1–3 tashlab yuboriladi**. Javob miyaga
kiradi, lekin **hech narsaga ulanmaydi**. 3 kundan keyin yo'qoladi.

```
QIYNALISH  →  URINISH  →  XATO  →  TUSHUNTIRISH  →  MUSTAHKAM BILIM   ✅
                                    ↑
                              AI shu yerda kerak

TUSHUNTIRISH  →  "tushundim" hissi  →  3 kun  →  hech narsa            ❌
    ↑
AI shu yerda zararli
```

**Bitta jumla bilan:** AI'ni **qiyinchilikdan keyin** ishlat, **qiyinchilik o'rniga** emas.

---

## 3. "Generation effect" — o'zing chiqargan javob 2 barobar yaxshi eslanadi

Tadqiqotlar barqaror natija beradi: agar sen javobni **o'zing chiqarsang** (hatto xato
chiqarsang ham!), keyin to'g'risini ko'rsang — eslab qolish darajasi tayyor javobni
o'qishdan sezilarli yuqori bo'ladi.

Ya'ni:

> **Xato urinish — behuda vaqt emas. Xato urinish — to'g'ri javob uchun ilgak.**

Shuning uchun bu repozitoriyda masalalar va yechimlar **alohida fayllarda**.

---

## 4. Kognitiv yuklamani tashlab yuborish (cognitive offloading)

Odam biror ish uchun tashqi vositaga tayansa, miya **o'sha ma'lumotni saqlashni
to'xtatadi** — chunki "kerak bo'lsa qayta olaman" degan hisob-kitob qiladi. Buni
kalkulyator, GPS va Google misolida ko'p o'rganishgan ("digital amnesia" deb ataladi).

AI bu effektning eng kuchli shakli, chunki u faqat **ma'lumotni** emas, **fikrlash
jarayonini** ham o'z zimmasiga oladi.

Halol bo'laylik: LLM'lar bo'yicha bu tadqiqotlar hali yosh, kuchli uzoq muddatli
xulosalar chiqarish erta. Lekin generation effect va retrieval practice — o'nlab yillik,
juda mustahkam natijalar. Ular yo'nalishni aniq ko'rsatadi.

---

## 5. Eng kuchli motivatsiya: **AI xato qiladi va sen buni ko'rishing kerak**

Bu senga ayanchli emas, **kuch beradigan** haqiqat:

- AI matematik hisoblarda arifmetik xato qiladi.
- AI ishonchli ohangda **noto'g'ri isbot** yozib berishi mumkin.
- AI belgini (`≤` / `<`), ODZ'ni, chegara holatlarni tushirib qoldirishi mumkin.
- AI sen xohlagan javobga **moslashib** ketishi mumkin.

Endi savol:

> **Agar sen matematikani bilmasang, AI xato qilganini qanday bilasan?**

Javob: bilmaysan. Va agar bilmasang — sen AI bilan ishlayotgan **muhandis** emassan,
sen AI'ning **chiqishini nusxalayotgan odam**san. Bu ikkisi orasida karyera farqi bor.

```
Matematikani bilmaydigan odam + AI  =  AI'ning natijasiga ishonishdan boshqa chorasi yo'q
Matematikani biladigan odam   + AI  =  AI'ni 10x tezlashtiruvchi sifatida ishlatadi
```

**Sen matematikani AI o'rniga emas, AI ustidan nazorat qilish uchun o'rganyapsan.**

Bu, ayniqsa, sening maqsading (AI → DL → LLM → AGI) uchun to'g'ri. Chunki bu sohada
ishlaydigan odamning asosiy ishi — **model nima uchun bunday natija berdi** degan savolga
javob berish. Bu savolga matematikasiz javob yo'q.

---

## 6. 🔒 AI BILAN ISHLASH SHARTNOMASI

Buni bosib chiqar yoki stol ustiga yoz. Har kuni amal qil.

### ❌ TAQIQLANGAN

1. Masalani o'qib, darrov AI'ga tashlash.
2. "Menga buni tushuntirib ber" — **birinchi qadam sifatida**.
3. Yechimni nusxalab, "tushundim" deb keyingisiga o'tish.
4. AI yozgan yechimni tekshirmasdan qabul qilish.
5. AI'dan uy vazifasini qildirib olish. (Buyurtmachi sen emas — sen **o'quvchisan**.)

### ✅ RUXSAT ETILGAN

1. **15 daqiqa qoidasi.** Masala ustida kamida 15 daqiqa **o'zing** ishla. Qog'ozda.
   Faqat shundan keyin AI'ga murojaat qil.

2. **Javob emas, ishora so'ra.** Prompt shunday bo'lsin:
   > "Men bu masalani yechyapman. Mana mening urinishim: [...]. Javobni **berma**.
   > Faqat bitta ishora ber va men qayerda adashganimni ayt."

3. **AI — tekshiruvchi, ustoz emas.** O'zing yechganingdan keyin:
   > "Mana mening yechimim: [...]. Tekshir. Xato bo'lsa, **qayerda** va **nega**
   > xato ekanini ayt, lekin to'g'ri yechimni to'liq yozma."

4. **Feynman texnikasi — teskari.** Sen AI'ga tushuntirasan, AI tanqid qiladi:
   > "Men sizga interval usulini tushuntiraman, siz 12 yoshli bola kabi savol bering
   > va mening tushuntirishimdagi bo'shliqlarni toping."

5. **Masala generatori.** Bu AI'ning eng foydali roli:
   > "Menga kvadrat tengsizliklar bo'yicha 10 ta masala ber. Yechimini berma.
   > 3 tasi qiyin bo'lsin, 1 tasida yechim yo'q bo'lsin."

6. **Xato ovchisi.** Oyiga bir marta:
   > "Menga kvadrat tenglama haqida yechim yoz, lekin ichiga **1 ta jiddiy xato**
   > joyla. Qayerdaligini aytma."
   > Keyin xatoni o'zing top. Bu eng yaxshi mashq.

---

## 7. Kunlik amaliy tartib (45–90 daqiqa)

```
┌──────────────────────────────────────────────────────────┐
│ 0–5 daq    Bo'sh qog'oz testi: kechagi mavzudan          │
│            eslaganingni yoz. Hech narsaga qaramay.       │
├──────────────────────────────────────────────────────────┤
│ 5–20 daq   Yangi nazariyani o'qi. Qog'ozga KO'CHIRMA —   │
│            o'z so'zing bilan qayta yoz.                  │
├──────────────────────────────────────────────────────────┤
│ 20–60 daq  Masala yech. Qog'ozda. Telefon boshqa xonada. │
│            Qiynalsang — 15 daqiqa qoidasi.               │
├──────────────────────────────────────────────────────────┤
│ 60–75 daq  Yechimlar faylini och. Solishtir.             │
│            Har xatoni "Xatolar daftari"ga yoz.           │
├──────────────────────────────────────────────────────────┤
│ 75–85 daq  Python bilan tekshir (code/ papkasi).         │
├──────────────────────────────────────────────────────────┤
│ 85–90 daq  Progress log'ni to'ldir. 3 qator bas.         │
└──────────────────────────────────────────────────────────┘
```

---

## 8. Takrorlash jadvali (spaced repetition)

Unutish egri chizig'i (Ebbinghaus) shafqatsiz: yangi materialning katta qismi bir necha
kun ichida yo'qoladi — **agar takrorlanmasa**. Yechim — kengaytiriluvchi intervallar:

| Takror | Qachon | Nima qilinadi |
|--------|--------|---------------|
| 1 | Xuddi shu kuni kechqurun | 5 daqiqa: bo'sh qog'ozga asosiy formulalar |
| 2 | +1 kun | 10 daqiqa: 2 ta masala qayta yech |
| 3 | +3 kun | 10 daqiqa: checklist bo'yicha o'zingni tekshir |
| 4 | +7 kun | 15 daqiqa: eng qiyin 3 masala |
| 5 | +21 kun | 15 daqiqa: mavzuni AI'ga tushuntir |

Har mavzu papkasidagi `06-checklist.md` shu uchun kerak.

---

## 9. Xatolar daftari (eng past baholanadigan vosita)

Fayl tayyor: [`xatolar-daftari.md`](xatolar-daftari.md). Har xato uchun 3 qator:

```markdown
### 2026-09-12 — Tengsizlikni manfiy songa bo'lganda belgini almashtirmadim
- Masala: -3x > 6 → men x > -2 deb yozdim. To'g'risi: x < -2.
- Sabab: avtomatik ravishda tenglamadek yechdim.
- Oldini olish: manfiy songa bo'lish/ko'paytirish oldidan qalam bilan ⚠️ qo'yaman.
```

Bir oydan keyin bu daftarni o'qisang — **o'z miyangning xaritasini** ko'rasan.
Bu AI bermaydigan yagona narsa.

---

## 10. Qisqacha xulosa

| Noto'g'ri model | To'g'ri model |
|-----------------|---------------|
| AI — mening o'qituvchim | AI — mening **mashqlar sherigim** |
| AI javob beradi | AI **savol beradi va tekshiradi** |
| Men AI'dan o'rganaman | Men **qiyinchilikdan** o'rganaman, AI qiyinchilikni sozlaydi |
| AI'ga ishonaman | AI'ni **tekshiraman** — chunki men bilaman |

> Sen AI'ni yaxshi ko'rasan. Bu yomon emas. Lekin sevgi bilan ishonch — boshqa narsa.
> AI'ni sev, lekin **tekshir**. Tekshira olish uchun esa — mana shu repozitoriy.

---

**Keyingi fayl:** [02-motivatsiya-va-psixologiya-uz.md](02-motivatsiya-va-psixologiya-uz.md)
