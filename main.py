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


from datetime import datetime 
import shutil 

backup_dir = Path.home() / "Documents" / "PythonFiles" 
backup_dir.mkdir(exist_ok=True) 

def write_with_backup(filename: str, content: str): 
    file_path = backup_dir / filename 

    if file_path.exists(): 
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
        backup_path = file_path.with_name(
            f"{file_path.stem}_backup_{timestamp}{file_path.suffix}"
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


from pathlib import Path 
from datetime import datetime 
import shutil 

backup_dir = Path.home() / "Documents" / "PythonFiles" 
backup_dir.mkdir(exist_ok=True)

def file_manager(): 
    file_name = input("Enter filename (e.g., notes.txt): ") 
    file_path = backup_dir / file_name

    while True: 
        print("\n--- MENU ---") 
        print("1. Write to file") 
        print("2. Append to file") 
        print("3. Read file") 
        print("4. Backup file") 
        print("5. Exit") 
        
        choice = input("Choose an option (1-5): ")

        if choice == "1": 
            content = input("Enter content to write:\n") 
            with open(file_path, "w", encoding="utf-8") as f: 
                f.write(content) 
            print("File written successfully.") 

        elif choice == "2": 
            more = input("Enter content to append:\n") 
            with open(file_path, "a", encoding="utf-8") as f: 
                f.write("\n" + more) 
            print("Content appended.") 

        elif choice == "3": 
            if file_path.exists(): 
                with open(file_path, "r", encoding="utf-8") as f: 
                    print("\nFile Content:\n", f.read())
            else:
                print("File not found.")

        elif choice == "4": 
            if file_path.exists(): 
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
                backup_file = file_path.with_name( 
                    f"{file_path.stem}_backup_{timestamp}{file_path.suffix}" 
                ) 
                shutil.copy2(file_path, backup_file) 
                print(f"Backup created: {backup_file.name}") 
            else: 
                print("Cannot backup. File does not exist.") 

        elif choice == "5": 
            print("Exiting the file manager.") 
            break 

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    file_manager()


print("DATA AND OBSERVATION")