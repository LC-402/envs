# 10.4 存储数据

# 10.4.1 使用json.dumps()和json.loads()
from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)


# # 10.4.2 保存和读取用户生成的数据
# from pathlib import Path
# import json

# username = input("What is your name?\n")

# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)

# print(f"We'll remreber you when you come back, {username}!")

from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back,{username}!\n")


from pathlib import Path
import json 

path = Path('username.json')    # 读取username.json的绝对路径,并将其赋给path
if path.exists():   # 如果指定的文件或文件夹存在,exists()方法返回True,否则返回False
    contents = path.read_text() # 读取文件中的全部内容,并作为一个字符串赋给contents
    username = json.loads(contents) # json.load() 读取
    print(f"Welcome back, {username}!\n")
else:
    username = input("What is your name?")
    contents = json.dumps(username) # 使用json.dumps()来存储这组数
    path.write_text(contents)   # 使用write_text()方法将其写入文件
    print(f"We'll remember you when you come back, {username}!\n")


from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)

# 10.4.3 重构
from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """提示用户输入用户名"""
    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()