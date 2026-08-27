"""
第 04 章：字符串

本文件演示：
1. 单引号、双引号、三引号
2. 索引与切片
3. 常用字符串方法
4. f-string 格式化
5. 转义字符
"""

# ---------- 1. 怎么写字符串 ----------
s1 = "单引号也可以"
s2 = "双引号也可以"
s3 = "里面有'单引号'时，外层用双引号更方便"
s4 = """三引号可以
跨越多行"""
print(s1)
print(s2)
print(s3)
print(s4)

# ---------- 2. 索引：从 0 开始数；负数从右边数 ----------
word = "Python"
#  下标:  0 1 2 3 4 5
#  字符:  P y t h o n
# 负下标: -6-5-4-3-2-1
print("第一个字符 word[0] =", word[0])
print("最后一个字符 word[-1] =", word[-1])
print("长度 len(word) =", len(word))

# ---------- 3. 切片：[start:stop:step]，含头不含尾 ----------
print("word[0:2] =", word[0:2])  # Py，取到下标 2 之前
print("word[2:] =", word[2:])  # thon，从 2 一直到末尾
print("word[:4] =", word[:4])  # Pyth，从头到下标 4 之前
print("word[::2] =", word[::2])  # Pto，从左往右，每次跳 2
print("word[::-1] =", word[::-1])  # 步长为 -1，相当于反转 从右往左，每次跳 1
print("word[::-2] =", word[1::2])  # 从下标 1 开始，每次跳 2

# ---------- 4. 字符串不可变：不能 word[0] = "J" ----------
# 想改内容，只能生成一个新字符串
new_word = "J" + word[1:]
print("新字符串:", new_word, "原字符串仍是:", word)

# ---------- 5. 常用方法（都会返回新字符串，原串不变） ----------
msg = "  Hello Python  "
print("strip 去两端空白:", msg.strip())
print("lower 变小写:", msg.lower())
print("upper 变大写:", msg.upper())
print("replace 替换:", msg.replace("Python", "World"))
print("split 按空格切成列表:", "a b c".split())
print("join 把列表拼回去:", "-".join(["a", "b", "c"]))
print("find 找子串下标:", "banana".find("na"))  # 找不到返回 -1
print("startswith:", "demo.py".startswith("demo"))
print("isdigit 是否全是数字:", "123".isdigit())

# ---------- 6. f-string：在字符串里直接嵌入表达式 ----------
name = "韩梅梅"
score = 95.5
print(f"{name} 考了 {score} 分")
print(f"分数保留 1 位小数: {score:.1f}")
print(f"1 + 1 = {1 + 1}")

# ---------- 7. 转义字符 ----------
print("换行:\n下一行")
print("制表符:\t对齐")
print("想打印反斜杠本身: C:\\Users\\name")
print(r"原始字符串不处理转义: C:\Users\name")  # 前面加 r
