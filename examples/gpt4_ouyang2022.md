### Abstract: Motivation, Method, and Key Results

The paper addresses the challenge that larger language models (LMs) do not inherently align better with user intent, often generating untruthful, toxic, or unhelpful outputs. To tackle this, the authors propose InstructGPT, a model fine-tuned with human feedback to align with a wide range of tasks reflecting user intentions. The approach involves collecting labeler-written prompts and using these for supervised learning fine-tuning of GPT-3, followed by reinforcement learning from human feedback. InstructGPT shows preference in human evaluations over standard GPT-3, despite having fewer parameters. It demonstrates improvements in truthfulness and reductions in toxicity, with minimal performance regressions on public NLP datasets.

### Methodology

The methodology combines explicit (following instructions) and implicit (truthfulness, non-toxicity) user intentions. InstructGPT is fine-tuned using a reinforcement learning from human feedback (RLHF) approach. This process involves collecting human-written demonstrations and labeler rankings of model outputs to create a dataset. A reward model (RM) is trained on this dataset to predict human-preferred outputs. This RM is then used as a reward function to fine-tune GPT-3 using the Proximal Policy Optimization (PPO) algorithm. This approach specifically aligns GPT-3 with the preferences of a selected group of people (labelers and researchers).

### Key Point 1: User Preference

In human evaluations, InstructGPT's outputs are significantly preferred over those of GPT-3. For instance, outputs from the 1.3B parameter InstructGPT model are chosen over the 175B parameter GPT-3 model, despite having significantly fewer parameters. InstructGPT models are noted for generating more appropriate outputs and reliably following explicit instructions.

### Key Point 2: Truthfulness and Toxicity

InstructGPT models exhibit a notable improvement in truthfulness compared to GPT-3, particularly in the TruthfulQA benchmark. They generate truthful and informative answers more frequently and demonstrate a lower rate of making up information not present in the input (e.g., in summarization tasks). However, while InstructGPT shows improvements in reducing toxicity, it does not significantly advance in mitigating bias.

### Key Point 3: Performance on Public NLP Datasets

The paper notes an "alignment tax," where aligning models with human intent leads to performance regressions on some public NLP datasets like SQuAD and DROP. The authors address this by modifying the RLHF fine-tuning process, blending updates that increase the log likelihood of the pretraining distribution (PPO-ptx) with PPO updates. This approach effectively minimizes performance regressions without compromising user preference scores.

### Key Point 4: Generalization to Diverse User Preferences

InstructGPT models also show promising generalization to the preferences of "held-out" labelers who did not contribute to the training data. This suggests the models' capability to align with a broader spectrum of user preferences, although further research is needed to confirm their performance across diverse user groups and in scenarios with varying user opinions.
