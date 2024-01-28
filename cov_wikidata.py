from prompts_wikidata import *

def wikidata_question_chain(article, question, options, answer):
    baseline_response_prompt_template = BASELINE_PROMPT_MCQ_QUESTION.format(article=article, question=question, options=options)
    baseline_response = llm(prompt.format(text=baseline_response_prompt_template))
    verification_question_prompt_template = VERIFICATION_QUESTION_PROMPT_MCQ_QUESTION.format(article=article, question=question, answer=answer, baseline_response=baseline_response)


    verification_questions = llm(prompt.format(text=verification_question_prompt_template))


    question_pattern = r'"(.*?)"'
    verification_questions = re.findall(question_pattern, verification_questions)

    # print(f"Verification Questions:\n{verification_questions}")

    verification_q_a_pair = {}
    for query in verification_questions:
        execute_verification_question_prompt_template = EXECUTE_PLAN_PROMPT_SELF_LLM.format(article=article, verification_question=query)
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
    final_answer_prompt_template = FINAL_REFINED_PROMPT_MCQ_QUESTION.format(article=article, question=question, options=options, baseline_response=baseline_response, verification_answers=verification_q_a_pair_str)

    final_response = llm(prompt.format(text=final_answer_prompt_template))
    return {'article':article, 'question':question, 'baseline response':baseline_response, 'verification questions':verification_questions, 'verification response':verification_q_a_pair_str, 'final refined response':final_response}, [baseline_response_prompt_template, verification_question_prompt_template, execute_verification_question_prompt_template, final_answer_prompt_template]
