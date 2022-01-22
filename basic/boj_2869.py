
# -*- coding: utf-8 -*-

#백준 2869번 달팽이는 올라가고 싶다.

import sys
input = sys.stdin.readline
import math

a, b, v = map(int, input().split())

day = math.ceil((v - b) / (a - b))
print(day)


#달팽이가 올라가야 하는 최종 높이는 `V-B`
#하루동안 올라갈 수 있는 높이는 `A-B`
#총 걸리는 일수는 `(V-B) / (A-B)`
