import json

path = "wikidata_questions.json"

with open(path, 'r', encoding="utf8") as json_file:
    wiki_data = json.load(json_file)
