---
configs:
- config_name: spambase
  data_files:
  - path: spambase/train.csv
    split: train
  default: true
language: en
license: cc
pretty_name: Spambase
size_categories: 1M<n<10M
tags:
- tabular_classification
- binary_classification
- multiclass_classification
task_categories:
- tabular-classification
---
# Spambase
The [Spambase dataset](https://archive.ics.uci.edu/ml/datasets/Spambase) from the [UCI ML repository](https://archive.ics.uci.edu/ml/datasets).
Is the given mail spam?

# Configurations and tasks
| **Configuration** | **Task**                  | **Description**  |
|-------------------|---------------------------|------------------|
| spambase          | Binary classification     | Is the mail spam?|


# Usage
```python
from datasets import load_dataset

dataset = load_dataset("mstz/spambase")["train"]
```