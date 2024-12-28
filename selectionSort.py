arr = [34,3,23,22,5,8,33,90,88,76,4,6,9,0]

for i in range(0,len(arr)):
    minindex = i 
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            minindex = j
            arr[i], arr[j] = arr[j],arr[i]
print(arr)            