### 打包方法
`Help_functions_for_python`目录下，运行 `python setup.py sdist`
### 安装方法
`Help_functions_for_python`目录下，运行 `pip install ./dist/packer-0.1.0.tar.gz`
### 测试方法
安装后，运行`python -m packer`，若打印出python 的位置则安装成功
### 使用方法
#### 生成图片目录
python -m packer -lg -f=/path/to/folder/ -l=/path/to/list