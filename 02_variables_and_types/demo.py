"""
第 02 章：变量与基本类型

本文件演示：
1. 如何给变量起名、赋值
2. 整数、浮点数、布尔、空值
3. type() 查看类型
4. 类型转换
"""

# ---------- 1. 赋值：把右边的值贴到左边的名字上 ----------
# Python 变量名：字母/下划线开头，可包含数字；区分大小写。
name = "李雷"
age = 18
height = 1.75

print("姓名:", name)
print("年龄:", age)
print("身高:", height)

# 可以一次给多个变量赋值
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# 多个名字指向同一个值
a = b = 100
print("a =", a, "b =", b)

# ---------- 2. 四种最常用的基本类型 ----------
n = 10          # int    整数
pi = 3.14       # float  浮点数（小数）
ok = True       # bool   布尔值，只有 True / False（注意首字母大写）
empty = None    # NoneType  表示“没有值”，不是 0，也不是空字符串

print("整数:", n, "类型:", type(n))
print("小数:", pi, "类型:", type(pi))
print("布尔:", ok, "类型:", type(ok))
print("空值:", empty, "类型:", type(empty))

# ---------- 3. 动态类型：同一个名字可以先后指向不同类型 ----------
value = 1
print("现在是", type(value), "值 =", value)
value = "变成文字了"
print("现在是", type(value), "值 =", value)

# ---------- 4. 类型转换：把一种类型变成另一种 ----------
text_number = "42"
as_int = int(text_number)     # 字符串 -> 整数
as_float = float(text_number) # 字符串 -> 浮点数
as_str = str(99)              # 数字 -> 字符串，才能和文字拼接
as_bool_1 = bool(1)           # 非 0、非空一般视为 True
as_bool_0 = bool(0)           # 0、""、None、[] 等视为 False

print("int('42') =", as_int)
print("float('42') =", as_float)
print("str(99) =", as_str)
print("bool(1) =", as_bool_1, "bool(0) =", as_bool_0)

# 注意：无法转换的内容会报错，例如 int("hello")
# 这种情况会在第 13 章用 try/except 处理。
