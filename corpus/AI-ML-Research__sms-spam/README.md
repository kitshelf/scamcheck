---
license: apache-2.0
task_categories:
- text-classification
tags:
- parquet
- modify-datasets
---

# sms-spam

Processed tabular dataset created with [https://huggingface.co/spaces/aimlresearch2023/modify_datasets](https://huggingface.co/spaces/aimlresearch2023/modify_datasets) and published to
[`AI-ML-Research/sms-spam`](https://huggingface.co/datasets/AI-ML-Research/sms-spam).

## Metadata

- **Source type:** Hugging Face
- **Source:** `https://huggingface.co/datasets/ucirvine/sms_spam`
- **Original rows:** 5,574
- **Output rows:** 5,574
- **Output size:** 187.9 KB
- **Shards:** 1
- **Max words:** 512

## Schema

| Column | Dtype |
|--------|-------|
| `sms` | String |
| `label` | Int64 |

## Preview (head 10)

| sms | label |
| --- | --- |
| Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
 | 0 |
| Ok lar... Joking wif u oni...
 | 0 |
| Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's
 | 1 |
| U dun say so early hor... U c already then say...
 | 0 |
| Nah I don't think he goes to usf, he lives around here though
 | 0 |
| FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, £1.50 to rcv
 | 1 |
| Even my brother is not like to speak with me. They treat me like aids patent.
 | 0 |
| As per your request 'Melle Melle (Oru Minnaminunginte Nurungu Vettam)' has been set as your callertune for all Callers. Press *9 to copy your friends Callertune
 | 0 |
| WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.
 | 1 |
| Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030
 | 1 |
