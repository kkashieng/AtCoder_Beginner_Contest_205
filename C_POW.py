A, B, C = list(map(int, input().split()))

# Cが偶数
if C % 2 ==0:
    if abs(A) == abs(B):
        print("=")
    elif abs(A) < abs(B):
        print("<")
    elif abs(A) > abs(B):
        print(">")
# Cが奇数
else:
    if A == B:
        print("=")
    elif A < B:
        print("<")
    elif A > B:
        print(">")