"""
第 13 章：异常处理

程序出错时 Python 会抛出异常。不处理就会中断；
用 try/except 可以抓住错误并给出友好的后续行为。

本文件演示：
1. 常见异常长什么样
2. try / except
3. 捕获多种异常
4. else 与 finally
5. raise 主动抛出
"""

# ---------- 1. 没有 try 时，异常会直接中断程序 ----------
# print(10 / 0)          # ZeroDivisionError
# print(int("hello"))    # ValueError
# print([1, 2][9])       # IndexError
# print({"a": 1}["b"])   # KeyError

# ---------- 2. 最常用形态 ----------
raw = "abc"
try:
    number = int(raw)
    print("转换成功:", number)
except ValueError:
    # 只捕获“值不合法”这一类错误，其他错误仍然会冒出去
    print(f"无法把 {raw!r} 转成整数")

# ---------- 3. 多种异常：可以分开处理，也可以写在一个元组里 ----------
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("除数不能为 0")
        return None
    except TypeError:
        print("请传入数字")
        return None


print("10 / 2 =", safe_div(10, 2))
print("10 / 0 =", safe_div(10, 0))
print("'10' / 2 =", safe_div("10", 2))

# ---------- 4. else：try 里完全没出错才执行
#            finally：无论成功失败都会执行（常用来做清理） ----------
path = "not_used_here.txt"
try:
    value = 10 / 2
except ZeroDivisionError:
    print("失败分支")
else:
    print("成功分支, value =", value)
finally:
    print("这里总会执行")

# ---------- 5. 想看具体错误信息时，用 as ----------
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError as e:
    print("捕获到异常对象:", type(e).__name__, "-", e)

# ---------- 6. raise：自己发现问题，主动抛出去让调用方处理 ----------
def score_level(score):
    if score < 0 or score > 100:
        raise ValueError("分数必须在 0 到 100 之间")
    return "及格" if score >= 60 else "不及格"


try:
    print(score_level(150))
except ValueError as e:
    print("调用方收到:", e)
