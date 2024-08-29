def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    
    vowels = 'aeiou'
    result = {}

    treated_phrase = phrase.lower()

    for char in treated_phrase:
        if char in vowels:
            result[char] = result.get(char, 0) + 1

    return result