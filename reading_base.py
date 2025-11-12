def data1():
    with open('data.txt', 'r', encoding="utf-8", errors="ignore") as f: return eval(f.read())
def data2(data: str) -> dict:
    with open('data.txt', 'w', encoding="utf-8", errors="ignore") as f: f.write(data)
def base1():
    with open('base.txt', 'r', encoding="utf-8", errors="ignore") as f: return eval(f.read())
def base2(base: str) -> list:
    with open('base.txt', 'w', encoding="utf-8", errors="ignore") as f: f.write(base)
def tsk1():
    with open('tasks.txt', 'r', encoding="utf-8", errors="ignore") as f: return eval(f.read())
def tsk2(tsks: str) -> list:
    with open('tasks.txt', 'w', encoding="utf-8", errors="ignore") as f: f.write(tsks)
