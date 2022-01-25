def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    lettersList = list(phrase)

    lettersList.reverse()

    return "".join(lettersList)

    # return phrase[::-1]