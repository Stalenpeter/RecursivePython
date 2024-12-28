arr = [34,3,23,22,5,8,33,90,88,76,4,6,9,0]

for i in range(1,len(arr)):
    key = arr[i]
    j = i - 1 

    while j >= 0 and arr[j] > key :
        arr[j+1] = arr[j]
        j = j - 1 
    arr[j + 1] = key

print(arr)    
