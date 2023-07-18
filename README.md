# PanelGPT: Prompt Language Models with a Penal Discussion

We introduce new zero-shot prompting magic words that improve language models' reasoning ability: **Panel Discussion**!

## Motivation

In conferences and workshops, there are always **penal discussions** among experts, and people exchange their opinions on a given topic, improving the understanding of new concepts, changing perspectives of thinking, and reaching a more comprehensive understanding of prevailing debates or discussions.

This idea is related to the work of self-consistency [Wang, Xuezhi, et al.](https://arxiv.org/pdf/2203.11171.pdf) (as multiple experts may disagree with each other during the panel discussion.)


## Empirical Results on Benchmarks

We evaluate the effectiveness of the proposed prompt method on the GSM8K dataset, using gpt-3.5-turbo api.

The cost for evaluating each prompt on the 1k GSM8k test dataset is less than 2 USD. 


| Method\Dataset  | GSM8K (test 1k) | Prompt Content | Reference | 
|---------|---------|---------|-----------|
| No-Prompt | 0.789 | The answer is:| - |
| Zero-Shot CoT | 0.854 | Let's think step by step: | [(Kojima, Takeshi, et al. 2022)](https://arxiv.org/pdf/2205.11916.pdf) | 
| APE Improved CoT | 0.845 | Let’s work this out in a step by step way to be sure we have the right answer:| [Zhou, Yongchao, et al. 2023](https://arxiv.org/pdf/2211.01910.pdf) |
| ToT Prompting | 0.842 | Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realises they're wrong at any point then they leave | [Dave Hulbert's Repo 2023](https://github.com/dave1010/tree-of-thought-prompting) | 
| PanelGPT |  **0.899** | 3 experts are discussing the question with a _panel_ discussion, trying to solve it step by step, and make sure the result is correct _and avoid penalty_: | (This Repo, July 18, 2023) |
| PanelGPT w/o AE and EA |  0.878 | 3 experts are discussing the question with a discussion, trying to solve it step by step, and make sure the result is correct: | (Ours, Ablation Study)
| PanelGPT w/o AE|   | 3 experts are discussing the question with a discussion, trying to solve it step by step, and make sure the result is correct and avoid penalty: | (Ours, Ablation Study)
| PanelGPT w/o EA |   | 3 experts are discussing the question with a panel discussion, trying to solve it step by step, and make sure the result is correct: | (Ours, Ablation Study)
| PanelGPT (Mis-spelled) |   | 3 experts are discussing the question with a penal discussion, trying to solve it step by step, and make sure the result is correct: | (Ours, Ablation Study)
## Related Works


## Citation

If you use our code and prompt, please consider citing our GitHub repository:

```bibtex
@misc{sun2023panelgpt,
  author = {Hao Sun},
  title = {PanelGPT: Prompt Language Models with a Penal Discussion},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/holarissun/PanelGPT}},
}
