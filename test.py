import streamlit as st
import subprocess
import time
import os
import sys 

python_path = sys.executable
st.write(f"当前运行的 Python 路径: {python_path}")
from importlib.metadata import distributions
packages = []
for dist in distributions():
    name = dist.metadata['Name']
    version = dist.version
    if name:
        packages.append((name, version))

packages.sort(key=lambda x: x[0].lower())

for name, version in packages:
    st.write(f"{name}=={version}")
    
    
st.write("运行子程序示例")

def run_subprocess():
    try:
        result = subprocess.run(
            [python_path, "subtest.py"],
            capture_output=True,
            text=True,
            check=True
        )
        st.write("子程序输出:")
        st.code(result.stdout)
    except subprocess.CalledProcessError as e:
        st.error(f"子程序运行失败: {e}")
    except Exception as e:
        st.error(f"发生错误: {e}")

if st.button("运行子程序"):
    run_subprocess()
    
    
    