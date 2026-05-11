print("Try It 2")
from pathlib import Path

documents_path = Path.home() / "Documents" / "Activity_5_Files"
documents_path.mkdir(parents=True, exist_ok=True)

student_id = "2025-0291"   
student_name = "Kurt Russel Belnas"

file_path = documents_path / f"intro_{student_id}.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!")

print(f"File saved to: {file_path}")



file_path = Path.home() / "Documents" / "Activity_5_Files" / "intro_2025-0291.txt"

if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:\n", content)

with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        if "Python" in line:
            print(f"Line {line_number}: {line.strip()}")

with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        word_count = len(line.split())
        print(f"Line {line_number} has {word_count} words.")