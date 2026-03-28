def atmost(s,k):
    left = 0
    count = 0
    freq = {}
    
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        
        while len(freq) > k:
            freq[s[left]] -=1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
        
        count += (right-left+1)
    
    return count
    
def exactly(s,k):
    return atmost(s,k)-atmost(s,k-1)
    
s = "abcabc"
k = 2
print(exactly(s,k))
