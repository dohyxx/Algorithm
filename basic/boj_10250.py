

#백준 10250번 ACM 호텔

#호텔 층 수 = h
#각 층의 방 수 = w
#몇번째 손님인지 = n

import sys
input = sys.stdin.readline

num = int(input()) #반복 횟수

for i in range(num):
    h, w, n = map(int, input().split())

    floor = n % h #층 수
    room_line = (n // h) + 1 #방 번호

    if floor == 0:
        floor = h
        room_line -= 1

    print (floor * 100 + room_line)

# ACM 호텔에서 손님이 왔을 때 몇번방에 배정해야 하는가? 하는 문제이다. 기본적으로 엘레베이터에 가까운 쪽부터 방을 배정해준다.
# 1층부터 h층까지 1호실을 다채우고 1층부터 h까지 2호실을 다 채우는 형식이다.
# h / w / n 순차적으로 입력을 받아서 몇호실에 배정할지 정하는 문제이다.
