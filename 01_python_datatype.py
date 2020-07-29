# 1. 주석
# python의 주석: 1줄 주석은 =>#
# 여러줄 주석은 """  """
"""
여기는 몽땅
주석입니다
"""
'''
이것도
주석입니다.
'''

# 2. python의 keyword
import keyword
print(keyword.kwlist)
# 어떤 키워드를 사용할 수 있는지 확인해보아요

# 3. 변수의 생성과 삭제 (파이썬 변수를 지정할 때 데이터 타입 지정 필요 x / weak ?)
# my_var = 100
# print(my_var)

# 4. 변수를 삭제할 수 있다 (다른 언어와의 차이점..?)
# del my_var

# Python의 데이터 타입(data type)
# python의 built-in data type (이미 가지고 있는 내부 정의되어 있는 type들 - 총 6개)
# - Numeric(숫자)
# - Text Sequence (문자열)
# - Sequence(순서 e.g. list)
# - Mapping
# - Set
# - Bool

# Numeric Data Type (숫자형)
# int(정수)
# float(실수)
# complex(복소수)

# a = 100 # 정수
# b = 3.14159265358979 # 실수
# c = 1 + 2j
# d = 0o34 # 8진수 int
# e = 0xAB # 16진수 int

# 데이터타입을 알고 싶을때 ! type():어떤 class인것을 알려주는 함수
# print(type(a)) # class int
# print(type(b)) # class float
# print(type(c)) # class complex

# my_result = 3 / 4 # 다른 언어는 같은 type끼리 연산하여 결과가 0, python은 그냥 0.75
# print(my_result)

# my_result = 10 % 3 # %모듈라 : 나머지 연산자
# print(my_result)

# my_result = 10 // 3 # 몫 연산자
# print(my_result)

##################################################

# 2. Text Sequence Type(str)

# 다른 언어는 문자(한글자)와 문자열(두글자 이상)을 구분
# 문자를 표현할 때 다른 언어는 ''
# 문자열을 표현할 때 다른 언어는 ""
# python은 문자열을 표현할 때 ('',"") 둘 다 가능 , 일반적으로 '' 많이 씀
a = "Hello"
b = "K"
c = 'python'

# 문자열 연산
first = 'haha'
second = 'hoho'

# print(first + second) #hahahoho
# print(first + 10) # 자바는 haha10, 파이썬은 error가 나옴 -> str(10)으로 변경 필요
# print(first * 3) #hahahahahaha

# indexing
my_var = "Hello"
# print(my_var[-1]) # 아주 중요함 / 맨 뒤의 문자를 하려면 -1부터 - slicing/indexing에 자주 사용

# slicing
my_var = "Hello"
# print(my_var[0:3]) # 앞에 있는 숫자가 시작 , 뒤가 끝, 다만 맨 뒤 숫자는 포함 안함***)
# print(my_var[0:]) # 뒤에가 없으면 끝까지, 앞에가 없으면 맨 앞 부터
# print (my_var[0:-1]) # 맨 뒤빼고 다
# print (my_var[:]) # 처음부터 끝까지

# in , not in 연산자
# myStr = 'This is a sample Text'
# print("sample" in myStr) # sample이라는게 myStr에 있니? -> true
# print("Sample" not in myStr) # sample이라는게 myStr에 없니? -> false

# formatting  %d, %s 등등 이렇게 쓰긴함
# num_of_apple = 10
# myStr = "나는 사과를 %d개 가지고 있어요!" % num_of_apple
# print(myStr)

# 문자열 formatting은 아래의 표현을 주로 사용합니다!
# num_of_apple = 10
# myStr = "나는 사과를 {}개, 바나나 {}개 가지고 있어요!".format(num_of_apple,20)
# print(myStr)

# 문자열 method를 이용해서 문자열 처리를 할 수 있다 !
# myStr = "cocacola"

# 문자열의 길이를 알고 싶으면? len() 함수를 이용
# print(len(myStr))

# print(myStr.count('c')) # str의 method인 count()를 이용
# print(myStr.find('o')) # str 중 o가 처음으로 어디에서 발견되는지 알려줌 -> 결과값:1

# myStr = "   myHobby" # 공백도 하나의 문자
# print(myStr.upper()) # 대문자로 변환
# print(myStr.lower()) # 소문자로 변환
# print(myStr.strip()) # 공백을 다 날림

