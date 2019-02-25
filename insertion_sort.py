A = [11, 5, 55, 12, 2]


for i in range(1, len(A)):
    curr_val = A[i]
    position = i
    while(position > 0 and curr_val < A[position-1]):
        A[position] = A[position - 1]
        position = position - 1
    A[position] = curr_val

print(A)
