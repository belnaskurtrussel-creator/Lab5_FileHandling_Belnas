from pathlib import Path
from collections import Counter
from datetime import datetime
import csv
import json
import shutil
import string

# STUDENT INFORMATION
student_id = "TUPM-25-0291"
student_name = "Kurt Russel S. Belnas"

# DIRECTORY SETUP
activity_folder = Path.home() / "Documents" / "Activity_5_Files"
activity_folder.mkdir(parents=True, exist_ok=True)

exercise_folder = Path.home() / "Documents" / "Activity_5_Exercises"
exercise_folder.mkdir(parents=True, exist_ok=True)

# EXERCISE 1: FILE CONTENT COMPLEXITY ANALYZER
def analyze_file_complexity(export_csv=True):
    txt_files = list(activity_folder.glob("*.txt"))

    if not txt_files:
        print("No .txt files found in the activity folder.")
        return

    results = []

    print("\n" + "=" * 90)
    print("FILE CONTENT COMPLEXITY ANALYSIS")
    print("=" * 90)

    for file in txt_files:
        lines = [line.strip() for line in file.read_text(encoding="utf-8").splitlines() if line.strip()]

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

        words_per_line = word_count / line_count if line_count else 0
        chars_per_word = char_count / word_count if word_count else 0

        results.append({
            "Filename": file.name,
            "Lines": line_count,
            "Words": word_count,
            "Characters": char_count,
            "Words/Line": words_per_line,
            "Chars/Word": chars_per_word
        })

    results.sort(key=lambda x: x["Words/Line"], reverse=True)

    print(f"{'Filename':<30} {'Lines':>7} {'Words':>7} {'Chars':>9} {'Words/Line':>12} {'Chars/Word':>12}")
    print("-" * 90)

    for item in results:
        print(f"{item['Filename']:<30} {item['Lines']:>7} {item['Words']:>7} {item['Characters']:>9} {item['Words/Line']:>12.2f} {item['Chars/Word']:>12.2f}")

    print("-" * 90)
    print(f"Most content-dense file : {results[0]['Filename']}")
    print(f"Least content-dense file: {results[-1]['Filename']}")

    if export_csv:
        csv_path = activity_folder / "content_summary.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"Summary exported to: {csv_path}")



# EXERCISE 2: CONTEXT-AWARE WORD FREQUENCY ANALYZER
def load_stopwords():
    stopwords_file = activity_folder / "stopwords.txt"

    default_stopwords = {
        "the", "is", "and", "to", "a", "an", "in", "of", "for", "on",
        "with", "at", "by", "from", "this", "that", "it", "as", "are",
        "was", "were", "be", "or", "not", "your", "you"
    }

    if stopwords_file.exists():
        custom_words = {
            line.strip().lower()
            for line in stopwords_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        }
        return default_stopwords.union(custom_words)

    return default_stopwords


def word_frequency_analyzer(export_csv=True, top_n=20):
    txt_files = list(activity_folder.glob("*.txt"))

    if not txt_files:
        print("No .txt files found.")
        return

    stopwords = load_stopwords()
    overall_counter = Counter()
    per_file_counters = {}

    translator = str.maketrans("", "", string.punctuation)

    for file in txt_files:
        text = file.read_text(encoding="utf-8").lower()
        text = text.translate(translator)

        words = [word for word in text.split() if word and word not in stopwords]

        counter = Counter(words)
        per_file_counters[file.name] = counter
        overall_counter.update(counter)

    print("\n" + "=" * 70)
    print("MOST FREQUENT MEANINGFUL WORDS")
    print("=" * 70)

    for word, count in overall_counter.most_common(top_n):
        print(f"{word:<20} {count:>5}")

    if export_csv:
        csv_path = activity_folder / f"word_frequency_{student_id}.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Word", "Frequency"])
            for word, count in overall_counter.most_common():
                writer.writerow([word, count])
        print(f"\nWord frequency data exported to: {csv_path}")



# EXERCISE 3: SMART FILE BACKUP SYSTEM
def smart_backup(target_filename):
    source_file = exercise_folder / target_filename

    if not source_file.exists():
        print(f"File not found: {source_file}")
        return

    backup_folder = exercise_folder / f"backup_{student_id}"
    backup_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_filename = (
        f"{source_file.stem}_{student_id}_{timestamp}{source_file.suffix}"
    )
    backup_path = backup_folder / backup_filename

    shutil.copy2(source_file, backup_path)

    log_file = backup_folder / f"backup_log_{student_id}.txt"
    file_size = backup_path.stat().st_size

    with log_file.open("a", encoding="utf-8") as log:
        log.write("=" * 70 + "\n")
        log.write(f"Student ID      : {student_id}\n")
        log.write(f"Student Name    : {student_name}\n")
        log.write(f"Original File   : {source_file.name}\n")
        log.write(f"Backup Timestamp: {timestamp}\n")
        log.write(f"File Size       : {file_size} bytes\n")
        log.write(f"Backup Path     : {backup_path}\n")

    print("\nBackup completed successfully!")
    print(f"Backup completed for {student_id} ({student_name})")
    print(f"File saved as: {backup_filename}")
    print(f"Log updated at: {backup_folder}")



# MAIN PROGRAM MENU
def main():
    while True:
        print("\n" + "=" * 60)
        print("ACTIVITY 5 - ADDITIONAL EXERCISES")
        print("=" * 60)
        print("1. Analyze and Compare File Content Complexity")
        print("2. Context-Aware Word Frequency Analyzer")
        print("3. Smart File Backup System")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            analyze_file_complexity()
        elif choice == "2":
            word_frequency_analyzer()
        elif choice == "3":
            filename = input("Enter the filename to back up: ")
            smart_backup(filename)
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()