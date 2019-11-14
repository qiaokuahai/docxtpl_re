import re


def t1():
    pattern = r"Windows(?=95|98|NT|2000)(.*)"
    line = "我是中国人，我要用Windows99电脑"
    res = re.findall(pattern, line)
    res = re.search(pattern, line)
    print(res.group())


def t2():
    pattern = r"Windows(?!95|98|NT|2000)(.*)"
    line = "我是中国人，我要用Windows98电脑"
    res = re.findall(pattern, line)
    res = re.search(pattern, line)
    print(res.group())


def t3():
    pattern = r"(?<=用)Windows(.*)"
    line = "我是中国人，我要用Windows98电脑"
    res = re.findall(pattern, line)
    res = re.search(pattern, line)
    print(res.group())


def t4():
    pattern = r"(?<!用)Windows(.*)"
    line = "我是中国人，我要Windows98电脑"
    res = re.findall(pattern, line)
    res = re.search(pattern, line)
    print(res.group())


def t5():
    pattern = r"(?:用)Windows(.*)"
    line = "我是中国人，我要用Windows98电脑"
    res = re.findall(pattern, line)
    res = re.search(pattern, line)
    print(res.group(1))


def t6():
    pattern = r"(是.*人)(?:.*)Windows(.*)"
    line = "我是中国人，我要用Windows98电脑"
    res = re.findall(pattern, line)
    res = re.search(pattern, line)
    print(res.group(0))


if __name__ == "__main__":
    t6()





