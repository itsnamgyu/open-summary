### Abstract and Key Findings

**Larger-Scale Transformers for Multilingual Masked Language Modeling**: This paper presents the results of two enlarged multilingual masked language models, XLM-RXL and XLM-RXXL, with 3.5 billion and 10.7 billion parameters, respectively. These models demonstrate significant improvements over the previous XLM-R model, with average accuracy increases of 1.8% and 2.4% on the XNLI benchmark, and outperforming the RoBERTa-Large model in several English GLUE benchmark tasks. The study suggests that large-capacity models achieve strong performance in high-resource languages while significantly enhancing low-resource languages.

### Methodology

The methodology involves scaling the capacity of the XLM-R model while training on the same CC100 dataset. Two new models, XLM-RXL and XLM-RXXL, are developed with significantly larger parameter sizes (3.5 billion and 10.7 billion, respectively) compared to the previous XLM-R model. These models are trained using a multilingual masked language model objective, leveraging the Transformer architecture. The training involves sampling streams of text from each language and training the model to predict masked tokens in the input.

### Cross-Lingual Language Understanding Impact

The paper highlights the impact of increased model capacity on cross-lingual language understanding (XLU). The larger models, XLM-RXL and XLM-RXXL, outperform the previous XLM-R model on cross-lingual understanding benchmarks. This improvement is more pronounced in low-resource languages, indicating the effectiveness of these models in handling a wide range of languages. The ability to perform well in both high-resource and low-resource languages demonstrates the versatility of the larger-capacity models.

### Performance on Benchmark Tasks

The results show that the new models significantly outperform the previous XLM-R model on XNLI and other cross-lingual tasks. In addition, the models achieve competitive performance against multilingual T5 models. The XLM-RXXL model sets new state-of-the-art results on French, Vietnamese, and Hindi on the XNLI benchmark. Furthermore, it surpasses the RoBERTa-Large model on the English GLUE benchmark, illustrating its strong performance in high-resource languages.

### Comparison to Monolingual and Other Multilingual Models

The XLM-RXXL model demonstrates that larger capacity enables a multilingual model to achieve high performance in high-resource languages without losing cross-lingual transfer abilities for lower-resource languages. This finding is significant considering the challenges in balancing performance across a diverse set of languages. The study provides a comparison with monolingual models like RoBERTa and other multilingual models like mT5, highlighting the advancements made by the XLM-RXXL in both high-resource and low-resource language understanding.

### Conclusion and Contributions

The paper concludes that scaling up the model capacity of XLM-R to 10.7 billion parameters results in enhanced performance on cross-lingual understanding benchmarks. The study underlines the potential of large-capacity multilingual models in achieving state-of-the-art results across diverse languages. It contributes to the understanding of the relationship between model capacity and language model performance, particularly in the context of multilingual settings. The release of these models and their codebase provides valuable resources for future research and applications in multilingual natural language processing.
