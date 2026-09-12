# 🔗 Bu mavzu AI'da qayerda ishlatiladi / Where This Topic Shows Up in AI

> Bu fayl **ikki tilda**: har bo'lim o'zbekcha, atamalar inglizcha.
> Maqsad — "bu maktab algebrasi, menga nima keragi bor?" degan savolni butunlay yopish.

---

## Umumiy xarita

```
                    TENGLAMALAR                    TENGSIZLIKLAR
                         │                              │
        ┌────────────────┼────────────┐      ┌──────────┼──────────┐
        ↓                ↓            ↓      ↓          ↓          ↓
   Chiziqli         Kvadrat      Modulli  Chegaralar  Shartlar  Cheklovlar
   sistemalar       (convexity)  (norms)  (bounds)  (conditions) (constraints)
        │                │            │      │          │          │
        ↓                ↓            ↓      ↓          ↓          ↓
   Linear           Optimization   L1/L2   Learning   Conver-     SVM
   regression       landscape      norms   rate       gence       margins
   Ax = b           minimum        ReLU    bounds     criteria    KKT
```

---

## 1. Chiziqli sistemalar → Linear Regression'ning yuragi

**O'zbekcha:** Sen D blokida `Ax = b` ko'rinishidagi sistemani qo'lda yechding.
Machine learning'dagi eng birinchi model — **linear regression** — aynan shu.

**English:** The normal equations of least squares are a linear system:

```
XᵀX · w  =  Xᵀy
└─┬─┘      └─┬─┘
  A          b
```

| Maktab algebrasi | Linear Algebra | Machine Learning |
|------------------|----------------|------------------|
| `2x + y = 7` | `Ax = b` | `XᵀXw = Xᵀy` |
| Kesishish nuqtasi | Yagona yechim | Yagona optimal `w` |
| Parallel chiziqlar | `rank(A) < n`, nomuvofiq | Model mos kelmaydi |
| Ustma-ust chiziqlar | Cheksiz yechim | **Overparameterized** model |

> **Eng muhim ulanish:** D4 masalasidagi "cheksiz ko'p yechim" holati — bu zamonaviy
> neyron tarmoqlarning **normal holati** (parametrlar soni ma'lumotdan ko'p).
> Shuning uchun `L2 regularization` kerak: u cheksiz yechimlardan **eng kichik normali**
> ni tanlaydi.

---

## 2. Hosila = 0 → har qanday optimizatsiya bir tenglama

**O'zbekcha:** Calculus'da minimum topish quyidagicha:

```
1. Loss funksiyani yoz:     L(w)
2. Hosilasini ol:           dL/dw
3. Nolga tenglashtir:       dL/dw = 0      ←  BU TENGLAMA
4. Yech                     →  w*
```

Ya'ni **butun optimizatsiya nazariyasi tenglama yechishga qaytadi.** Sen bugun
o'rgangan narsa — o'sha oxirgi qadam.

**Misol (F1 dan):** `S(w,b) = Σ(wxᵢ + b − yᵢ)²` ning minimumi →
ikkita chiziqli tenglama → sen ularni qo'lda yechding.

---

## 3. Kvadrat funksiya → optimizatsiya landshafti

**O'zbekcha:** `f(x) = ax² + bx + c` parabolasi — optimizatsiyadagi eng oddiy model.

```
a > 0   →   ∪   →   minimum bor        →  convex (qavariq)
a < 0   →   ∩   →   maksimum bor       →  concave (botiq)
a = 0   →   —   →   chiziqli
```

| Algebra | Ko'p o'lchovli | AI'dagi ma'nosi |
|---------|----------------|-----------------|
| `a > 0` | Hessian musbat aniq | Bu nuqta **minimum** |
| `a < 0` | Hessian manfiy aniq | Bu nuqta **maksimum** |
| `D < 0`, `a > 0` | `xᵀAx > 0` barcha x uchun | **Positive definite** matritsa |
| Parabola cho'qqisi | `∇f = 0` nuqtasi | Konvergensiya nuqtasi |

> E4 masalasi (`x² + 4x + 5 > 0` barcha x uchun) — bu aynan **positive definiteness**
> ning bir o'lchovli holati. Ko'p o'lchovda u `xᵀAx > 0` ko'rinishida yoziladi va
> "bu kritik nuqta minimum" degan xulosani beradi.

---

## 4. Modul → Norm → Regularizatsiya

**O'zbekcha:** `|x|` — bu 1 o'lchovli **norm**. Ko'p o'lchovda:

