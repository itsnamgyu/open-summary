### Abstract and Overview

**Abstract**
The paper introduces LLaMA, a series of foundation language models ranging from 7 billion to 65 billion parameters. These models, trained on trillions of tokens, demonstrate that it is possible to achieve state-of-the-art performance using only publicly available datasets, without relying on proprietary data. Notably, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, while LLaMA-65B competes with top models like Chinchilla-70B and PaLM-540B. All models have been released to the research community.

### Methodology

**Approach**
The training approach for LLaMA models follows established methods and is inspired by the Chinchilla scaling laws. Large transformers are trained on a massive corpus of textual data using a standard optimizer. The focus is on achieving the best possible performance within various inference budgets, emphasizing training on more tokens than typically used in the field. This approach leads to models that are more efficient during inference, offering competitive performance compared to the largest existing language models but with significantly fewer parameters.

### Key Findings

**Main Results**
The LLaMA models were evaluated on 20 benchmarks, including zero-shot and few-shot tasks. They were compared with other foundation models like GPT-3, Gopher, Chinchilla, PaLM, OPT, GPT-J, and GPT-Neo. The evaluation showed that LLaMA models perform competitively in free-form generation tasks, often outperforming or matching the performance of much larger models.

**Common Sense Reasoning**
On eight common sense reasoning benchmarks (including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, and OpenBookQA), LLaMA-65B outperformed Chinchilla-70B on most benchmarks and was competitive with PaLM-540B. LLaMA-13B also outperformed GPT-3 on most benchmarks, despite having only a fraction of GPT-3's parameters.

**Closed-book Question Answering**
In closed-book question answering tasks (Natural Questions and TriviaQA benchmarks), LLaMA-65B achieved state-of-the-art performance in both zero-shot and few-shot settings. LLaMA-13B was also competitive with GPT-3 and Chinchilla, even though it is 5-10 times smaller. This smaller model can run on a single V100 GPU during inference, making it more accessible.

**Reading Comprehension**
The LLaMA models were tested on the RACE reading comprehension benchmark. LLaMA-65B showed competitive performance with PaLM-540B, and LLaMA-13B outperformed GPT-3 by a few percentage points. These results indicate the models' robust capability in understanding and processing complex reading comprehension tasks designed for middle and high school students.
