a = "bd\0"
b = "abcd\0"

# recursive
def common_seq(i, j):
    if A[i] == "\0" or B[j] == "\0":
        return 0
    elif A[i] == B[j]:
        return 1 + LCS(i + 1, j + 1)
    else:
        return max(LCS(i + 1, j), LCS(i, j + 1))

# memoization
'''Build a matrix that stored the value of computation'''

# Dynamic Programming
if (A[i] = B[j]):
    LCS[i, j] = 1 + :CS[i - 1, j - 1]
else:
    LCS[i, j] = max(LCS[i - 1, j], LCS[i, j - 1])
