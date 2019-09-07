

def is_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    str_count = {}

    for ch in str1:
        str_count[ord(ch)] = str_count.get(ord(ch), 0) + 1

    for ch in str2:
        str_count[ord(ch)] = str_count.get(ord(ch), 0) - 1
        if str_count[ord(ch)] < 0:
            return False

    if any(x != 0 for x in str_count.values()):
        return False
    return True


###
str1 = "test"
str2 = "ttew"
if is_permutation(str1, str2):
    print "Yes"
else:
    print "No"
