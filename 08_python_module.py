#
# python에서 Module은 함수나 변수 또는 클래스를 모아놓은 파일을 지칭
# 다른 python 파일에서 불러와서 사용할 수 있어요 !

# module을 사용하는 이유는 코드의 재사용성과 관리목적

# python 모듈은 크게 2가지가 있어요 !
# - C 언어로 구성된 binary module
# - python 언어로 구현된 일반 module
# module을 사용하기 위해서 사용하는 keyword : import
# module도 파이썬입장에서는 객체로 관리돼요 !

import sys

print(sys.path)                         # list로 되어있다.        module을 어따가 저장해야되는지???

sys.path.append("C:/python_data")       # module을 저장할 폴더를 지정\
#
# # module을 하나 생성해 보아요! (module1 python file을 생성해서 저 폴더에 잘라 붙여넣기)
#
# # module을 만들었으니 가져다가 사용해보자.
#
# import module1 as m1            # 파일 명이 길어서 별명을 붙여줄 수 있음 as ~~
# print(m1.my_pi)
# print(m1.my_adder(10,20))


# from module1 import my_adder        # 파일 안에 있는 함수 자체를 땡겨오면 파일명을 앞에 안 써줘도 됨
# print(my_adder(10, 20))

# from module1 import *                # 파일 안에 있는 모든 것을 땡겨올 떄는 *
# print(my_pi)

# c:/python_data안에 module1.py를 저장해 놓았다. -> 근데 python 파일이 많을 때는 계층별 폴더를 만들어서 관리 -> 패키지
# c:/python_data/test_module/module1.py  로 다시 저장

import test_module.module1 as my_module

print(my_module.my_pi)