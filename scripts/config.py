import json
import os

def load_config():
    config_file = os.path.join(os.path.dirname(__file__), '../config/project_config.json')
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        default_config = {
            "project_directory": "my_vue_project",
            "dependencies": [
                "vue-router@4",
                "pinia"
            ]
        }
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=4)
        print(f"默认配置文件已创建，请编辑 {config_file} 然后重新运行脚本。")
        exit()

config = load_config()
