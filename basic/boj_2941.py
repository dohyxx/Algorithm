

"""
백준 2941번 크로아티아 알파벳
"""
import sys
input = sys.stdin.readline


alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()

for i in alpha:
       str = str.replace(i,"@")
       print(str)

print(len(str))



