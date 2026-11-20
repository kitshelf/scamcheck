---
license: apache-2.0
task_categories:
- text-classification
language:
- en
tags:
- synthetic
- multi-turn
- dialogue
- scam
- conversation
pretty_name: scam and non-scam phone conversation.
size_categories:
- 1K<n<10K
---

# Synthetic Multi-Turn Scam and Non-Scam Phone Conversation Dataset 

## Dataset Description
The dataset is designed to help develop and evaluate models for detecting and classifying various types of phone-based scams.


## Dataset Structure
The dataset consists of three columns:

- **dialogue**: The transcribed conversation between the caller and receiver.
- **type**: The specific type of scam or non-scam interaction.
- **labels**: A binary label indicating whether the conversation is a scam (1) or not (0).


In the dialogue column, the caller is annotated as **Suspect** while the receiver is annotated as **Innocent**.

## Scam Types (label 1)
- **ssn**: Social security number scams, where the scammer attempts to obtain the victim's SSN.
- **refund**: Refund scams, where the scammer tries to convince the victim that they are owed a refund.
- **support**: Technical support scams, where the scammer impersonates a support representative to gain access to the victim's computer or personal information.
- **reward**: Reward scams, such as those involving gift cards, where the scammer promises a reward in exchange for personal information or money.

## Non-Scam Types (label 0)
- **delivery**: Legitimate delivery confirmation calls.
- **insurance**: Genuine insurance sales calls.
- **appointment**: Legitimate appointment scheduling or reminder calls.
- **wrong**: Wrong number calls for various reasons.

## Dataset Creation
The dialogue in this dataset were synthetically generated to mimic real-world scam and non-scam phone interactions using meta-llama-3-70b-instruct.

## Intended Use
This dataset is intended for research and development in natural language processing, specifically for building models to detect and classify phone-based scams. By providing a labeled dataset of scam and non-scam conversations with varied receiver personalities, researchers can develop and evaluate algorithms to help protect individuals from falling victim to phone scams.

## Limitations and Ethical Considerations
As the dialogues in this dataset are synthetically generated, they may not capture all the nuances and variations found in real-world phone interactions. Additionally, while efforts have been made to create realistic conversations, there may be biases present in the generated dialogues.

Users of this dataset should be aware of the potential limitations and biases and should use the data responsibly. The dataset should not be used to make decisions that could harm individuals or groups.

## License
This dataset is released under the Apache license 2.0. By using this dataset, you agree to abide by the terms and conditions of the license.
```