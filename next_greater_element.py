def next_element(arr):
  n = len(arr)
  result = [-1]*n
  stack = []

  for i in range(n):
    while len(stack) > 0 and arr[i] > arr[stack[-1]]:
      idx = stack.pop()
      result[idx] = arr[i]

    stack.append(i)

  return result


print(next_element([2,1,3]))
