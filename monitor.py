import shutil
import time

history = []

print("=== DiskAlert Monitor ===")
print("Monitoring disk usage...\n")

while True:
    total, used, free = shutil.disk_usage("D:/")

    usage = (used / total) * 100
    current_time = time.time() / 3600

    history.append((current_time, usage))

    print(f"Disk Usage: {usage:.2f}%")

    if len(history) >= 2:
        old_time, old_usage = history[-2]

        time_diff = current_time - old_time
        usage_diff = usage - old_usage

        if time_diff > 0 and usage_diff > 0:
            rate = usage_diff / time_diff
            remaining = 100 - usage
            hours_left = remaining / rate

            print(f"Growth Rate: {rate:.2f}%/hour")
            print(f"Estimated Full: {hours_left:.2f} hours")

    print("-" * 40)

    time.sleep(10)