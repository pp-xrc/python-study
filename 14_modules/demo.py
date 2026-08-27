"""
第 14 章：模块

模块就是一个 .py 文件。用 import 把别人（或自己）写好的函数拿过来用，
避免把所有代码堆在一个文件里。

本文件演示：
1. 导入标准库
2. 三种 import 写法
3. 导入自定义模块 greet.py
4. if __name__ == "__main__"
"""

# ---------- 1. 导入整个模块：用 模块名.函数 的方式调用 ----------
import math
import random

print("圆周率 math.pi =", math.pi)
print("平方根 math.sqrt(9) =", math.sqrt(9))
print("随机整数:", random.randint(1, 6))

# ---------- 2. 只导入需要的名字 ----------
from math import ceil, floor

print("向上取整 ceil(3.2) =", ceil(3.2))
print("向下取整 floor(3.8) =", floor(3.8))

# ---------- 3. 起别名：名字太长或发生冲突时用 ----------
import math as m

print("用别名计算 2 的 10 次方:", m.pow(2, 10))

# ---------- 4. 导入同一目录下的自定义模块 ----------
# 请在 14_modules 目录中运行: python demo.py
# 或者从项目根目录运行: python -m 不行（本课不涉及包），请 cd 到本章目录。
import greet

print(greet.hello("李雷"))
print("1 + 2 =", greet.add(1, 2))

from greet import hello as say_hi

print(say_hi("韩梅梅"))

# ---------- 5. 不推荐 from xxx import * ----------
# 会把模块里的名字一股脑倒进当前文件，容易互相覆盖，读代码时也看不出名字从哪来。

# ---------- 6. 当前文件被直接运行时，__name__ 等于 "__main__" ----------
print("本文件的 __name__ =", __name__)
