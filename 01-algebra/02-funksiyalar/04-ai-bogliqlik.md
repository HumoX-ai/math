# 🔗 Funksiyalar AI'da qayerda / Where Functions Show Up in AI

> Ikki tilda: o'zbekcha tushuntirish, inglizcha atamalar. Maqsad: "neyron tarmoq —
> bu funksiya" degan gapni **his qilish**, shunchaki bilish emas.

---

## 0. Bitta jumla

```
MODEL  =  FUNKSIYA  fθ : kirish → chiqish,   θ — parametrlar (w, b)
TRAINING  =  "ma'lumotga eng yaxshi mos keladigan θ ni topish"
```

Hamma narsa shu ikki qatordan kelib chiqadi.

---

## 1. Har bir qatlam — chiziqli funksiya (§6)

```
Maktab:       y = kx + b
1 kirish:     y = wx + b
n kirish:     y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b  =  w·x + b
m chiqish:    y = Wx + b        W — m×n matritsa (linear algebra'da)
PyTorch:      nn.Linear(n, m)
```

| Maktab | ML | Ma'no |
|--------|----|----|
| `k` (slope) | `w` (weight) | kirish qanchalik ta'sir qiladi |
| `b` (y-kesma) | `b` (bias) | kirishdan mustaqil siljish |
| ikki nuqtadan `k, b` topish | training | ma'lumotdan parametr topish |

> `nn.Linear(784, 10)` — bu 784 ta kirishli, 10 ta chiqishli **chiziqli funksiya**.
> MNIST raqamlarni tanish uchun birinchi model — shu. Sen B4 va G1 da uning 1 o'lchovli
> versiyasini qo'lda o'rgatding.

---

## 2. Neyron tarmoq — kompozitsiya (§10)

```
y = fₙ ∘ σ ∘ fₙ₋₁ ∘ σ ∘ ... ∘ σ ∘ f₁ (x)

     x ──►[f₁]──►[σ]──►[f₂]──►[σ]──► ... ──►[fₙ]──► y
          linear  ReLU  linear  ReLU         linear
```

- **Depth** (chuqurlik) = kompozitsiyadagi funksiyalar soni.
- **Width** (kenglik) = har bir `fᵢ` ning chiqishlar soni.
- **Forward pass** = kompozitsiyani ichkaridan tashqariga hisoblash (E7 da qilganing).
- **Backward pass** (keyingi mavzular) = zanjir qoidasi — kompozitsiyaning hosilasi.

### Nima uchun aktivatsiya kerak — isbot (yana bir marta, chunki muhim)

```
(ax + b) ∘ (cx + d) = a(cx + d) + b = (ac)x + (ad + b)     ← chiziqli
```

**Xulosa:** aktivatsiyasiz 1000 qatlam = 1 qatlam. Butun "deep" so'zi — `σ` tufayli.

> Bu — `04-ai-bogliqlik.md` dagi eng muhim jumla. Uni bo'sh qog'ozga isbotlay olishing kerak.

---

## 3. Aktivatsiyalar — range tanlash (§3, §13)

| Funksiya | Formula | Range | Qayerda |
|----------|---------|-------|---------|
| Sigmoid | `1/(1+e⁻ˣ)` | (0, 1) | binary klassifikatsiya chiqishi, gates (LSTM) |
| tanh | `(eˣ−e⁻ˣ)/(eˣ+e⁻ˣ)` | (−1, 1) | RNN, markazlashgan chiqish kerak bo'lsa |
| ReLU | `max(0, x)` | [0, ∞) | deyarli hamma yashirin qatlamlar |
| LeakyReLU | `max(0.01x, x)` | ℝ | dead ReLU'ga qarshi |
| GELU / SiLU | silliq ReLU | ≈[−0.17, ∞) | Transformer'lar (GPT, BERT) |
| Softmax | `eᶻⁱ/Σeᶻʲ` | (0,1), Σ=1 | ko'p sinfli chiqish, attention og'irliklari |

