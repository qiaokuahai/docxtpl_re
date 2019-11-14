from demo.scripts import get_file_dir_path
import re
import os


def striptags(m):
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


def replace_ele(src_xml):
    src_xml = re.sub(r'{%(?:(?!%}).)*|{{(?:(?!}}).)*',
                     striptags,
                     src_xml,
                     flags=re.DOTALL)
    return src_xml


def search_ele(src_xml):
    res = re.search(r'{%(?:(?!%}).)*|{{(?:(?!}}).)*', src_xml, re.M)
    print(res.group())


def findall_ele(src_xml):
    pass


search_ele(src_xml)







