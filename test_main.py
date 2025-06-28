import pytest
from main import main

def test_main_function():
    """测试 main 函数是否正常运行"""
    # 这个测试会捕获 main 函数的输出
    import io
    import sys
    
    # 捕获标准输出
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        main()
        output = captured_output.getvalue().strip()
        assert output == "Hello from test!"
    finally:
        sys.stdout = sys.__stdout__

def test_main_function_exists():
    """测试 main 函数是否存在"""
    assert callable(main)

if __name__ == "__main__":
    pytest.main([__file__]) 