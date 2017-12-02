

def first_repeat_of_a_char(haystack):
    found = []
    for straw in haystack:
        if straw in found:
            return straw
        found.append(straw)
    return None


chk1 = "ABCDFECBCDES"
print( first_repeat_of_a_char(chk1))
