import os

def get_directory_sizes(path):
    results = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            total_size = 0

            try:
                for root, dirs, files in os.walk(full_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        try:
                            total_size += os.path.getsize(file_path)
                        except (PermissionError, OSError):
                            pass

                results.append((item, total_size))

            except (PermissionError, OSError):
                pass

    results.sort(key=lambda x: x[1], reverse=True)

    return results


print("================================")
print("   TOP DISK CONSUMING FOLDERS")
print("================================")

folders = get_directory_sizes("D:/")

for name, size in folders[:5]:
    size_gb = size / (1024 ** 3)
    print(f"{name:<30} {size_gb:.2f} GB")