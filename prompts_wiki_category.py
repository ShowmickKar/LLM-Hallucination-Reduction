BASELINE_PROMPT_WIKI_CATEGORY = """Answer the below question which is asking for a list of entities (names, places, locations etc). Output should be a numbered list and only contains the relevant & concise enitites as answer. NO ADDITIONAL DETAILS.

Example Question: Name some movies directed by Steven Spielberg.
Example Answer: 1. Jaws
2. Jurassic Park
3. Indiana Jones
4. E.T.
5. TENET

Example Question: Name some football stadiums from the Premier League.
Example Answer: 1. Old Trafford
2. Anfield
3. Stamford Bridge
4. Santiago Bernabeu

The list should be as large as possible.

Question: {original_question}"""

PLAN_VERIFICATION_TWO_STEP_PROMPT_WIKI_CATEGORY = """Your task is to create a series of verification questions based on the below question, and baseline response.

Example Actual Question Template: Name some movies directed by Steven Spielberg.
Example Verification Question Template: Is [movie] directed by [Steven Spielberg]?

Generate the questions in the form of a numbered list.

Actual Question: {original_question}
Baseline Response: {baseline_response}"""

EXECUTE_VERIFICATION_FACTORED_PROMPT_WIKI_CATEGORY = """Answer the following question. Think step by step and answer the question concisely.

Example Question: Is Jaws directed by Steven Spielberg?
Example Answer: Yes.

Example Question: Is Jurassic Park directed by Steven Spielberg?
Example Answer: Yes, Jaws is directed by Steven Spielberg.

Example Question: Is Indiana Jones directed by Steven Spielberg?
Example Answer: Yes, Indiana Jones is directed by Steven Spielberg.

Example Question: Is E.T. directed by Steven Spielberg?
Example Answer: Yes, E.T. is directed by Steven Spielberg.

Example Question: Is TENET directed by Steven Spielberg?
Example Answer: No, TENET is directed by Christopher Nolan.

Actual Question: {verification_question}"""

FINAL_VERIFIED_TWO_STEP_PROMPT_WIKI_CATEGORY = """Given the below `Original Question` and `Baseline Answer`, analyze the `Verification Questions & Answer Pairs` to finally filter the refined answer. NO ADDITIONAL DETAILS.

Example Context:
Example Original Question: Name some movies directed by Steven Spielberg.
Example Baseline Answer: 1. Jaws
2. Jurassic Park
3. Indiana Jones
4. E.T.
5. TENET
Example Verification Questions & Answer Pairs From another source:
1. Is Jaws directed by Steven Spielberg? Yes, Jaws is directed by Steven Spielberg.
2. Is Jurassic Park directed by Steven Spielberg? Yes, Jurassic Park is directed by Steven Spielberg.
3. Is Indiana Jones directed by Steven Spielberg? Yes, Indiana Jones is directed by Steven Spielberg.
4. Is E.T. directed by Steven Spielberg? Yes, E.T. is directed by Steven Spielberg.
5. Is TENET directed by Steven Spielberg? No, TENET is directed by Christopher Nolan.
Example Final Refined Answer: 1. Jaws
2. Jurassic Park
3. Indiana Jones
4. E.T.

Example Explanation: Based on the verification questions and answers, only Jaws, Jurassic Park, Indiana Jones and E.T. are directed by Steven Spielberg. TENET is directed by Christopher Nolan.

Context:

Actual Original Question: {original_question}
Baseline Response: {baseline_response}

Verification Questions & Answer Pairs From another source: {verification_q_a_pairs} """
