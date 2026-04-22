#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查Python环境和依赖安装情况
"""

import sys
import subprocess

print("=" * 60)
print("Python环境检查")
print("=" * 60)

print(f"\n1. Python信息:")
print(f"   版本: {sys.version}")
print(f"   可执行文件路径: {sys.executable}")
print(f"   平台: {sys.platform}")

print(f"\n2. 检查pip是否可用:")
try:
    import pip
    print(f"   ✓ pip 已安装，版本: {pip.__version__}")
except ImportError:
    print("   ✗ pip 未安装")

print(f"\n3. 尝试安装依赖:")
dependencies = ['requests', 'beautifulsoup4', 'pandas', 'lxml']

for dep in dependencies:
    print(f"\n   正在检查 {dep}...")
    try:
        # 尝试导入
        if dep == 'beautifulsoup4':
            import bs4
            print(f"   ✓ {dep} 已安装，版本: {bs4.__version__}")
        elif dep == 'lxml':
            import lxml
            print(f"   ✓ {dep} 已安装，版本: {lxml.__version__}")
        else:
            module = __import__(dep)
            print(f"   ✓ {dep} 已安装，版本: {module.__version__}")
    except ImportError:
        print(f"   ✗ {dep} 未安装，尝试安装...")
        try:
            # 尝试使用pip安装
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dep, '-v'])
            print(f"   ✓ {dep} 安装成功")
        except subprocess.CalledProcessError as e:
            print(f"   ✗ {dep} 安装失败: {e}")

print("\n" + "=" * 60)
print("检查完成")
print("=" * 60)
