A, P = map(int, input().split())
D = [A]
idx = 0
while True:
    addition = 0
    for i in str(D[idx]):
        addition += int(i)**P

    if addition in D:
        break
    else:
        D.append(addition)
        idx += 1

num = D.index(addition)
print(len(D[:num]))
        
# 반복문을 사용하고 언제 break해야하는지 생각해보자
# break해야할 때에는 이미 list에 존재하는 수가 나왔을 때
# 그러면 중복을 제외한 것의 갯수를 세려면 중복이 시작한 위치를 찾으면 된다
# num 변수가 중복된 위치를 찾은 변수
