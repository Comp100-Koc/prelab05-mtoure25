def remove_adjacent_duplicates(s):
    changed = True
    while changed:
        changed = False
        i = 0
        result = ""
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                i += 2
                changed = True
            else:
                result += s[i]
                i += 1
        s = result
    return s
            
print(remove_adjacent_duplicates("abbacadd"))            