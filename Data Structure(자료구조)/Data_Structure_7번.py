points = []
answer = 0
n = int(input())
for _ in range(n):
  point = tuple(map(int, input().split()))
  points.append(point)

points = sorted(points)
xs = []
for i in range(len(points)):
  for j in range(i+1, len(points)):
    if points[i][0] == points[j][0]:
      if not points[i][0] in xs:
        xs.append(points[i][0])
        answer +=1
      break

    else:break

ys = []
points = sorted(points, key=lambda x:x[1])
for i in range(len(points)):
  for j in range(i+1, len(points)):
    if points[i][1] == points[j][1]:
      if not points[i][1] in ys:
        ys.append(points[i][1])
        answer += 1
      break

    else:
      break

print(answer)
