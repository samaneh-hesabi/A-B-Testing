<div style="font-size:2.5em; font-weight:bold; text-align:center; margin-top:20px;">A/B Testing (A-B)</div>

# 1. Purpose

This repository is a beginner-friendly example of **A/B testing analysis** for an email campaign. It loads a small dataset and compares key metrics (open rate, click rate, purchase rate, revenue), then runs basic statistical tests.

# 2. Project files

- **`ab_test_simple.py`**: Main script that loads the dataset, prints summary tables, runs statistical tests, and prints recommendations.
- **`ab_test_data.txt`**: Sample dataset (CSV-formatted text) used by the script.
- **`requirements.txt`**: Pip dependencies (useful if you prefer `pip` + virtualenv).
- **`environment.yml`**: Conda environment definition (recommended if you use conda).
- **`aaa.ipynb`**: Notebook (exploration/experiments).
- **`ddd.py`**: Extra Python script (misc/experiments).

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
