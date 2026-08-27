"""
第 07 章：字典

字典用 {} 表示，保存“键 -> 值”的映射。键必须是不可变类型
（常用字符串、数字、元组），值可以是任意类型。

本文件演示：
1. 创建、读取、修改
2. 增加与删除
3. 遍历 keys / values / items
4. 安全取值 get
"""

# ---------- 1. 创建 ----------
student = {
    "name": "李雷",
    "age": 18,
    "passed": True,
}
empty = {}
# 也可以用 dict()，键会变成字符串
from_pairs = dict(name="韩梅梅", age=17)

print("student =", student)
print("from_pairs =", from_pairs)

# ---------- 2. 读取与修改 ----------
print("姓名:", student["name"])       # 键不存在会 KeyError
student["age"] = 19                   # 键已存在 -> 修改
student["city"] = "上海"              # 键不存在 -> 新增
print("更新后:", student)

# ---------- 3. 安全读取：get 找不到时返回默认值，不报错 ----------
print("成绩（没有这个键）:", student.get("score"))          # 默认返回 None
print("成绩默认 0:", student.get("score", 0))

# ---------- 4. 删除 ----------
city = student.pop("city")            # 弹出指定键
print("pop 出 city =", city, "剩下:", student)

del student["passed"]
print("del passed 之后:", student)

# ---------- 5. 判断键是否存在 ----------
print("'name' in student:", "name" in student)
print("'score' not in student:", "score" not in student)

# ---------- 6. 遍历 ----------
scores = {"语文": 90, "数学": 88, "英语": 92}

print("只遍历键:")
for subject in scores:                # 默认遍历的是键
    print(" ", subject)

print("遍历键和值:")
for subject, score in scores.items():
    print(f"  {subject} = {score}")

print("所有键:", list(scores.keys()))
print("所有值:", list(scores.values()))

# ---------- 7. 嵌套：值也可以是字典或列表 ----------
class_info = {
    "title": "一班",
    "students": [
        {"name": "李雷", "age": 18},
        {"name": "韩梅梅", "age": 17},
    ],
}
print("班里第一个人:", class_info["students"][0]["name"])
