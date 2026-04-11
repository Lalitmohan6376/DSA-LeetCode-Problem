def maxheight(h):
    n = len(h)
    result = []
    max_height = -1
    i = n-1
    
    while i >= 0:
        if h[i] > max_height:
            result.insert(0,i)
            
            max_height = h[i]
        i-=1
    return result
    
    
print(maxheight([4,2,3,1]))
