from typing import Dict
import re

import torch
import transformers
from transformers import AutoTokenizer

PROMPT_FORMAT_LLAMA2 = {
    "description": "Llama 2 summarization prompt",
    "sec_prompt": '''[INST] <<SYS>> You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. 
<</SYS>> Summarize the given section in 1-2 paragraphs {text} [/INST]''',
    "accmul_prompt": '''[INST] <<SYS>> You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.
<</SYS>> Please summarize the given paper in **4-6 paragraphs**.
- In the first paragraph, give a brief abstract of the motivation and goal, overall method, and key results/findings.
- In the second paragraph, briefly explain how the method actually works.
- Each subsequent paragraph should coherently explain a key point of the paper.
- Each paragraph should have a header.
- Prioritize the most important contributions and discussions in the paper. Avoid repetition and **be concise**. Each paragraph should have 3-4 short sentences.
{text} [/INST] '''
}


class MyModel:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.pipeline = transformers.pipeline(
            "text-generation",
            model=model_path,
            return_full_text=False,
            torch_dtype=torch.bfloat16,
            device_map={"": 0},
        )

    def generate(self, input_data, prompt, max_new=512):
        input_data = prompt.format(text=input_data)
        sequences = self.pipeline(
            input_data,
            eos_token_id=self.tokenizer.eos_token_id,
            max_new_tokens=max_new,
        )

        return sequences


model_path = f'/projects/tdc2023/data/dev/base/model/llama-2-7b-chat-hf'
current_model = MyModel(model_path)


def summarize(template: Dict) -> Dict:
    """
    :param template:
    :return: {
        'title': 'Title of the paper',
        'abstract': 'Abstract of the paper',
        'sec_summary': [
            {
                'section_name': 'section_summary'
            },
            ...
        ],
        'total_summary': 'total_summary'
    }
    """

    def generate_sec_summary(template, current_model, max_new):
        sec_summary_lst = []
        for sec in template['sections']:
            for key, value in sec.items():
                # context = f'Abstract: {template["abstract"]}\nSection: {key}\n{value}'
                context = f'Section: {key}\n{value}'
                response = current_model.generate(context, PROMPT_FORMAT_LLAMA2["sec_prompt"], max_new=max_new)
                summary = response[0]['generated_text']
                sec_summary_lst.append({
                    key: summary
                })
        template['sections_summary'] = sec_summary_lst
        return template

    def generate_accmul_summary(sec_template, current_model, max_new=1024):
        whole_context = ''
        if len(sec_template['sections_summary']) > 8:
            whole_context1 = ''
            whole_context2 = ''
            sec_template_1 = sec_template['sections_summary'][:5]
            sec_template_2 = sec_template['sections_summary'][5:]

            for sec in sec_template_1:
                for key, value in sec.items():
                    whole_context1 += value

            for sec in sec_template_2:
                for key, value in sec.items():
                    whole_context2 += value

            whole_context1 = re.sub(r'\n\n+', '\n\n', whole_context1, flags=re.DOTALL)
            response1 = current_model.generate(whole_context1, PROMPT_FORMAT_LLAMA2["accmul_prompt"], max_new=max_new)

            whole_context2 = re.sub(r'\n\n+', '\n\n', whole_context2, flags=re.DOTALL)
            response2 = current_model.generate(whole_context2, PROMPT_FORMAT_LLAMA2["accmul_prompt"], max_new=max_new)

            input_agg = f'Abstract: {template["abstract"]}' + response1[0]['generated_text'] + response2[0][
                'generated_text']
            response_together = current_model.generate(input_agg, PROMPT_FORMAT_LLAMA2["accmul_prompt"],
                                                       max_new=max_new)
            sec_template['accmul_summary'] = response_together[0]['generated_text']
            return sec_template

        else:
            for sec in sec_template['sections_summary']:
                for key, value in sec.items():
                    whole_context += value

            whole_context = re.sub(r'\n\n+', '\n\n', whole_context, flags=re.DOTALL)
            response = current_model.generate(whole_context, PROMPT_FORMAT_LLAMA2["accmul_prompt"], max_new=max_new)
            summary = response[0]['generated_text']
            sec_template['accmul_summary'] = summary
            return sec_template

    sec_template = generate_sec_summary(template, current_model, max_new=512)

    whole_template = generate_accmul_summary(sec_template, current_model, max_new=1024)
    print(whole_template['accmul_summary'])

    paper_summary = {
        'title': template['title'],
        'abstract': template['abstract'],
        'sec_summary': sec_template['sections_summary'],
        'total_summary': whole_template['accmul_summary']
    }
    return paper_summary
