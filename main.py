from dataset import wiki_data
from cov_wikidata import *

def evaluate_wikidata(llm_response, gold_list):
    tp = len([item for item in llm_response if item in gold_list])
    fp = len(llm_response) - tp

    return tp, fp


tp_baseline = 0
fp_baseline = 0
tp_final = 0
fp_final = 0

for question in wiki_data:
    intermediate_responses = wikidata_chain(question)
    baseline_response = intermediate_responses["baseline_response"]
    final_response = intermediate_responses["final_response"]
    tp, fp = evaluate_wikidata(baseline_response, wiki_data[question])
    tp_baseline += tp
    fp_baseline += fp
    tp, fp = evaluate_wikidata(final_response, wiki_data[question])
    tp_final += tp
    fp_final += fp

precision_baseline = (tp_baseline)/(tp_baseline+fp_baseline)
precision_final = (tp_final)/(tp_final+fp_final)