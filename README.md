# PanelGPT: Prompt Language Models with a Penal Discussion 

# 💡: 💁🏼🎤     (👾💬) (🤖💭) (🤯🗯)

We introduce new zero-shot prompting magic words that improve language models' reasoning ability: **Panel Discussion**!

## Motivation

In conferences and workshops, there are always **penal discussions** among experts, and people exchange their opinions on a given topic, improving the understanding of new concepts, changing perspectives of thinking, and reaching a more comprehensive understanding of prevailing debates or discussions.

<figure>
  <figcaption> Figure 1: A panel discussion between Jack Ma and Elon Musk, WAIC, 2019: </figcaption>
  <img src="figs/Jack-Ma_Elon-Musk.jpeg" alt="panel discussion between Jack Ma and Elon Musk" width="600">
</figure>

This idea is related to the work of self-consistency [(Wang, Xuezhi, et al.)](https://arxiv.org/pdf/2203.11171.pdf) (as multiple experts may disagree with each other during the panel discussion.)


## Empirical Results on Benchmarks

We evaluate the effectiveness of the proposed prompt method on the GSM8K dataset, using gpt-3.5-turbo api.

The cost for evaluating each prompt on the 1k GSM8k test dataset is less than 2 USD. 


| Method\Dataset  | GSM8K (test 1k) | Prompt Content | Reference | 
|---------|---------|---------|-----------|
| No-Prompt | 0.789 | The answer is:| - |
| Zero-Shot CoT | 0.854 | Let's think step by step: | [(Kojima, Takeshi, et al. 2022)](https://arxiv.org/pdf/2205.11916.pdf) | 
| APE Improved CoT | 0.845 | Let’s work this out in a step by step way to be sure we have the right answer:| [(Zhou, Yongchao, et al. 2023)](https://arxiv.org/pdf/2211.01910.pdf) |
| ToT Prompting | 0.842 | Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realises they're wrong at any point then they leave | [(Dave Hulbert's Repo 2023)](https://github.com/dave1010/tree-of-thought-prompting) | 
| PanelGPT |  **0.899** | 3 experts are discussing the question with a _panel_ discussion, trying to solve it step by step, and make sure the result is correct _and avoid penalty_: | (This Repo, July 18, 2023) |
| PanelGPT w/o AE and EA |  0.878 | 3 experts are discussing the question with a discussion, trying to solve it step by step, and make sure the result is correct: | (Ours, Ablation Study)
| PanelGPT w/o AE| 0.84 | 3 experts are discussing the question with a discussion, trying to solve it step by step, and make sure the result is correct and avoid penalty: | (Ours, Ablation Study)
| PanelGPT w/o EA |  <ins>0.894</ins>  | 3 experts are discussing the question with a panel discussion, trying to solve it step by step, and make sure the result is correct: | (Ours, Ablation Study)
| P<ins>e</ins>n<ins>a</ins>lGPT  (Mis-spelled) |  _0.883_  | 3 experts are discussing the question with a penal discussion, trying to solve it step by step, and make sure the result is correct: | (Ours, Ablation Study)
## Related Works

### Zero-Shot and Few-Shot Prompting 
The ability of Zero-shot prompting emerges in the language models trained on large amounts of data like GPT-3 and GPT-4 (Ouyang et al., 2022; OpenAI, 2023). And it was shown in Wei et al. (2021) that instruction-fine-tuning improves the zero-shot learning ability of language models.

Notwithstanding the impressive zero-shot performance exhibited by large language models, these models often exhibit suboptimal performance in executing more complex tasks under a zero-shot setting. Leveraging few-shot prompting presents a viable approach for facilitating in-context learning (Brown et al., 2020; Min et al., 2022). This technique necessitates the inclusion of demonstrations within the prompt, effectively guiding the model toward enhanced performance. These demonstrations act as conditioning mechanisms for succeeding examples, leading the model to generate better responses.

### Chain-of-Thought Prompting 

In some more challenging tasks like complex arithmetic, commonsense, and symbolic reasoning tasks, the chain-of-thought (CoT) prompting is shown to be more effective in helping the language models to get correct answers (Wei et al., 2022). CoT includes additional reasoning steps in the few-shot prompting examples. Kojima et al. (2022) further introduces zero-shot CoT, showing that adding task-agnostic instruction can improve the model performance in specific tasks. In Zhang et al. (2022b), Auto-CoT combines the universality of zero-shot CoT and the capability of original CoT driven by demonstrations and proposes to automatically construct demonstrations based on clustering and diversity-based sampling that are beneficial for CoT reasoning.

### Other Prompting Strategies 
Wang et al. (2022) improve the few-shot CoT method by sampling multiple diverse reasoning paths and marginalizing those paths, choosing the most consistent answers among all sampled reasoning paths. The Generated Knowledge Prompting Liu et al. (2021) improves commonsense reasoning by incorporating knowledge or information related to the questions to make more accurate predictions. Tree-of-thoughts (ToT) methods (Long, 2023; Yao et al., 2023) combine tree-based planning methods with reasoning skills of language models, and solves hard reasoning problems step by step via multiple round conversations. Hulbert (2023) also put forward a related idea that leverages multiple thoughts of a language model in a single prompt. Memory and Retrieval Augmented Generation (RAG) (Lewis et al., 2020), which is able to combine parametric memory and non-parametric memory like Wikipedia in completing knowledge-intensive tasks. MoT (Li & Qiu, 2023): Pre-thinking based on the external unlabeled dataset and then recalling the related knowledge during inference.



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
