import os
import templates

def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)

def create_files(project_directory):
    create_file(os.path.join(project_directory, "src/main.ts"), templates.main_ts)
    create_file(os.path.join(project_directory, "src/App.vue"), templates.app_vue)
    create_file(os.path.join(project_directory, "src/router/index.ts"), templates.router_index_ts)
    create_file(os.path.join(project_directory, "src/store/index.ts"), templates.store_index_ts)
    create_file(os.path.join(project_directory, "src/views/Login.vue"), templates.login_vue)
    create_file(os.path.join(project_directory, "src/views/Dashboard.vue"), templates.dashboard_vue)
    create_file(os.path.join(project_directory, "vite.config.ts"), templates.vite_config_ts)
    print("Files created.")
