A = [11, 5, 55, 1]

for i in range(len(A)):
    min_idx = i

    for j in range(i+1, len(A)):
        if(A[j] < A[min_idx]):
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print(A)
