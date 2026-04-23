# Mirror string
def mirrorstring(s):
    count = 0
    n = len(s)
    
    for i in range(0,n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                count+=1
    return count
        
print(mirrorstring("abba"))
