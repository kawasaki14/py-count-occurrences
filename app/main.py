def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    phrase = phrase.lower()
    letter = letter.lower()
    return phrase.count(letter)
