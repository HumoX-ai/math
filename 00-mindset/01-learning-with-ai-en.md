# Learning With AI: The Main Risk and How to Escape It

> You wrote: *"Ever since AI came out, I've started trusting it too much."*
> This file is about exactly that — not motivational slogans, but the mechanism and the rules.

---

## 1. The real name of the problem: **the fluency illusion**

When AI explains something, the text is **clear, ordered, fluent**. You read it, and your
brain produces this feeling:

> "Yes, I understand."

That feeling is **a lie**. In psychology it is called the *fluency illusion*, or the
*illusion of explanatory depth*.

The reason is simple:

| What you feel | What actually happened |
|---------------|------------------------|
| "This makes sense" | You **recognized** it (recognition) |
| "I know this" | Not the same as being able to **recall** it |
| "That was easy" | Someone else absorbed the difficulty for you |

**Recognition** and **recall** are two completely different processes in the brain.
Reading a book and saying "I got it" is the first one. Writing it on a blank sheet from
memory is the second. Exams, jobs, and real problems always ask for the second.

**Test yourself now:** without looking at anything, **derive** the quadratic formula on a
blank page (not from memory — starting from `ax² + bx + c = 0`). If you can't, you don't
know it. You only recognize it.

---

## 2. Why AI breaks learning: **desirable difficulties**

Robert Bjork's research on *desirable difficulties*:

> **Difficulty during learning is not a defect. It is the mechanism.**

The brain only rewires when it meets **resistance**. When you struggle with a problem for
20 minutes, your brain:

1. searches existing knowledge,
2. links pieces together,
3. marks the failed attempts,
4. and when the right answer arrives, writes it down **strongly**.

If you get the answer from AI immediately, **steps 1–3 are skipped**. The answer enters
your head but **connects to nothing**. In three days it is gone.

```
STRUGGLE  →  ATTEMPT  →  ERROR  →  EXPLANATION  →  DURABLE KNOWLEDGE   ✅
                                       ↑
                                AI belongs here

EXPLANATION  →  feeling of "I get it"  →  3 days  →  nothing              ❌
     ↑
AI is harmful here
```

**In one sentence:** use AI **after** the difficulty, never **instead of** it.

---

## 3. The generation effect

Research is consistent: if you **produce** an answer yourself — even a wrong one — and
then see the correct one, retention is substantially higher than if you had simply read
the correct answer.

Which means:

> **A failed attempt is not wasted time. A failed attempt is the hook the correct answer hangs on.**

That is why in this repository the problems and the solutions live in **separate files**.

---

## 4. Cognitive offloading

When a person relies on an external tool for a task, the brain **stops storing that
information** — it computes that "I can fetch it again if needed." This has been studied
extensively with calculators, GPS, and search engines ("digital amnesia").

AI is the most powerful form of this effect, because it takes over not just the
**information** but the **thinking process** itself.

To be honest: research specifically on LLMs is young, and strong long-term conclusions
would be premature. But the generation effect and retrieval practice are decades old and
very robust. They point clearly in the same direction.

---

## 5. The strongest motivation: **AI makes mistakes, and you must be able to see them**

This is not a depressing fact — it is an **empowering** one:

- AI makes arithmetic slips.
- AI can write a **wrong proof** in a completely confident tone.
- AI can drop a sign (`≤` vs `<`), forget the domain, or miss edge cases.
- AI can **agree with you** when you are wrong.

So the question is:

> **If you don't know the math, how would you ever know the AI was wrong?**

You wouldn't. And if you can't, you are not an **engineer working with AI** — you are a
**person copying AI output**. There is an entire career gap between those two.

```
No math + AI  =  no choice but to trust the output
Math    + AI  =  AI becomes a 10x accelerator you control
```

**You are not learning math to replace AI. You are learning math to supervise it.**

This is especially true for your goal (AI → DL → LLM → AGI). The core job in that field is
answering **"why did the model produce this?"** — and there is no answer to that question
without mathematics.

---

## 6. 🔒 THE AI USAGE CONTRACT

Print this. Follow it daily.

### ❌ FORBIDDEN

