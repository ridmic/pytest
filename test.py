

def first_repeat_of_a_char(haystack):
    found = []
    for straw in haystack:
        if straw in found:
            return straw
        found.append(straw)
    return None


def most_repeated_char(haystack):
    found = {}
    for straw in haystack:
        if straw in found:
            found[straw] += 1
        else:
            found[straw] = 1
    found = sorted(found, key=found.get, reverse=True)
    return found[0]


chk1 = "ABCDFECBCDESABBA"
print(first_repeat_of_a_char(chk1))
print(most_repeated_char(chk1))
