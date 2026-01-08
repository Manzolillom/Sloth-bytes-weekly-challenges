import re

def remove_last_vowel(txt: str) -> str:
    words = txt.split()
    x = ""
    for word in words:
        x += re.sub(r'([aeiouAEIOU])(?!.*[aeiouAEIOU]\w*)', '', word) + " "
    x = x[:-1] # Removes the extra space
    return x
