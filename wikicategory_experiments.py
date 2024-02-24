from itertools import islice
from dataset import wiki_category_dataset
from cov_wiki_category import *

import time

start = time.time()


def evaluate_wikidata(llm_response, gold_list):
    tp = len([item for item in llm_response if item in gold_list])
    fp = len(llm_response) - tp

    return tp, fp


tp_baseline = 0
fp_baseline = 0
tp_final = 0
fp_final = 0

# small_list = dict(islice(wiki_data.items(), 3))
# print(small_list)

p1 = []
p2 = []

step = 1
for data in wiki_category_dataset:
    intermediate_responses = wikidata_chain(data["question"])
    baseline_response = intermediate_responses["baseline_response"]
    final_response = intermediate_responses["final_response"]
    print(data["question"])
    # print(baseline_response)
    # print(final_response)
    tp, fp = evaluate_wikidata(baseline_response, data["answer"])
    tp_baseline += tp
    fp_baseline += fp
    tp, fp = evaluate_wikidata(final_response, data["answer"])
    tp_final += tp
    fp_final += fp

    precision_baseline = ((tp_baseline)/(tp_baseline+fp_baseline)) * 100
    precision_final = ((tp_final)/(tp_final+fp_final)) * 100

    p1.append(precision_baseline)
    p2.append(precision_final)

    print(f"============= STEP {step} =============\nPrecision baseline on wiki data: {precision_baseline} and Precision Final on wiki data: {precision_final}")
    step += 1

print(p1)
print(p2)

end = time.time()
print(end - start)
