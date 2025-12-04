import os

def count_all_lines(root="."):
    total = 0
    per_file = {}

    for folder, _, files in os.walk(root):
        for name in files:
            path = os.path.join(folder, name)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = sum(1 for _ in f)
                    total += lines
                    per_file[path] = lines
            except Exception as e:
                # Some files may not be readable as text (binaries, images, etc.)
                print(f"Skipping (binary or unreadable): {path}")

    return total, per_file

if __name__ == "__main__":
    root = os.getcwd()
    total, per_file = count_all_lines(root)

    print("\n===== Line Count Report =====")
    for p, n in per_file.items():
        print(f"{p}: {n} lines")

    print(f"\nTOTAL LINES IN ALL FILES: {total}")
