import json

path = "wikidata_questions.json"

with open(path, 'r', encoding="utf8") as json_file:
    data = json.load(json_file)

print(len(data))

for key in data:
    print(len(data[key]))

