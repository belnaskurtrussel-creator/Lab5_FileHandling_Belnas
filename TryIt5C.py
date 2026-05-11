from pathlib import Path
from datetime import datetime
import shutil

backup_dir = Path.home() / "Documents" / "PythonFiles"
backup_dir.mkdir(exist_ok=True)



from pathlib import Path 

output_dir = Path.home() / "Documents" / "PythonFiles" 
output_dir.mkdir(exist_ok=True)  # Creates folder if missing

file_path = output_dir / "Act5_example.txt"

with open(file_path, "w", encoding="utf-8") as file: 
    file.write("Hello, Welcome to Python Programming!\n") 
    file.write("File saved safely with pathlib.")

print(f"File saved to: {file_path.resolve()}")



if file_path.exists(): 
    with open(file_path, "r", encoding="utf-8") as file: 
        content = file.read() 
print("File content:\n", content)

with open(file_path, "r", encoding="utf-8") as file: 
    for line_number, line in enumerate(file, 1): 
        print(f"Line {line_number}: {line.strip()}") 



with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis line was added!")

print("Data appended successfully.")

lines_to_add = ["\nLine A", "Line B", "Line C"]
with open(file_path, "a", encoding="utf-8") as file:
    file.writelines(lines_to_add)

user_input = input("Enter a line to append: ")
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + user_input)