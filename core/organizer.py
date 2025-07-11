import os
import shutil
from pathlib import Path
from core.scanner import scan_desktop
from core.categorizer import categorize_file
from typing import List, Optional, Dict

class DesktopOrganizer:
    def __init__(self):
        self.desktop_path = ""
        self.organized_root= ""
        self.logger = setup.logger()

    def initialize(self):
        try:
            self.desktop_path  = str(Path.home() / "Desktop")
            self.organized_root = str(Path.home() / input("Enter the name of the organized root folder: "))

            if not os.path.exists(self.organized_root):
                os.makedirs(self.organized_root, exist_ok=True)

            self.logger.info(f"Desktop path: {self.desktop_path}")
            self.logger.info(f"Organized root path: {self.organized_root}")

            return True
        except Exception as e:
            self.logger.error(f"Error initializing DesktopOrganizer: {e}")
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
        
    