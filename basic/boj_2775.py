


# 백준 2775번 부녀회장이 될테야
#3층 4호에 살려면 2층 1, 2, 3, 4호에 사는 사람들의 수의 합만큼 사람들을 데려와 살아야한다.
#0층의 i호에는 i명이 살기 때문에 이를 이런식으로 나타낼 수 있다.
#3층 : 1 5 15 35
#2층 : 1 4 10 20
#1층 : 1 3 6 10
#0층 : 1 2 3 4

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for x in range(k):
        for y in range(1, n):
            people[y] += people[y-1]
    print(people[-1])

