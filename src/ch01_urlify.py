def urlify(input_str, n=0):
    return input_str[:n].replace(' ', '%20')


def urlify_solution(string, n=0):
    spaces_count = string.count(' ')
    non_spaces_count = n - spaces_count
    if len(string) == 0 or n == 0:
        return ''
    elif (spaces_count*3)+non_spaces_count > n:
        return 'String is too short for output'

    # Convert string to list so that it can be modified
    letters = list(string)

    letter_index = n - 1
    last_index = n - 1

    # Find the last index where it contains a character in the list
    while letters[letter_index] == ' ':
        letter_index -= 1

    while letter_index > 0:
        if letters[letter_index] == ' ':
            letters[last_index-2] = '%'
            letters[last_index-1] = '2'
            letters[last_index] = '0'
            last_index -= 3
        else:
            letters[last_index] = letters[letter_index]
            last_index -= 1
        letter_index -= 1
        
    return ''.join(letters)
