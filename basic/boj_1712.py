"""
백준 1712 손익분기점
A = 고정비용
B = 가변비용
C = 판매가격


(가변비용 - 판매가격) => 한 번의 판매로 생기는 이익
=> 고정가격 A를 한 번의 판매로 생기는 이익으로 나눈다. 그리고 1을 더해준다.

EX) A = 10000원 B = 3000원 C = 5000원

B-C = 2000 ( 한 번의 판매로 얻는 이익 )
A / (B-C) = 5, 5대를 파는 순간 비용과 이익이 정확히 같으므로, 한 대 더 팔아야 손익분기점이 됩니다 따라서, 5+1 = 6
"""


import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c <= b:
    print (-1)
else:
    print (int(a/(c-b)) + 1)
