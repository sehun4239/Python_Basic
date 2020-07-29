## 문제 5.
## 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
## 이 소수들을 그 수의 소인수라고 합니다.
## 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

## 600851475143의 소인수 중에서 가장 큰 수를 구하세요.
n = 600851475143
m = int(n**0.5)         # 775146
result = []

i = 3
while n != 1:
    if n % i == 0:
        n = n / i
        result.append(i)
        i+=2
    else:
        i+=2
print(max(result))


#문제 6. 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수라한다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (91=99) 입니다
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요.
def samenum():
    i = 0
    for a in range (100,1000,1):
        for b in range (100,1000,1):
            mylist = str(a*b)
            relist = mylist[: : -1]
            if mylist == relist and i < a*b:
                i = a*b
                # print(a,b)                  ##  돌면서 나옴
    return i

result = samenum()
print(result)


# 문제 7. 1~10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520. 1~20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마?

def maxyak(a,b):
    n = 0
    while True:
        m = a % b
        a = b
        b = m
        if m == 0:
            n = a
            break
    return n
k = 1
for i in range(2, 21, 1):
    k = k * i // maxyak(k, i)
print(k)

## 문제 8.
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
## 1**2 + 2**2 + ... + 10**2 = 385

## 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
## (1 + 2 + ... + 10)**2 = 552 = 3025

## 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의
## 차이는 3025 - 385 = 2640 이 됩니다.

## 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는
## 얼마입니까?

def jegobcha(n):
    sum1=0
    sum2=0
    for i in range(1, n+1):
        sum1+=i
    for j in range(1, n+1):
        sum2+=j**2
    return sum1**2 - sum2
print(jegobcha(100))

# 문제 9. 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다. 10,001번째 소수를 구하세요.
# 2,3,5,7,11 정도 넣고 1씩 증가 시키면서 list 안에 있는 어떤거로도 모듈라가 0이 아니면 append, len(list)가 10001 일때까지

# def sosu(n):
#     m = [2]
#     a = 3
#     while len(m) <= n:
#         for b in m:
#             if a % b == 0:
#                 break
#             else:
#                 m.append(a)
#         a = a + 2
#     return m
#
# print(sosu(10000))

def sosu(n):
    che = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if che[i] == True:
            for j in range(i+i, n, i):
                che[j] = False
    sos = [tmp for tmp in range(2, n) if che[tmp] == True]
    return sos

for i in range(104741, 999999, 2):          # 너무 오래걸린다............ 잘 모르겠음
    if len(sosu(i)) == 10001:
        print(sosu(i)[-1])
        break






## 문제 10.
## 세 자연수 a, b, c 가 피타고라스 정리 a**2 + b**2 = c**2 를 만족하면
## 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
## 예를 들면 3**2 + 4**2 = 9 + 16 = 25 = 5**2이므로
## 3, 4, 5는 피타고라스 수입니다.

## a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다.
## 이 때, a × b × c 는 얼마입니까?
for b in range(1, 667):
    for a in range(1, b):
        if a**2 + b**2 == (1000-a-b)**2:
            print(a*b*(1000-a-b))


## 문제 11.
## 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

## n → n / 2 (n이 짝수일 때)
## n → 3 * n + 1 (n이 홀수일 때)

## 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도
## 마지막에는 1로 끝나리라 생각됩니다.
## (이런 수들을 우박수 hailstone sequence라 합니다.)

## 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데
## 가장 긴 과정을 거치는 숫자는 얼마입니까?
## 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.

def hail(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n /2
            count += 1
        elif n % 2 == 1:
            n = 3*n + 1
            count += 1
    return count


# hail_count = []
# for i in range(1, 1000001):
#     hail_count.append(hail(i))
# print(hail_count.index(max(hail_count))+1)      # 837799          ,   525
# print(hail(837799))
print("우박수 답은 837799")