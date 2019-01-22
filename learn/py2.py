# coding:utf-8

try:
    # 尝试执行的代码
    num = int(raw_input('输入一个整数：'))

    result = 2/num

except ValueError:
    print '输入了非整数'

except Exception as msg:
    print msg



try:
    # 尝试执行的代码

except 错位类型1:
    # 捕获异常时执行的代码

except Exception as msg:
    # 捕获未知错误

else:
    # 没有异常时的代码

finally:
    # 无论有没有异常都执行


