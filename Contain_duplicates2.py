num = [1, 2,2,2,2,2, 3, 3]
# Step 1: Temporary element aur count set karo
candidate = num[0]
count = 1
# Step 2: Array ke next elements traverse karo
for i in range(1, len(num)):
    if num[i] == candidate:
        count += 1
    else:
        count -= 1
        if count == 0:
            candidate = num[i]
            count = 1

print(candidate)
