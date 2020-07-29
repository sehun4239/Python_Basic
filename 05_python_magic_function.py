# magic function

# - 1. method의 이름 앞 뒤에 더블 언더스코어(__)가 붙어 있는 method를 지칭한다.
# 대표적인 magic function => __init__ (생성자)
# - 2. class 안에 정의할 수 있는 특수한 형태의 method
# - 3. 특수한 상황에서 그에 맞는 magic function이 호출됩니다 ! (callback)

# class Student(object):
#     def __init__(self, name, dept):           # 생성자, constructor, initializer
#         self.name = name
#         self.dept = dept
#         print("{} 학과 {} 학생이 생성되었습니다".format(self.dept, self.name))
#     #자바는 생성자만 있고 소멸자는 없는디, 파이썬이나 c++은 소멸자도 있다.
#
#     def __del__(self):
#         print("소멸자가 호출되었어요!")
#
# stu1 = Student("홍길동", "심리")
#
# del stu1            # 객체를 메모리에서 삭제해요 !! __del__ 호출돼요

#################################################

# a = 100
# print(type(a))  # class int가 존재한다 !

# class MyInt(int):
#     pass
#
# my_num = MyInt(100)
# print(my_num + 200)
# print(my_num.__add__(200))

#################################################

# class Student(object):
#     def __init__(self, name, dept):           # 생성자, constructor, initializer
#         self.name = name
#         self.dept = dept
#         print("{} 학과 {} 학생이 생성되었습니다".format(self.dept, self.name))
#
#     def __repr__(self):
#         return self.name
#
# stu1 = Student("홍길동", "심리")
#
# print(stu1) # instance의 class 정보와 저장되어 있는 메모리 주소가 출력

####################################################


class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __lt__(self, other):
        if self.price < other.price :
            return "{} 가격이 더 낮습니다.".format(self.model)
        else:
            return "{} 가격이 더 높습니다.".format(self.model)

car1 = Car("G70", 5000)
car2 = Car("Sonata", 3000)

print(car1 < car2)      # 원래라면 error가 뜨는데 __lt__ 라는 magic function을 overriding 해서 재정의하여 저렇게 바꿈
#######################################################



