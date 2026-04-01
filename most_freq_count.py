def count(arr,k):
    freq = {}
    left = 0
    max_freq = 0
    result = 0
    
    for right in range(len(arr)):
        freq[arr[right]] = freq.get(arr[right],0)+1
        if freq[arr[right]] > max_freq:
            max_freq = freq[arr[right]]
            result = arr[right]
        if right-left+1 > k:
            freq[arr[left]]-=1
            if freq[arr[left]]==0:
                del freq[arr[left]]
            left+=1
    return result
    
    
print(count([1,2,1,3,4,5,5,5,5],3))
    
