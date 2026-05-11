print("Try It 1")

from pathlib import Path
from datetime import datetime
import shutil

backup_dir = Path.home() / "Documents" / "PythonFiles"
backup_dir.mkdir(exist_ok=True)

output_dir = Path.home() / "Documents" / "Belnas_Activity_5"
output_dir.mkdir(exist_ok=True)

file_path = output_dir / "Act5_example.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Welcome to Python Programming!\n")
    file.write("File saved safely with pathlib.\n")
    file.write("Python makes file handling easy!")  # Added third line

print(f"File saved to: {file_path.resolve()}")