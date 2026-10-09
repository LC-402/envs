# 8.3 返回值

# 8.3.1 返回简单的值
def get_formatted_name(first_name,last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# 8.3.2 让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"    
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

# 8.3.3 返回字典
def build_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

def build_person(first_name,last_name,age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)

musician = build_person('john','hendrix')
print(musician)

# 8.3.4 结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit ) ")

#     f_name = input("First name:")
#     if f_name =='q':
#         break

#     l_name = input("Last name:")
#     if l_name =='q':
#         break

#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello,{formatted_name}!")



# 动手试一试

# 练习8.6
def city_country(city,country):
    """返回一个字符串，包含城市和国家"""
    area = f"{city}, {country}"
    return area.title()

zone = city_country('shang hai','china')
print(zone)

zone = city_country('beijing','china')
print(zone)

zone = city_country('new york','usa')
print(zone)

# 练习8.7
def make_album(musician,album):
    """返回一个描述音乐专辑的字典，包括歌手名和专辑名"""
    music_text = {'歌手名':musician,'专辑名':album}
    return music_text

message = make_album('周杰伦','七里香')
print(message)

message = make_album('周杰伦','范特西')
print(message)

message = make_album('周杰伦','叶惠美')
print(message)

def make_album(musician,album,song_number=None):
    """返回一个描述音乐专辑的字典，包含歌手名、专辑名和歌曲数"""
    if song_number:
        music_text = {'歌手名':musician,'专辑名':album,'歌曲数':song_number}
    else:
        music_text = {'歌手名':musician,'专辑名':album}
    return music_text

message = make_album('周杰伦','七里香',10)
print(message)

message = make_album('周杰伦','范特西')
print(message)

# 练习8.8

def make_album(musician,album):
    """返回一个描述音乐专辑的字典，包括歌手名和专辑名"""
    music_text = {'歌手名':musician,'专辑名':album}
    return music_text

while True:
    musician_name = input('请输入歌手名：')
    if musician_name == 'q':
        break

    album_name = input('请输入专辑名：')
    if album_name == 'q':
        break

    message = make_album(musician_name,album_name)
    print(message)

    




