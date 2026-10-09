# 9.1 创建和使用类

# 9.1.1 创建Dog类
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name    # self.name是属性名
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

'''
类中的函数成为方法。前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。
__init__() 是一个特殊方法，每当你根据Dog类创建新实例时，python都会自动运行它。
在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免python默认方法与普通方法发生名称冲突

我们将__init__()方法定义成包含三个形参：self、name和age。这个方法的定义中，形参self必不可少，而且必须位于其他形参的前面。
'''

# 9.1.2 根据类船舰实例

my_dog = Dog('Willie',6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print("***********************************")

# 1.访问属性    my_dog.name

# 2.调用方法    
my_dog.sit()
my_dog.roll_over()

print("******************************")

# 3.创建多个实例
your_dog = Dog('Lucy',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()

print("*****************************************")


# 动手试一试

# 练习9.1：餐馆
class Restaurant:
    """餐馆的基本信息"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"这家餐馆的名字叫 {self.restaurant_name}")
        print(f"这家餐馆的菜系是 {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业")

restaurant = Restaurant("中餐厅","大陆菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("*************************************")

# 练习9.2：三家餐馆
restaurant_1 = Restaurant("沙县小吃","小吃")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("武汉热干面","面食")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("逍遥镇胡辣汤",'早餐')
restaurant_3.describe_restaurant()

print("************************************")

# 练习9.3：用户
class User:
    """用户基本信息"""

    def __init__(self,first_name,last_name):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name


    def describe_user(self):
        """打印用户信息摘要"""
        print(f"用户姓名: {self.first_name}{self.last_name}.")

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"Good morning {self.first_name}{self.last_name}!")

# 创建不同用户实例

user_1 = User("张","三")
user_1.describe_user()
user_1.greet_user()

user_2 = User('李','四')
user_2.describe_user()
user_2.greet_user()











