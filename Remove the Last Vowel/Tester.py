from RemoveLastVowel import remove_last_vowel

def test(test_str : str, expected_output : str):
    x = remove_last_vowel(test_str)
    if x == expected_output:
        print("Test passed")
    else:
        print(f"Test Failed on {test_str}")
        print(f"Risultato: \t\t {x}END")
        print(f"Risultato atteso: \t {expected_output}END")
    
test("Those who dare to fail miserably can achieve greatly.", "Thos wh dar t fal miserbly cn achiev gretly.")
test("Love is a serious mental disease.", "Lov s  serios mentl diseas.")
test("Get busy living or get busy dying.", "Gt bsy livng r gt bsy dyng.")
test("If you want to live a happy life, tie it to a goal, not to people.", "f yo wnt t liv  hppy lif, ti t t  gol, nt t peopl.")

# Attempt one </3 (\w+(?=[aeiouAEIOU]))|[^aeiouAEIOU]