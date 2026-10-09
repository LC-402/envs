# 定义名为greet_user():
def greet_user():
    """显示简单的问候语"""
    print("Hello!")

greet_user() # 调用函数

# 8.1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!") # title()方法将首字母大写

greet_user("jesse") # 调用函数并传递参数jesse

# 8.1.2 实参和形参
def greet_user(username): # username是形参  形参即函数完成工作所需的信息
    print(f"Hello, {username.title()}!")

greet_user('jesse')  # 'jesse'是实参    实参即在调用函数时传递给函数的信息



# 动手试一试

# 练习8.1
def display_message():
    """显示你正在学习的内容"""
    print("I am learning about functions in this chapter.")

display_message()

# 练习8.2
def favorite_book(title):
    """显示你喜欢的书"""
    print(f"One of my favorite books is {title.title()} in Wonderland.")

favorite_book('alice')