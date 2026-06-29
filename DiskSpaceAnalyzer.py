import os
from collections import defaultdict


def human_readable(size):
    """Convert bytes to KB, MB, GB, etc."""
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def scan_directory(path):
    total_size = 0
    extension_sizes = defaultdict(int)
    largest_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)

            try:
                size = os.path.getsize(filepath)
            except (PermissionError, FileNotFoundError):
                continue

            total_size += size

            ext = os.path.splitext(file)[1].lower()
            if ext == "":
                ext = "[No Extension]"

            extension_sizes[ext] += size
            largest_files.append((size, filepath))

    largest_files.sort(reverse=True)

    return total_size, extension_sizes, largest_files[:10]


def print_report(path):
    print("=" * 70)
    print("           DISK SPACE ANALYZER")
    print("=" * 70)

    print(f"\nScanning:\n{path}\n")

    total_size, ext_sizes, largest = scan_directory(path)

    print(f"Total Size : {human_readable(total_size)}")

    print("\nSpace Used By File Type")
    print("-" * 40)

    for ext, size in sorted(ext_sizes.items(), key=lambda x: x[1], reverse=True):
        print(f"{ext:<15} {human_readable(size):>12}")

    print("\nTop 10 Largest Files")
    print("-" * 70)

    for size, file in largest:
        print(f"{human_readable(size):>10}   {file}")

    print("\nScan Complete!")


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()

    if not os.path.isdir(folder):
        print("Invalid directory.")
    else:
        print_report(folder)