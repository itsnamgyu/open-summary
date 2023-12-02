### Abstract and Key Findings

**Motivation and Goal**: This paper, titled "Garbage in garbage out: Zero-shot detection of crime using Large Language Models," aims to leverage the common sense knowledge of large language models (LLMs) for zero-shot reasoning about crimes from textual descriptions of surveillance videos. The authors demonstrate that LLMs, specifically GPT-4, can detect and classify crimes effectively when provided with high-quality human-generated textual descriptions. However, they also find that automated video-to-text conversion methods currently fail to generate sufficiently detailed descriptions for LLMs to reason accurately.

### Methodology

**Method Overview**: The approach involves converting surveillance videos into textual descriptions and using GPT-4 for zero-shot reasoning about the likelihood of a crime. High-quality, objective descriptions of surveillance videos were manually created, avoiding race and gender details. GPT-4 then analyzed these descriptions to list possible explanations and categorize them into specific crime types or normal activities. The effectiveness of this method was compared against automated caption generation techniques like GIT Captions, LLaVA Descriptions, and YOLO-v8 + ByteTrack.

### Key Contribution 1: Efficacy of LLMs in Crime Detection

**Large Language Models in Crime Detection**: The study found that when provided with manually generated captions, GPT-4 achieved a 58.7% accuracy in correctly identifying the crime category, a significant improvement over existing methods. This demonstrates the potential of LLMs in assisting law enforcement by analyzing large volumes of surveillance data efficiently.

### Key Contribution 2: Limitations of Automated Video-to-Text Conversion

**Challenges in Automated Captions**: The research revealed significant shortcomings in automated video-to-text conversion methods. These methods often lacked the necessary detail for LLMs to reason effectively about the potential for crime. For instance, the GIT Captions and LLaVA Descriptions methods showed markedly lower accuracy rates (11.4% and 10.2% respectively), highlighting the need for more sophisticated automated description generation techniques.

### Key Contribution 3: Implications for Future Research

**Future Research Directions**: The findings suggest that while LLMs are effective in reasoning about crime from textual descriptions, the quality of these descriptions is crucial. This poses a challenge for fully automated surveillance analysis, as current automated description methods fall short. The paper calls for future research to enhance the objectivity and detail of automated video-to-text conversion to fully leverage the potential of LLMs in crime detection and prevention.

### Conclusion

**Overall Conclusion**: The paper concludes that LLMs, particularly GPT-4, are capable of effective zero-shot crime detection and classification when provided with high-quality textual descriptions. However, the current state of automated video-to-text conversion technologies limits the practical application of this approach. This highlights a crucial area for further research and development in the field of AI-assisted crime detection.
