A = input()
A_length = len(A)
B = input()
B_length = len(B)
word = ""
arr = [[0] * (A_length + 1) for _ in range(B_length + 1)]

for i in range(1, B_length + 1):
    for j in range(1, A_length + 1):
        if(B[i-1] == A[j-1]):
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
LCS_length = arr[-1][-1]

while(True):
    if(arr[B_length][A_length] == 0):
        break

    if(arr[B_length][A_length] == arr[B_length-1][A_length]):
        B_length -= 1
    elif(arr[B_length][A_length] == arr[B_length][A_length-1]):
        A_length -= 1
    else:
        word += A[A_length-1]
        A_length -= 1
        B_length -= 1

if(LCS_length):
    print(LCS_length)
    print(word[::-1])
else:
    print(0)                                                          