# exception (예외)
# Error - compile time error : 문법오류
#         runtime error : 실행시 발생하는 오류

# 어떤 runtime error들은 비정상 종료되지 않고 프로그램을 지속적으로 수행시킬 수 있는 방법이 있다.

# exception 처리는 하나의 구문밖에 없어요!

# try~~~~
# except: try에 오류가 있을경우 끝나지 않고 바로 except로 간다.
# else: try에 오류가 없을 경우 else로 간다.
# finally: 있던 없던 무조건 마지막으로 수행된다.

def my_func(my_list):
    total_sum = 0       # list 안의 숫자들을 누적해요!
    try:
        total_sum = my_list[0] + my_list[1] + my_list[2]
        print("try가 수행되었어요!")
    except Exception:                    # Exception : 모든 오류를 전부 지칭한다.
        print("오류가 존재합니다.")     # 예외처리를 해야 해요 !
    else:
        print("오류가 없어요!")
    finally:
        print("무조건 수행돼요!")

my_func([1, 2, 3])
my_func([1, 2])