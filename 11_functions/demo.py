"""
第 11 章：函数

函数把一段可复用的逻辑起个名字。调用时把数据传进去，把结果拿出来。

本文件演示：
1. 定义与调用
2. 参数：位置、默认、关键字、*args、**kwargs
3. 返回值
4. 作用域
5. lambda 匿名函数
"""

# ---------- 1. 最简单的函数 ----------
def greet():
    """没有参数、没有返回值，只是执行一段代码。"""
    print("你好，Python")


greet()  # 名字后面加 () 才是调用；只写 greet 只是拿到函数对象


# ---------- 2. 位置参数与返回值 ----------
def add(a, b):
    """把两个数加起来并返回。return 后面的值会回到调用处。"""
    return a + b


result = add(3, 5)
print("3 + 5 =", result)


# ---------- 3. 默认参数：调用时可以不传 ----------
def power(base, exp=2):
    return base ** exp


print("默认平方 3^2 =", power(3))
print("指定指数 3^3 =", power(3, 3))


# ---------- 4. 关键字参数：按名字传，可以打乱顺序 ----------
def intro(name, city):
    print(f"{name} 来自 {city}")


intro(city="北京", name="李雷")


# ---------- 5. *args 收集多余的位置参数成元组
#            **kwargs 收集多余的关键字参数成字典 ----------
def summarize(title, *items, **options):
    print("标题:", title)
    print("列表项:", items)
    print("选项:", options)


summarize("购物", "牛奶", "面包", "鸡蛋", urgent=True, store="楼下")


# ---------- 6. 作用域：函数内部的变量外面看不到 ----------
count = 1  # 全局变量


def demo_scope():
    count = 100  # 这是函数内部的局部变量，和外面那个同名但不是同一个
    print("函数内部 count =", count)


demo_scope()
print("函数外部 count 仍是", count)


def add_to_global():
    global count          # 明确声明：我要改的是外面那个 count
    count += 1


add_to_global()
print("用 global 修改后 count =", count)

# ---------- 7. lambda：只能写一个表达式的匿名小函数 ----------
double = lambda x: x * 2
print("lambda 把 5 乘 2 =", double(5))

# 常配合 sorted 的 key 使用
pairs = [("b", 2), ("a", 3), ("c", 1)]
print("按第二个元素排序:", sorted(pairs, key=lambda p: p[1]))
