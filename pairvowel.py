# pair vowel find
def pairvowel(s):
    s = list(s)
    i = 0
    j = len(s)-1
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    
    while i < j:
        if s[i] in vowel and s[j] in vowel:
            count+=1
        i+=1
        j-=1
            
    return count
            
            
ans = pairvowel("aeiokmnguaepq")
print(ans)
            
