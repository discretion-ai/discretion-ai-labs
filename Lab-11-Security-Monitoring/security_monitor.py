from datetime import datetime

def monitor_event(event_type, severity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} | Monitoring event: {event_type}")

    if severity == "HIGH":
        print("ALERT: High-severity security event detected!")

    elif severity == "MEDIUM":
        print("WARNING: Medium-severity security event detected!")

    elif severity == "INFO":
        print("No alert required.")

    else:
        print("ERROR: Unknown severity level.")
