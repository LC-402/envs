# 9.3 继承
'''
当一个类继承另一个类是，将自动获得后者的所有属性和方法。
原有的类称为父类，而新类称为子类。
子类不仅可以继承父类的所有属性和方法，还可以定义自己的属性和方法
'''

# 9.3.1 子类的__init__()方法
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

class ElectricCar(Car):     # class 子类(父类):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)   # super()是一个特殊的函数，让你能够调用父类的方法

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())

print("************************************")


# 9.3.2 给子类定义属性和方法
'''
让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了
'''
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        '''
        先初始化父类的属性，在初始化电动汽车特有的属性
        '''
        super().__init__(make,model,year)
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

print("**************************************")

# 9.3.3 重写父类中的方法
'''
在子类中定义一个与要重写的父类方法同名的方法。这样，python将忽略这个父类方法，只关注你在子类中定义的相应方法
'''
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        '''
        先初始化父类的属性，在初始化电动汽车特有的属性
        '''
        super().__init__(make,model,year)
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")

# 9.3.4 将实例用作属性
'''
在使用代码模拟实物时，你可能会发现自己给类添加了太多细节：属性和方法越来越多，文件越来越长。
在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。将大型类拆分成多个协同工作的小类，这种方法称为组合。
'''
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

class Battery:
    """一次模拟电动汽车电池的简单尝试"""

    def __init__(self,battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")