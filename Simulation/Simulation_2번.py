
import sys
king, rock, N = sys.stdin.readline().split()
locations = {'R':(1,0), 'L':(-1,0), 'B':(0,1), 'T': (0,-1), 'RT': (1,-1), 'LT': (-1,-1), 'RB':(1,1), 'LB':(-1,1)} 
for _ in range(int(N)):
    move = sys.stdin.readline().rstrip()
    location = locations[move]
    nx = ord(king[0]) + location[0]
    ny = (8-int(king[1])) + location[1]
    if nx>= ord('A') and nx<= ord('H') and ny>=0 and ny<8:

        if nx == ord(rock[0]) and ny == (8-int(rock[1])):
            dx = ord(rock[0]) + location[0]
            dy = (8-int(rock[1])) + location[1]
            if dx>=ord('A') and dx<=ord('H') and dy>=0 and dy<8:
            
                king = chr(nx)+str(8-ny)
                rock = chr(dx)+str(8-dy)
        else:
            king = chr(nx)+str(8-ny)


print(king)
print(rock)

