import shutil
import os
from telegram_bot import send_alert

print("================================")
print("        DISKALERT SYSTEM")
print("================================")


# ==============================
# 1. REAL DISK MONITORING
# ==============================

total, used, free = shutil.disk_usage("D:/")

usage = (used / total) * 100

print()
print("💾 DISK STATUS")
print(f"Total : {total / (1024**3):.2f} GB")
print(f"Used  : {used / (1024**3):.2f} GB")
print(f"Free  : {free / (1024**3):.2f} GB")
print(f"Usage : {usage:.2f}%")

if usage >= 90:
    print("🚨 ALERT: Disk usage is critically high!")
elif usage >= 80:
    print("⚠️ WARNING: Disk usage is high!")
else:
    print("✅ Disk usage is healthy.")


# ==============================
# 2. STORAGE PREDICTION
# ==============================

print()
print("🔮 STORAGE PREDICTION")

history = [
    (0, 70),
    (1, 75),
    (2, 80),
    (3, 85),
    (4, 90)
]

rates = []

for i in range(1, len(history)):

    previous_time, previous_usage = history[i - 1]
    current_time, current_usage = history[i]

    time_difference = current_time - previous_time
    usage_difference = current_usage - previous_usage

    if time_difference > 0:
        rate = usage_difference / time_difference
        rates.append(rate)

prediction_alert = False
hours_left = None

if rates:

    average_rate = sum(rates) / len(rates)

    simulated_usage = history[-1][1]

    remaining = 100 - simulated_usage

    hours_left = remaining / average_rate

    print(f"Average Growth Rate : {average_rate:.2f}% per hour")
    print(f"Current Usage       : {simulated_usage:.2f}%")
    print(f"Predicted Full      : {hours_left:.2f} hours")

    if hours_left <= 2:
        prediction_alert = True
        print("🚨 ALERT: Disk may become full within 2 hours!")

else:
    print("Not enough data for prediction.")


# ==============================
# 3. INODE MONITORING
# ==============================

print()
print("📁 INODE STATUS")

# Simulated for Windows
total_inodes = 10_000_000
used_inodes = 9_200_000

inode_usage = (used_inodes / total_inodes) * 100

print(f"Total Inodes : {total_inodes}")
print(f"Used Inodes  : {used_inodes}")
print(f"Inode Usage  : {inode_usage:.2f}%")

inode_alert = False

if inode_usage >= 90:
    inode_alert = True
    print("🚨 ALERT: Inode usage is critically high!")
elif inode_usage >= 80:
    print("⚠️ WARNING: Inode usage is high!")
else:
    print("✅ Inode usage is healthy.")


# ==============================
# 4. TOP DISK-CONSUMING FOLDERS
# ==============================

print()
print("📂 TOP DISK-CONSUMING FOLDERS")


def get_directory_sizes(path):

    results = []

    try:
        items = os.listdir(path)
    except (PermissionError, OSError):
        items = []

    for item in items:

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


folders = get_directory_sizes("D:/")

top_folders = folders[:5]

for name, size in top_folders:

    size_gb = size / (1024 ** 3)

    print(f"{name:<30} {size_gb:.2f} GB")


# ==============================
# 5. TELEGRAM ALERT
# ==============================

if prediction_alert or inode_alert:

    message = "🚨 DISKALERT INCIDENT\n\n"

    if prediction_alert:
        message += (
            "🔮 STORAGE PREDICTION\n"
            f"Predicted full: {hours_left:.2f} hours\n"
            "⚠️ Action required\n\n"
        )

    if inode_alert:
        message += (
            "📁 INODE ALERT\n"
            f"Inode usage: {inode_usage:.2f}%\n"
            "⚠️ Inode saturation detected\n\n"
        )

    message += "📂 TOP DISK CONSUMERS\n"

    for index, (name, size) in enumerate(top_folders, start=1):

        size_gb = size / (1024 ** 3)

        message += f"{index}. {name} — {size_gb:.2f} GB\n"

    message += "\n🛡️ DiskAlert monitoring system"

    send_alert(message)


print()
print("================================")
print("       MONITORING COMPLETE")
print("================================")