"""
第 15 章：文件读写

本文件演示：
1. 用 with open 打开文件（推荐，会自动关闭）
2. 读全部 / 按行读
3. 写入与追加
4. 常见出错点：路径、编码
"""

from pathlib import Path

# 找到与本文件同目录的 sample.txt，避免“在哪个文件夹运行”导致找不到文件
here = Path(__file__).parent
sample = here / "sample.txt"
output = here / "output.txt"

# ---------- 1. 读全部内容 ----------
# encoding="utf-8" 明确用 UTF-8，避免中文乱码
with open(sample, "r", encoding="utf-8") as f:
    text = f.read()
print("----- 全文 -----")
print(text)

# ---------- 2. 按行读取 ----------
with open(sample, "r", encoding="utf-8") as f:
    lines = f.readlines()          # 每行末尾通常带着 \n
print("行数:", len(lines))
for i, line in enumerate(lines, start=1):
    print(f"第{i}行:", line.strip())  # strip 去掉换行和两端空白

# 也可以直接迭代文件对象，一行一行来，省内存
print("----- 迭代读取 -----")
with open(sample, "r", encoding="utf-8") as f:
    for line in f:
        print(">", line.strip())

# ---------- 3. 写入：'w' 会覆盖整个文件；'a' 是追加到末尾 ----------
with open(output, "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

with open(output, "a", encoding="utf-8") as f:
    f.write("追加的第三行\n")

print("已写入:", output)

with open(output, "r", encoding="utf-8") as f:
    print("----- output.txt -----")
    print(f.read())

# ---------- 4. 为什么一定要用 with ----------
# with 结束时会自动 close()。如果只写 f = open(...) 而忘记关闭，
# 在异常或提前 return 时可能造成文件句柄泄漏。

# ---------- 5. 模式速查 ----------
# "r"  只读（文件必须存在）
# "w"  只写（文件不存在就创建；存在就清空）
# "a"  追加
# "x"  只在文件不存在时创建，避免误覆盖
# 文本模式默认即可；处理图片等二进制文件时用 "rb" / "wb"（基础语法了解即可）
