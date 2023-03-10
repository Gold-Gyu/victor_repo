# 비트연산을 통한 부분집합 이해

arr = [3, -2, -1, -4, 5, 4]
# arr의 원소가 6개면 부분집합은 2 ** 6

n = len(arr) # n : 원소의 개수

# 우리는 부분집합의 개수를 구하는 공식을 알고 있다.
# 부분집합의 개수 => 2 ** n

'''
부분집합에 포함되면 1로 표시 /포함되지 않으면 0으로 표시 => 비트연산
부분집합의 개수 2 ** n => 2 ** 6 = 64
2^0 2^1 2^2 2^3 2^4 2^5
[3,  6,  7,  1,  5,  4]

[1,  0,  0,  1,  1,  0] => 1 + 8 + 16 = 25 -> 25번째 부분집합
[1,  1,  0,  0,  0,  0] => 3번쨰
[0,  1,  0,  0,  0,  0] => 2번째
[1,  0,  0,  0,  0,  0] => 1번째 부분집합
[0,  0,  0,  0,  0,  0] => 0 번쨰 부분집합


'''

for i in range(1<<n): # i번째 부분집합에 대해
    # i를 2진수로 바꿈.
    print(f"{i} 번째 부분집합 : ", end = " ")

    sub_set = []
    for j in range(n): # i번째 부분집합의 n개의 요소 중에 j 번쨰 원소를 포함하는지 검사
        if i & (1<<j): # i를 2진수로 바꿨을 떄 원소가 1인 경우 그 j 번째 원소를 포함하는 부분집합이다.
            # print(arr[j], end = ', ')
            sub_set.append(arr[j])
    print(sub_set)
    if sum(sub_set) == 0:
        print("합이 0인 집합 : ", sub_set)

print()
