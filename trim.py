# Trim same ends
def trim(s):
    i = 0
    j = len(s) - 1
    
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return s[i:j+1]
    
    return ""

ans = trim("abca")
print(ans)
