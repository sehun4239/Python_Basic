# Object Oriented Programming (객체지향)
# 1990년도 이전 : 가장 대표적인 프로그램 작성 방식 (기법)
# 구조적 프로그래밍 (절차적 프로그래밍)
# 프로그램 작성시 기능으로 세분화해서 각각의 기능을 모듈(함수)로 제작해서 프로그램을 작성 (은행 -예금/대출/외환/펀드... - 예금에는 입금 출금 송금 .... 이런식)
# 장점 -> 설계가 쉽다 - 빨리 만들 수 있다 ! - 프로그램 하기가 쉽다 - 비용절감효과
# 단점 -> 수정(유지 보수)이 어렵다, 프로그램 재사용이 어렵다 (세부 module/function을 수정하면 그걸 쓰는 모든 부분에 영향을 미치기 때문에)
# 90년대 이후 인터넷이 등장하면서 사회가 급변해 유지 보수 사항이 많아져 수정을 많이하게 되고 비용이 많이 발생하게 됨 -> 기능 세분화 문제점
# 세상이 변하고 프로그램의 유지보수가 중요하게 대두됨 -> 현실세계의 해결해야 하는 문제에 대한 구성요소를 파악
# => 은행지점, 고객, 텔러, ATM, 계좌, ... (개체 object) 
# => object oriented programming의 시대가 열린다 (90년대~)
# => 개체들을 파악해서 그 개체들간의 관계를 프로그래밍 하는 방식을 객체지향 프로그래밍이라고 한다.
# => 내가 해결해야 하는 문제 (구현해야 하는 시스템)을 그대로 프로그램으로 모델링하는 방식.
# 그렇기 때문에 기능으로 세분화하지 않고 구성요소를 파악한 후 구성요소간의 데이터 흐름에 집중해서 구현하게 된다.

# => 개체들을 파악한 후 이 각각의 개체를 프로그램적으로 묘사해야 해요
# => 객체 모델링
#    객체 모델링을 하기 위해서 현실 세계의 객체를 단순화 (abstraction 추상화)

# 예) 사람을 프로그램적으로 묘사해보아요 (객체모델링을 해 보아요)
# 추상화(abstraction)과정을 거쳐서 사람을 객체모델링 할 거다
# 이런 개체들은 속성과 행위가 있더라
#             변수(property, member field, field),
#             함수(method)
# class라는 걸 이용해서 추상화과정을 거친 개체를 프로그램적으로 표현하게 된다.
# class가 뭔가요?? => 1. 객체모델링의 수단

# class 사람
#       키 (변수) height => float
#       몸무게 (변수) weight => float
#       나이 (변수) age => int
#       이름 (변수) name => str
#       걷는다 (메소드)
#       말한다 (메소드)
#       잔다 (메소드)

# class 안의 함수는 메소드다
# class는 data type의 관점에서 봤을때는 기존 데이터타입을 이용해서
# 새로운 data type을 만드는 것이라고 볼 수 있다.
# class => 2. 추상적인 데이터 타입이라고 부른다. (abstract data type) =>  ADT
# class에서 instance를 생성해야 한다 -> instance는 객체 (object) = > 메모리 공간

#############################################################

# 구조적 프로그래밍 (절차적 프로그래밍)
# 프로그램 작성 시 기능으로 세분화해서 각각의 기능을 모듈화(함수화)해서 구현
# 프로그램 구조를 이해하기 쉽고 (Tree구조) 프로그램을 빠르게 만들 수 있다 !
# 프로그램 규모가 커지면 유지보수와 코드의 재사용에 한계가 오게된다 !

# 객체지향 프로그래밍
# 현실 세계의 해결해야 하는 문제를 그대로 프로그램으로 묘시(표현)
# 프로그램을 구성하는 주체들 (개체, 객체, object)을 파악하고 그 객체들 간의 데이터 흐름에 초점을 맞추어서 프로그램을 작성
# 프로그램을 설계하고 작성하는 것이 상대적으로 어렵다!
# 일단 제대로 작성된 객체지향 프로그램은 유지보수와 재사용성에 상당한 이점이 있다. *** 객체지향의 모토

###################################################################

# 학생의 이름, 학과, 학번, 평균평점을 저장하는 방법

# stu_name = "홍길동"
# stu_dept = "심리학과"
# stu_num = "20201134"  # 숫자로 할 경우는 연산의 의도가 있다, 문자로 하면 slicing등 뭐 찾아내기도 좋다.
# stu_grade = 3.5