# 3. Sequence type
# list
# 임의의 객체 (데이터)를 순서대로 저장하는 집합 자료형
# Java의 ArrayList와 유사...
# list는 literal로 표현할 때 [] (대괄호로 표현)
# my_list = []
# print(type(my_list))
# my_list = list()
# my_list = [1, 2, 3]
# my_list = [1, 2, 3.14, "Hello"]
# my_list = [1, 2, 3.14, "Hello", [5, 6, 7], 100] # 중첩 리스트

# indexing과 slicing을 할 수 있어요
# print(my_list[1]) #2
# print(my_list[-2]) # [5, 6, 7] 인덱싱은 그대로 떼어내옴
# print(my_list[4:5]) # [[5, 6, 7]] 하나만 떼어내는 slicing으로 리스트기 때문에 원래 형태를 유지해 리스트로 표현
# print(my_list[4][1]) #6
# print(my_list[0:2]) # [1, 2]

# list 연산
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)  # [1, 2, 3, 4, 5, 6]
# print(a * 2)  # [1, 2, 3, 1, 2, 3]

# a = [1, 2, 3]
# a[0] = 5
# print(a) #[5, 2, 3]
# a[0] = [7, 8, 9]
# print(a) #[[7, 8, 9], 2, 3]
# a[0:1] = [7, 8, 9] # slicing은 원래 형태를 유지함 -> 리스트인데 7, 8, 9니깐 안에 그대로 7, 8, 9 넣음
# print(a) #[7, 8, 9, 2, 3]

# a = [1, 2, 3]
# a.append(4)
# a.append([5, 6, 7])
# print(a) # [1, 2, 3, 4, [5, 6, 7]]  append는 맨 끝에 뭐가 됐던 간에 박는다.

# my_list = ["홍길동", "아이유", "강감찬", "신사임당", "Kim"]
# result = my_list.sort() # sort()는 리스트를 오름차순으로 정렬해줌
# 
# print(result) # None으로 나옴 - sort method는 return값이 없고 걍 정렬함, 영어가 한글보다 앞
# print(my_list)

## Sequence type (tuple) # list는 []로 표현, tuple은 ()로 표현
# a = (1, 2, 3)  # tuple은 일단 만들어지면 내용 변경이 안돼요 !! Read Only

# a = (1,) # 요소가 1개인 tuple은 뒤에 콤마를 찍어줌
# a = 1, 2, 3 # tuple은 괄호를 생략 가능
# print(type(a))
# a = (1, 2, 3)
# b = (4, 5, 6)
# print(a+b) # 각각 요소의 원본이 안 바뀔 뿐이지 연산 가능하다

# a = (1, 2, 3) # tuple을 [1, 2, 3]으로 바꾸고 싶을 때
# my_list = list(a)
# print(my_list)

# my_tuple = tuple(my_list)
# print(my_tuple)


## Sequence type (range)
# 주로 for문에서 사용함. 같은 데이터를 적은양의 데이터로 표현이 가능
# my_range = range(10) # 시작, 끝, 증감치 지정이 필요함 - 걍 10만 쓰면 끝이 10이고 증감치 1
# print(type(my_range))
# print(my_range[1:4]) # range(1, 4)    -> slicing은 원본 데이터 유형 그대로 따라감
# my_range = range(1, 10, 3)

# Mapping( dictionary:dict ) - key를 가지고 value를 찾는 것, 3.8부터 순서가 생김, JAVA에서는 map이라고 부름
# dictionary는 순서에 상관 없이 key와 value로 데이터를 저장하는 구조다. {}로 표현함 !
a = { "name": "홍길동", "age": 40} # JSON 표현법?
print(type(a))
print(a["name"])  #홍길동, 이렇게 써도 되고 get method 사용해도 가능하다.
a["address"] = "서울"
print(a)
print(a.get("age"))

# dict에서 많이 사용하는 대표적인 method 3개
a = { "name": "홍길동", "age": 40, "address": "서울"}
print(a.keys()) # dict_keys(['name', 'age', 'address'])
print(type(a.keys()))  # list처럼 생겼지만 아니다 dict_keys임
print(list(a.keys())) # 이렇게 해야 리스트로 나옴
print(a.values()) # 얘도 dict_values임
print(a.items()) # key와 value를 tuple로 표현해서 리스트로 만듦

