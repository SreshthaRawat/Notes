# brute force

# buggy version
arr.append([num, count]) # [number, frequency]
res.append(arr.pop()[0]) # take "number"

# working version

for num, cnt in count.items():
    arr.append([cnt, num])   # frequency first
arr.sort() # without key sort we only sort according tto first element of arr
res = []
while len(res) < k:
    res.append(arr.pop()[1]) # take number
return res
