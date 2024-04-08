from itertools import islice
from dataset import wiki_data
from cov_wikidata import *

import json
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

inspect_list = []

step = 1
for question in wiki_data:
    intermediate_responses = wikidata_chain(question)
    baseline_response = intermediate_responses["baseline_response"]
    final_response = intermediate_responses["final_response"]
    print(question)
    # print(baseline_response)
    # print(final_response)
    # tp, fp = evaluate_wikidata(baseline_response, wiki_data[question])
    # tp_baseline += tp
    # fp_baseline += fp
    # tp, fp = evaluate_wikidata(final_response, wiki_data[question])
    # tp_final += tp
    # fp_final += fp

    # precision_baseline = ((tp_baseline)/(tp_baseline+fp_baseline)) * 100
    # precision_final = ((tp_final)/(tp_final+fp_final)) * 100

    # p1.append(precision_baseline)
    # p2.append(precision_final)

    tp, fp = evaluate_wikidata(baseline_response, wiki_data[question])
    precision_baseline = ((tp)/(tp+fp)) * 100
    tp_baseline += tp
    fp_baseline += fp
    tp, fp = evaluate_wikidata(final_response, wiki_data[question])
    precision_final = ((tp)/(tp+fp)) * 100
    tp_final += tp
    fp_final += fp

    precision_baseline_microaveraged = ((tp_baseline)/(tp_baseline+fp_baseline)) * 100
    precision_final_microaveraged = ((tp_final)/(tp_final+fp_final)) * 100

    print(f"============= STEP {step} =============\nPrecision baseline on wiki data: {precision_baseline} and Precision Final on wiki data: {precision_final}")
    item  = {'Step': step,
             'Question': question,
             'Answer': wiki_data[question],
             'Baseline_Response_Unparsed': intermediate_responses['baseline_unparsed'],
             'Baseline_Response_Parsed': intermediate_responses['baseline_response'],
             'Final_Response_Unparsed': intermediate_responses['final_response_unparsed'],
             'Final_Response_Parsed': intermediate_responses['final_response'],
             'Precision_Baseline_Response': precision_baseline,
             'Precision_Final_Response': precision_final}
    inspect_list.append(item)
    step += 1

print(f"Microaveraged Precision Baseline: {precision_baseline_microaveraged}")
print(f"Microaveraged Precision Final: {precision_final_microaveraged}")

end = time.time()
total_time = end - start

print(total_time)

inspect_list.append({"Microaveraged Precision Baseline": precision_baseline_microaveraged,
                     "Microaveraged Precision Final": precision_final_microaveraged,
                     "Time": total_time})

with open("wikidata_inspect.json", 'w') as json_file:
    json.dump(inspect_list, json_file, indent=4, sort_keys=False)
