# createVue

# Vue Project Generator

This Python project automates the creation of a Vue3 project with Vite, TypeScript, Router, and Pinia.

## Configuration

Edit the `config/project_config.json` file to specify the project directory and dependencies.

## Usage

Run the `scripts/main.py` script to generate the project:

```shell
cd your_project_directory
npm install
npm run dev
```

```bash
python scripts/main.py

### 使用说明

1. 创建上述目录和文件。
2. 编辑 `config/project_config.json` 配置文件以指定项目目录和依赖项。
3. 在 PyCharm 或其他 IDE 中运行 `scripts/main.py` 脚本。
4. 脚本运行完成后，将生成一个包含 Vue3、Vite、TypeScript、Router 和 Pinia 的 Web 项目。
5. 在生成的项目目录中运行 `npm install` 安装依赖。
6. 运行 `npm run dev` 启动开发服务器。

After generating the project, navigate to the project directory and install the dependencies:
```