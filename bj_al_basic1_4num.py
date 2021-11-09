import sys

input = sys.stdin.readline

n = list(map(int, input().split()))

num1 = str(n[0]) + str(n[1])

num2 = str(n[2]) + str(n[3])

num3 = int(num2) + int(num1)

print(num3)