# 만약 3명의 학생이 있으면 어떻게 하나요?

# stu1_name = "홍길동"
# stu1_dept = "심리학과"
# stu1_num = "20201134"
# stu1_grade = 3.5

# stu2_name = "김길동"
# stu2_dept = "컴퓨터"
# stu2_num = "20201135"
# stu2_grade = 2.0

# stu3_name = "신사임당"
# stu3_dept = "경영학과"
# stu3_num = "20201138"
# stu3_grade = 4.0

# 코드가 너무 불필요하게 반복적이고 확장성이 없는 코드가 됐다.

# stu_name = ["홍길동", "김길동", "신사임당"]
# stu_dept = ["심리학과", "컴퓨타", "경영학과"]
# stu_num = ["20201134", "20201135", "20201138"]
# stu_grade = [3.5, 2.0, 4.0]

# index를 이용해 처리하는게 쉬운작업은 아니고 코드에 모든 의미가 다 내포되어 있는게 아닌 문제가 발생.

# 어떻게 하면 이런 내용을 class 이용해서 객체지향적으로 표현 할 수 있을까???
# 학생이라는 개념을 프로그램적으로 모델링을 해 보자 - class이름은 관용적으로 첫 글자 대문자 (함수는 소문자)

# class Student(object):           # 괄호는 상속의 의미 # self는 현재 사용하는 객체에 대한 reference다. self가 없으면 어떤 객체(공간)를 사용하는지 알 수 없다.
#     def __init__(self,name,dept,num,grade):# class를 기반으로 instance 공간을 만들면서 자동으로 호출되며, 그 공간을 초기화 데이터를 넣음.
#         self.name = name                       # 셀프 뒤의 "."은 dot operator (연산자) 셀프에 대해서~
#         self.dept = dept                       # . 뒤의 네개는 instance variable이라 부른다.
#         self.num = num
#         self.grade = grade
# 
# students = []
# students.append(Student("홍길동", "심리학과", "20201134", 3.5))
# students.append(Student("김길동", "컴퓨터", "20201135", 2.0))
# students.append(Student("신사임당", "경영학과", "20201138", 4.0))

####################################

## python은 객체지향 언어입니다. (자바가 객체지향에 가장 가까움, 무조건 객체지향 사용)
## python에서 나오는 모든것은 다 객체(instance)다.

# a = 10       # 객체(instance)다. 객체가 잇다는 것은 class도 있다 -> class 'int'
# print(type(a))  # class 'int'

# my_list = [10]
# print(type(my_list))

# class list(object):        이제 우리는 요런 클래스가 파이썬에 있다는 것을 알 수 있다.
#       ~~~
#       ~~~

# 숫자도 객체(instance)고, 리스트도 객체(instance)고, str(문자열)도 객체고, 함수도 객체
# 객체(instnace)가 있다는 건 => class가 존재한다는 이야기다.
# 객체(instance) => 변수, method

# 객체(instance)란 속성과 같은 여러가지 데이터 + 메소드를 가지고 있는 데이터 구조를 지칭한다.

# class Student(object):
#     def __init__(self,name,dept,num,grade):   # constructor (생성자)(자바), initializer (파이썬) 용어
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):                     # print 했을때 어떤게 나올지 정해주는 메소드
#         return self.name
#
#     def change_dpt(self,tmp_dept):
#         # tmp_dept가 정상적인 학과인지 check하는 코드가 들어가야 한다. 그러면 아주 좋다
#         self.dept = tmp_dept
#
# student = Student("홍길동","심리학과","20201134",4.5)
# # print(student)  # 홍길동
#
# #student.dept = "경영학과"  # 이렇게 하면 안 좋대 -> method를 이용해서 수정하게끔 만드는게 더 좋은 방식이다.
# #information hiding (정보은닉) 개념도 알아둬야 합니다!
#
# student.change_dpt("경영학과")
# print(student.dept)

##########################################################

# python이 제공하는 내장함수 중 dir() 에 대해서 알아보자
# 객체가 인자로 들어오면 해당 객체의 모든 속성과 메소드를 알려준다.

