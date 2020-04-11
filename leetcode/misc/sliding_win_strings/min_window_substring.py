
def minWindowSubstring(s, t):
    table = {}

    for ch in t:
        table[ch] = table.get(ch, 0) + 1

    begin, end = 0, 0
    counter = len(table)
    len_window = 99999999

    ans = ""

    while end < len(s):
        endchar = s[end]

        if table.get(endchar, 0) > 0:
            table[endchar] -= 1
            if table[endchar] == 0:
                counter -= 1

        end += 1

        while counter == 0:
            if end - begin < len_window:
                len_window =end- begin


