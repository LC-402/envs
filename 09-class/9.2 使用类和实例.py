# 9.2 使用类和实例

# 9.2.1 Car 类
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

# 9.2.2 给属性指定默认值
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 9.2.3 修改属性的值
'''
可以用三种不同的方式修改属性的值：直接通过实例修改，通过方法设置，以及通过方法递增(增加特定的值)。
'''
# 1. 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2.通过方法修改属性的值
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

my_new_car = Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

print("***********************************")

# 3.通过方法让属性的值递增
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles

my_used_car = Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print("************************************")




# 动手试一试

# 练习9.4：就餐人数
class Restaurant:
    """餐馆的基本信息"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"这家餐馆的名字叫 {self.restaurant_name}")
        print(f"这家餐馆的菜系是 {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业")

    def set_number_served(self,number_served):
        """设置就餐人数"""
        self.number_served = number_served
        

    def increment_number_served(self,people):
        """刷新餐厅的就餐人数"""
        self.number_served += people

    def print_number_served(self):
        """打印就餐人数"""
        print(f"{self.restaurant_name}有{self.number_served}人就过餐.")

restaurant = Restaurant('沙县小吃','家常菜')

restaurant.set_number_served(23)
restaurant.print_number_served()

restaurant.increment_number_served(100)
restaurant.print_number_served()

print("*******************************")

# 练习9.5：尝试登录次数
class User:
    """用户基本信息"""

    def __init__(self,first_name,last_name):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0


    def describe_user(self):
        """打印用户信息摘要"""
        print(f"用户姓名: {self.first_name}{self.last_name}.")

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"Good morning {self.first_name}{self.last_name}!")

    def increment_login_attempts(self):
        """让属性的值递增"""
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        """将属性login_attempts重置为0"""
        self.login_attempts = 0
        print(self.login_attempts)

# 创建不同用户实例
user_1 = User('张','三')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

user_1.reset_login_attempts()
user_1.increment_login_attempts()

