# 사칙연산
#----------------------------------------10869----------
# a,b = input().split()
# a = int(a)
# b = int(b)

# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)


# 곱셈
#----------------------------------------2588----------
# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)


# 알람시계
#----------------------------------------2884----------
# H,M = input().split()
# H = int(H)
# M = int(M)

# if (M < 45):
#     wake_up_minute = M + 15
#     if (H != 0):
#         wake_up_hour = H - 1
#     else :
#         wake_up_hour = 23
# else:
#     wake_up_minute = M - 45
#     wake_up_hour = H
    
# print(wake_up_hour, wake_up_minute)


# 더하기사이클
#----------------------------------------1110----------
# start = int(input())
# instead = start
# other = 101
# num = 0

# while other != start :
#     value = (instead // 10)+(instead % 10)
#     value1 = (value % 10)+((instead % 10)* 10)
#     other = value1
#     instead = value1
#     num = num + 1 

# print(num)


# 평균은 넘겠지
#----------------------------------------4344----------
# for i in range(int(input())):
#     j = list(map(int, input().split()))
#     average = sum(j[1:]) / j[0]
#     cnt = 0 
#     for l in range(1, len(j)):
#         if j[l] > average : 
#             cnt += 1  
#     st_aver = (cnt / j[0] * 100)
#     print(format(st_aver, ".3f")+"%")


# 셀프넘버
#----------------------------------------4673----------
# def d(n):
#     value = n
#     for c in str(n):
#         value += int(c)
#     return value

# list = []
# for l in range(1,10001):
#     list.append(d(l))

# for i in range(1,10001):
#     if i not in list :
#         print(i)


#단어공부
#----------------------------------------1157----------
# a = input().upper()

# bet = list(set(a))
# count = 0
# b = []
# for char in bet:
#     cnt = a.count(char)
#     if cnt >= count :
#         if cnt == count :
#             b.append(char)
#         else :
#             b = []
#             b.append(char)
#         count =  cnt
# if len(b) >= 2 :
#     print('?')
# else :
#     print(b[0])


#크로아티아 알파벳
#----------------------------------------2941----------
# alphabet = str(input())

# Croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# for i in Croatia_list: 
#     alphabet = alphabet.replace(i,'*')

# print(len(alphabet))


#달팽이는 올라가고싶다
#----------------------------------------2869----------
up, down, top = input().split()

up = int(up)
down = int(down)
top = int(top)

day1 = up-down
dayT = ((top - up) / day1)

if int(dayT) < dayT:
    dayT = dayT + 2
else:
    dayT = dayT + 1

print(int(dayT))


#ACM 호텔
#----------------------------------------10250----------




#소수 구하기
#----------------------------------------1929----------