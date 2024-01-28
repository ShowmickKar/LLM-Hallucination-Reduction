BASELINE_PROMPT_WIKIDATA_QUESTION = """

Generate the question of the form "Who are some [Profession]s who were born in [City]?"
Output format: Return a python list. comma separate each of the answers and place them inside double quote.
Question: {question}
"""

VERIFICATION_QUESTION_PROMPT_WIKIDATA_QUESTION = """ 
Given the below `Original Question` and the `Baseline Response`

"""

EXECUTE_PLAN_PROMPT_SELF_LLM = """Given an article, Answer the following question correctly in one sentence.

Article: {article}
Question: {verification_question}

Answer:"""

FINAL_REFINED_PROMPT_WIKIDATA_QUESTION = """Given the below `Article`, `Original question` and `Baseline Answer`, output the answer to the original question. If the baseline response seems correct, don't change it. Otherwise change it to another choice. 
Answer format: Just output the best choice. Don't write any explanation. Don't write anything extra. Just the answer choice.

Article: {article}
Original Question: {question}
Options: {options}
Baseline Answer: {baseline_response}
Verification Questions & Answer Pairs:
{verification_answers}
"""