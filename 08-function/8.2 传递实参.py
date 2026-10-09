# 传递实参

# 8.2.1 位置实参
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

# 1.调用函数多次
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

# 2.位置实参的顺序很重要
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry','hamster')

# 8.2.2 关键字参数
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

# 8.2.3 默认值
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry',animal_type='hamster')

# 8.2.4 等效的函数调用

# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 一条名为Willie的狗
describe_pet('willie')  # 位置实参
describe_pet(pet_name='willie') # 关键字实参

# 一只名为Harry的仓鼠
describe_pet('harry','hamster') # 位置实参
describe_pet(pet_name='harry',animal_type='hamster') # 关键字实参
describe_pet(animal_type='hamster',pet_name='harry') # 关键字实参,顺序无关

# 8.2.5 避免实参错误
def describe_pet(pet_name,animal_type):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie','dog') 



# 动手试一试

# 练习8.3
def make_shirt(size,text):
    """显示T恤的尺寸和字样"""
    print(f"\nThe size of the shirt is {size}.")
    print(f"The words on the shirt are {text}.")

make_shirt('L','I love Python')

# 练习8.4
def make_shirt(size,text='I love Python'):
    """显示T恤的尺寸和字样"""
    print(f"\nThe size of the shirt is {size}.")
    print(f"The words on the shirt are {text}.")

make_shirt('M')
make_shirt('L')
make_shirt('XL','Python is awsome!')

# 8.5 城市
def describe_city(cityname,country='iceland'):
    """显示城市和国家"""
    print(f"\n{cityname.title()} is in {country.title()}.")

describe_city('beykjavik')
describe_city('londan')
describe_city('beijing','china')



