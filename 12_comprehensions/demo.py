"""
第 12 章：推导式

推导式用一行语法从旧容器生成新容器，本质仍是 for + 可选 if。
先会写普通循环，再改写成推导式。

本文件演示：
1. 列表推导式
2. 带条件过滤
3. 集合推导式
4. 字典推导式
5. 什么时候不要用推导式
"""

nums = [1, 2, 3, 4, 5, 6]

# ---------- 1. 列表推导式：[表达式 for 变量 in 可迭代对象] ----------
# 普通写法：
squares_loop = []
for n in nums:
    squares_loop.append(n * n)

# 推导式写法，结果一样
squares = [n * n for n in nums]
print("平方:", squares)

# ---------- 2. 过滤：后面加 if ----------
evens = [n for n in nums if n % 2 == 0]
print("偶数:", evens)

# 表达式里也可以做转换
labels = [f"第{n}项" for n in nums if n <= 3]
print("标签:", labels)

# ---------- 3. 集合推导式：自动去重 ----------
words = ["Apple", "apple", "BANANA", "banana"]
lowered = {w.lower() for w in words}
print("小写去重:", lowered)

# ---------- 4. 字典推导式 ----------
names = ["李雷", "韩梅梅", "Jim"]
name_len = {name: len(name) for name in names}
print("名字长度:", name_len)

# 把现有字典加工成新字典
scores = {"语文": 90, "数学": 55, "英语": 72}
passed = {k: v for k, v in scores.items() if v >= 60}
print("及格科目:", passed)

# ---------- 5. 嵌套循环的推导式（能看懂即可，别硬写太复杂） ----------
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("两层循环配对:", pairs)

# 可读性优先：逻辑超过两层，或表达式很长时，请改回普通 for。
# 推导式不是越短越好，是“短且一眼能看懂”才好。
