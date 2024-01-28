BASELINE_PROMPT_WIKIDATA_QUESTION = """

Generate the question of the form "Who are some [Profession]s who were born in [City]?"
Output format: Return a python list. comma separate each of the answers and place them inside double quote.
Question: {question}
"""

PLAN_VERIFICATION_TWO_STEP_PROMPT_WIKI = """Your task is to create a series of verification questions based on the below question, the verfication question template and baseline response.
Example Question: Who are some movie actors who were born in Boston?
Example Verification Question Template: Where Was [movie actor] born?
Example Baseline Response: 1. Donnie Wahlberg
2. Chris Evans
3. Mark Wahlberg
4. Ben Affleck
5. Uma Thurman
Verification questions: 1. Where was Donnie Wahlberg born?
2. Where was Chris Evans born?
3. Where was Mark Wahlberg born?
4. Where was Ben Affleck born?
5. Where was Uma Thurman born?

Explanation: In the above example the verification questions focused only on the ANSWER_ENTITY (name of the movie actor) and QUESTION_ENTITY (birth place) based on the template and substitutes entity values from the baseline response.
Similarly you need to focus on the ANSWER_ENTITY and QUESTION_ENTITY from the actual question and substitute the entity values from the baseline response to generate verification questions.

Actual Question: {original_question}
Baseline Response: {baseline_response}"""

EXECUTE_VERIFICATION_FACTORED_PROMPT_WIKI = """Answer the following question. Think step by step and answer the question concisely.
Example Question: Where was Donnie Wahlberg born?
Example Answer: Boston, Massachusetts

Example Question: Where was Chirs Evans born?
Example Answer: Boston, Massachusetts

Example Question: Where was Mark Wahlberg born?
Example Answer: Boston, Massachusetts

Example Question: Where was Ben Affleck born?
Example Answer: Berkeley, California

Example Question: Where was Uma Thurman born?
Example Answer: Boston, Massachusetts

Actual Question: {verification_question}"""

FINAL_VERIFIED_TWO_STEP_PROMPT_WIKI = """Given the below `Original Question` and `Baseline Answer`, analyze the `Verification Questions & Answer Pairs` to finally filter the refined answer. NO ADDITIONAL DETAILS.
Provide the answer as a numbered list of persons.
Example Context: 

Example Original Question: Who are some movie actors who were born in Boston?
Example Baseline Answer: 1. Donnie Wahlberg
2. Chris Evans
3. Mark Wahlberg
4. Ben Affleck
5. Uma Thurman
Example Verification Questions & Answer Pairs From another source: 
1. Where was Donnie Wahlberg born?
2. Where was Chirs Evans born?
3. Where was Mark Wahlberg born?
4. Where was Ben Affleck born?
5. Where was Uma Thurman born?
&
1. Boston, Massachusetts
2. Boston, Massachusetts
3. Boston, Massachusetts
4. Berkeley, California
5. Boston, Massachusetts
Example Final Refined Answer: 1. Donnie Wahlberg 
2. Chris Evans
3. Mark Wahlberg
4. Uma Thurman

Example Explanation: Based on the verification questions and answers, only Donnie Wahlberg, Chris Evans, Mark Wahlberg and Uma Thurman were born in Boston. Ben Affleck was born in Berkeley, California. 


Example Original Question: Who are some football players who were born in Madrid?
Example Baseline Answer: 1. Sergio Ramos
2. Marcos Alonso
3. David De Gea
4. Fernando Torres
Example Verification Questions & Answer Pairs From another source:
1. Where was Sergio Ramos born?
2. Where was Marcos Alonso born?
3. Where was David De Gea born?
4. Where was Fernando Torres born?
&
1. Camas, Spain
2. Madrid, Spain
3. Madrid, Spain
4. Fuenlabrada, Spain
Example Final Refined Answer: 1. Marcos Alonso, 2. David De Gea

Example Explanation: Based on the verification questions and answers, only Marcos Alonso and David De Gea were born in Madrid. Sergio Ramos was born in Camas, Spain and Fernando Torres was born in Fuenlabrada, Spain.

Context:

Actual Original Question: {original_question}
Baseline Answer: {baseline_response}

Verification Questions & Answer Pairs From another source:
{verification_q_a_pairs}"""
