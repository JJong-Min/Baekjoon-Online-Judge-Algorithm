N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(str, input().split())))

for i in arr:
    zero_num = 0
    one_num = 0
    for j in range(len(i[0])):
        if i[0][j] == i[1][j]:
            continue
        elif i[0][j] == '0':
            zero_num += 1
        else:
            one_num += 1

    print(max(zero_num, one_num))


# 바꿀수 있는 경우가 2가지가 주어졌지만 이를 고려해서 카운팅할 필요는 없음
# 첫번째 2진수와 두번째 2진수를 비교하면서 같으면 넘어가고
# 만약 다르다면, 2진수의 그 자리 값이 0이면 zero_num 1을 더함
# else, one_num 1을 더함
# 결과로 zero_num과 one_num 중 큰 값을 출력

    
        