# class Student(object):
#     def __init__(self,name,dept,num,grade):   # constructor (생성자)(자바), initializer (파이썬) 용어
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):                     # print 했을때 어떤게 나올지 정해주는 메소드
#         return self.name
#
#     def change_dpt(self,tmp_dept):
#         # tmp_dept가 정상적인 학과인지 check하는 코드가 들어가야 한다. 그러면 아주 좋다
#         self.dept = tmp_dept
#
# student = Student("홍길동","심리학과","20201134",4.5)
# print(dir(student))

# 한 가지를 더 생각해보자
# student.depts = "철학과"   # s가 오타나면 에러인가 ?? 다른 언어(자바 씨 등등)면 다 error, 근데 파이썬은 그냥 추가해줌
# print(dir(student))         # 프로그램 유연성 측면에서는 좋지만 객체지향 측면에서는 안 좋음

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', 'change_dpt', 'dept', 'grade', 'name', 'num']

# def my_func(a,b):
#     return a+b

# print(dir(my_func))

# my_func.myName = "홍길동"
# print(dir(my_func))

##
# class Student(object):
#     scholarship_rate = 3.0        # class variable (모든 인스턴스가 공유하는 변수)
#
#     def __init__(self, name, dept, num, grade):   # constructor (생성자)(자바), initializer (파이썬) 용어
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def is_scholarship(self):
#         if self.grade > Student.scholarship_rate:
#             return True
#         else:
#             return False
#
# student = Student("홍길동","심리학과","20201134",4.5)
# print(Student.is_scholarship(student))

######################################

# class Student(object):
#     scholarship_rate = 3.0
#
#     def __init__(self, name, dept, num, grade):
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     def __repr__(self):
#         return self.name
#
#     def is_scholarship(self):                       # instance method ( __XXXX__은 magic function)
#         if self.grade > Student.scholarship_rate: #self.scholarship 으로 해도 error가 아님 -> instance namespace에 없으면, class namespace에서 찾아서 똑같이 나옴
#             return True
#         else:
#             return False
#
# student = Student("홍길동","심리학과","20203311",4.0)
#
# student.scholarship_rate = 4.5     # student instance에 없는 속성을 써서 scholarship_rate가 속성으로 추가된다.
#
# print(student.is_scholarship())   # 위의 def is_scholarship에서 Student를 넣으면 True값 , self를 넣으면 False




###################################################
#4일차####

# namespace (네임스페이스    ~~ scope 개념)
# 객체가 가지는 데이터를 나누어서 관리하는 공간  (공간이 나눠져 있으므로 속성이름이 똑같아도 space가 다르면 다름)
# instance namespace
# class namespace
# superclass namespace
# instance namespace < class namespace < superclass namespace (포함 관계)

# python은 동적으로 속성이나 method를 추가할 수 있어요

# print(student.dept)
# student.depts = "컴퓨터"      # depts 속성이 추가된다
#
# print(student.depts)

##########
# class Student(object):
#     scholarship_rate = -3.0
#
#     def __init__(self, name, dept, num, grade):
#         self.name = name
#         self.dept = dept
#         self.num = num
#         self.grade = grade
#
#     @classmethod       # class method decorator
#     def change_scholarship(cls, rate):                # class 인자를 받아서 처리하겠다 ! -> class method
#         cls.scholarship_rate = rate
#         print("장학금 기준이 변경되었어요!")
#
#     @staticmethod      # static method decorator       # 자바에서의 staticmethod랑은 다르다
#     def is_valid_scholarship(rate):
#         if rate < 0:
#             print("장학금 기준 학점은 음수가 될 수 없습니다")
#
#     def is_scholarship(self):                       # instance method ( __XXXX__은 magic function)
#         if self.grade > Student.scholarship_rate: #self.scholarship 으로 해도 error가 아님 -> instance namespace에 없으면, class namespace에서 찾아서 똑같이 나옴
#             return True
#         else:
#             return False
#
# student = Student("홍길동","심리학과","20203311",4.0)
#
# Student.is_valid_scholarship(Student.scholarship_rate)
# Student.change_scholarship(3.7)



# 1. instance method (self 인자를 가지고 있는 method)
# 인스턴스에 한정된 데이터를 생성, 변경, 참조하기 위해서 사용된다.

# 2. class method는 클래스를 인자로 받아서 class variable을 생성, 변경, 참조하기 위해서 사용

# 3. static method는 class 안에서 정의된 일반 함수

#######################################################################################

# information hiding (정보 은닉)
# instance가 가지는 데이터는 매우매우 중요한 데이터이기 때문에
# 외부에서 직접적으로 access하는건 좋지 않아요 !   (e.g. student.dept = "컴퓨터 " 이런식으로 직접 변경하는 것)

