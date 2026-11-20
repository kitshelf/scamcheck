---
license: cc-by-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.parquet
  - split: test
    path: data/test.parquet
task_categories:
- text-classification
- tabular-classification
- token-classification
- text2text-generation
size_categories:
- n<1K
annotations_creators:
- found
tags:
- phishing
- url
- security
language:
- en
pretty_name: TabNetone
---



# Dataset Description

The provided dataset includes **11430** URLs with **87** extracted features.  
The dataset are designed to be used as a benchmark for machine learning based **phishing detection** systems.  
The datatset is balanced, it containes exactly 50% phishing and 50% legitimate URLs.  

Features are from three different classes:
- **56** extracted from the structure and syntax of URLs
- **24** extracted from the content of their correspondent pages
- **7** are extracetd by querying external services.


The dataset was partitioned randomly into training and testing sets, with a ratio of **two-thirds for training** and **one-third for testing**.

## Details

- **Funded by:** Abdelhakim Hannousse, Salima Yahiouche
- **Shared by:** [pirocheto](https://github.com/pirocheto)
- **License:** [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- **Paper:** [https://arxiv.org/abs/2010.12847](https://arxiv.org/abs/2010.12847)

## Source Data

The diagram below illustrates the procedure for creating the corpus.  
For details, please refer to the paper.

<div align="center">
  <img src="images/source_data.png" alt="Diagram source data">
</div>

<p align="center">
  <em>Source: Extract form the <a href="https://arxiv.org/abs/2010.12847">paper</a></em>
</p>

## Load Dataset

- With **datasets**:
```python
from datasets import load_dataset

dataset = load_dataset("pirocheto/phishing-url")
```

- With **pandas** and **huggingface_hub**:
```python
import pandas as pd
from huggingface_hub import hf_hub_download

REPO_ID = "pirocheto/phishing-url"
FILENAME = "data/train.parquet"

df = pd.read_parquet(
    hf_hub_download(repo_id=REPO_ID, filename=FILENAME, repo_type="dataset")
)
```

- With **pandas** only:
```python
import pandas as pd

url = "https://huggingface.co/datasets/pirocheto/phishing-url/resolve/main/data/train.parquet"
df = pd.read_parquet(url)
```

## Citation

To give credit to the creators of this dataset, please use the following citation in your work:

- BibTeX format

```
@article{Hannousse_2021,
   title={Towards benchmark datasets for machine learning based website phishing detection: An experimental study},
   volume={104},
   ISSN={0952-1976},
   url={http://dx.doi.org/10.1016/j.engappai.2021.104347},
   DOI={10.1016/j.engappai.2021.104347},
   journal={Engineering Applications of Artificial Intelligence},
   publisher={Elsevier BV},
   author={Hannousse, Abdelhakim and Yahiouche, Salima},
   year={2021},
   month=sep, pages={104347} }
```

- APA format

```
Hannousse, A., & Yahiouche, S. (2021).
Towards benchmark datasets for machine learning based website phishing detection: An experimental study.
Engineering Applications of Artificial Intelligence, 104, 104347.
```