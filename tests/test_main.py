import pytest
import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import main

def test_main_function():
    """测试 main 函数是否正常运行"""
    # 这个测试会捕获 main 函数的输出
    import io
    
    # 捕获标准输出
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    try:
        main()
        output = captured_output.getvalue().strip()
        assert output == "Hello from test!"
    finally:
        sys.stdout = original_stdout

def test_main_function_exists():
    """测试 main 函数是否存在"""
    assert callable(main)

if __name__ == "__main__":
    pytest.main([__file__]) 