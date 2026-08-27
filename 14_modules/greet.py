"""
这是一个自定义模块：把可复用的函数放在独立文件里。
其他文件通过 import 来使用这里的函数。
"""


def hello(name):
    """返回一句问候语。"""
    return f"你好, {name}"


def add(a, b):
    """两数相加。"""
    return a + b


# 只有直接运行本文件时，下面才会执行。
# 被别人 import 时，__name__ 不是 "__main__"，因此不会打印。
if __name__ == "__main__":
    print("直接运行 greet.py 时的自测:", hello("模块"))
