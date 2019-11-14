from demo.scripts import get_file_dir_path
import re


def striptags(m):
    # 将jinja2语法中的 openxml标签全部移除
    res = re.sub('</w:t>.*?(<w:t>|<w:t [^>]*>)',
                 '',
                 m.group(0),
                 flags=re.DOTALL)

    # if res != m.group(0):
    #     print("--->>>")
    #     print(m.group(0))
    #     print(res)
    #     print("---<<<")
    return res


def get_content(path):
    with open(path, "rb") as f:
        f_stream = f.read()
        return f_stream.decode("utf-8")


path = get_file_dir_path()
path = path + "resume_tpl.txt"
src_xml = get_content(path)


def sub_ele(src_xml):
    src_xml = re.sub(r'{%(?:(?!%}).)*|{{(?:(?!}}).)*',
                     striptags,
                     src_xml,
                     flags=re.DOTALL)
    return src_xml


def search_ele(src_xml):
    res = re.search(r'{%(?:(?!%}).)*|{{(?:(?!}}).)*', src_xml)
    print(res.group())


def match_ele(src_xml):
    res = re.match(r'{%(?:(?!%}).)*|{{(?:(?!}}).)*', src_xml)
    if res is None:
        print("未匹配到数据")
        return
    print(res.group())


def findall_ele(src_xml):
    # 搜索所有{{ }}, {% %}之间的内容，两边括号包含头，不包含尾，例如{% endfor
    res = re.findall(r'{%(?:(?!%}).)*|{{(?:(?!}}).)*', src_xml)
    # 如果匹配到，则将元素放入list中，如果一个都没有匹配到，则列表为空
    print(res)
    for m in res:
        print(m)


if __name__ == "__main__":
    findall_ele(src_xml)







