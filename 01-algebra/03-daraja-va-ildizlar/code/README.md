# 🐍 Daraja va Ildizlar — Python

> Avval qog'ozda. Keyin kod.

```bash
source /Users/macmini/Desktop/math/.venv/bin/activate
python3 01_daraja_ildiz.py     # A–E: hamma javoblar + Python tuzoqlari ((-2)**4, (-8)**(1/3))
python3 02_osish_va_float.py   # F: 2ⁿ vs n², qog'oz buklash, float32/16/bf16 chegaralari
python3 03_ai_bogliqlik.py     # G: norm, √n tajribasi, He init, RMSNorm, Noam lr (+ grafik)
```

| Fayl | Nima |
|------|------|
| `01_daraja_ildiz.py` | SymPy/Python bilan A–E javoblari; `-2**4` va `(-2)**4`; `np.cbrt` |
| `02_osish_va_float.py` | O'sish jadvali; `np.finfo`; `16777216 + 1`; `0.1 + 0.2`; fp16 overflow |
| `03_ai_bogliqlik.py` | `√n` — 10 000 tasodifiy vektor bilan; init tajribasi; RMSNorm; lr grafigi → `plots/` |
