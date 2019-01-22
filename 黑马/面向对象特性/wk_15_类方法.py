class Tool(object):

    # 使用赋值语句定义类属性, 记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1. 创建工具对象
tool1 = Tool("剪刀")
tool2 = Tool("石头")
tool3 = Tool("布")

# 2. 输出工具对象的总数
Tool.show_tool_count()
