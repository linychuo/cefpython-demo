# CEF Python Demo

此项目使用[cefpython](https://github.com/cztomczak/cefpython)来构建跨平台的桌面应用，关于cef可参考[https://bitbucket.org/chromiumembedded/cef](https://bitbucket.org/chromiumembedded/cef)，界面使用preact来构建。

## 使用步骤
1. 首先
```bash
git clone https://github.com/linychuo/cefpython-demo.git
```

2. 由于项目使用了python和nodejs，先讲python的环境配置
    1. 安装python(2 or 3)，然后安装virtualenv
    2. 进入项目目录后，在命令行里输入
    ```bash
    virtualenv .env
    ```
    3. 然后激活创建的env，可自行搜索怎样激活env
    4. 安装项目所需要的python依赖，其中pyinstaller为创建可执行的exe文件所用
    ```bash
      pip install cefpython3==57.0 pyinstaller
    ```

3. 接下nodejs的相关配置
    1. 首先安装nodejs，这一点不罗嗦了
    2. 在项目的根目录下执行以下命令来安装项目所需要的js依赖
    ```bash
    npm install
    ```
    3. 运行以下命令用来build界面
    ```bash
    npm run build
    ```

4. 最后，可以通过
```bash
python main.py
```
来运行当前项目查看应用

5. 在生成exe之前，可以安装[upx](https://github.com/upx/upx)，这个工具可以有效的降低最终生成exe相关依赖的dll文件的大小，使得最终产生的exe目录变小，建议使用!!


## 生成exe
```bash
pyinstaller build.spec
```
命令执行完成后会生成dist和build目录，可以将dist目录拷贝到任何地方运行