# 어떻게 외부에서 직접적으로 access하는 것을 막을 수 있는가?
# 프로그래밍 언어마다 다름 !
# Java => access modifier(접근제어자)
#        public vs. private
# Python에서 속성에 직접적으로 접근하는 것을 막기위해서는 어떻게 해야 하나요 ?? => private으로 지정하려면 어떻게 해야하나??
#"__"

class Student(object):

    def __init__(self, name, dept, num, grade):
        self.name = name
        self.__dept = dept
        self.num = num
        self.grade = grade

    def getDept(self):          # getter
        return self.__dept
    # setter는 값을 설정해주는 method
    def setDept(self, dept):
        self.__dept = dept

    def __print_date(self):     # 속성뿐만아니라 method도 __로 감출 수 있다.
        return self.name

student = Student("홍길동","심리학과","20203311",4.0)
# print(student.__dept)               # __를 넣어서 dept가 있지만 dept에 direct access할 수가 없게됨 (private 처리)
# student.__dept = "컴퓨터"            # 반응 없음

# private으로 처리된 속성이 있으면 외부에서 직접적인 access가 안되기 때문에 method를 이용해서 사용하도록 처리해야한다.
# private으로 되어 있는 속성의 값을 알아보는 용도의 이런 method를 getter라고 한다. (getter의 이름을 짓는 방법이 정해져 있다)

# print(student.getDept())
# student.setDept("컴퓨터")
# print(student.getDept())

# 여기까지가 단일 class에 대한 이론적인 내용이다.
########################################


# 객체지향을 하는 이유는 ==> 유지보수와 재사용성
# 재사용성을 위한 대표적인 객체지향 기법 => Inheritance (상속)  /  객체지향의 꽃
# class A (parent class, super class)(속성 n개, method m개)  ----->   B  (child class, sub class)
# is - A 관계 (sub class is a super class) 단 역은 성립하지 않는다 ! 사람은 포유류다 !

# 두 개의 class를 이용해서 상속을 알아보자
# Unit class, Marine class
# Unit class => 모든 unit이 공통으로 가지고 있는 속성과 method로 구성
#                super class로 사용, base class
# Marine => sub class

# class object(): ~~~~  실제 이런 클래스가 존재한다.
# Python의 모든 class는 object class다. (즉, object class를 상속해야 한다, 괄호의 의미는 상속이다)

# class Unit(object):
#     def __init__(self, damage, life):
#         self.utype = self.__class__.__name__     # 객체의 class를 찾아가 class의 name을 넣는다.
#         self.damage = damage
#         self.life = life
#
#     def show_status(self):
#         print("직업: {}".format(self.utype))
#         print("공격력: {}".format(self.damage))
#         print("생명력: {}".format(self.life))
#
# # class Marine(Unit):
# #     pass                                        # 내용이 없을 때는 pass
# # marine_1 = Marine("100", "100")
# # marine_1.show_status()
#
# class Marine(Unit):
# # 아래처럼 하위 클래스에서 method를 재정의해서 사용하는 것을 over riding?이라고 한다.
#     def __init__(self, damage, life, range_upgrade):
#         super(Marine, self).__init__(damage, life)          # 마린 클래스의 상위 클래스를 찾아라 -> 유닛 / 아래 3줄 대신
#         # self.utype = self.__class__.__name__              # 객체의 class를 찾아가 class의 name을 넣는다.
#         # self.damage = damage
#         # self.life = life
#         self.range_upgrade = range_upgrade
#
#     def show_status(self):
#         super(Marine, self).show_status()
#         # print("직업: {}".format(self.utype))
#         # print("공격력: {}".format(self.damage))
#         # print("생명력: {}".format(self.life))
#         print("사거리 업그레이드 유무: {}".format(self.range_upgrade))
#
# marine_1 = Marine("100", "100", True)
# marine_1.show_status()

##################################################################

# 사용할 유닛들은 Marine, Medic, Vulture, Dropship 4 종류의 unit

