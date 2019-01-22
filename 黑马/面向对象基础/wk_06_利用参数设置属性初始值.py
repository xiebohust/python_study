class Cat:
    """这是一个猫类"""

    def __init__(self, new_name):

        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):

        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候, 会自动调用初始化方法
tom = Cat("Tom")
tom.eat()


lazy_cat = Cat("大懒猫")
lazy_cat.eat()






