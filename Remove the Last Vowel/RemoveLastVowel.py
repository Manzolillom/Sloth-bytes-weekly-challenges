import re

def remove_last_vowel(txt: str) -> str:
    no_last_vowel = re.compile(r'(\w*)([aeiou])(\w*)', re.I)
    return no_last_vowel.sub(r'\1\3', txt)