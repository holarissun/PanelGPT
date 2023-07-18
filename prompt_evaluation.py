'''
File: prompt evaluation.py
Author: Hao Sun
Email: hs789@cam.ac.uk
Date: July 18, 2023
Description: This code performs parallelized prompt evaluation on the GSM8K dataset.
Requirement: Clone the GSM8K dataset first: https://github.com/openai/grade-school-math
'''

import torch as th
from dataset import get_examples, GSMDataset, extract_answer
import time
import numpy as np
import os
import openai
from concurrent.futures import ThreadPoolExecutor
OPENAI_API_KEY = 'YOUR API KEY HERE'

def init_openai():
    openai.api_key = OPENAI_API_KEY

def create_chat_completion(prompt, tokens=512, temperature=0, error_count=0):
    try:
        response = openai.ChatCompletion.create(
                                        model="gpt-3.5-turbo",
                                        messages=[
                                                    {"role": "system", "content": "You are a helpful assistant."},
                                                    {"role": "user", "content": prompt}
                                                ],
                                        max_tokens = tokens,
                                        temperature=temperature
                                        )
        return response
    except:
        # sleep for 5 seconds
        time.sleep(10)
        error_count += 1
        if error_count > 600:
            raise Exception("Too many errors")
        return create_chat_completion(prompt, tokens, temperature, error_count)

def test_single_example(example, prompt):
    qn, asr = example["question"], example["answer"]
    start_time = time.time()

    response = create_chat_completion(qn + prompt)
    response_content = response.choices[0].message.content

    check_response = create_chat_completion(f"The correct answer is {extract_answer(asr)}. Is the following answer correct? {response_content}.")
    check_response_content = check_response.choices[0].message.content

    is_correct = 'Yes' in check_response_content

    total_time = time.time() - start_time
    total_tokens = (response.usage.prompt_tokens + response.usage.completion_tokens +
                    check_response.usage.prompt_tokens + check_response.usage.completion_tokens)

    return is_correct, response_content, total_time, total_tokens

def run_test(test_examples, prompt, num_threads=10):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(test_single_example, test_examples, [prompt]*len(test_examples)))

    return {
        'result_list': [result[0] for result in results],
        'answers_list': [result[1] for result in results],
        'total_time': sum(result[2] for result in results),
        'accuracy': sum(result[0] for result in results) / len(results),
        'total_tokens': sum(result[3] for result in results),
        'average_tokens': sum(result[3] for result in results) / len(results)
    }

def eval_prompt(prompt = " ", n_eval = 1000, file_alias = 'alias', num_threads=500):
    init_openai()
    test_examples = get_examples("test")[:n_eval]

    results = run_test(test_examples, prompt, num_threads=num_threads)

    print('Total time:', results['total_time'])
    print('Accuracy:', results['accuracy'])
    print('Total tokens used:', results['total_tokens'])
    print('Average tokens used per question:', results['average_tokens'])

    np.save(f'results/result_list_{file_alias}.npy', results['result_list'])
    np.save(f'results/answers_list_{file_alias}.npy', results['answers_list'])
    np.save(f'results/promt_{file_alias}.npy', prompt)

if __name__ == '__main__':
    PROMPT = "To make sure to get the correct answer, we have 3 experts in a step-by-step discussion to solve the problem."
    wall_time_start = time.time()
    eval_prompt(prompt = PROMPT)
    print('prompt:', PROMPT)
    print(f"Wall time: {time.time() - wall_time_start}")
