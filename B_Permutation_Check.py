N = int(input())

A_n = list(map(int, input().split()))

# 同じ要素を持っているか否か
def has_duplicates(seq):
    return len(seq) != len(set(seq))

def sum_N():
    result = 0
    for n in range(1,N+1):
        result += n
    return result

# もし要素が重複していない場合
if not has_duplicates(A_n):
    if sum(A_n) == sum_N():
        print("Yes")
    else:
        print("No")
# 要素が重複している場合
else:
    print("No")