n = int(input())
arr = list(map(int, input().split()))
m = int(input())
students = []
for i in range(m):
    students.append(list(map(int, input().split())))

for student in students:
    if student[0] == 1:
        for idx in range(len(arr)):
            if (idx + 1) % student[1] == 0:
                if arr[idx] == 0:
                    arr[idx] = 1
                else:
                    arr[idx] = 0
    else:
        k = 1
        while True:
            down = student[1] - k - 1
            up = student[1] + k - 1
            if down <0 or up > n - 1:
                k -= 1
                break
            elif arr[down] != arr[up]:
                k -= 1
                break
            else:
                k += 1
    
        
        for j in range(down+1, up):
            if arr[j] == 1:
                arr[j] = 0
            else:
                arr[j] = 1

for idx in range(len(arr)):
    if idx % 20 == 19:
        print(arr[idx])
    else:
        print(arr[idx], end=' ')


# 출력조건에서 헤맸다...
# 입력조건에 따른 0과 1을 바꾸는 것은 조건문과 반복문을 이
