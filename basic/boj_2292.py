
"""
백준 2292번 벌집

1 -> 7 -> 19 -> 37 -> 61  6의 배수로 증가
"""

import sys
input = sys.stdin.readline

n = int(input())
room = 1
cnt = 1

# n이 room 보다 클 동안만 반복
while n > room:
    room = room + (6 * cnt)
    cnt += 1

print(cnt)



