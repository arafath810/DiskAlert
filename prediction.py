def predict_exhaustion(history):
    """
    history = list of (time_hours, used_percent)
    """

    if len(history) < 2:
        return None

    t1, u1 = history[-2]
    t2, u2 = history[-1]

    time_difference = t2 - t1
    usage_difference = u2 - u1

    if time_difference <= 0 or usage_difference <= 0:
        return None

    rate = usage_difference / time_difference

    remaining = 100 - u2
    hours_left = remaining / rate

    return rate, hours_left


# Sample telemetry
history = [
    (0, 70),
    (1, 75),
    (2, 80),
    (3, 85),
    (4, 90)
]

result = predict_exhaustion(history)

if result:
    rate, hours_left = result

    print(f"Consumption rate: {rate:.2f}% per hour")
    print(f"Predicted time until full: {hours_left:.2f} hours")