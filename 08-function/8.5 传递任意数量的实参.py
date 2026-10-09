# 8.5 传递任意数量的实参

def make_pizza(*toppings):  # *toppings 中的星号让python创建一个名为toppings的元组，该元组包含函数收到的所有值
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperroni')
make_pizza('mushrooms','green peppers','extra cheese')

# 8.5.1 结合使用位置实参和任意数量的实参
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# 8.5.2 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)



# 动手试一试

# 练习8.12：三明治
def san_ming_zhi(*args):
    """打印消息，对顾客点的三明治进行概述"""
    print(f"{args}")

san_ming_zhi('洋葱')
san_ming_zhi('洋葱','黄油')
san_ming_zhi('洋葱','黄油','香肠')

# 练习8.13：用户简介
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('马','博',age=18,status='student')
print(user_profile)

# 练习8.14：汽车
def make_car(create_name,model,**args):
    """显示汽车的信息"""
    args['制造商'] = create_name
    args['型号'] = model
    return args 


car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)