from prediction import predict_exhaustion

# Simulated disk usage over time
history = [
    (0, 70),
    (1, 75),
    (2, 80),
    (3, 85),
    (4, 90)
]

print("=== DiskAlert Simulation ===")

for time, usage in history:
    print(f"Hour {time}: Disk usage = {usage}%")

result = predict_exhaustion(history)

if result:
    rate, hours_left = result

    print()
    print(f"Consumption rate: {rate:.2f}% per hour")
    print(f"Predicted exhaustion: {hours_left:.2f} hours")

    if hours_left <= 2:
        print("🚨 ALERT: Disk may become full within 2 hours!")