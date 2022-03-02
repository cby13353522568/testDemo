class Students:

    def __init__(self):
        self.__age = 0


    # def getAge(self):
    #     return self.__age
    #
    # def setAge(self, age):
    #     self.__age = age

    @property   # 方法名为 私有属性去掉__
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


stu = Students()

# print(stu.age) 私有属性调不到，只能用get，set方法
# stu.setAge(5)
# print(stu.getAge())

stu.age = 10   # 使用property之后，可以用对象属性调用
print(stu.age)
