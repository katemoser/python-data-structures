def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count = {}

    for letter in phrase:
        if not letter_count.get(letter): 
            letter_count[letter] = 1
        else:
            letter_count[letter] +=1
    return letter_count