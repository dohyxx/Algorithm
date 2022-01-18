"""
백준 1712 손익분기점
A = 고정비용
B = 가변비용
C = 판매가격
"""


import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c <= b:
    print (-1)
else:
    print (int(a/(c-b)) + 1)

