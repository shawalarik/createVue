import os

def create_structure(project_directory):
    os.makedirs(project_directory, exist_ok=True)
    os.makedirs(os.path.join(project_directory, "src/views"), exist_ok=True)
    os.makedirs(os.path.join(project_directory, "src/store"), exist_ok=True)
    os.makedirs(os.path.join(project_directory, "src/router"), exist_ok=True)
    os.makedirs(os.path.join(project_directory, "src/assets"), exist_ok=True)
    os.makedirs(os.path.join(project_directory, "src/components"), exist_ok=True)
    print(f"Project structure created at {project_directory}.")
