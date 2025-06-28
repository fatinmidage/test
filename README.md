# GitHub Actions 简单演示

这是一个最简单的 GitHub Actions 演示项目，帮助你理解 CI/CD 的基本概念。

## 项目结构

```
test/
├── .github/
│   └── workflows/
│       ├── ci.yml              # 基础 GitHub Actions 工作流
│       └── advanced-ci.yml     # 高级 GitHub Actions 工作流
├── tests/
│   ├── __init__.py             # 测试包初始化文件
│   └── test_main.py            # 测试文件
├── main.py                     # 简单的 Python 程序
├── pyproject.toml              # Python 项目配置
└── README.md                   # 项目说明
```

## GitHub Actions 工作流说明

### 基础工作流 (`ci.yml`)
最简单的 CI 演示，包含：
- 代码检出
- Python 环境设置
- 依赖安装
- 简单测试运行

### 高级工作流 (`advanced-ci.yml`)
更完整的 CI/CD 流程，包含：
- 依赖缓存（提高构建速度）
- 代码格式检查（Black）
- 代码质量检查（Flake8）
- 自动化测试（Pytest）
- 详细的构建信息输出

### 触发条件
- 当代码推送到 `main` 分支时
- 当创建针对 `main` 分支的 Pull Request 时

### 工作流步骤

1. **检出代码** (`actions/checkout@v4`)
   - 从 GitHub 仓库下载最新代码

2. **设置 Python 环境** (`actions/setup-python@v4`)
   - 安装 Python 3.13 运行环境

3. **缓存依赖** (`actions/cache@v3`)
   - 缓存 pip 依赖，提高后续构建速度

4. **安装依赖**
   - 升级 pip
   - 安装项目依赖和开发工具

5. **代码质量检查**
   - Black 格式检查
   - Flake8 代码质量检查

6. **运行测试**
   - Pytest 自动化测试
   - 简单功能测试

7. **显示构建信息**
   - 输出详细的构建状态信息

## 如何使用

1. 将此代码推送到 GitHub 仓库
2. 在 GitHub 仓库页面，点击 "Actions" 标签
3. 你会看到两个工作流：
   - "简单 CI 演示" - 基础版本
   - "高级 CI 演示" - 完整版本
4. 点击任意工作流可以查看详细执行过程

## 学习要点

- **CI/CD**: 持续集成/持续部署
- **工作流文件**: `.github/workflows/` 目录下的 YAML 文件
- **触发条件**: `on` 部分定义何时运行工作流
- **作业**: `jobs` 部分定义要执行的任务
- **步骤**: `steps` 部分定义具体的执行步骤
- **运行环境**: `runs-on` 指定运行环境（如 ubuntu-latest）
- **缓存**: 使用缓存提高构建效率
- **代码质量**: 集成代码格式和质量检查工具

## 工具说明

- **Black**: Python 代码格式化工具
- **Flake8**: Python 代码质量检查工具
- **Pytest**: Python 测试框架
- **GitHub Actions**: GitHub 的 CI/CD 平台

## 问题解决

### 常见问题
1. **setuptools 多模块错误**: 已通过明确指定 `py-modules` 和重新组织项目结构解决
2. **依赖安装问题**: 简化了安装过程，移除了可能导致问题的 `-e .` 安装

## 下一步学习

- 添加更多测试步骤
- 配置自动部署到服务器
- 使用环境变量和密钥
- 配置多环境部署（开发、测试、生产）
- 集成 Docker 容器化
- 添加安全扫描和漏洞检查

## 运行项目

```bash
# 本地运行
python main.py

# 运行测试
pytest tests/ -v

# 代码格式化
black .

# 代码质量检查
flake8 .
```

## 输出示例

```bash
# main.py 输出
Hello from test!

# pytest 输出
tests/test_main.py::test_main_function_exists PASSED
tests/test_main.py::test_main_function PASSED
```

这个演示展示了 GitHub Actions 的基本用法，你可以在此基础上添加更多功能！
