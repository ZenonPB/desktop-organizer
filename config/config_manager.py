import os
import json
from config import settings

class ConfigManager:
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'userconfig.json')

    @classmethod
    def load_config(cls):
        default_config = {
            "root_folder": "Arquivos_Organizados",
            "category_mapping": {
                "Documentos": [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"],
                "Planilhas": [".xlsx", ".xls", ".csv", ".ods"],
                "Apresentacoes": [".pptx", ".ppt", ".odp"],
                "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
                "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
                "Audios": [".mp3", ".wav", ".ogg", ".flac"],
                "Arquivos_Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"]
            },
            "ignore_files": ["desktop.ini"],
            "ignore_extensions": [".lnk", ".tmp"],
            "enable_backup": True,
            "max_backups": 5
        }

        try:
            with open(cls.CONFIG_PATH, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
        except FileNotFoundError
            with open(cls.CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, indent=4)
            return default_config
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de configuração. Usando configuração padrão.")
            return default_config
        
    @classmethod
    def save_config(cls, config):
        try:
            with open(cls.CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
            print("Configuração salva com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar o arquivo de configuração: {e}")
            return False
    
    @classmethod
    def get_category_mapping(cls):
        config = cls.load_config()
        return config.get("category_mapping", {})
    
    @classmethod
    def get_ignore_files(cls):
        config = cls.load_config()
        return config.get("ignore_files", [])
    
    @classmethod
    def get_ignore_extensions(cls):
        config = cls.load_config()
        return config.get("ignore_extensions", [])
    
    