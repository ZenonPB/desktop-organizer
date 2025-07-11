import os
import shutil
from pathlib import Path
from core.scanner import scan_desktop
from core.categorizer import categorize_file
from config.file_categorizer import CATEGORY_MAPPING, IGNORE_EXTENSIONS, IGNORE_FILES
from typing import List, Optional, Dict

class DesktopOrganizer:
    def __init__(self):
        self.desktop_path = ""
        self.organized_root= ""
        self.logger = setup.logger()

    def initialize(self):
        try:
            self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            
            if not os.path.exists(self.desktop_path):
                raise FileNotFoundError(f"Desktop path not found: {self.desktop_path}")
            
            self.organized_root = os.path.join(self.desktop_path, "Arquivos_Organizados")
            
            # Carregar configurações
            self.category_mapping = CATEGORY_MAPPING    
            self.ignore_files = IGNORE_FILES
            self.ignore_extensions = IGNORE_EXTENSIONS
            
            logger.info("Organizador inicializado com sucesso")
            return True
        except Exception as e:
            logger.error(f"Erro na inicialização: {str(e)}")
            return False
    
    def organize(self):
        try:
            files = scan_desktop(self.desktop_path)
            
            if not files:
                self.logger.info("No files found on the desktop.")
                return
            
            self.logger.info(f"Found {len(files)} files on the desktop.")

            organized_files_count = 0
            for file in files:
                category = categorize_file(file)
                if move_file(file, self.organized_root, category):
                    organized_files_count += 1
                
            self.logger.info(f"Organized {organized_files_count} files.")
            return True
        
        except Exception as e:
            self.logger.error(f"Error organizing desktop files: {e}")
            return False
        
    