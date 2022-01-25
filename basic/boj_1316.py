
"""
백준 1316번 그룹 단어 체커
"""

import sys
input = sys.stdin.readline

n = int(input())
count = n

for _ in range(n):
    word = input()
    #단어 길이 -1만큼 확인
    for i in range(len(word)-1):
        #현재 위치의 알파벳과 다음 알파벳의 위치가 다르고
        if word[i] != word[i+1]:
            #현재위치의 알파벳이 뒤에 똑같이 있으면 총 단어 -1
            if word[i] in word[i+1:]:
                count -= 1
                break

print (count)




