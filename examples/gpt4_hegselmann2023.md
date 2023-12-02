### Abstract and Motivation

**Abstract and Goal**
The paper investigates the application of large language models (LLMs) for zero-shot and few-shot classification of tabular data. The approach involves serializing tabular data into a natural-language string, accompanied by a brief classification problem description, and prompting the LLM with this information. In the few-shot setting, the LLM is fine-tuned using some labeled examples. This technique, despite its simplicity, outperforms previous deep-learning-based methods for tabular classification on several benchmark datasets, demonstrating non-trivial performance in most cases, even in the zero-shot classification. This method is also competitive with strong traditional baselines like gradient-boosted trees, particularly in the very-few-shot setting.

### Methodology

**Method Overview**
TabLLM, introduced in this paper, leverages LLMs for few-shot classification of tabular data. It prompts the LLM with serialized tabular data, converted into a natural-language representation, along with a concise classification problem description. The study experiments with nine different serialization methods and various sizes of the T0 language model. For fine-tuning, the parameter-efficient T-Few method updates the LLM's parameters using some labeled examples. Additionally, GPT-3 is evaluated in the zero-shot setting. This comprehensive evaluation is among the first of its kind for zero- and few-shot tabular classification using LLMs.

### Technical Details

**Problem Formalization and Serialization**
The process begins with a tabular dataset, transformed into a natural text representation. Each row is serialized using a function that combines the column names and feature values into a textual representation, then combined with a task-specific prompt to form the LLM input. The study primarily focuses on the serialization aspect, exploring various complex methods including incorporating another LLM and feature selection. The LLM then generates text based on this input, which must be mapped to a valid class using methods like the verbalizer.

**Serialization Techniques**
The performance of LLMs heavily depends on the serialization of the input data. The paper experiments with nine different serialization formats, ranging from simple lists of column names and feature values to more complex methods like employing an LLM fine-tuned on a table-to-text generation task. The study aims to generate inputs closer to the LLM's training distribution to enhance zero and very-few-shot performance. It also tests ablations like using only feature values or permuted column names to understand the relevance of these elements in classification performance.

### Key Findings

**Effects of Serialization on Performance**
The Text Template serialization method showed significant performance across experiments, especially in zero-shot settings, indicating the benefits of a serialization closer to the LLM's training distribution. However, more complex serialization methods using LLMs did not consistently outperform simpler template methods. It was observed that if enough training examples are available, the serialization approach becomes less critical, but in the zero-shot and few-shot settings, the correct association of feature names and values is crucial. The study also noted that the smaller T0 3B model had slightly reduced performance compared to larger models.

### Comparative Analysis

**Performance Against Baseline Models**
TabLLM, using the Text Template serialization, was compared against baseline models across various datasets. It achieved notable zero-shot performance in all tasks except for two specific datasets, improving with more training examples. Notably, TabLLM was on par with or outperformed traditional tree ensemble baselines and neural baselines like SAINT, NODE, and TabNet, particularly in settings with fewer training examples. This indicates the effectiveness of TabLLM in leveraging the power of LLMs for tabular data classification, especially in scenarios with limited labeled data.