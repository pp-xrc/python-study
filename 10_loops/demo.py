"""
第 10 章：循环

本文件演示：
1. for 遍历
2. range()
3. while
4. break / continue
5. enumerate、zip
6. for-else（知道即可）
"""

# ---------- 1. for：挨个取出容器里的元素 ----------
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print("我喜欢", fruit)

# 遍历字符串会得到每一个字符
for ch in "Hi":
    print("字符:", ch)

# ---------- 2. range：生成一串整数，常用来数次数 ----------
# range(stop)           -> 0, 1, ..., stop-1
# range(start, stop)    -> start ... stop-1
# range(start, stop, step)
print("range(5):", list(range(5)))
print("range(2, 6):", list(range(2, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))

for i in range(3):
    print("第", i + 1, "次打招呼: hello")

# ---------- 3. while：条件为真就一直做 ----------
n = 3
while n > 0:
    print("倒计时", n)
    n -= 1                  # 别忘了修改条件，否则会无限循环
print("发射")

# ---------- 4. break 立刻结束整个循环；continue 跳过本轮剩余语句 ----------
print("找第一个偶数:")
for x in [1, 3, 4, 6]:
    if x % 2 == 0:
        print("  找到了", x)
        break               # 后面的 6 不会再看

print("只打印奇数:")
for x in [1, 2, 3, 4]:
    if x % 2 == 0:
        continue            # 偶数直接进入下一轮
    print("  ", x)

# ---------- 5. enumerate 带上序号；zip 把两个序列配对 ----------
for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ["李雷", "韩梅梅"]
scores = [90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ---------- 6. for-else：循环没有被 break 打断时，才会走 else ----------
target = 7
for x in [1, 3, 5]:
    if x == target:
        print("找到了")
        break
else:
    print("列表里没有", target)
