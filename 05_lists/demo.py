"""
第 05 章：列表

列表用 [] 表示，有序、可变，适合保存一组会变化的数据。

本文件演示：
1. 创建、索引、切片
2. 增删改
3. 遍历与常用方法
"""

# ---------- 1. 创建与读取 ----------
fruits = ["苹果", "香蕉", "橙子"]
empty = []                  # 空列表
mixed = [1, "文本", True]    # 可以混放不同类型（初学时尽量别混）

print("完整列表:", fruits)
print("第一个:", fruits[0])
print("最后一个:", fruits[-1])
print("切片 fruits[0:2]:", fruits[0:2])
print("长度:", len(fruits))

# ---------- 2. 修改某一个位置 ----------
fruits[1] = "葡萄"
print("改完第 2 个之后:", fruits)

# ---------- 3. 增加元素 ----------
fruits.append("西瓜")          # 追加到末尾
fruits.insert(1, "草莓")       # 在下标 1 处插入
fruits.extend(["芒果", "梨"])  # 一次追加多个
print("增加之后:", fruits)

# ---------- 4. 删除元素 ----------
last = fruits.pop()            # 弹出最后一个，也可以 pop(下标)
print("弹出了:", last, "剩下:", fruits)

fruits.remove("草莓")          # 按值删除第一次出现的那个
print("remove 草莓之后:", fruits)

del fruits[0]                  # 按位置删除
print("del 下标 0 之后:", fruits)

# ---------- 5. 查找、统计、排序 ----------
nums = [3, 1, 4, 1, 5, 9, 2]
print("1 出现几次:", nums.count(1))
print("4 的下标:", nums.index(4))     # 找不到会报错
print("9 在不在列表里:", 9 in nums)

sorted_copy = sorted(nums)     # 返回新列表，原列表不变
print("sorted 新列表:", sorted_copy, "原列表:", nums)

nums.sort()                    # 原地排序，改变原列表
print("sort 之后原列表:", nums)
nums.reverse()
print("reverse 之后:", nums)

# ---------- 6. 列表是可变的：赋值只是起了个别名 ----------
a = [1, 2, 3]
b = a                          # b 和 a 指向同一份数据
c = a.copy()                   # c 是一份浅拷贝，互不影响（元素本身是不可变时）
b.append(4)
print("改 b 之后 a =", a, "c 仍是", c)
