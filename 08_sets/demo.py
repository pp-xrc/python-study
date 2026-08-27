"""
第 08 章：集合

集合用 {} 表示（空集合必须写 set()，因为 {} 是空字典）。
无序、元素不重复，适合去重和求交并差。
集合本身是可变的，但元素是不可变的。
本文件演示：
1. 创建与去重
2. 增删
3. 交、并、差、对称差
"""

# ---------- 1. 创建；重复元素会自动丢掉 ----------
colors = {"红", "绿", "蓝"}
print("自动去重后:", colors)

from_list = set([1, 2, 2, 3, 3, 3])
print("由列表得到集合:", from_list)

empty_set = set()
print("空集合:", empty_set, "类型:", type(empty_set))
print("空花括号其实是字典:", type({}))

# ---------- 2. 集合没有下标，不能 colors[0] ----------
# 可以判断是否包含
print("'红' in colors:", "红" in colors)

# ---------- 3. 增删 ----------
colors.add("黄")
print("add 之后:", colors)

colors.discard("绿")  # 没有这个元素也不报错
print("discard 绿之后:", colors)

# colors.remove("不存在")     # 没有这个元素会 KeyError，初学更推荐 discard

# ---------- 4. 交并差 ----------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("交集 a & b =", a & b)  # 两边都有
print("并集 a | b =", a | b)  # 两边合在一起（仍去重）
print("差集 a - b =", a - b)  # 在 a 不在 b
print("对称差 a ^ b =", a ^ b)  # 只在一边出现

# 方法写法与符号写法等价
print("a.intersection(b) =", a.intersection(b)) 
print("a.union(b) =", a.union(b))
print("a.difference(b) =", a.difference(b))

# ---------- 5. 实用例子：两份名单求共同好友 ----------
me = {"小明", "小红", "小刚"}
you = {"小红", "小李", "小刚"}
print("共同好友:", me & you)
print("只有我认识:", me - you)
