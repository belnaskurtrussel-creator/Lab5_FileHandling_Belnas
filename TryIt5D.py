from pathlib import Path
from datetime import datetime
import shutil

backup_dir = Path.home() / "Documents" / "PythonFiles"
backup_dir.mkdir(exist_ok=True)



backup_dir = Path.home() / "Documents" / "PythonFiles"
backup_dir.mkdir(exist_ok=True)

def write_with_backup(filename: str, content: str):
    file_path = backup_dir / filename
    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.with_name(
            f"{file_path.stem}_Belnas_backup_{timestamp}{file_path.suffix}"
        )
        shutil.copy2(file_path, backup_path)
        print(f"Backup saved: {backup_path.name}")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"File saved: {file_path.name}")

def read_file(filename: str):
    file_path = backup_dir / filename
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def list_backups(filename: str):
    for backup in backup_dir.glob(f"{Path(filename).stem}_*backup*"):
        print("-", backup.name)

print("=== File Operations Demo ===")
print("\n1. Creating new file:")
write_with_backup("demo.txt", "Initial content")

print("\n2. Updating file (with backup):")
write_with_backup("demo.txt", "Updated content")

print("\n3. Reading file:")
print(read_file("demo.txt"))

print("\n4. Listing backups:")
for backup in backup_dir.glob("*backup*"):
    print("-", backup.name)

choice = input("Overwrite (O) or Append (A)? ").strip().upper()
if choice == "O":
    write_with_backup("demo.txt", "Overwritten content")
elif choice == "A":
    with open(backup_dir / "demo.txt", "a", encoding="utf-8") as file:
        file.write("\nAppended content")