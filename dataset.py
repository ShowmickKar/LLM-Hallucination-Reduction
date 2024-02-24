import json
import re

with open("wikidata_questions.json", 'r', encoding="utf8") as json_file:
    wiki_data = json.load(json_file)


with open("wiki_category_dataset.json", 'r', encoding="utf8") as json_file:
    wiki_category_dataset = json.load(json_file)


def extract_substring_before_bracket(input_string):
    pattern = r'^[^(\s]*'
    
    match = re.search(pattern, input_string)
    
    if match:
        return match.group(0)
    else:
        return None
    

for data in wiki_category_dataset:
    parsed_answers = []
    answers = data["answer"]
    for ans in answers:
        ans = extract_substring_before_bracket(ans)
        parsed_answers.append(ans)
    data["answer"] = parsed_answers


with open("multispanqa_dataset.json", 'r', encoding="utf8") as json_file:
    multispanqa_dataset = json.load(json_file)
