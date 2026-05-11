from pathlib import Path
from datetime import datetime
import shutil

backup_dir = Path.home() / "Documents" / "PythonFiles"
backup_dir.mkdir(exist_ok=True)



backup_dir = Path.home() / "Documents" / "Surname_Activity_5"
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
        print("6. List all backups")

        choice = input("Choose an option (1-6): ")

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
                    f"{file_path.stem}_Surname_backup_{timestamp}{file_path.suffix}"
                )
                shutil.copy2(file_path, backup_file)
                print(f"Backup created: {backup_file.name}")
            else:
                print("Cannot backup. File does not exist.")

        elif choice == "6":
            print("Listing all backups:")
            for backup in backup_dir.glob("*backup*"):
                print("-", backup.name)

        elif choice == "5":
            print("Exiting the file manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    file_manager()