1. Reading a problem and immediately pasting it into AI.
2. "Explain this to me" — **as the first step**.
3. Copying a solution and moving on because "I understood it."
4. Accepting an AI solution without verifying it.
5. Having AI do the work for you. (You are not the client here — you are the **student**.)

### ✅ ALLOWED

1. **The 15-minute rule.** Work on the problem **yourself**, on paper, for at least 15
   minutes. Only then may you ask AI.

2. **Ask for a hint, not an answer:**
   > "I'm solving this problem. Here is my attempt: [...]. Do **not** give me the answer.
   > Give me exactly one hint and tell me where my reasoning went wrong."

3. **AI as a grader, not a teacher.** After you've solved it:
   > "Here is my solution: [...]. Check it. If it's wrong, tell me **where** and **why**,
   > but do not write out the correct solution."

4. **Reverse Feynman technique.** You explain, AI criticizes:
   > "I'm going to explain the sign-chart method to you. Ask me questions like a curious
   > 12-year-old and find the gaps in my explanation."

5. **Problem generator** — AI's single most useful role:
   > "Give me 10 problems on quadratic inequalities. No solutions. Make 3 of them hard,
   > and make 1 of them have no solution."

6. **Bug hunt.** Once a month:
   > "Write a solution about quadratic equations, but plant **exactly one serious error**
   > in it. Don't tell me where."
   > Then find it yourself. This is the single best exercise.

---

## 7. Daily routine (45–90 minutes)

```
┌──────────────────────────────────────────────────────────┐
│ 0–5 min    Blank-page test: write what you remember      │
│            from yesterday. Look at nothing.              │
├──────────────────────────────────────────────────────────┤
│ 5–20 min   Read new theory. Do NOT copy it — rewrite     │
│            it in your own words.                         │
├──────────────────────────────────────────────────────────┤
│ 20–60 min  Solve problems. On paper. Phone in another    │
│            room. If stuck → the 15-minute rule.          │
├──────────────────────────────────────────────────────────┤
│ 60–75 min  Open the solutions file. Compare.             │
│            Log every mistake in your Error Notebook.     │
├──────────────────────────────────────────────────────────┤
│ 75–85 min  Verify with Python (code/ folder).            │
├──────────────────────────────────────────────────────────┤
│ 85–90 min  Fill in the progress log. Three lines is fine.│
└──────────────────────────────────────────────────────────┘
```

---

## 8. Spaced repetition schedule

The forgetting curve is brutal: most new material disappears within days — **unless it is
retrieved**. The fix is expanding intervals:

| Review | When | What to do |
|--------|------|------------|
| 1 | Same evening | 5 min: key formulas on a blank page |
| 2 | +1 day | 10 min: re-solve 2 problems |
| 3 | +3 days | 10 min: self-test with the checklist |
| 4 | +7 days | 15 min: the 3 hardest problems |
| 5 | +21 days | 15 min: explain the topic to AI |

That's what `06-checklist.md` in each topic folder is for.

---

## 9. The Error Notebook (the most underrated tool that exists)

Open `00-mindset/xatolar-daftari.md` (the Error Notebook). Three lines per mistake:

```markdown
### 2026-09-12 — Forgot to flip the sign when dividing by a negative
- Problem: -3x > 6 → I wrote x > -2. Correct: x < -2.
- Cause: I solved it on autopilot, like an equation.
- Prevention: draw a ⚠️ in the margin before any division by a negative.
```

Read this notebook a month later and you will see **a map of your own brain**.
That is the one thing AI cannot give you.

---

## 10. Summary

| Wrong model | Right model |
|-------------|-------------|
| AI is my teacher | AI is my **training partner** |
| AI gives answers | AI gives **questions and verification** |
| I learn from AI | I learn from **difficulty**; AI tunes the difficulty |
| I trust AI | I **verify** AI — because I know the material |

> You love AI. That isn't a problem. But love and trust are different things.
> Love AI — and **verify** it. This repository is how you earn the ability to verify.

---

**Next file:** [02-motivation-and-psychology-en.md](02-motivation-and-psychology-en.md)