###############2일차#############################

# bool data type -> boolean (True, False)
# 사용하는 연산자 => and, or, not 연사자를 사용 가능
# &, | - 연산자를 이용해 비트연산 가능함

# 다음의 경우는 python에서 False로 간주
# 1. 빈 문자열은 False로 간주 => "", ''
# 2. 빈 리스트는 False로 간주 => []
# 3. 빈 튜플도 False로 간주 => ()
# 4. 빈 dict도 False로 간주 => {}
# 5. 숫자 0은 False로 간주, 다른 숫자는 싹 다 True로 간주 (자바는 안 그럼)
# 6. None은 당연히 False로 간주

a = 5
b = 0
# print(a & b) # 주의* & : bitwise 연산 (2진수로 변환) -> 0101 & 0000 => 0000  (True and True만 True)

print(a | b) # -> 0101 | 0000 => 0101 (or)   |도 bitwise 연산


### Set datatype
# 집합 자료형이고 중복을 허용하지 않음
# 순서가 존재하지 않는 자료형

# {} => dict => {"key" : "value"}
# set도 {}로 표현 => { 1, 2, 3 }
# my_set = {1, 2, 3, 4, 1, 2} # 중복 제거해서 {1, 2, 3, 4}가 나옴
# print(my_set)

# my_list = [1, 2, 3, 4, 1, 2]
# my_set = set(my_list)

# my_str = "Hello"
# my_set= set(my_str)
# print(my_set)

# set에서 사용하는 연산자
# 합집합(union-|), 교집합(intersection-&), 차집합(difference-> -)
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(s1 | s2) # union {1, 2, 3, 4, 5, 6}
# print(s1 & s2) # {3, 4}
# print(s1 - s2) # {1, 2}


################여기까지가 built-in datatype#########################

# 추가적으로 날짜관련 사항도 알아보자
# date와 datetime에 대해서 알아보자

# from datetime import date, datetime
# today = date.today()
# print(today) # 2020-07-15
# # 오늘 날짜는 : 2020년 07월 15일 입니다.
# my_str = "오늘 날짜는 : {}년 {}월 {}일 입니다."
# my_str = my_str.format(today.year,today.month,today.day)
# print(my_str)
#
# my_datetime = datetime.today()
# print(my_datetime)
#
# print("현재 시간은 : {}시 {}분입니다.".format(my_datetime.hour,my_datetime.minute))

# 오늘이 07월 15일이다. 내일의 날짜는 07월 16일이다. => 이건 쉬운데...
# 오늘이 01월 31일이다. 내일의 날짜는 02월 1일이에요 => 그래도 할만해
# 오늘이 03월 01일이다. 어제의 날짜는 02월 29일이에요 => 할게 아님...

## 결론, 날짜 연산은 처리하기가 너무 힘들어서 계산을 통해 처리하는게 아니라 delta(외부 모듈)를 이용해서 처리한다!

# from datetime import date, datetime, timedelta #(days, hours, minutes, seconds)

# today = date.today()
# past = timedelta(days=-20) # 20일 전
# print(today + past)

# today = datetime.today()
# past = timedelta(hours=-20) # 20시간 전
# print(today + past)

# 1달전 날짜를 알아보자, 예) 오늘 날짜가 3월 31일이면 => 1달전 날짜는 2월 28일
# 연도와 월에 대한 timedelta는 존재하지 않다 -> 그래서 새로운 외부 module을 사용해야 한다. (package 다운 필요)
# from datetime import date
# from dateutil.relativedelta import relativedelta

# today = date.today()
# past = relativedelta(months=-1)
# print(today + past)

# 현재 날짜와 시간만 하고 있는디... 문자열로 되어 있는 날짜를 진짜 날짜로 변환해서 연산을 하고 싶다면?
# 문자열은 parse를 사용, 숫자로 되어 있으면 datetime으로 처리하는게 가장 편함
from datetime import datetime
from dateutil.parser import parse
my_date = parse("2019-01-30")
print(my_date)
my_date = datetime(2019, 1, 30)
print(my_date)

##################날짜 끝 #############################################

# Python의 Data type은 여기까지 정리했다.

a = "::"
b = "abcd"
result = a.join(b)
print(result)  # a::b::c::d



