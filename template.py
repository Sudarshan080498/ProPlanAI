import os
from pathlib import Path

def create_folder_structure():
    folders = [
        ".github/workflows",
        "app",
        "app/config",
        "app/data",
        "app/models",
        "app/utils",
        "app/tests",
        "notebooks",
        "docs"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def create_files():
    # Create files within the app folder
    app_files = [
        "app/__init__.py",
        "app/config/__init__.py",
        "app/config/config.yaml",
        "app/data/__init__.py",
        "app/data/sql_queries.py",
        "app/data/preprocessing.py",
        "app/data/data_loading.py",
        "app/models/__init__.py",
        "app/models/train_model.py",
        "app/utils/__init__.py",
        "app/utils/logger.py",
        "app/utils/exceptions.py",
        "app/utils/database.py",
        "app/tests/__init__.py",
        "app/tests/test_preprocessing.py",
        "app/tests/test_train_model.py",
        "app/main.py"
    ]

    for file in app_files:
        Path(file).touch()

    # Create files in the root folder
    root_files = [
        "notebooks/data_preprocessing.ipynb",
        "docs/user_manual.md",
        "README.md",
        "requirements.txt",
        "setup.py"
    ]

    for file in root_files:
        Path(file).touch()

if __name__ == "__main__":
    create_folder_structure()
    create_files()
    print("Folder structure and files generated successfully.")
