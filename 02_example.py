# 문제 1. 1000보다 작은 자연수 중에 3 또는 5의 배수들을 모두 합하면 얼마인가요?
# my_sum=0
# for i in range(1,1000):
#     if i % 3 == 0:
#         my_sum+=i
#     elif i % 5 == 0:
#         my_sum+=i
#     else:
#         pass
# print(my_sum)

tmp3 = [i for i in range(1, 1000) if i % 3 == 0]
tmp5 = [i for i in range(1, 1000) if i % 5 == 0]
result = set(tmp3).union(set(tmp5))
print(sum(result))

# 문제 2. 피보나치 수열 중 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?
pi_sum=0
j=1
k=1
l=j+k
while l<=4000000:
    if l % 2 ==0:
        pi_sum+=l
        j = k
        k = l
        l = j+k
    else:
        j = k
        k = l
        l = j + k
print(pi_sum)


# 문제 3. 문자열 중에 가장 많이 사용된 알파벳이 무엇인지 출력하는 프로그램을 작성하시요. 대소문자 구별 x
# 단 동률이 존재하는 경우 알파벳 순으로 제일 앞에 있는 문자를 출력하세요 input("문자열을 넣으세요")

# my_str=input("문자열을 입력하십시오. :")
# my_str=my_str.lower()
# my_list=list(my_str)
# my_set=set(my_list)
# a=[]
# x=0
# for i in my_set:
#     j = my_str.count(i)
#     if x<j:
#         x=j
#         a=[]
#         a.append(i)
#     elif x == j:
#         a.append(i)
# a.sort()
# print("가장 많은 알파벳은 {}입니다".format(a[0]))

## 문제 4.
## 로또 프로그램 작성
## 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.
## 즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
## 쉬운버전을 해결했다면
## 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
## 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
## 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 꽝 몇개로 출력
## 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
## 4등 몇개, 5등 몇개, 꽝 몇개로 출력

## 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
import random

def buy():
    lotto = []
    for i in range(45):
        i = random.randrange(1, 46)
        if i not in lotto:
            lotto.append(i)
            if len(lotto) == 7:
                break
    return lotto

def bonus(lotto):
    bonu = lotto.pop()
    return bonu

print(bonus(buy()))

##### 추가문제
##### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?
##### 로또 1게임은 1000원입니다.
def com(x,y):
    total = 1
    for i in range(1, y):
        total = total * (x-i-1) / i
    return(total)

print(1000*com(45,6))