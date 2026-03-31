
def max_subarray(arr,k):
    window_sum = 0
    left = 0
    n = len(arr)
    
    for right in range(k):
       window_sum+=arr[right]
    print(arr[0:k])
    
    for right in range(k,n):
        window_sum -= arr[left]
        window_sum += arr[right]
        left+=1
        print(arr[left:right+1])
        
    return window_sum
        
print(max_subarray([1,2,3,4,5],3))
        
