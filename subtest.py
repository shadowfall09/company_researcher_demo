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
    print(f"{name}=={version}")
    
    
