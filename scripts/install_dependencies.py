import subprocess

def install_dependencies(dependencies):
    subprocess.run(["npm", "install"], check=True)
    subprocess.run(["npm", "install"] + dependencies, check=True)
    print("Dependencies installed.")
