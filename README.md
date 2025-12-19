<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">A/B Testing (A-B)</div>

# 1. Purpose

This repository contains beginner-friendly examples of **A/B testing** (2 variants) and **A/B/n testing** (3+ variants).

- The **A/B** example in the repository root analyzes an email-campaign dataset from a CSV file.
- The **A/B/n** example in `A-B-n/` runs with a built-in simulation (so it does not require a dataset file).

# 2. Project files

- **`ab_test_simple.py`**: A/B testing analysis for an email campaign (loads a CSV dataset, prints metrics, runs statistical tests, prints recommendations).
- **`ab_test_data.csv`**: Sample dataset used by `ab_test_simple.py`.
- **`A-B-n/`**: A/B/n testing example (see `A-B-n/README.md`).
- **`requirements.txt`**: Pip dependencies (useful if you prefer `pip` + virtualenv).
- **`environment.yml`**: Conda environment definition (recommended if you use conda).
- **`.gitignore`**: Git ignore rules.

# 3. Setup

## 3.1 Conda (recommended)

Create/update the environment:

```bash
conda env update -n A-B -f environment.yml
conda activate A-B
```

## 3.2 Pip

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

# 4. Run

```bash
python ab_test_simple.py
```

To run the A/B/n simulation example:

```bash
python A-B-n/abn-testing-python.py
```
