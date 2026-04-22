#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试依赖是否正确安装
"""

import sys

print(f"Python版本: {sys.version}")
print(f"Python路径: {sys.executable}")

# 测试导入所需的依赖
try:
    import requests
    print(f"✓ requests 已安装，版本: {requests.__version__}")
except ImportError as e:
    print(f"✗ requests 未安装: {e}")

try:
    from bs4 import BeautifulSoup
    import bs4
    print(f"✓ beautifulsoup4 已安装，版本: {bs4.__version__}")
except ImportError as e:
    print(f"✗ beautifulsoup4 未安装: {e}")

try:
    import pandas as pd
    print(f"✓ pandas 已安装，版本: {pd.__version__}")
except ImportError as e:
    print(f"✗ pandas 未安装: {e}")

try:
    import lxml
    print(f"✓ lxml 已安装，版本: {lxml.__version__}")
except ImportError as e:
    print(f"✗ lxml 未安装: {e}")

print("\n所有依赖检查完成！")
