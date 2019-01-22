# 定义一个全局变量
num = 10


def demo1():

    # 希望修改全局变量的值
    # 在 Python 中, 是不允许直接修改全局变量的值
    # 如果使用赋值语句, 会在函数内部, 定义一个局部变量
    # 虚线的意思就是, 全局变量已经有这个名字了,需要自己换一个
    num = 100

    print("demo1 %d" % num)


def demo2():

    print("demo2 %d" % num)


demo1()


demo2()