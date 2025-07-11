import os 
from config.file_categorizer import category_mapping, ignored_extensions, ignored_files

def categorize_file(file_path):
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1].lower()

    for category, extensions in category_mapping.items():
        if extension in extensions:
            return category
        
    return "Others"

