def _vertical_txt_rec(txt: str, max: int, current: int, i : int, end : int, word_n : int):
    # Base case
    if i == end:
        return [[' ' for _ in range(word_n + 1)] for _ in range(max + 1)]
    # Recursive case
    else:
        if current > max:
            max = current
            
        if txt[i] == ' ':
            current = -1 # resets current letter n in word
            word_n += 1 # goes to next word

        # going back , fill the array
        result = _vertical_txt_rec(txt, max, current+1, i+1, end, word_n)
        if txt[i] != ' ':
            result[current][word_n] = txt[i]
        return result


def vertical_txt(txt: str) -> list[list[chr]]:
    return _vertical_txt_rec(txt, 0, 0, 0, len(txt), 0)