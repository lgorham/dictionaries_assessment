def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    char_count = {}
    highest_count = 0

    for char in phrase:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        if count > highest_count:
            highest_count = char_count[char]
            related_char = char
        if count == highest_count:
            tie_char = char

    return [related_char, tie_char]


print top_chars("The rain in spain stays mainly in the plain.")