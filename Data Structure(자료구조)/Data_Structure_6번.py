import sys

inputVal = sys.stdin.readline()
values = []

while (inputVal != "고무오리 디버깅 끝"):

  inputVal = sys.stdin.readline().rstrip()
  

  if inputVal == "문제":
    values.append(1)
  if inputVal == "고무오리":
    if len(values) == 0:
      values.append(1)
      values.append(1)
    else:
      values.pop()


print("고무오리야 사랑해") if len(values) == 0 else print("힝구")
    
