"""
第 09 章：条件判断

本文件演示：
1. if / elif / else
2. 缩进决定分支范围
3. 嵌套 if
4. 三元表达式
5. 真值判断
"""

# ---------- 1. 基本二分支 ----------
score = 72

if score >= 60:
    print("及格")
else:
    print("不及格")

# ---------- 2. 多分支：从上往下匹配，命中一个就停 ----------
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("等级:", grade)

# ---------- 3. 逻辑组合 ----------
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("可以入场")

# ---------- 4. 嵌套：分支里面再分支 ----------
weather = "下雨"
has_umbrella = False
if weather == "下雨":
    if has_umbrella:
        print("撑伞出门")
    else:
        print("先别出门")
else:
    print("出门逛逛")

# ---------- 5. 三元表达式：简单二分支的一行写法 ----------
# 格式：真值 if 条件 else 假值
status = "成年" if age >= 18 else "未成年"
print("状态:", status)

# ---------- 6. 真值判断：条件位置不一定非要写 == True ----------
name = "李雷"
items = []
if name:                 # 非空字符串视为 True
    print("名字存在")
if not items:            # 空列表视为 False
    print("购物车是空的")

# 常见“假值”：False、None、0、0.0、""、[]、()、{}、set()
# 其他大多数对象在 if 里都视为 True
