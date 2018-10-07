def is_unique(input_str):
    # if a user input empty string
    if not input_str:
        return False
    else:
        for char in input_str:
            count = input_str.count(char)
            if count > 1:
                return False
        # after iterate through all the characters in the string
        else:
            return True
