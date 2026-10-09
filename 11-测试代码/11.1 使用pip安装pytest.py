# 11.1 使用pip安装pytest

# 11.1.1 更新pip
# python -m pip install --upgrade pip   更新pip包
# python -m pip install --upgrade package_name  更新安装的任何包

# 11.1.2 安装pytest
# python -m pip install --user pytest   如果在执行这个命令时遇到麻烦，可尝试在不指定标志--user的情况下再次执行它

# 11.2 测试函数
# from name_function import get_formatted_name

# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == 'q':
#         break
#     last = input("Please give me a last name:")
#     if last == 'q':
#         break

#     formatted_name = get_formatted_name(first,last)
#     print(f"\tNeatly formatted name: {formatted_name}.")

# 11.2.2 可通过的测试


