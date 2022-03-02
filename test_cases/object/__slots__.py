class Students:
    __slots__ = ('name', 'age')  # 这个类只允许添加name和age

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


stu = Students(1, 1, 1)
stu.grade = 1
