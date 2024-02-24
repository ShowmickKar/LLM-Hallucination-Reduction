import json



with open("wikidata_questions.json", 'r', encoding="utf8") as json_file:
    wiki_data = json.load(json_file)


with open("wiki_category_dataset.json", 'r', encoding="utf8") as json_file:
    wiki_category_dataset = json.load(json_file)


with open("multispanqa_dataset.json", 'r', encoding="utf8") as json_file:
    multispanqa_dataset = json.load(json_file)