# super class
# class Unit(object):
#     def __init__(self, damage, life):
#         self.utype = self.__class__.__name__
#         self.damage = damage
#         self.life = life
#
#     def show_status(self):
#         print("직업: {}".format(self.utype))
#         print("공격력: {}".format(self.damage))
#         print("생명력: {}".format(self.life))
#
#     def attack(self):
#         pass
#
# class Marine(Unit):
#     def __init__(self, damage, life, range_upgrade):
#         super(Marine, self).__init__(damage, life)
#         self.range_upgrade = range_upgrade
#
#     # overriding
#     def show_status(self):
#         super(Marine, self).show_status()
#         print("사정거리 업그레이드 유무: {}".format(self.range_upgrade))
#
#     # overriding
#     def attack(self):
#         print("마린이 총으로 공격합니다. 탕탕!")
#
#     def stimpack(self):
#         if int(self.life) < 20:
#             print("체력이 낮아서 스팀팩 사용이 불가능합니다.")
#         else:
#             # self.life -= 10
#             # self.damage *= 1.5
#             print("마린이 스팀팩을 사용했습니다!")
#
# class Medic(Unit):
#     def attack(self):
#         print("메딕이 치료합니다. 힐힐!")
#
# class Vulture(Unit):
#     def __init__(self, damage, life, amount_of_mine):
#         super(Vulture, self).__init__(damage, life)
#         self.amount_of_mine = amount_of_mine
#
#     def attack(self):
#         print("벌쳐가 공격합니다. ~~~")
#
# class Dropship(Unit):
#     def attack(self):
#         print("특정 목표지점으로 이동합니다. 슝~")
#
#     def board(self, unit_list):
#         self.unit_list = unit_list
#         print("유닛들을 드랍쉽에 태웠습니다.")
#
#     def drop(self):
#         print("모든 유닛이 드랍쉽에서 내립니다.")
#         return self.unit_list
#
# # marine을 3마리 생성
#
# marine_1 = Marine("100", "100", False)
# marine_2 = Marine("100", "100", False)
# marine_3 = Marine("100", "100", False)
#
# # medic을 1마리 생성
# medic = Medic("0", "100")
#
# # vulture를 2마리 생성
# vulture_1 = Vulture("200", "100", 3)
# vulture_2 = Vulture("200", "100", 3)
#
# # list를 이용해서 여러개의 객체를 저장할거에요
# troop = list()
# troop.append(marine_1)
# troop.append(marine_2)
# troop.append(marine_3)
# troop.append(medic)
# troop.append(vulture_1)
# troop.append(vulture_2)
#
# # dropship 생성
# dropship = Dropship("0", "100")
#
# # dropship에 유닛들을 태워요
# dropship.board(troop)
#
# # 공격지점으로 이동
# dropship.attack()
#
# # 공격지점에서 내리기
# my_list = dropship.drop()
#
# # 스팀팩을 쓰고 공격
# for unit in my_list:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     unit.attack()

############################################################

class Student(object):

    def __init__(self, name, kor, eng, math):
        self.__name = name                      # 기본적으로 instance variable들은 private으로
        self.__kor = kor
        self.__eng = eng
        self.__math = math
        self.avg = round((kor + eng + math) / 3, 1)

    def __repr__(self):
        return "{} {}".format(self.__name, self.avg)

file1 = open("C:/python_data/student_score.txt", "r")
students = list()

while True:
    line = file1.readline()     # 홍길동,18,7,19
    if not line:
        break
    stu_data = line.split(",")  # ['홍길동','18','7','19']
    students.append(Student(stu_data[0], int(stu_data[1]), int(stu_data[2]), int(stu_data[3])))

result = reversed(sorted(students, key=lambda stu:stu.avg))
for tmp in result:
    print(tmp)

file1.close()


# student_score.txt 파일에서 불러와서 class만들어 처리해보자. (나중에는 pandas를 써서 땡겨옴)
# 각 사람에 대한 데이터를 읽어서 성적순으로 출력하시면 된다. 출력양식은 다음과 같다.
# 1등 아이유 95.6
# 2등 홍길동 89.3 ~~~ 이런 식으로

# file1 = open("C:/python_data/student_score.txt", "r")
#
# mylist = []
# while True:
#     line = file1.readline()
#     if not line:
#         break
#     mylist.append(line[0:-1])
#
# file1.close()
# print(mylist)
#
# class Student(object):
#     def __init__(self, list):
#         self.name = list[0]
#         self.s1 = list[1]
#         self.s2 = list[2]
#         self.s3 = list[3]
#
#     def avg(self):
#         return (int(self.s1)+int(self.s2)+int(self.s3)) / 3
#
# for i in range()
#     student_i = str(mylist[0]).split(",")
#

