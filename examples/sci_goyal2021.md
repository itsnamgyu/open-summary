**Experimental Results**

This study investigates the impact of larger capacity multilingual masked language models on cross-lingual language understanding (XLU). The authors present two new models, XLM-RXL and XLM-RXXL, with 3.5B and 10.7B parameters, respectively, and demonstrate their superior performance on cross-lingual understanding benchmarks compared to the previous XLM-R model. The new models outperform XLM-R by 1.8% and 2.4% average accuracy on XNLI, and also outperform RoBERTa-Large on several English tasks of the GLUE benchmark.

The study shows that larger capacity models may achieve strong performance on high-resource languages while greatly improving low-resource languages. The authors highlight the potential of pretrained models with larger capacity to enable supervised and unsupervised cross-lingual transfer, reducing the need for training one model per language. However, it is noted that the better performance of self-supervised cross-lingual models on low-resource languages may come at the cost of lower performance on higher-resource languages.

**Benefits and Challenges of Scaling Multilingual Models**

The study addresses the potential benefits and challenges associated with scaling the capacity of multilingual models, emphasizing that very large-scale multilingual models may benefit from strong performance on high-resource languages while allowing for zero-shot transfer and low-resource language understanding. The authors also compare their models to mT5 models and provide a technical study suggesting that larger capacity multilingual models can obtain state-of-the-art cross-lingual understanding results while maintaining strong performance on high-resource languages.

Overall, this research contributes to understanding the impact of larger capacity models on cross-lingual language understanding and demonstrates the potential for achieving state-of-the-art performance across multiple languages using larger multilingual masked language models.
