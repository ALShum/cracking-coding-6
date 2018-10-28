def palindrome_permutation(input_str):
    no_of_odd = 0

    # Make string to be all lower and remove spaces
    formatted_str = input_str.lower().replace(' ', '')

    # Only unique letters in the string
    letters = set(formatted_str)
    for letter in letters:
        if formatted_str.count(letter) % 2 != 0:
            no_of_odd += 1

    if len(formatted_str) % 2 == 0 and no_of_odd == 0:
        return True
    elif len(formatted_str) % 2 != 0 and no_of_odd == 1:
        return True
    
    return False
