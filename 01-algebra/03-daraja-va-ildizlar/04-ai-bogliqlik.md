# 🔗 Daraja va ildizlar AI'da qayerda / Where Powers and Roots Show Up in AI

> Ikki tilda. Maqsad: `√`, `x²`, `x^(−1/2)`, `2ⁿ`, `10⁻⁵` belgilarini ML formulasida
> ko'rganda — "bu maktab algebrasi" deb tanish.

---

## 0. Xarita

```
        x²                 √x                x^(−1/2)             2ⁿ, 10ⁿ            xᵃ (a<0)
        │                  │                    │                    │                  │
   MSE loss           L2 norm             RMSNorm              float32/16        Scaling laws
   variance           distance            Adam                 bit'lar           L ∝ N^(−α)
   L2 reg             RMSE                1/√d attention       param soni
   (a+b)²≠a²+b²       std = √var          1/√n init            FLOPs
                      ‖u+v‖ ≤ ‖u‖+‖v‖     η/√t                 1e-5, 1e9
```

---

## 1. `x²` — kvadrat hamma joyda

| Formula | Nomi | Nega kvadrat |
|---------|------|--------------|
| `L = (1/n)Σ(yᵢ − ŷᵢ)²` | MSE loss | Manfiy/musbat xato bir xil jazolanadi; silliq (hosilasi bor); katta xatoni ko'proq jazolaydi |
| `Var(x) = (1/n)Σ(xᵢ − μ)²` | Variance | O'rtachadan og'ish kvadrati — ishoradan qutulish |
| `λ‖w‖² = λΣwᵢ²` | L2 regularization / weight decay | Katta og'irliklarni jazolash |
| `‖u + v‖² = ‖u‖² + 2u·v + ‖v‖²` | Kosinus teoremasi | `(a+b)² = a² + 2ab + b²` ning vektor versiyasi |

**Oxirgisi muhim:** `(a + b)² ≠ a² + b²` xatosi vektorlarda `‖u + v‖² ≠ ‖u‖² + ‖v‖²` bo'lib
qaytadi. Tenglik faqat `u·v = 0` (perpendikulyar) bo'lganda — bu **Pifagor teoremasi**.

---

## 2. `√` — norm, masofa, standart og'ish

```
‖v‖₂ = √(v₁² + ... + vₙ²)              L2 norm (Evklid uzunligi)
d(u, v) = ‖u − v‖ = √(Σ(uᵢ − vᵢ)²)      Evklid masofasi
std = √Var                              standart og'ish
RMSE = √MSE                             root mean squared error
```

**Nima uchun ildiz?** `Σx²` — "kvadrat birlik"da. Ildiz — asl birlikka qaytaradi.
Metrlarni kvadratlasang m² bo'ladi; ildiz olsang yana metr.

**Ildiz xossalari → norm xossalari:**

| Ildiz | Norm |
|-------|------|
| `√(a²) = \|a\|` | `‖cv‖ = \|c\|·‖v‖` |
| `√a ≥ 0` | `‖v‖ ≥ 0`, `= 0 ⟺ v = 0` |
| `√(a+b) ≠ √a + √b` | `‖u+v‖ ≤ ‖u‖ + ‖v‖` (uchburchak) |

---

## 3. `√n` — n ta tasodifiy sonning yig'indisi

**Eng muhim intuitsiya** (ehtimollar mavzusida isbotlanadi, hozir his qil):

```
n ta tasodifiy ±1 ni qo'shsang, natija ~n EMAS, ~√n.
Chunki ko'pi bir-birini yo'qotadi.

n = 100:  yig'indi tipik jihatdan ±10 atrofida, ±100 emas.
```

Bu bitta fakt **uchta** ML formulasini tushuntiradi:

### 3.1 Attention: `softmax(QKᵀ/√d_k)`
`q·k` — `d_k` ta hadning yig'indisi → o'lchami `~√d_k` → `√d_k` ga bo'lsak `~1` →
softmax to'yinmaydi (hamma ehtimollik bitta tokenga yig'ilib qolmaydi).

### 3.2 Initialization: `std = √(2/n_in)` (He), `√(1/n_in)` (Xavier/LeCun)
Neyron `n` ta kirishni yig'adi → chiqish `~w√n` → `w ~ 1/√n` qilsak chiqish `~1` →
qatlamdan qatlamga signal portlamaydi, so'nmaydi.

