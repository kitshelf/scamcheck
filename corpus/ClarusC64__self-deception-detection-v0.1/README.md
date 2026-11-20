---
language: en
license: mit
task_categories:
- text-classification
tags:
- self-deception
- stability-geometry
- reasoning
- clarus
- sios
size_categories:
- n<1K
pretty_name: Self-Deception Detection v0.1
---

# What this dataset does

This dataset tests whether a model can detect self-deception.

The task is simple:

Given a scenario and a self-deception claim, predict whether the claim is supported.

# Core stability idea

Self-deception occurs when a system maintains a preferred narrative despite contradictory evidence.

Common signs include:

- externalizing blame
- ignoring contradictory evidence
- preserving identity over accuracy
- selective interpretation
- rationalization
- narrative protection

Self-deception is dangerous because it prevents corrective action.

# Prediction target

Binary label:

- 1 = self-deception is present
- 0 = self-deception is not present

# Row structure

Each row contains:

- scenario_id
- scenario_text
- claim
- label

# Files

- data/train.csv
- data/test.csv
- scorer.py
- README.md

# Evaluation

```bash
python scorer.py --predictions predictions.csv --truth data/test.csv

Structural Note

This dataset is intentionally small.

Its purpose is to test whether a model can recognize narrative preservation in the face of conflicting evidence.

The hidden value is in detecting rationalization, blame displacement, evidence avoidance, and identity-protective reasoning.

License

MIT