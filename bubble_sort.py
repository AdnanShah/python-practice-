arr = [11, 5, 55, 1, 45]


for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]


print(arr)
