#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安装依赖脚本
"""

import subprocess
import sys

def install_package(package_name):
    """
    安装单个包
    """
    print(f"\n正在安装 {package_name}...")
    try:
        # 尝试使用pip安装，不使用缓存，显示详细输出
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', package_name, '--no-cache-dir', '-v'],
            capture_output=True,
            text=True,
            timeout=300  # 5分钟超时
        )
        
        if result.returncode == 0:
            print(f"✓ {package_name} 安装成功")
            print(f"输出: {result.stdout[-500:] if len(result.stdout) > 500 else result.stdout}")
            return True
        else:
            print(f"✗ {package_name} 安装失败")
            print(f"错误: {result.stderr[-1000:] if len(result.stderr) > 1000 else result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"✗ {package_name} 安装超时")
        return False
    except Exception as e:
        print(f"✗ {package_name} 安装出错: {e}")
        return False

def check_package(package_name):
    """
    检查包是否已安装
    """
    try:
        if package_name == 'beautifulsoup4':
            import bs4
            print(f"✓ beautifulsoup4 已安装，版本: {bs4.__version__}")
            return True
        elif package_name == 'lxml':
            import lxml
            print(f"✓ lxml 已安装，版本: {lxml.__version__}")
            return True
        else:
            module = __import__(package_name)
            print(f"✓ {package_name} 已安装，版本: {module.__version__}")
            return True
    except ImportError:
        print(f"✗ {package_name} 未安装")
        return False

def main():
    print("=" * 60)
    print("依赖安装脚本")
    print("=" * 60)
    
    # 需要安装的依赖列表
    dependencies = [
        'requests',
        'beautifulsoup4',
        'pandas',
        'lxml'
    ]
    
    print("\n1. 检查当前已安装的依赖:")
    installed = []
    not_installed = []
    
    for dep in dependencies:
        if check_package(dep):
            installed.append(dep)
        else:
            not_installed.append(dep)
    
    if not not_installed:
        print("\n✓ 所有依赖已安装！")
        return
    
    print(f"\n2. 需要安装的依赖: {not_installed}")
    
    # 安装缺失的依赖
    print("\n3. 开始安装依赖...")
    install_success = []
    install_failed = []
    
    for dep in not_installed:
        if install_package(dep):
            install_success.append(dep)
        else:
            install_failed.append(dep)
    
    # 最终检查
    print("\n" + "=" * 60)
    print("4. 最终检查:")
    
    final_installed = []
    final_missing = []
    
    for dep in dependencies:
        if check_package(dep):
            final_installed.append(dep)
        else:
            final_missing.append(dep)
    
    print("\n" + "=" * 60)
    if final_missing:
        print(f"✗ 以下依赖安装失败: {final_missing}")
        print("\n建议手动安装:")
        print(f"  {sys.executable} -m pip install {' '.join(final_missing)}")
        print("\n或者检查网络连接和代理设置。")
    else:
        print("✓ 所有依赖安装成功！")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
