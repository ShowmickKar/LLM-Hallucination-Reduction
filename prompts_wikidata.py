BASELINE_PROMPT_WIKIDATA_QUESTION = """Anwwer the question in a numbered list of 25-30 items. In the numbered list, just write the individual names. Don't add anything else.

Actual Question: {original_question}
"""
PLAN_VERIFICATION_TWO_STEP_PROMPT_WIKI = """Your task is to craete a series of verification questions based on the below question and the baseline response. The verification questions should be constructed in such a way that answering those questions will help verify the baseine response.
Generate the questions in a numbered list.

Actual Question: {original_question}
Baseline Response: {baseline_response}"""

EXECUTE_VERIFICATION_FACTORED_PROMPT_WIKI = """Answer the following question Make sure to follow the answer format given in the example questions and answers.
Example Question: Where was Donnie Wahlberg born?
Example Answer: Boston, Massachusetts
Example Question: Where was Ben Affleck born?
Example Answer: Berkeley, California

Actual Question: {verification_question}"""
FINAL_VERIFIED_TWO_STEP_PROMPT_WIKI = """Given the following  original question and the baseline response, there are a couple of verification question-answer pairs. Based on those pairs revise the baseline response to the original question. Make sure to answer in a numbered list. Just write the names. Don't add anytthing extra
Actual Original Question: {original_question}
Baseline Answer: {baseline_response}

Verification Questions & Answer Pairs From another source:
{verification_q_a_pairs}
"""
