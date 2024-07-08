import os
import subprocess
import shutil
from scripts.config import config
from scripts.create_structure import create_structure
from scripts.install_dependencies import install_dependencies
from scripts.create_files import create_files


def remove_dist():
    project_directory = config["project_directory"]
    if os.path.exists(project_directory):
        shutil.rmtree(project_directory)
        print(f"{project_directory} has been removed.")


def clear_directory(directory):
    """
    删除指定目录中的所有文件和子目录。

    :param directory: 需要清理的目录路径
    :type directory: str
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def main():
    project_directory = config["project_directory"]
    dependencies = config["dependencies"]

    # 强制删除并重新创建项目目录
    if os.path.exists(project_directory):
        print(f"Removing existing project directory '{project_directory}'...")
        shutil.rmtree(project_directory)

    os.makedirs(project_directory, exist_ok=True)

    create_structure(project_directory)

    os.chdir(project_directory)
    subprocess.run(["npm", "init", "vite@latest", ".", "--template", "vue-ts"], check=True)

    install_dependencies(dependencies)
    create_files(project_directory)

    print(f"Vue3+Vite+TypeScript+Router+Pinia 项目已在 {project_directory} 目录下生成。")
    print("请运行以下命令以启动项目：")
    print(f"cd {project_directory} && npm install && npm run dev")


if __name__ == "__main__":
    main()
