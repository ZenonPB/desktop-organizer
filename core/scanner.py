from config.file_categorizer import category_mapping, ignored_extensions, ignored_files
from core.organizer import DesktopOrganizer
import os

def scan_desktop(desktop_path: str):
    # Scan the desktop directory for files; Return a list of file paths
    valid_files = []

    try:
        for item in os.listdir(desktop_path):
            item_path = os.path.join(desktop_path, item)
            
            if not os.path.isfile(item_path):
                continue

            if item in ignored_files:
                continue

            _, extension = os.path.splitext(item) # underline to ignore the filename, only extension is needed
            if extension.lower() in ignored_extensions:
                continue

            if item.startswith('.'):
                continue

            if item == DesktopOrganizer.organized_root:
                continue

            valid_files.append(item_path)
    
    except Exception as e:
        print(f"Error scanning desktop: {e}")
        return []
    
    return valid_files
