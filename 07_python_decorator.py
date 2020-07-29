# Decorator

# Decorator의 사전적 의미는 장식가, 도배업자
# Python에서 Decorator는 기존의 코드에 여러가지 기능을 추가하는 python구문이라고 이해하면 편하다.

# Closure
# first class에 대해서 알아보았다. first class function (일급함수): 파이썬은 일급함수를 지원하는 언어다.
# 1. 파이썬의 함수는 변수에 저장할 수 있다.
# 2. 함수의 인자로 함수를 이용할 수 있다. ==> Decorator
# 3. 함수의 결과값(리턴값)으로 함수를 이용할 수 있다. ==> Closure

# def my_outer_func(func):
#
#     def my_inner_func():
#         func()
#
#     return my_inner_func
#
# def my_func():
#     print("my_func() 함수가 호출 되었어요!!")
#
# decorated_my_func = my_outer_func(my_func)
# decorated_my_func()
# my_func()

# import time
# def my_outer_func(func):
#
#     def my_inner_func():
#         print("{} 함수 수행 시간을 계산합니다.".format(func.__name__))
#         start = time.time()     # 1970년 1월 1일 0시 0분 0초 의 값이  0이다.
#         func()
#         end = time.time()
#         print("함수 수행 시간은 {}입니다..".format(start-end))
#
#
#     return my_inner_func
#
# @my_outer_func                      # 이걸 decorator라 한다.
# def my_func():
#     print("my_func() 함수가 호출 되었어요!!")
#
# #위의 decorator를 풀어쓰면 아래처럼 나옴
# # decorated_my_func = my_outer_func(my_func)
# # decorated_my_func() # my_func에 추가적인 기능을 넣고 싶은데 함수 원형은 변화시키고 싶지 않다면 다른 함수를 만들어서 decorator 사용
# my_func()

###################################################################

# def print_user_name(*args):      #인자로 들어온 사람의 이름을 출력    -   여러개 들어올 수 있으니 *xxx
#     # args는 tuple로 받는다!
#     for name in args:
#         print(name)
#
# print_user_name("홍길동", "신사임당")  # 이렇게도 가능
# print_user_name("홍길동", "신사임당", "유관순")  # 이렇게도 가능

# def print_user_name(**kwargs):      #인자로 들어온 사람의 이름을 출력
#     # kwargs는 dict로 받는다!
#     for key in kwargs.keys():
#         print(kwargs.get(key))
# # ( "name1" : "홍길동", "name2" : "신사임당" )
# print_user_name(name1="홍길동", name2="신사임당")

# Decorator에 대해서 한가지 더 알아보아요!

def my_outer(func):

    def my_inner(*args,**kwargs):
        print("데코레이터! 시작")
        func(*args,**kwargs)
        print("데코레이터! 끝")

    return my_inner

@my_outer
def my_func():
    print("이것은 소리없는 아우성!")

@my_outer
def my_add(x,y):                            # error가 뜸 -> my_outer에는 함수안에 인자가 없음. -> 그래서 *args~~~ 넣음
    print("두 수의 합은 : {}".format(x+y))

my_func()

my_add(10, 20)