### 3.3 Random walk / SGD shovqini
`t` qadamdan keyin tasodifiy yurish `~√t` uzoqlashadi. SGD shovqini ham shunday →
`η/√t` kamaytirish shovqinni muvozanatlaydi.

> **Bitta ildiz — uchta formula.** `code/03_ai_bogliqlik.py` da `√n` ni sonli ko'rasan.

---

## 4. `x^(−1/2)` — manfiy kasr ko'rsatkich

```
RMSNorm:   x̂ = x · (mean(x²) + ε)^(−1/2) · γ       LLaMA, Mistral, Gemma
LayerNorm: x̂ = (x − μ) · (σ² + ε)^(−1/2) · γ + β    BERT, GPT-2
Adam:      θ ← θ − η · m̂ · (√v̂ + ε)^(−1)            v̂ — gradient kvadratlarining o'rtachasi
Noam lr:   η = d^(−0.5) · min(t^(−0.5), t·w^(−1.5))  Transformer
```

Kodda `x**-0.5` yoki `torch.rsqrt(x)` — "reciprocal square root", alohida tez operatsiya.
`ε` (`1e-8`, `1e-5`) — nolga bo'lishdan himoya (1-mavzu: ODZ!).

---

## 5. `2ⁿ` — kompyuter sonlari

### 5.1 Float formatlari

```
float32:  ±(1.mantissa₂₃) × 2^(exp₈ − 127)     ε = 2⁻²³ ≈ 1.2e-7,   max ≈ 2¹²⁸ ≈ 3.4e38
float16:  ±(1.mantissa₁₀) × 2^(exp₅ − 15)      ε = 2⁻¹⁰ ≈ 1e-3,     max = 65504
bfloat16: ±(1.mantissa₇)  × 2^(exp₈ − 127)     ε = 2⁻⁷ ≈ 8e-3,      max ≈ 3.4e38
```

**Amaliy oqibatlar:**

| Muammo | Sabab | Yechim |
|--------|-------|--------|
| `loss = inf` fp16 da | `2¹⁶ = 65536 > 65504` — overflow | bfloat16 yoki loss scaling |
| Gradient `= 0` fp16 da | `< 2⁻²⁴ ≈ 6e-8` — underflow | loss scaling (×2ᵏ, keyin ÷2ᵏ) |
| `0.1 + 0.2 != 0.3` | 0.1 ikkilikda cheksiz | `abs(a − b) < eps` bilan tekshir |
| `16777217.0f == 16777216.0f` | `2²⁴` dan keyin butun sonlar sakraydi | indekslar uchun int64 |
| Softmax `exp(1000) = inf` | `e¹⁰⁰⁰ > 2¹²⁸` | `exp(x − max(x))` (log-sum-exp trick) |

### 5.2 Hisoblash hajmi

```
Parametrlar:   BERT 1.1e8 · GPT-2 1.5e9 · GPT-3 1.75e11 · Llama-3 4e11
Xotira (fp16): N × 2 bayt.  175e9 × 2 = 350 GB.  Bitta H100 = 80 GB → 5 ta kerak (faqat saqlash!)
Training:      FLOPs ≈ 6·N·D.  GPT-3: 6 × 1.75e11 × 3e11 ≈ 3e23
Kontekst:      attention O(n²):  n = 4096 → 1.7e7;  n = 128k → 1.6e10  (100× uzun → 1000× qimmat)
```

### 5.3 Kombinatorik portlash

```
Vocab 50 000, ketma-ketlik 10 token:  50 000¹⁰ ≈ 10⁴⁷ ta mumkin ketma-ketlik
Shuning uchun LLM "hamma variantni saqlash" emas, funksiyani O'RGANADI.
```

---

## 6. `xᵃ` (a kichik manfiy) — scaling laws

```
L(N) = (N_c/N)^α,   α ≈ 0.076        (Kaplan 2020)
L(D) = (D_c/D)^β,   β ≈ 0.095
Chinchilla:  L(N,D) = E + A/N^0.34 + B/D^0.28
```

