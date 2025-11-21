def remove_adjacent_duplicates(s):
    while non_adjacent_duplicates_exists(s):
        result = ""
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                i += 2
            else:
                result += s[i]
                i += 1
        s = result
    return s
def non_adjacent_duplicates_exists(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

