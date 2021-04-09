N = int(input())
arr = []
answer =0
for i in range(N):
    arr.append(list(map(int, input().split())))

go = sorted(arr, key = lambda x: x[0])
back = sorted(arr, key = lambda x: x[1])

result = go[-1][0] - back[0][1]

if result <=0:
    print(0)
else:
    print(result)

# 풀이 생각법
# 가장 늦게 등교한 학생의 등교시간 - 가장 일찍 하교한 학생의 하교시간을 계산
# 계산하기 위해 sorted함수를 사용하여 정렬