**Range = chiqish qanday bo'lishi mumkin.** Ehtimollik kerak → (0,1) → sigmoid.
Manfiy ham bo'lsin → tanh. Yashirin qatlam → ReLU (arzon, to'yinmaydi).

---

## 4. Bo'lakli funksiyalar — ReLU tarmoq nima quradi (§12, G3)

```
ReLU(x − 1) + ReLU(1 − x) = |x − 1|          ← 2 neyron
2 + ReLU(x − 2) = max(x, 2)                  ← 1 neyron + bias
```

**Fakt:** ReLU-tarmoq har doim **bo'lakli chiziqli** funksiya chiqaradi. Neyronlar ko'p
bo'lsa, bo'laklar ko'p, egri chiziqqa yaqinlashadi. Bu **universal approximation theorem**
ning intuitsiyasi: yetarlicha keng bitta yashirin qatlam istalgan uzluksiz funksiyani
xohlagancha aniq taxminlay oladi.

---

## 5. Loss — parametrlar funksiyasi (§7, G5)

```
L(w) = Σ(wxᵢ − yᵢ)²  =  14w² − 50w + 45        ← G5 da chiqarding
```

| Parametrlar soni | Loss shakli | Nomi |
|------------------|-------------|------|
| 1 | parabola | — |
| 2 | piyola (paraboloid) | bowl |
| millionlab | ko'rinmas | **loss landscape** |

**Gradient descent** = parabola cho'qqisiga dumalab tushish:
```
w ← w − η · L'(w)        L'(w) = 28w − 50  (calculus'da)
```
Cho'qqida `L'(w*) = 0` → `28w = 50` → `w* = 25/14` — G5 dagi javob.

**Convex** (qavariq) = "bitta chuqurlik, lokal minimum yo'q" = parabola shakli.
Chiziqli regressiya loss'i convex — kafolatlangan yechim. Neyron tarmoq loss'i
non-convex — ko'p chuqurliklar, shuning uchun qiyin.

---

## 6. Almashtirishlar — normalizatsiya (§9, G4)

```
z = (x − μ)/σ          ← chapga μ, siqish 1/σ.  Bu §9 dagi f(x−c) va a·f(x).
x = σz + μ             ← teskari funksiya (denormalizatsiya)
```

| Nomi | Formula | Qayerda |
|------|---------|---------|
| Min-max | `(x − min)/(max − min)` | rasm pikseli [0,255] → [0,1] |
| Z-score / Standardization | `(x − μ)/σ` | tabular data, `StandardScaler` |
| BatchNorm | `(x − μ_batch)/σ_batch · γ + β` | CNN qatlamlari orasida |
| LayerNorm | `(x − μ_layer)/σ_layer · γ + β` | Transformer'ning har qatlamida |

BatchNorm/LayerNorm'dagi `γ`, `β` — **o'rganiladigan** `k` va `b`. Ya'ni normalizatsiyadan
keyin yana bitta chiziqli funksiya.

---

## 7. Teskari funksiyalar (§11)

| `f` | `f⁻¹` | Ma'no |
|-----|-------|-------|
| `exp` | `log` | log-probabilities ↔ probabilities |
| `sigmoid` | `logit = ln(p/(1−p))` | ehtimollik ↔ "xom" ball (logit) |
| normalize | denormalize | model ichida ↔ odam o'qiydigan |
| `tokenizer.encode` | `tokenizer.decode` | matn ↔ raqamlar |
| encoder | decoder | ma'lumot ↔ siqilgan ko'rinish (autoencoder, VAE) |
| forward diffusion | reverse diffusion | rasm → shovqin ↔ shovqin → rasm |

**Muhim:** encoder/decoder — **taxminan** teskari. `decode(encode(x)) ≈ x`, `=` emas.
Farq — **reconstruction loss**. Aniq teskari funksiya bo'lsa, siqish yo'q edi.

---

## 8. Monotonlik — tartib saqlanadi (§8.2)

```
softmax monoton  ⟹  argmax(z) = argmax(softmax(z))
```

Amaliy natija: inference'da softmax hisoblash **shart emas** — eng katta logit'ni ol.
`log` monoton → `argmax P = argmax log P` → shuning uchun log-likelihood bilan ishlash
mumkin (sonlar kichik bo'lib ketmaydi).

---

## 9. Juft/toq — simmetriya (§8.1)

- `MSE = (y − ŷ)²` — juft: `+2` xato va `−2` xato bir xil jazolanadi.
- `tanh` — toq: `tanh(−x) = −tanh(x)`, manfiy signal aynan aks.
- Data augmentation: rasmni gorizontal aylantirish = `f(−x)` (§9) — model bunga
  **invariant** bo'lishini xohlaymiz.

---

## 10. Grafik o'qish — training curve (§4)

```
loss
  │╲
  │ ╲
  │  ╲___          ← yaxshi: kamayadi, tekislanadi
  │      ‾‾‾‾‾‾
  └──────────── epoch

