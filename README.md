<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">A/B Testing (A-B)</div>

# 1. Purpose

This repository contains a beginner-friendly example of **A/B testing** (2 variants) for an email campaign. It loads a small CSV dataset, compares key metrics, and runs basic statistical tests.

# 2. Project files

- **`ab_test_simple.py`**: A/B testing analysis for an email campaign (loads a CSV dataset, prints metrics, runs statistical tests, prints recommendations).
- **`ab_test_data.csv`**: Sample dataset used by `ab_test_simple.py`.
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
