# 8.4 传递列表

def greet_users(names):
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

# 8.4.1 在函数中修改列表

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

# 模拟打印每个设计，知道没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()    # list.pop() 删除指定下标的元素，并把被删除的值返回出来;不传索引，默认删除最后一项
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print('****************************************************************')

def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print("******************************************")

# 8.4.2 禁止函数修改列表

def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，知道没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models) # unprinted_designs[:] 创建一个unprinted_designs列表的副本
show_completed_models(completed_models)

print('**************************************')




# 动手试一试

# 练习8.9：消息
def show_messages(messages):
    """打印列表中的每条消息"""
    for message in messages:
        print(message)

# 创建一个包含简短文本消息的列表
messages = ["Hello!","How are you?",'Welcome to python.']

# 将列表传递给函数
show_messages(messages)

print("**************************")

# 练习8.10：发送消息
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    """打印每条消息，并将其移动到sent_messages列表中"""
    while messages:
        # 从源列表中删除最后一条信息
        current_message = messages.pop()
        
