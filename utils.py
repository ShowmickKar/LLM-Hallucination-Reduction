import re

def parse_numbered_list(llm_response):
    pattern = re.compile(r'\d+\.\s+(.+)')
    matches = pattern.findall(llm_response)
    return matches

