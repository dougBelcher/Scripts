import os
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        folder = os.getcwd()
    elif os.path.isdir(sys.argv[1]):
        folder = sys.argv[1]
    else:
        folder = os.getcwd()
        print(f"\nThe folder {sys.argv[1]} does not exist.")
    print(f"\nAnalyzing {folder}.\n")
    total_lines = 0
    number_of_files = 0

    for (dir_path, dir_names, file_names) in os.walk(folder):
        for file in file_names:
            if file.endswith(".py"):
                total_lines += sum(1 for _ in open(os.path.join(dir_path, file), encoding="utf-8"))
                number_of_files += 1

    print(
        f'The {folder} directory (and its subdirectories, if any) contains '
        f'{number_of_files} python (*.py) files, which have '
        f'{total_lines:,} lines altogether.\n'
    )