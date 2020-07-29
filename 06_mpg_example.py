class Car(object):
    def __init__(self, manufac, model, displ, year, cyl, trans, drv, cty, hwy, fl, type):
        self.manufac = manufac
        self.model = model
        self.displ = displ
        self.year = year
        self.cyl = cyl
        self.trans = trans
        self.drv = drv
        self.cty = cty
        self.hwy = hwy
        self.fl = fl
        self.type = type
        self.yeonbi = (hwy + cty) / 2


    def dividea(self):
        if self.displ <= 4:
            return self.hwy
        else:
            pass

    def divideb(self):
        if self.displ >= 5:
            return self.hwy
        else:
            pass

    def dividename(self,name):
        if self.manufac == name:
            return self.cty
        else:
            pass

    def dividenamehwy(self,name):
        if self.manufac == name:
            return self.hwy
        else:
            pass


def avg(list):
    sum=0
    for i in list:
        sum += float(i)
    result = sum / len(list)
    return result

file1 = open("C:/python_data/mpg.txt", "r")
cars = list()

while True:
    line = file1.readline()
    if not line:
        break
    car_data = line.split(",")
    cars.append(Car(car_data[0], car_data[1], float(car_data[2]), int(car_data[3]), float(car_data[4]), car_data[5], car_data[6],
                float(car_data[7]), float(car_data[8]), car_data[9], car_data[10].strip()))

#1번
a=[]
b=[]
for car in cars:
    a.append(car.dividea())
for car in cars:
    b.append(car.divideb())
list_a = list(filter(None, a))
list_b = list(filter(None, b))

print("1번")
print("4이하는 {}".format(avg(list_a)))
print("5이상은 {}".format(avg(list_b)))

#2번
result_audi=[]
result_toyota=[]
for car in cars:
    result_audi.append(car.dividename("audi"))
for car in cars:
    result_toyota.append(car.dividename("toyota"))
result_audi = list(filter(None, result_audi))
result_toyota = list(filter(None, result_toyota))
print("2번")
print("아우디는 {}".format(avg(result_audi)))
print("토요타는 {}".format(avg(result_toyota)))

# 3번
result_chevrolet=[]
result_ford=[]
result_honda=[]
for car in cars:
    result_chevrolet.append(car.dividenamehwy("chevrolet"))
for car in cars:
    result_ford.append(car.dividenamehwy("ford"))
for car in cars:
    result_honda.append(car.dividenamehwy("honda"))
result_chevrolet = list(filter(None, result_chevrolet))
result_ford = list(filter(None, result_ford))
result_honda = list(filter(None, result_honda))
print("3번")
print("쉐보레는 {}".format(avg(result_chevrolet)))
print("포드는 {}".format(avg(result_ford)))
print("혼다는 {}".format(avg(result_honda)))

#4번
list_audi=[tmp for tmp in cars if tmp.manufac == "audi"]

result = reversed(sorted(list_audi, key=lambda car: car.hwy))





#5번
list_company=[tmp.manufac for tmp in cars]
list_company= set(list_company)
list_suv=[(tmp.manufac, tmp.yeonbi)  for tmp in cars if tmp.type == "suv"]

result=[]
sum = 0
i = 0
for com in list_company:
    for (tmp1, tmp2) in list_suv:
        if tmp1 == com:
            sum += tmp2
            i += 1
    try:
        avera = sum / i
    except ZeroDivisionError:
        pass
    sum = 0
    i = 0
    result.append((com,avera))
result = sorted(result, key=lambda x: -x[1])
result = result[0:5]
i = 1
print("5번")
for (tmp1, tmp2) in result:
    print("{}등은 {}입니다. 연비는 {}".format(i,tmp1,tmp2))
    i+=1

# 6번
list_typecty = [(tmp.type, tmp.cty) for tmp in cars]
list_type = [tmp.type for tmp in cars]
list_type = set(list_type)

result=[]
sum = 0
i = 0
for type in list_type:
    for (tmp1, tmp2) in list_typecty:
        if tmp1 == type:
            sum += tmp2
            i += 1
    average = sum / i
    sum = 0
    i = 0
    result.append((type,average))
i = 1
result = sorted(result, key=lambda x: -x[1])

print("6번")
for (tmp1, tmp2) in result:
    print("{}등은 {}입니다. 연비는 {}".format(i,tmp1,tmp2))
    i+=1

#7번
list_hwy = [(tmp.manufac, tmp.hwy) for tmp in cars]
list_company = set(list_company)
result=[]
sum = 0
i = 0
aver = 0
for com in list_company:
    for (tmp1, tmp2) in list_hwy:
        if tmp1 == com:
            sum += tmp2
            i += 1
        try:
            aver = sum / i
        except ZeroDivisionError:
            pass
    sum = 0
    i = 0
    result.append((com, aver))
i = 1
result = sorted(result, key=lambda x: -x[1])
result = result[0:3]

print("7번")
for (tmp1, tmp2) in result:
    print("{}등은 {}입니다. 연비는 {}".format(i,tmp1,tmp2))
    i+=1

# 8번
list_compact = [tmp.manufac for tmp in cars if tmp.type == "compact"]
result = []
for n in list_compact:
    result.append((n, list_compact.count(n)))
result = set(result)
result = sorted(result, key=lambda x: -x[1])
i = 1
print("8번")
for (tmp1, tmp2) in result:
    print("{}등은 {}입니다. 수는 {}".format(i,tmp1,tmp2))
    i+=1