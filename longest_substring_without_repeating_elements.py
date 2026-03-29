def repeat(s):
    # abca
    left = 0
    freq = {}
    max_len = 0
    
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        
        while freq[s[right]] > 1:
            # window shrink
            freq[s[left]]-=1
            if freq[s[left]] == 0:
                del freq[s[left]]
                
            left+=1
            
            max_len = max(max_len,right-left+1)
            
    return max_len
    

            
s = "abcabcbb"
print(longest_substring(s))          
            
            
        