loss
  │╲    ╱╲
  │ ╲  ╱  ╲  ╱     ← yomon: sakraydi — learning rate katta (oldingi mavzu F2!)
  │  ╲╱    ╲╱
  └──────────── epoch

loss
  │╲  train
  │ ╲______
  │╲       val      ← overfitting: val yana o'sadi
  │ ╲__╱‾‾‾
  └──────────── epoch
```

Bu — funksiya grafigini o'qish. Kamayuvchi? Minimum qayerda? Ikki funksiya qayerda
ajraladi? — §4 va §8 savollari.

---

## 11. Jadval: bugungi mavzu → AI

| Funksiyalar mavzusi | AI'dagi nomi |
|---------------------|--------------|
| `f(x) = kx + b` | `nn.Linear`, weight & bias |
| Ikki nuqtadan `k, b` | Training (eng oddiy) |
| Jadval → formula | Dataset → model |
| Domain | Input space, valid inputs |
| Range | Output space; aktivatsiya tanlash |
| Kompozitsiya `f∘g` | Layer stacking, depth |
| `(ax+b)∘(cx+d)` chiziqli | Aktivatsiyasiz chuqurlik befoyda |
| Bo'lakli funksiya | ReLU, clip, Huber, ReLU-tarmoq chiqishi |
| Kvadrat funksiya cho'qqisi | Loss minimum, convexity |
| `f(x−μ)/σ` | Normalization, BatchNorm, LayerNorm |
| Teskari funksiya | encode/decode, log/exp, logit/sigmoid |
| Monotonlik | argmax invariantligi, log-likelihood |
| Juft/toq | MSE simmetriyasi, tanh, augmentation |
| Grafik o'qish | Training curve tahlili |

---

## 12. Amaliy vazifa

`code/03_ai_bogliqlik.py`:
1. E7 tarmog'ini kodda qur, grafigini ko'r — bo'lakli chiziqli.
2. G3: `|x − 1|` ni ReLU'lardan qur, 200 tasodifiy neyron bilan `sin(x)` ni taxminlab ko'r.
3. G5: `L(w)` parabolasini chiz, gradient descent cho'qqiga tushishini ko'r.
4. Sigmoid xossalarini sonli tekshir.

---

## 13. Keyingi mavzuga ko'prik

**Daraja va ildizlar.** Nima uchun kerak:
- `‖x‖ = √(Σxᵢ²)` — norm (L2) — ildiz
- `1/√d_k` — attention scaling — ildiz
- `x²` — MSE; `x^(−1/2)` — RMSNorm, Adam
- `2ⁿ` — hisoblash hajmi, `10⁹` parametrlar — daraja
- `e^x` — sigmoid, softmax — daraja (asos `e`)

Funksiya haqida bilganing bilan endi **darajali funksiyalar** oilasini o'rganasan.
