import re
from config_llm import llm
from prompts_wikidata import *
from utils import *

def wikidata_chain(question):
    baseline_response_prompt_template = BASELINE_PROMPT_WIKIDATA_QUESTION.format(question=question)
    baseline_response = llm(prompt.format(text=baseline_response_prompt_template))
    baseline_response_parsed = parse_numbered_list(baseline_response)
    verification_question_prompt_template = PLAN_VERIFICATION_TWO_STEP_PROMPT_WIKI.format(original_question=question, baseline_response=baseline_response)


    verification_questions = llm(prompt.format(text=verification_question_prompt_template))


    verification_questions = parse_numbered_list(verification_questions)

    verification_q_a_pair = {}
    for question in verification_questions:
        execute_verification_question_prompt_template = EXECUTE_VERIFICATION_FACTORED_PROMPT_WIKI.format(verification_question=question)
        verification_question_llm_response = llm(prompt.format(text=execute_verification_question_prompt_template))
        verification_q_a_pair[query] = verification_question_llm_response

    verification_q_a_pair_str = ""
    i = 1
    for query, answer in verification_q_a_pair.items():
        verification_q_a_pair_str += f"Q{i}: {query}\nA{i}: {answer}\n\n"            
        i+=1
    verification_q_a_pair_str.strip()

    # print(f"Verification Answers:\n{verification_q_a_pair_str}")

    """ Generate Final Refined Response """
    final_answer_prompt_template = FINAL_VERIFIED_TWO_STEP_PROMPT_WIKI.format(original_question=question, baseline_response=baseline_response, verification_q_a_pair=verification_q_a_pair_str)

    final_response = llm(prompt.format(text=final_answer_prompt_template))
    final_response_parsed = parse_numbered_list(final_response)
    return {"question": question,  "baseline_response":baseline_response_parsed, "verification_q_a_pairs": verification_q_a_pair_str, "final_response":final_response_parsed}
