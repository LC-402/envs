# Python 学习练习（envs）

这是我学习 **《Python 编程：从入门到实践》** 时敲的练习代码，按章节整理。

## 目录结构

| 目录 | 对应内容 |
| --- | --- |
| `08-function/` | 第 8 章 函数：定义函数、传递实参、返回值、传递列表、任意数量实参、把函数存到模块中 |
| `09-class/` | 第 9 章 类：创建和使用类、使用类和实例、继承 |
| `10-文件和异常/` | 第 10 章 文件和异常：读取文件、用 `json` 存储数据 |
| `11-测试代码/` | 第 11 章 测试代码：安装 pytest、测试函数 |
| `alien_invasion/` | 项目：外星人入侵（pygame） |

## 环境要求

- Python 3.12.6（代码里用到了 f-string 等新语法）
- 第三方库见 `requirements.txt`

## 快速开始

```bash
# 1. 创建并激活虚拟环境
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 2. 安装依赖
python -m pip install -r requirements.txt
```

### 运行章节练习

```bash
python "08-function/8.1 定义函数.py"
python "09-class/9.1 创建和使用类.py"
python "10-文件和异常/10.4 存储数据.py"
```

### 运行测试（第 11 章，pytest）

```bash
cd "11-测试代码"
python -m pytest -v
```

### 运行小游戏（外星人入侵）

```bash
cd alien_invasion
python alien_invasion_copy.py
```

> 用方向键左右移动飞船，空格键开火（当前是第一阶段的版本）。

## 说明

- 仓库里的 `.venv1/`、`.venv2/` 只是我本地用的虚拟环境，已经被 `.gitignore` 忽略，**不会**提交到 GitHub。
- 第 10 章的脚本会在当前目录生成 `numbers.json`、`username.json`，这两个文件也已被忽略。