`N` 10 marta oshsa → `L` `10^(−0.076) ≈ 0.84` marta → **16% pasayish**. Yana 10 marta →
yana 16%. Bu — darajali funksiya (§8 nazariya). **Log-log grafikda to'g'ri chiziq** —
keyingi mavzu (logarifmlar) buni tushuntiradi.

---

## 7. `m × 10ⁿ` — hyperparametr tili

```
lr = 3e-4           "uch e minus to'rt" = 0.0003     ← Karpathy konstantasi (Adam uchun)
weight_decay = 1e-2
eps = 1e-8
batch = 2**19 = 524 288 tokens
warmup = 2000, max_steps = 1e5
```

`3e-4` va `1e-3` orasidagi farq — `3.3×`. Bu "kichik farq" emas — lr tanlashda tartib (10ˣ)
muhim, aniq raqam emas. Shuning uchun lr `1e-5, 3e-5, 1e-4, 3e-4, 1e-3` **log-shkalada** qidiriladi.

---

## 8. Polinomial features va ko'phad

```
Chiziqli model:      y = w₁x + b
Polinomial (d=3):    y = w₃x³ + w₂x² + w₁x + b     ← x², x³ — yangi "feature"lar
```

`sklearn.PolynomialFeatures(degree=3)` — aynan shu. Overfitting → yuqori daraja → §8 nazariya:
katta `a` da `xᵃ` juda tez o'sadi → ma'lumot tashqarisida model "portlaydi".

---

## 9. Jadval: bugungi mavzu → AI

| Daraja/ildiz | AI'dagi nomi | Qayerda |
|--------------|--------------|---------|
| `x²` | MSE, variance, L2 reg | Har regressiya |
| `(a+b)² = a²+2ab+b²` | `‖u+v‖² = ‖u‖²+2u·v+‖v‖²` | Kosinus teoremasi, Pifagor |
| `√(Σx²)` | L2 norm, distance, RMSE, std | Hamma joyda |
| `√(a²) = \|a\|` | `‖cv‖ = \|c\|‖v‖` | Norm xossasi |
| `√(a+b) ≠ √a+√b` | Uchburchak tengsizligi | Metrikalar |
| `√n` | `1/√d_k`, `√(2/n)` init, `η/√t` | Attention, init, schedule |
| `x^(−1/2)` | `rsqrt`, RMSNorm, LayerNorm, Adam | Har Transformer qatlami |
| `2ⁿ` | float32/16/bf16, `2²⁴`, `2⁻²³` | Numerical stability |
| `aˣ = aʸ ⟺ x = y` | Logarifmga zarurat | Keyingi mavzu |
| `xᵃ`, `a < 0` | Scaling laws | Research |
| `m × 10ⁿ` | `3e-4`, `1e-8` | Hyperparametrlar |
| `x²`, `x³` features | PolynomialFeatures | Klassik ML |

---

## 10. Amaliy vazifa

`code/03_ai_bogliqlik.py`:
1. `√n` tajribasi: 10 000 ta tasodifiy ±1 vektor juftligi, skalyar ko'paytma std'si `√d` ga yaqinmi?
2. He init: `n_in` ta kirishli qatlam chiqishi std'si — `1/√n` bilan va usiz.
3. RMSNorm qo'lda va NumPy'da.
4. Noam lr schedule grafigi.
5. float32/16 chegaralari: `np.finfo`, `16777216 + 1`, `0.1 + 0.2`.

---

## 11. Keyingi mavzuga ko'prik — Logarifmlar

```
2ˣ = 32   →  x = 5        asosni tenglashtirdik
2ˣ = 10   →  x = ?        tenglashtirib bo'lmaydi  →  x = log₂10 ≈ 3.32
```

**Logarifm** — `aˣ = b` ni yechish uchun. AI'da:
- `cross_entropy = −Σ y log(ŷ)` — **har bir** klassifikatsiya loss'i
- `log_softmax`, `logsumexp` — sonli barqarorlik
- `log(P)` — ehtimolliklar ko'paytmasini yig'indiga aylantirish
- Log-log grafik — scaling laws to'g'ri chiziqqa aylanadi
- `perplexity = 2^(cross_entropy)` — daraja va log birga

Daraja qoidalarini yaxshi bilsang, logarifm qoidalari — ularning **ko'zgu aksi**:
`aᵐaⁿ = aᵐ⁺ⁿ` ↔ `log(mn) = log m + log n`.
