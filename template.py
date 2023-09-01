import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s] : %(message)s:')

project_name = "cellSegmentation"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/ .gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/__init__.py",
]