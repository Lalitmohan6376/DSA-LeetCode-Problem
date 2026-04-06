def increase(arr):
  stack = []

  for num in arr:
    while stack and stack[-1] > num:
      stack.pop()
    stack.append(num)

  return stack

print(increase([5,2,8,3,6]))
