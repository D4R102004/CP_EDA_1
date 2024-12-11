from CP_3Recursion import CP3
# MIN(i, A): minimum value in an array A from position i
#     if i == |A|:
#       return infinity
#     return min(A[i], MIN(i + 1, A))


arr = [100, 5000, 78, 23, 90, 45, 68, 23]
print(CP3.minimum(0, arr))




