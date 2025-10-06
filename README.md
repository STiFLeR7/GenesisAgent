# 🌱 GenesisAgent v1.0.0

> **Autonomous Creative Evolution Engine — No LLMs, No RAG, Pure Idea Evolution.**

---

## 🚀 Overview

**GenesisAgent** is an **autonomous creative ideation and evolution system** — a lightweight Python agent that generates, mutates, scores, polishes, and preserves innovative ideas **without using LLMs or RAG**.

It mimics **biological evolution** — generating raw idea DNA, applying mutations (context, materials, features), scoring based on heuristic novelty, and evolving the fittest ideas across generations.

This makes GenesisAgent capable of **offline autonomous creativity**, suitable for **edge AI research**, **creativity automation**, or **idea generation pipelines**.

---

## 🧠 Core Features

### 💡 Idea Generation

* Creates raw idea seeds from a curated set of creative templates.
* Deterministic reproducibility with random seeds.

### 🔁 Evolution Engine

* Multi-generation idea refinement.
* Mutation, recombination, and selection pipeline.
* Supports configurable evolution depth and twist count.

### 🧩 Mutator

* Introduces adaptive traits, environments, materials, and usage contexts.
* Example mutations:

  * `for children`
  * `using self-healing polymers`
  * `in extreme weather zones`
  * `with gesture control`

### ⚙️ Scorer

* Heuristic-based evaluation of **novelty**, **creativity**, and **feasibility**.
* Rewards innovation buzzwords (e.g., *AI, adaptive, wearable, biodegradable*).
* Produces normalized 0–1 scores with slight randomness for diversity.

### 🧼 Polisher

* Refines phrasing and visual presentation of ideas.
* Adds ✨ emojis and balanced formatting.

### 🤖 Autonomous Mode

* Fully self-driven idea evolution (no input required).
* Saves the top ideas to `src/core/best_ideas.json`.

### 🧹 Cleaner

* Deduplicates and normalizes saved ideas using regex normalization.

---

## 🧩 CLI Commands

GenesisAgent provides a **modern command-line interface** using [`click`](https://click.palletsprojects.com/) and [`rich`](https://rich.readthedocs.io/).

| Command                                      | Description                                |
| -------------------------------------------- | ------------------------------------------ |
| `python cli.py generate --n 3`               | Generate N creative ideas.                 |
| `python cli.py evolve --n 5 --generations 3` | Run controlled multi-generation evolution. |
| `python cli.py polish "idea text"`           | Refine a specific idea.                    |
| `python cli.py auto --n 5 --generations 4`   | Run fully autonomous idea evolution.       |
| `python cli.py clean-best`                   | Clean and dedupe stored ideas JSON.        |

---

## 🧬 Example Autonomous Run

```
(.venv) PS D:\GenesisAgent> python cli.py auto --n 5 --generations 3

Generation 0
  Idea 1: A mirror that gives micro-coaching during routines
  Idea 2: Earbuds that summarize your day into a journal
  Idea 3: A desk that auto-tunes height/lighting to focus
  Idea 4: Furniture that adapts its shape based on mood
  Idea 5: Shoes that harvest kinetic energy for IoT devices

Generation 3
  Idea 1: Furniture that adapts its shape based on mood — using self-healing polymers — that learns from user feedback — with micro-goals and for urban environments
  Idea 2: Shoes that harvest kinetic energy for IoT devices — that personalizes via biometrics — for athletes — for disaster relief and with recycled plastics
  Idea 3: A mirror that gives micro-coaching during routines — with nanomaterials — with recycled plastics — with collaborative features
  Idea 4: A desk that auto-tunes height/lighting to focus — for underwater habitats and with haptic feedback — in extreme weather zones — that adapts in real-time
  Idea 5: Earbuds that summarize your day into a journal — with peer-to-peer sharing — with AR overlays and for elderly — for disaster relief and with streak rewards

[Storage] ✅ Saved 5 ideas to src/core/best_ideas.json
```

---

## ⚙️ Tech Stack

| Component         | Technology               |
| ----------------- | ------------------------ |
| Language          | Python 3.10+             |
| CLI Framework     | `click`                  |
| Output Formatting | `rich`                   |
| Storage           | JSON + `pathlib`         |
| Randomization     | Python `random` (seeded) |
| Cleaning          | Regex (`re`)             |

No LLMs. No RAG. 100% rule-based, evolutionary creativity.

---

## 📁 Project Structure

```
GenesisAgent/
├── cli.py
├── src/
│   └── core/
│       ├── generator.py
│       ├── mutator.py
│       ├── evolution.py
│       ├── polisher.py
│       ├── scorer.py
│       ├── storage.py
│       ├── autonomous.py
│       └── best_ideas.json
└── README.md
```

---

## 🧠 How It Works (Simplified Flow)

1. **Generate** → Create random idea seeds.
2. **Mutate** → Apply adaptive/contextual changes.
3. **Score** → Rate ideas heuristically.
4. **Select** → Keep top N ideas.
5. **Repeat** → Continue for multiple generations.
6. **Store** → Save best-performing ideas.

---

## 🔮 Future Roadmap (v2.0.0+)

* 🌐 **Web Dashboard** (FastAPI / Streamlit) for visual evolution tracking.
* 🧩 **Knowledge Graph Memory** — reuse past ideas for hybrid mutations.
* 🧠 **Hybrid LLM Mode (Optional)** for polishing and context evaluation.
* 📊 **Visualization Module** — track idea fitness over time.
* 💾 **Cross-Breeding Engine** — combine features from top-performing ideas.
* 🧮 **Quantized Edge Inference** — deploy on low-resource devices.


## 🧑‍💻 Author

**STiFLeR** — AI/ML Researcher, Edge AI Developer, and Founder of CudaBit.
Focus: Efficient, deployable, and research-backed AI systems.

---

## ⚡ License

MIT License — free for research and development use.

---

> *GenesisAgent v1.0.0 — Where creativity evolves, autonomously.*
