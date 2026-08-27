"""
第 03 章：运算符

本文件演示：
1. 算术运算符
2. 比较运算符
3. 逻辑运算符
4. 赋值运算符
5. 成员运算符 in / not in
6. 身份运算符 is / is not
"""

# ---------- 1. 算术运算 ----------
print("加 3 + 2 =", 3 + 2)
print("减 3 - 2 =", 3 - 2)
print("乘 3 * 2 =", 3 * 2)
print("除 7 / 2 =", 7 / 2)  # 结果永远是 float
print("整除 7 // 2 =", 7 // 2)  # 向下取整，得到整数部分
print("取余 7 % 2 =", 7 % 2)  # 余数，常用来判断奇偶
print("幂 2 ** 3 =", 2**3)  # 2 的 3 次方

# ---------- 2. 比较运算：结果是 True 或 False ----------
print("3 > 2  =", 3 > 2)
print("3 == 2 =", 3 == 2)  # 相等用 ==，一个 = 是赋值
print("3 != 2 =", 3 != 2)  # 不等于
print("3 >= 3 =", 3 >= 3)

# 字符串也能比较（按字典序）
print("'apple' < 'banana' =", "apple" < "banana")

# ---------- 3. 逻辑运算 ----------
# and：两边都真才真；or：有一边真就真；not：取反
age = 20
print("成年且未退休:", age >= 18 and age < 60)
print("未成年或老年人:", age < 18 or age >= 60)
print("not True =", not True)

# 短路：and 遇到 False 后面不再算；or 遇到 True 后面不再算
print("False and 会不会执行后面:", False and print("这行不会打印"))
print("True or 会不会执行后面:", True or print("这行也不会打印"))

# ---------- 4. 赋值运算：先算再写回变量 ----------
n = 10
n += 2  # 等价于 n = n + 2
n *= 3  # 等价于 n = n * 3
print("经过 += 和 *= 之后 n =", n)

# ---------- 5. 成员运算：某个元素在不在容器里 ----------
text = "Python"
nums = [1, 2, 3]
print("'th' in 'Python' =", "th" in text)
print("4 not in [1, 2, 3] =", 4 not in nums)

# ---------- 6. 身份运算：是不是同一个对象（不是比值是否相等） ----------
# == 比值；is 比身份（内存中是否是同一个对象）
left = [1, 2]
right = [1, 2]
alias = left  # alias 和 left 指向同一份列表
print("left == right:", left == right)  # 内容相同
print("left is right:", left is right)  # 不是同一个对象
print("left is alias:", left is alias)  # 是同一个对象

# None 的判断约定俗成用 is，不用 ==
value = None
print("value is None:", value is None)
