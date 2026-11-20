---
license: cc-by-4.0
task_categories:
- text-classification
language:
- en
tags:
- code
pretty_name: Spam Detection
size_categories:
- n<1K
---
# Spam-Detection-500 Dataset

A synthetic dataset of 500 plus text messages labeled as spam (1) or ham (0).

## Dataset Structure

- **Format**: JSON
- **Samples**: 500+
- **Fields**:
  - `text`: Message content (string)
  - `label`: 0 for ham, 1 for spam (integer)

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("87praveen33/Spam-Detection-500")