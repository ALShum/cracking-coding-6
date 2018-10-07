def is_unique(input_str):
    # keep the character that was iterated
    char_collection = []
    # if a user input empty string
    if not input_str:
        return False
    else:
        for char in input_str:
            if char not in char_collection:
                char_collection.append(char)
            else:
                return False
        # after iterate through all the characters in the string
        else:
            return True
