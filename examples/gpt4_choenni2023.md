### Abstract and Overview

**Motivation and Key Results**
The study explores how Multilingual Large Language Models (MLLMs) use data from various languages during fine-tuning, investigating the extent and conditions under which languages influence each other. Utilizing TracIn, a training data attribution (TDA) method, it identifies the most influential training samples for specific test languages. Findings reveal that MLLMs rely on data from multiple languages from early fine-tuning stages, and this reliance increases over time. The study also discovers that different fine-tuning languages can both reinforce and complement the knowledge from the test language's data, showcasing a new perspective on cross-lingual sharing mechanisms at the data level.

### Methodology

**Approach and Technique**
The study employs TracIn to analyze the influence of training samples across different languages on test samples. This method assesses how changes in training data (inclusion or exclusion of specific samples) impact the loss for a test sample, thereby measuring each training sample's influence. This is the first approach to study cross-lingual sharing at the data level. It reveals that MLLMs utilize data from various languages extensively, even when the test language was prominently featured during fine-tuning, indicating more universal model representations than previously thought.

### Experimental Setup

**Tasks and Fine-Tuning**
The experiments involve fine-tuning models on three multilingual text classification tasks: Natural Language Inference (NLI), Paraphrasing, and Sentiment Analysis, using datasets like XNLI, PAWS-X, and MARC. They employ the XLM-R base model with a classification head for predictions, fine-tuning on a dataset of 10K samples drawn from five different languages. The study aims for a comprehensive understanding of how multilingual training data influences model predictions for a specific test language.

### Cross-Language Influence

**Influence Across Languages**
Analysis of the most influential training samples across test languages revealed substantial cross-language influence. For tasks with parallel datasets, such as XNLI and PAWS-X, most influential training samples often included numerous samples from languages other than the test language, indicating robust cross-lingual information sharing within the models. Korean, despite being the least similar to other fine-tuning languages, still exhibited some degree of cross-lingual contribution.

### Complementary vs. Reinforcing Influence

**Nature of Cross-Lingual Contribution**
The study differentiates between reinforcing and complementary contributions of cross-lingual samples. In the case of XNLI, over half of the influential contributions from different languages were translations of the most influential training samples from the test language, suggesting that the model benefits from reinforcing data across languages. In contrast, for PAWS-X, the benefit is more likely attributed to the model learning new complementary information from other languages, indicating diverse modes of cross-lingual learning.

### Dynamics of Cross-Lingual Sharing

**Evolution During Fine-Tuning**
The research investigates how the extent of cross-lingual sharing evolves during fine-tuning. It found that models generally start to rely less on their own language's fine-tuning data after the initial epochs of training, indicating an increase in cross-lingual sharing as fine-tuning progresses. This dynamic varies for different language pairs, reflecting fluctuating patterns of cross-lingual influence throughout the training process.

### Zero-Shot Testing and Data Imbalance

**Zero-Shot Scenarios and Data Imbalance Effects**
In zero-shot testing scenarios, where test languages were not included in fine-tuning, models showed surprisingly little reliance on specific training samples identified in regular fine-tuning. This suggests distinct cross-lingual sharing patterns in zero-shot setups. Additionally, the study examines how data imbalance affects cross-lingual sharing. Even with data imbalances, models continue to benefit significantly from cross-lingual sharing, though a more pronounced reliance on a language's own data is observed when it is overrepresented during training.