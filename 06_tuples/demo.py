"""
第 06 章：元组

元组用 () 表示，有序、不可变。适合表示“一组不该被改掉的值”，
例如坐标 (x, y)、身份证信息等。

本文件演示：
1. 创建与访问
2. 不可变意味着什么
3. 解包
4. 单元素元组的写法陷阱
"""

# ---------- 1. 创建 ----------
point = (3, 4)
rgb = (255, 128, 0)
also = 1, 2, 3              # 没有括号也可以，逗号才是关键
empty = ()
one = (7,)                  # 只有一个元素时，必须加逗号，否则只是括号运算

print("point =", point)
print("also =", also)
print("空元组:", empty)
print("单元素元组:", one, "类型:", type(one))
print("忘记逗号 (7) 的类型:", type((7)))  # 这是 int，不是 tuple

# ---------- 2. 访问方式和列表一样，但不能修改 ----------
print("横坐标 point[0] =", point[0])
print("切片 rgb[:2] =", rgb[:2])
print("长度:", len(rgb))

# 下面这行如果取消注释会报错：TypeError
# point[0] = 10

# 元组里如果装了列表，列表本身还能改（元组“不可变”指的是槽位不能换）
pair = (1, ["a", "b"])
pair[1].append("c")
print("元组槽位没换，但里面的列表变了:", pair)

# ---------- 3. 解包：按位置拆开赋给多个变量 ----------
x, y = point
print("解包后 x =", x, "y =", y)

# 交换两个变量：Python 经典写法
a, b = 10, 20
a, b = b, a
print("交换后 a =", a, "b =", b)

# * 可以接住“剩下的那些”
first, *middle, last = (1, 2, 3, 4, 5)
print("first =", first, "middle =", middle, "last =", last)

# ---------- 4. 元组常用场景：函数一次返回多个值（本质是返回一个元组） ----------
def min_max(numbers):
    return min(numbers), max(numbers)  # 返回的是元组

lo, hi = min_max([3, 1, 9, 2])
print("最小值:", lo, "最大值:", hi)
print("直接接收返回值:", min_max([3, 1, 9, 2]))
