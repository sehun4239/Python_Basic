# my_range = range(10) # 시작, 끝, 증감치 지정이 필요함 - 걍 10만 쓰면 끝이 10이고 증감치 1
# print(my_range)
# print(my_range[1:4]) # range(1, 4)    -> slicing은 원본 데이터 유형 그대로 따라감
# # my_range = range(1, 10, 3)
#
# print(list(my_range))
# print(len(my_range))
#
# sum=0
# for i in range(11):
#     sum+=i
# print('총 합계는 %d입니다' %sum)
#
# print('1', end = '')
# print('2')

list2 = ['1','2','3','2','4']
list3 = list2[: : -1]
print()

mystr = "12"
restr = mystr[: : -1]
print(restr)

my_dict = {"김":1000, "장":100}
sum = 0
for (key, value) in my_dict.items():
    sum += value
print(my_dict.values())

my_dict = {"stu" + str(x): x ** 2 for x in range(1, 10)}
print("my_dict : {0}".format(my_dict))

animal = ["멍멍이","사자","호랑이","개"]
print(",".join(animal))
print("-".join(animal))

a = [1,2,3]
b = ["a","b","c"]
c = list(zip(a,b))

print(c)

str=list(zip("Hello","World"))
print(str)

# map() : 특정함수에 입력값을 주어 반복 호출
def my_func(x):
    return x**2

a = list(map(my_func,range(1,10)))
print(a)


a = [ 1, 3, 5, 7, 9, 13, 15 ]
b = [ 4, 5, 6, 8, 13 ]
c = [ 5, 8, 13, 19 ]

d = set(a).intersection(set(b))
e = d.intersection(set(c))
result = list(e)
print(result)

phone_number = "010-1111-2222"
ans = phone_number.replace("-"," ")
print(ans)

string = 'abcdfe2a354a32a'


print(list(bin(27)))


n=6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
list_1 = [list(bin(i))[2:] for i in arr1]
list_2 = [list(bin(i))[2:] for i in arr2]
def mola(list):
    for i in list:
        if len(i) < 6:
            while len(i) <= 5 :
                i.insert(0,"0")
    return list
real_1 = mola(list_1)
real_2 = mola(list_2)

result = []
print(list(zip(real_1,real_2)))
for (i,j) in zip(real_1,real_2):
    result2 = []
    for num in range(n):
        if i[num] == "0" and j[num] == "0":
            result2.append(" ")
        elif i[num] == "1" or j[num] == "1":
            result2.append("#")
    result.append(result2)

print(result)
ans = ["".join(i) for i in result]
print(ans)
# ["######", "### #", "## ##", " #### ", " #####", "### # "]
