# A+B - 8 [https://www.acmicpc.net/problem/11022]
#----------------------------------------11022----------
import sys

C = sys.stdin.readline()
C = int(C)

for i in range(C):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}:", f"{A} + {B} =", A + B )
