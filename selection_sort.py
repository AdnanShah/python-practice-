A = [11, 5, 55, 1]

for i in range(len(A)):
    min_indx = i
    for j in range(i+1, len(A)):
        if(A[min_indx] > A[j]):
            min_indx = j
    A[min_indx], A[i] = A[i], A[min_indx]


print(A)
