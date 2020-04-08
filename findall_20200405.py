#查找中文和英文混合的文件中的英文單詞，並按照首字母進行排序-20200405
#A.txt:Hello Mr.??welcome you to ???
import re

file_path = '/home/shiyanlou/lj/A.txt'
with open (file_path, encoding='utf-8') as file_obj:
    content = file_obj.read()   
    a = re.findall(r'[a-zA-Z]+',content)
    result = sorted(a,key=str.upper);
    print (result)
