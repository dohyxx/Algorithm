

"""
백준 1193번 분수찾기
"""
import sys
input = sys.stdin.readline


X = int(input())
stage, key_X = 1, 1

while key_X + stage <= X:
    key_X += stage
    stage += 1

step = X - key_X
x, y = step + 1, stage - step

#짝수인가 홀수인가
if stage % 2 == 0: #짝수일때
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))