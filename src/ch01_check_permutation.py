def check_permutation(str1, str2):
    # if a user input empty string
    if not str1 or not str2:
        return False
    else:
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False
