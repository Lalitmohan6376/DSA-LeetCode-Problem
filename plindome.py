def substring(s):
    n = len(s)
    ans = ""
    
    for i in range(0,n):
        for j in range(i,n):
            sub = s[i:j+1]
            
            if sub == sub[::-1]:
                if len(sub) > len(ans):
                    ans = sub
                    
    return ans
    
print(substring("babad"))
