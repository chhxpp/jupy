import os

def start_jupyter():
    os.chdir("src")  # 强制切换到 src 目录
    os.system("jupyter notebook")  # 启动 Jupyter Notebook

if __name__ == "__main__":
    start_jupyter()