```
L1 norm:   ‖w‖₁ = |w₁| + |w₂| + ... + |wₙ|          →  Lasso regression
L2 norm:   ‖w‖₂ = √(w₁² + w₂² + ... + wₙ²)         →  Ridge regression
L∞ norm:   ‖w‖∞ = max(|w₁|, ..., |wₙ|)             →  Adversarial robustness
```

**Regularizatsiya** — loss'ga norm qo'shish:

```
L_ridge(w) = Σ(xᵢw − yᵢ)²  +  λ‖w‖₂²
L_lasso(w) = Σ(xᵢw − yᵢ)²  +  λ‖w‖₁
                                 ↑
                        modul — sen bugun o'rgangan narsa
```

> Nima uchun Lasso ba'zi koeffitsientlarni **aynan nolga** tenglaydi, Ridge esa yo'q?
> Javob `|w|` funksiyasining `w = 0` nuqtasida **burchakli** ekanida (hosilasi yo'q),
> `w²` esa silliq. Bu — modul funksiyasining shakli haqidagi savol.

---

## 5. Bo'lakli funksiyalar → Aktivatsiya funksiyalari

**O'zbekcha:** Modul — bo'lakli (piecewise) funksiya. Neyron tarmoqlardagi barcha
asosiy aktivatsiyalar ham shunday:

```
ReLU(z)       = max(0, z)              = (z + |z|)/2
LeakyReLU(z)  = max(αz, z)             α ≈ 0.01
Hardtanh(z)   = max(−1, min(1, z))
Clipping      = max(lo, min(hi, z))
```

Hammasi — **tengsizlik bilan aniqlangan shartlar**:

```
ReLU(z) = 0     ⟺   z ≤ 0        ← tengsizlik (F4-b masalasi)
ReLU(z) = z     ⟺   z > 0        ← tengsizlik
```

> 🔗 **Dead ReLU problem:** agar neyronning kirishi har doim `z ≤ 0` bo'lsa, chiqishi
> doim 0, gradienti ham 0 → neyron **o'ladi**, hech qachon o'rganmaydi.
> Bu butunlay tengsizlik haqidagi masala.

---

## 6. Tengsizliklar → Learning rate va konvergensiya

**O'zbekcha:** F2 masalasida sen isbotlading:

```
f(x) = (a/2)x²   uchun   gradient descent yaqinlashadi  ⟺  0 < η < 2/a
```

Ko'p o'lchovli umumlashma:

```
0 < η < 2/λ_max(H)
              ↑
      Hessian'ning eng katta xos qiymati
```

**English:** This is the classical convergence condition for gradient descent on a
quadratic. Beyond it, the iterates oscillate and diverge — which is what you see as
`loss: nan` in training logs.

| Tengsizlik | AI'dagi nomi |
|------------|--------------|
| `0 < η < 2/L` | Learning rate bound (L — Lipschitz constant) |
| `‖g‖ ≤ c` | Gradient clipping |
| `\|w\| ≤ B` | Weight constraint / weight decay |
| `L_val > L_train + ε` | Overfitting detection |
| `\|L_k − L_{k−1}\| < tol` | Early stopping criterion |

---

## 7. Koshi–Shvarts → Cosine similarity

Bu — maktab algebrasidan LLM'gacha bo'lgan **eng qisqa ko'prik**:

```
Koshi–Shvarts:      |u · v|  ≤  ‖u‖ · ‖v‖

Ikkala tomonni ‖u‖·‖v‖ ga bo'lamiz:

                    |u · v|
                  ───────────  ≤  1
                   ‖u‖ · ‖v‖

                    |cos θ| ≤ 1
                    −1 ≤ cos θ ≤ 1
```

**Qayerda ishlatiladi:**
- **RAG / vector search:** hujjatlarni so'rovga o'xshashligi bo'yicha saralash
- **Embeddings:** `text-embedding` modellari chiqishini solishtirish
- **Attention:** `softmax(QKᵀ/√d)` — `QKᵀ` skalyar ko'paytmalar matritsasi
- **Contrastive learning (CLIP, SimCLR):** loss to'g'ridan-to'g'ri cosine similarity'ga quriladi

> Har safar "bu ikki matn 0.87 darajada o'xshash" deb ko'rganingda — o'sha `0.87`
> nima uchun 1 dan oshmasligini **sen endi isbotlay olasan**.

---

## 8. Uchburchak tengsizligi → Masofa va metrikalar

```
‖u + v‖ ≤ ‖u‖ + ‖v‖
```

**Metrika (distance) bo'lishi uchun 3 ta shart kerak:**

```
1. d(x,y) ≥ 0,  va  d(x,y) = 0 ⟺ x = y
2. d(x,y) = d(y,x)                          (simmetriya)
3. d(x,z) ≤ d(x,y) + d(y,z)                 ← UCHBURCHAK TENGSIZLIGI
```

**Qayerda kerak:**
- **k-NN, clustering (k-means, DBSCAN):** masofa tushunchasisiz ishlamaydi
- **Vector databases (FAISS, Pinecone):** indekslash algoritmlari uchburchak
  tengsizligiga tayanib qidiruvni tezlashtiradi
- **Embedding space:** "yaqin ma'no = yaqin vektor" g'oyasi shu shartga asoslanadi

---

## 9. Cheklovli optimizatsiya → SVM, KKT

**O'zbekcha:** Ba'zan minimum topish kerak, lekin **cheklovlar bilan**:

```
min  f(w)
w

shart:   gᵢ(w) ≤ 0        ←  TENGSIZLIK cheklovlari
         hⱼ(w) = 0        ←  TENGLAMA cheklovlari
```

**SVM (Support Vector Machine)** — klassik misol:

```
min  ½‖w‖²
w,b

shart:   yᵢ(w·xᵢ + b) ≥ 1      ← har bir ma'lumot nuqtasi uchun tengsizlik
```

Bu tengsizlik "har bir nuqta ajratuvchi chiziqdan kamida 1 birlik uzoqlikda bo'lsin"
degan ma'noni beradi — **margin** tushunchasi.

> Bu masalalar **KKT shartlari** (Karush–Kuhn–Tucker) orqali yechiladi — ular
> tenglamalar va tengsizliklarning birlashmasi. Hozir tushunish shart emas, lekin
> bilib qo'y: u yerda hech qanday sehr yo'q, faqat kengaytirilgan algebra.

---

## 10. Jadval: bugungi mavzudan AI'gacha

| Bugun o'rgangan | AI'dagi nomi | Qayerda uchraydi |
|-----------------|--------------|------------------|
| Chiziqli sistema | Normal equations `XᵀXw = Xᵀy` | Linear regression |
| 3 xil yechim holati | Determined / inconsistent / underdetermined | Model sig'imi, regularizatsiya |
| Gauss usuli (D5) | Gaussian elimination | `np.linalg.solve` ichida |
| Kvadrat funksiya, `a > 0` | Convexity, positive definite Hessian | Optimizatsiya kafolatlari |
| To'la kvadratga to'ldirish | Completing the square | Gaussian PDF, ridge regression |
| Diskriminant `D` | Kritik nuqta turi | Minimum / maksimum / egar nuqta |
| Modul `\|x\|` | L1 norm | Lasso, sparsity |
| `√(x²) = \|x\|` | L2 norm asosi | Ridge, weight decay |
| Bo'lakli funksiya | ReLU, clipping | Aktivatsiyalar |
| Tengsizlik yechish | Feasible region | Constrained optimization |
| Interval usuli | Sign analysis | Barqarorlik tahlili |
| `\|1 − ηa\| < 1` | Convergence condition | Learning rate tanlash |
| Koshi–Shvarts | Cosine similarity bound | RAG, embeddings, attention |
| Uchburchak tengsizligi | Metric axiom | k-NN, vector search |
| AM–GM | Bounding arguments | Isbotlarda |

---

## 11. Amaliy vazifa (mavzu oxirida)

`code/03_ai_bogliqlik.py` ni ishga tushir va quyidagilarni **o'z qo'ling bilan**
hisoblaganing bilan solishtir:

1. Linear regression koeffitsientlari (F1)
2. Learning rate chegarasi (F2) — turli `η` lar bilan tajriba qil
3. Cosine similarity va Koshi–Shvarts (F3)
4. Gradient clipping (F5)

Agar raqamlar mos kelsa — **sen matematikani ham, kodni ham tushunding**.
Agar mos kelmasa — bu eng qiziqarli holat: qayerda adashganingni top.

---

## 12. Keyingi mavzuga ko'prik

Keyingi mavzu — **Funksiyalar**. U shu yerdan o'sib chiqadi:

```
Tenglama:   f(x) = 0        →  "funksiya qayerda nolga aylanadi?"
Tengsizlik: f(x) > 0        →  "funksiya qayerda musbat?"
                                        ↓
                            Bularning ikkalasi ham FUNKSIYA haqida savol
```

Ya'ni bugun sen aslida funksiyalarni o'rganding — shunchaki ularni shunday
atamading. Keyingi papkada ularga nom beramiz.
